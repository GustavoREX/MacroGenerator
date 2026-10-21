"""tem ferramentas que são compartilhadas no Forge, elas estão aqui... até então as de remoção de background hue"""
from pathlib import Path
import queue
import threading
from tkinter import TclError, filedialog, colorchooser, messagebox
from PIL import Image
from core.rendering import read_image

_ai_lock = threading.Lock()
_ai_session = None


def enable_dragdrop(widget, callback):
    try:
        from tkinterdnd2 import DND_FILES
        widget.drop_target_register(DND_FILES)
        widget.dnd_bind('<<Drop>>', callback)
    except (AttributeError, RuntimeError, TclError):
        pass


def open_image(obj):
    path = filedialog.askopenfilename(parent=obj, filetypes=[('Imagens', '*.png *.jpg *.jpeg *.webp *.bmp')])
    if path:
        load_image(obj, path)


def load_image(obj, path):
    try:
        image = read_image(path)
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        messagebox.showerror('Não foi possível abrir', str(error), parent=obj)
        return
    obj.current_path = str(path)
    obj.source_img = image
    obj.original_img = image.copy()
    obj.image_revision += 1
    obj.on_image_loaded()
    obj.set_status(f'{Path(path).name} · {image.width} × {image.height} px')
    obj.refresh_preview()


def on_drop(obj, event):
    paths = obj.tk.splitlist(event.data)
    if paths:
        load_image(obj, paths[0])


def auto_remove_bg(obj):
    if obj.source_img is None or obj.ai_busy:
        return
    obj.ai_busy = True
    obj.ai_button.configure(state='disabled')
    obj.set_status('Removendo fundo… Na primeira vez, o modelo pode ser baixado.')
    source = obj.source_img.copy()
    revision = obj.image_revision
    results = queue.Queue()

    def work():
        global _ai_session
        try:
            from rembg import remove, new_session
            with _ai_lock:
                if _ai_session is None:
                    _ai_session = new_session('u2net')
                result = remove(source, session=_ai_session).convert('RGBA')
            results.put((result, None))
        except Exception as error:
            results.put((None, str(error)))

    def poll():
        obj._ai_poll_job = None
        if not obj.winfo_exists():
            return
        try:
            image, error = results.get_nowait()
        except queue.Empty:
            obj._ai_poll_job = obj.after(100, poll)
            return
        obj.ai_busy = False
        obj.ai_button.configure(state='normal')
        if error:
            obj.set_status('Não foi possível remover o fundo.')
            messagebox.showerror('Remoção de fundo', error, parent=obj)
        elif obj.image_revision == revision:
            obj.source_img = image
            obj.image_revision += 1
            obj.refresh_preview()
            obj.set_status('Fundo removido. A imagem original pode ser restaurada.')
        else:
            obj.set_status('Resultado descartado: outra imagem foi carregada ou restaurada.')

    threading.Thread(target=work, daemon=True).start()
    obj._ai_poll_job = obj.after(100, poll)


def restore_image(obj):
    if obj.original_img is not None:
        obj.source_img = obj.original_img.copy()
        obj.image_revision += 1
        obj.refresh_preview()
        obj.set_status('Imagem original restaurada.')


def pick_color(obj):
    color = colorchooser.askcolor(color=obj.bg_color, parent=obj)[1]
    if color:
        obj.bg_color = color
        obj.bg_mode.set('solid')
        obj.refresh_preview()


def save_image(obj, image, mode_id=1):
    if image is None:
        return
    source = Path(obj.current_path) if obj.current_path else None
    name = (source.stem if source else 'image') + ('_token' if mode_id == 1 else '_edited')
    path = filedialog.asksaveasfilename(parent=obj, initialfile=name + '.png',
        initialdir=str(source.parent) if source else str(Path.home()),
        defaultextension='.png', filetypes=[('PNG transparente', '*.png')])
    if path:
        try:
            image.save(path, format='PNG')
            obj.set_status(f'Salvo: {Path(path).name} · {image.width} × {image.height} px')
        except OSError as error:
            messagebox.showerror('Erro ao salvar', str(error), parent=obj)
