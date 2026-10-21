"""Cursor da vila desenhado em tamanho real, com reprodução controlada pelo Tk."""
import ctypes
import json
from pathlib import Path
import sys
import tkinter as tk


def enable_mouse_passthrough(window):
    """A janela decorativa não recebe cliques, foco nem lugar na barra de tarefas."""
    from ctypes import wintypes as wt
    user = ctypes.WinDLL('user32', use_last_error=True)
    get_style = user.GetWindowLongPtrW if ctypes.sizeof(ctypes.c_void_p) == 8 else user.GetWindowLongW
    get_style.argtypes, get_style.restype = [wt.HWND, ctypes.c_int], ctypes.c_ssize_t
    set_style = user.SetWindowLongPtrW if ctypes.sizeof(ctypes.c_void_p) == 8 else user.SetWindowLongW
    set_style.argtypes, set_style.restype = [wt.HWND, ctypes.c_int, ctypes.c_ssize_t], ctypes.c_ssize_t
    handle = int(window.wm_frame(), 0)
    # WS_EX_TRANSPARENT, WS_EX_TOOLWINDOW e WS_EX_NOACTIVATE na janela em camadas.
    flags = 0x20 | 0x80 | 0x08000000
    style = get_style(handle, -20)
    ctypes.set_last_error(0)
    previous = set_style(handle, -20, style | flags)
    if not previous and ctypes.get_last_error():
        raise OSError(ctypes.get_last_error(), 'Não foi possível liberar os cliques sob o herói.')
    position = user.SetWindowPos
    position.argtypes = [wt.HWND, wt.HWND, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, wt.UINT]
    position.restype = wt.BOOL
    return handle, position


class VillageHero:
    """Sobreposição transparente; os quadros avançam mesmo com o mouse parado."""
    TRANSPARENT = '#010203'

    def __init__(self, master, folder):
        self.master = master
        self.window = None
        self.label = None
        self.frames, self.durations = {}, {}
        self.size, self.hotspot = 80, (40, 2)
        self.state, self.frame_index = 'idle', 2
        self.animated = self.visible = self.available = False
        self.frame_job = None
        self.completed_loops = 0
        self._position = None
        if sys.platform != 'win32':
            return
        try:
            folder = Path(folder)
            data = json.loads((folder/'frames.json').read_text(encoding='utf-8'))
            self.size, self.hotspot = data['size'], tuple(data['hotspot'])
            if self.size != 80 or self.hotspot != (40, 2):
                raise ValueError('Dimensões inválidas para o herói da vila.')
            for state, info in data['states'].items():
                frames = [tk.PhotoImage(master=master, file=str(folder/name)) for name in info['files']]
                times = info['durations_ms']
                if (len(frames) != 4 or len(times) != 4
                        or any(type(t) is not int or t <= 0 for t in times)
                        or any((frame.width(), frame.height()) != (self.size, self.size) for frame in frames)):
                    raise ValueError('Quadros inválidos para o herói da vila.')
                self.frames[state], self.durations[state] = frames, times
            if set(self.frames) != {'idle', 'macro', 'token', 'weapons', 'armor', 'apothecary', 'shopping'}:
                raise ValueError('O conjunto de ações do herói está incompleto.')
            window = self.window = tk.Toplevel(master)
            window.withdraw()
            window.overrideredirect(True)
            window.configure(bg=self.TRANSPARENT)
            window.wm_attributes('-transparentcolor', self.TRANSPARENT)
            window.wm_attributes('-topmost', True)
            window.wm_attributes('-disabled', True)
            window.wm_focusmodel('passive')
            self.label = tk.Label(window, bg=self.TRANSPARENT, bd=0, highlightthickness=0,
                                  image=self.frames['idle'][2], takefocus=False)
            self.label.pack()
            window.update_idletasks()
            self.native_handle, self._position_window = enable_mouse_passthrough(window)
            self.available = True
        except (OSError, ValueError, KeyError, TypeError, tk.TclError):
            if self.window is not None:
                self.window.destroy()
                self.window = None
            self.frames.clear()
            self.durations.clear()

    def show(self, x, y, state='idle', animated=True):
        if not self.available:
            return
        state = state if state in self.frames else 'idle'
        changed = not self.visible or state != self.state or animated != self.animated
        if changed:
            self._cancel_frame()
            self.state, self.animated = state, animated
            self.frame_index = 0 if animated else 2
            self.completed_loops = 0
            self._draw()
        position = (round(x-self.hotspot[0]), round(y-self.hotspot[1]))
        was_visible = self.visible
        if not was_visible:
            self.window.deiconify()
            self.visible = True
        if position != self._position or not was_visible:
            # Coordenadas negativas são posições reais, inclusive em outro monitor;
            # a geometria do Tk as interpretaria como distância da borda direita.
            self._position_window(self.native_handle, None, *position, self.size, self.size, 0x14)
            self._position = position  # SWP_NOACTIVATE | SWP_NOZORDER
        if self.animated and self.frame_job is None:
            self._schedule_frame()

    def _draw(self):
        self.label.configure(image=self.frames[self.state][self.frame_index])

    def _schedule_frame(self):
        self.frame_job = self.master.after(self.durations[self.state][self.frame_index], self._advance)

    def _advance(self):
        self.frame_job = None
        if not self.visible or not self.animated:
            return
        self.frame_index = (self.frame_index+1) % len(self.frames[self.state])
        if self.frame_index == 0:
            self.completed_loops += 1
        self._draw()
        self._schedule_frame()

    def _cancel_frame(self):
        if self.frame_job is not None:
            self.master.after_cancel(self.frame_job)
            self.frame_job = None

    def hide(self):
        self._cancel_frame()
        if self.visible:
            self.window.withdraw()
        self.visible = False

    def destroy(self):
        self.hide()
        if self.window is not None:
            self.window.destroy()
            self.window = None
        self.available = False
