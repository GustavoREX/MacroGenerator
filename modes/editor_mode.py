"""Editor de imagens com sobreposição, remoção de fundo e exportação em PNG."""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb
from PIL import Image, ImageTk
from core.rendering import read_image, checkerboard, square_pad
from core.shared import open_image, on_drop, enable_dragdrop, auto_remove_bg, restore_image, save_image
from core.ui import ImageMode, responsive_buttons


class EditorMode(ImageMode):
    def __init__(self, master):
        super().__init__(master)
        self.overlay_img = None
        self.ov_x = self.ov_y = 0.0  # Normalizados pela largura e altura da imagem original.
        self.overlay_zoom = tk.DoubleVar(value=.35)
        self.square = tk.BooleanVar(value=True)
        self.drag_start = None
        self.display_scale = 1
        self.size_var = tk.StringVar(value='1024')
        bar = ttk.Frame(self)
        bar.pack(fill='x', pady=(0, 10))
        buttons = [tb.Button(bar, text='Importar imagem', command=lambda: open_image(self)),
                   tb.Button(bar, text='Remover fundo IA', command=lambda: auto_remove_bg(self), bootstyle='light'),
                   tb.Button(bar, text='Adicionar overlay', command=self.add_overlay, bootstyle='light'),
                   tb.Button(bar, text='Exportar PNG', command=self.save_editor, bootstyle='success')]
        self.ai_button = buttons[1]
        responsive_buttons(bar, buttons)
        settings = ttk.Frame(self)
        settings.pack(fill='x', pady=(0, 8))
        controls = [tb.Button(settings, text='Restaurar imagem', command=lambda: restore_image(self)),
                    tb.Button(settings, text='Remover overlay', command=self.clear_overlay),
                    tb.Checkbutton(settings, text='Exportar quadrado', variable=self.square, command=self.refresh_preview),
                    tb.Spinbox(settings, from_=64, to=4096, increment=64, textvariable=self.size_var, width=8)]
        responsive_buttons(settings, controls)
        zoom = ttk.Frame(self)
        zoom.pack(fill='x', pady=(0, 8))
        ttk.Label(zoom, text='Tamanho do overlay').pack(side='left', padx=(0, 12))
        tb.Scale(zoom, from_=.05, to=2, variable=self.overlay_zoom, command=lambda _: self.refresh_preview()).pack(side='left', fill='x', expand=True)
        self.canvas = tk.Canvas(self, background='#edf1f8', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.bind('<Configure>', lambda _: self.refresh_preview())
        self.canvas.bind('<ButtonPress-1>', lambda e: setattr(self, 'drag_start', (e.x, e.y)))
        self.canvas.bind('<B1-Motion>', self.do_drag)
        self.canvas.bind('<ButtonRelease-1>', lambda _: setattr(self, 'drag_start', None))
        enable_dragdrop(self.canvas, lambda e: on_drop(self, e))
        ttk.Label(self, text='Arraste o overlay na prévia. O campo numérico define o lado maior exportado.', style='Muted.TLabel').pack(fill='x', pady=(8, 0))
        ttk.Label(self, textvariable=self.status_var, style='Muted.TLabel', wraplength=750).pack(fill='x', pady=4)
        self.refresh_preview()

    def on_image_loaded(self):
        self.ov_x = self.ov_y = 0
        self.overlay_img = None

    def clear_overlay(self):
        self.overlay_img = None
        self.refresh_preview()

    def add_overlay(self):
        if self.source_img is None:
            messagebox.showinfo('Importe uma imagem', 'Abra a imagem principal primeiro.', parent=self)
            return
        path = filedialog.askopenfilename(parent=self, filetypes=[('Imagens', '*.png *.webp *.jpg *.jpeg')])
        if path:
            try:
                self.overlay_img = read_image(path)
                self.ov_x = self.ov_y = 0
                self.refresh_preview()
            except (OSError, ValueError, Image.DecompressionBombError) as error:
                messagebox.showerror('Overlay inválido', str(error), parent=self)

    def make_image(self, size):
        if self.source_img is None:
            return None
        # Usa a resolução solicitada tanto na prévia quanto na exportação.
        source = self.source_img
        ratio = size / max(source.size)
        dimensions = (max(1, round(source.width * ratio)), max(1, round(source.height * ratio)))
        image = source.resize(dimensions, Image.Resampling.LANCZOS)
        if self.overlay_img is not None:
            overlay = self.overlay_img
            scale = size * self.overlay_zoom.get() / max(overlay.size)
            overlay = overlay.resize((max(1, round(overlay.width * scale)), max(1, round(overlay.height * scale))), Image.Resampling.LANCZOS)
            x = round((image.width - overlay.width) / 2 + self.ov_x * image.width)
            y = round((image.height - overlay.height) / 2 + self.ov_y * image.height)
            image.alpha_composite(overlay, (x, y))
        return square_pad(image) if self.square.get() else image

    def draw_preview(self):
        self.canvas.delete('all')
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        if self.source_img is None:
            self.canvas.create_text(width / 2, height / 2, text='Editor de imagem\nImporte uma imagem para começar',
                                    font=('Segoe UI', 16), fill='#536681', justify='center')
            return
        size = max(64, min(900, width - 30, height - 30))
        image = self.make_image(size)
        self.display_scale = size / max(self.source_img.size)
        backdrop = checkerboard(size).crop((0, 0, image.width, image.height))
        backdrop.alpha_composite(image)
        self.preview_tk = ImageTk.PhotoImage(backdrop, master=self)
        self.canvas.create_image(width / 2, height / 2, image=self.preview_tk)

    def do_drag(self, event):
        if self.drag_start and self.overlay_img is not None and self.source_img is not None:
            self.ov_x += (event.x - self.drag_start[0]) / (self.source_img.width * self.display_scale)
            self.ov_y += (event.y - self.drag_start[1]) / (self.source_img.height * self.display_scale)
            self.drag_start = (event.x, event.y)
            self.refresh_preview()

    def save_editor(self):
        if self.source_img is None:
            return
        try:
            size = int(self.size_var.get())
            if not 64 <= size <= 4096:
                raise ValueError
        except ValueError:
            messagebox.showerror('Tamanho inválido', 'Use um inteiro entre 64 e 4096 pixels.', parent=self)
            return
        save_image(self, self.make_image(size), 2)
