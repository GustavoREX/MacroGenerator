"""Ouso dizer que é aqui que a magia acontece... eu estaria errado se disse isso..."""
import multiprocessing
import sys
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD
from constants import VERSAO
from core.paths import ROOT
from core.ui import configure_style
from macro_app import MacroBuilderApp
from token_workspace import TokenWorkspace
from ui_theme import set_responsive_window_geometry

APP_NAME = 'Macro x Token'
DISPLAY_NAME = 'Macro Generator x TokenForge'
RELEASE_NOTES = (
    'Atualização completa de Visual.\n\n'
    'Integração do TokenForge: Plataforma de criação e edição de tokens PNG.'
)


class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.style = configure_style(self)
        self.title(f'{DISPLAY_NAME} {VERSAO}')
        set_responsive_window_geometry(self, 1320, 900, 640, 640)
        try:
            self.iconbitmap(str(ROOT / 'Token.ico'))
        except tk.TclError:
            pass
        self.active_tool = None
        self.info_window = None
        self.header = tk.Frame(self, background='white', padx=16, pady=12)
        self.header.pack(fill='x')
        titles = tk.Frame(self.header, background='white')
        titles.pack(anchor='w')
        self.title_buttons = {}
        for key, label in (('macro', 'Macro Generator'), ('token', 'TokenForge')):
            if key == 'token':
                tk.Label(titles, text='x', font=('Segoe UI', 17), fg='#9ca7b8', bg='white').pack(side='left', padx=10)
            button = tk.Button(titles, text=label, borderwidth=0, relief='flat',
                               background='white', activebackground='#f4f7fc',
                               cursor='hand2', highlightthickness=0, padx=0, pady=0,
                               command=lambda tool=key: self.show_tool(tool))
            button.pack(side='left', anchor='s')
            self.title_buttons[key] = button
        metadata = ttk.Frame(self.header)
        metadata.pack(anchor='w', pady=(4, 0))
        ttk.Label(metadata, text=VERSAO, style='Muted.TLabel').pack(side='left')
        self.info_button = tk.Button(metadata, text='ⓘ', font=('Segoe UI', 12),
                                    fg='#315ee7', bg='white', activebackground='#edf1f9',
                                    relief='flat', borderwidth=0, cursor='hand2',
                                    command=self.show_release_notes)
        self.info_button.pack(side='left', padx=8)
        self.info_button.bind('<Enter>', self.show_release_notes)
        self.content = ttk.Frame(self)
        self.content.pack(fill='both', expand=True)
        self.macro_host = ttk.Frame(self.content)
        self.macro = MacroBuilderApp(self, self.macro_host)
        self.token_workspace = TokenWorkspace(self.content)
        self.header.bind('<Configure>', self._resize_header)
        self.show_tool('macro')

    def _resize_header(self, event):
        self._style_titles(compact=event.width < 800)

    def _style_titles(self, compact=None):
        if compact is None:
            compact = self.winfo_width() < 800
        for key, button in self.title_buttons.items():
            selected = key == self.active_tool
            size = (20 if selected else 15) if compact else (26 if selected else 19)
            button.configure(font=('Segoe UI', size, 'bold' if selected else 'normal'),
                             fg='#315ee7' if selected else '#8490a3',
                             activeforeground='#254bc3' if selected else '#536681')

    def show_tool(self, tool):
        if tool not in ('macro', 'token'):
            raise ValueError('Ferramenta desconhecida')
        self.macro_host.pack_forget()
        self.token_workspace.pack_forget()
        self.active_tool = tool
        target = self.macro_host if tool == 'macro' else self.token_workspace
        target.pack(fill='both', expand=True)
        self._style_titles()
        if tool == 'macro':
            self.macro.update_preview()
        else:
            self.token_workspace.current.refresh_preview()

    def show_release_notes(self, _event=None):
        if self.info_window is not None and self.info_window.winfo_exists():
            self.info_window.lift()
            return
        window = tk.Toplevel(self)
        self.info_window = window
        window.title(f'Atualizações · {VERSAO}')
        window.transient(self)
        window.resizable(False, False)
        panel = ttk.Frame(window, padding=20)
        panel.pack(fill='both', expand=True)
        ttk.Label(panel, text=f'{DISPLAY_NAME}\n{VERSAO}', style='Section.TLabel').pack(anchor='w', pady=(0, 14))
        ttk.Label(panel, text=RELEASE_NOTES, wraplength=380, justify='left').pack(anchor='w')
        ttk.Button(panel, text='Fechar', command=window.destroy).pack(anchor='e', pady=(16, 0))
        window.bind('<Escape>', lambda _: window.destroy())
        window.update_idletasks()
        x = min(self.winfo_rootx() + 20, self.winfo_screenwidth() - window.winfo_width() - 20)
        y = min(self.winfo_rooty() + 80, self.winfo_screenheight() - window.winfo_height() - 40)
        window.geometry(f'+{max(0, x)}+{max(0, y)}')


def main():
    multiprocessing.freeze_support()
    if len(sys.argv) == 3 and sys.argv[1] == '--self-test':
        from integration_diagnostics import run_self_test
        return run_self_test(App, sys.argv[2])
    App().mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())
