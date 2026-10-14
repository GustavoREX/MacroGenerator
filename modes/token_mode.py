'''Yeap, esse aqui funfa 100%, o outro ta 10% feito kkkkk'''
import math
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb
from PIL import ImageTk
from core.paths import border_paths
from core.rendering import TokenSettings, Slice, render_token, checkerboard, read_image
from core.shared import open_image, on_drop, enable_dragdrop, auto_remove_bg, pick_color, save_image, restore_image
from core.ui import ImageMode, ScrollFrame, responsive_buttons, labeled_scale

SLICE_NAMES = ('1 · Superior direita', '2 · Inferior direita', '3 · Inferior esquerda', '4 · Superior esquerda')
SLICE_COLORS = ('#e47735', '#419c77', '#7b61bd', '#358cc4')


class TokenMode(ImageMode):
    def __init__(self, master):
        super().__init__(master)
        self.border_img = None
        self.bg_mode = tk.StringVar(value='transparent')
        self.bg_color = '#ffffff'
        self.size_var = tk.StringVar(value='512')
        self.advanced = tk.BooleanVar(value=False)
        self.img_zoom = tk.DoubleVar(value=1)
        self.border_zoom = tk.DoubleVar(value=.9)
        self.crop_scale = tk.DoubleVar(value=.9)
        self.crop_mode = tk.StringVar(value='circle')
        self.fit_mode = tk.StringVar(value='cover')
        self.trim_transparent = tk.BooleanVar(value=True)
        self.rotation = tk.DoubleVar(value=0)
        self.show_guides = tk.BooleanVar(value=True)
        self.offset_x = self.offset_y = 0.0
        self.drag_start = None
        self.preview_size = 320
        self.slice_vars = [(tk.DoubleVar(value=0), tk.DoubleVar(value=0), tk.BooleanVar(value=True)) for _ in range(4)]
        self.border_choice = tk.StringVar(value='Sem borda')
        self._compact = None
        self._build_ui()
        self.load_borders()
        self.refresh_preview()

    def _build_ui(self):
        toolbar = ttk.Frame(self)
        toolbar.pack(fill='x', pady=(0, 10))
        buttons = [tb.Button(toolbar, text='Importar imagem', command=lambda: open_image(self), bootstyle='primary'),
                   tb.Button(toolbar, text='Remover fundo IA', command=lambda: auto_remove_bg(self), bootstyle='light'),
                   tb.Button(toolbar, text='Restaurar imagem', command=lambda: restore_image(self), bootstyle='light'),
                   tb.Button(toolbar, text='Exportar PNG', command=self.save_token, bootstyle='success')]
        self.ai_button = buttons[1]
        responsive_buttons(toolbar, buttons)
        self.body = ttk.Frame(self)
        self.body.pack(fill='both', expand=True)
        self.preview_panel = ttk.Frame(self.body, padding=8)
        title = ttk.Frame(self.preview_panel)
        title.pack(fill='x', pady=(0, 8))
        ttk.Label(title, text='Seu token', style='Subheading.TLabel').pack(side='left')
        tb.Checkbutton(title, text='Guias', variable=self.show_guides, command=self.refresh_preview).pack(side='right')
        self.canvas = tk.Canvas(self.preview_panel, background='#edf1f8', highlightthickness=0, width=300, height=280)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.bind('<Configure>', lambda _: self.refresh_preview())
        self.canvas.bind('<ButtonPress-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.do_drag)
        self.canvas.bind('<ButtonRelease-1>', lambda _: setattr(self, 'drag_start', None))
        self.canvas.bind('<MouseWheel>', self.zoom_wheel)
        enable_dragdrop(self.canvas, lambda e: on_drop(self, e))
        ttk.Label(self.preview_panel, text='Arraste para posicionar · Roda do mouse para ampliar', style='Muted.TLabel').pack(pady=(6, 0))
        self.options_panel = ttk.Frame(self.body, padding=(8, 0))
        tb.Checkbutton(self.options_panel, text='Modo avançado · 6 camadas', variable=self.advanced,
                        command=self.toggle_advanced, bootstyle='primary-round-toggle').pack(anchor='w', pady=(8, 12))
        self.notebook = tb.Notebook(self.options_panel)
        self.notebook.pack(fill='both', expand=True)
        tabs = {}
        for name in ('Imagem', 'Borda', 'Camadas', 'Exportar'):
            pane = ScrollFrame(self.notebook)
            self.notebook.add(pane, text=name)
            tabs[name] = pane.content
        self._image_controls(tabs['Imagem'])
        self._border_controls(tabs['Borda'])
        self._layer_controls(tabs['Camadas'])
        self._export_controls(tabs['Exportar'])
        ttk.Label(self, textvariable=self.status_var, style='Muted.TLabel', wraplength=900).pack(fill='x', pady=(8, 0))
        self.body.bind('<Configure>', self._layout)

    def _layout(self, event):
        compact = event.width < 960
        if compact == self._compact:
            return
        self._compact = compact
        self.preview_panel.grid_forget()
        self.options_panel.grid_forget()
        self.body.columnconfigure(0, weight=1)
        self.body.columnconfigure(1, weight=0, minsize=0 if compact else 365)
        self.body.rowconfigure(0, weight=3)
        self.body.rowconfigure(1, weight=2 if compact else 0)
        self.preview_panel.grid(row=0, column=0, sticky='nsew')
        self.options_panel.grid(row=1 if compact else 0, column=0 if compact else 1, sticky='nsew')
        self.options_panel.configure(width=365, height=255 if compact else 500)
        self.options_panel.pack_propagate(False)

    def _image_controls(self, parent):
        ttk.Label(parent, text='Enquadramento', style='Subheading.TLabel').pack(anchor='w')
        actions = ttk.Frame(parent)
        actions.pack(fill='x', pady=8)
        tb.Button(actions, text='Ajustar', command=lambda: self.fit_image('contain')).pack(side='left', expand=True, fill='x')
        tb.Button(actions, text='Preencher', command=lambda: self.fit_image('cover')).pack(side='left', expand=True, fill='x', padx=4)
        tb.Button(parent, text='Centralizar imagem', command=self.center_image).pack(fill='x')
        labeled_scale(parent, 'Zoom da imagem', self.img_zoom, .1, 4, self.refresh_preview)
        tb.Checkbutton(parent, text='Ignorar margens transparentes', variable=self.trim_transparent, command=self.refresh_preview).pack(anchor='w', pady=10)
        ttk.Separator(parent).pack(fill='x', pady=8)
        ttk.Label(parent, text='Recorte da imagem', style='Subheading.TLabel').pack(anchor='w')
        for value, text in (('circle', 'Circular'), ('square', 'Quadrado livre · permite sair da borda')):
            tb.Radiobutton(parent, text=text, value=value, variable=self.crop_mode, command=self.refresh_preview).pack(anchor='w', pady=3)
        labeled_scale(parent, 'Diâmetro do recorte circular', self.crop_scale, .2, 1.4, self.refresh_preview)
        ttk.Label(parent, text='O recorte só afeta a imagem. A borda permanece centralizada no quadrado.',
                  wraplength=300, style='Muted.TLabel').pack(fill='x', pady=10)

    def _border_controls(self, parent):
        ttk.Label(parent, text='Biblioteca de bordas', style='Subheading.TLabel').pack(anchor='w')
        self.border_combo = tb.Combobox(parent, textvariable=self.border_choice, state='readonly', width=24)
        self.border_combo.pack(fill='x', pady=8)
        self.border_combo.bind('<<ComboboxSelected>>', lambda _: self.apply_border())
        tb.Button(parent, text='Importar borda PNG / WebP', command=self.import_border).pack(fill='x', pady=4)
        tb.Button(parent, text='Atualizar biblioteca', command=self.load_borders).pack(fill='x', pady=4)
        labeled_scale(parent, 'Tamanho da borda', self.border_zoom, .25, 1.0, self.refresh_preview)
        ttk.Label(parent, text='Valores menores deixam espaço para cabelo, armas e outros detalhes fora do anel.', wraplength=300, style='Muted.TLabel').pack(fill='x', pady=10)
        ttk.Separator(parent).pack(fill='x', pady=8)
        ttk.Label(parent, text='Fundo da exportação', style='Subheading.TLabel').pack(anchor='w')
        for value, text in (('transparent', 'Transparente'), ('solid', 'Cor sólida')):
            tb.Radiobutton(parent, text=text, value=value, variable=self.bg_mode, command=self.refresh_preview).pack(anchor='w', pady=3)
        tb.Button(parent, text='Escolher cor', command=lambda: pick_color(self)).pack(fill='x', pady=8)

    def _layer_controls(self, parent):
        ttk.Label(parent, text='Borda completa → imagem → 4 fatias', style='Subheading.TLabel', wraplength=290).pack(anchor='w')
        ttk.Label(parent, text='Ative o modo avançado. Os controles removem parte de cada fatia superior sem apagar a borda inferior.',
                  style='Muted.TLabel', wraplength=295).pack(fill='x', pady=8)
        labeled_scale(parent, 'Rotação da divisão em cruz (°)', self.rotation, 0, 90, self.refresh_preview, 0)
        self.slice_labels = []
        for index, (start, end, visible) in enumerate(self.slice_vars):
            box = tb.Labelframe(parent, text=SLICE_NAMES[index], padding=10)
            box.pack(fill='x', pady=7)
            tb.Checkbutton(box, text='Mostrar fatia sobre a imagem', variable=visible, command=self.refresh_preview).pack(anchor='w')
            labeled_scale(box, 'Ocultar pelo início (°)', start, 0, 90,
                          lambda i=index: self.clamp_slice(i, 'start'), 0)
            labeled_scale(box, 'Ocultar pelo fim (°)', end, 0, 90,
                          lambda i=index: self.clamp_slice(i, 'end'), 0)
            label = ttk.Label(box, text='Visível: 90° / 90°', style='Muted.TLabel')
            label.pack(anchor='w', pady=(6, 0))
            self.slice_labels.append(label)
        actions = ttk.Frame(parent)
        actions.pack(fill='x', pady=8)
        tb.Button(actions, text='Mostrar todas', command=lambda: self.set_slices(True)).pack(side='left', expand=True, fill='x')
        tb.Button(actions, text='Ocultar todas', command=lambda: self.set_slices(False)).pack(side='left', expand=True, fill='x', padx=4)

    def _export_controls(self, parent):
        ttk.Label(parent, text='PNG quadrado', style='Subheading.TLabel').pack(anchor='w')
        ttk.Label(parent, text='Largura e altura em pixels').pack(anchor='w', pady=(12, 4))
        tb.Spinbox(parent, from_=64, to=4096, increment=64, textvariable=self.size_var, width=10).pack(fill='x')
        presets = ttk.Frame(parent)
        presets.pack(fill='x', pady=8)
        for value in (256, 512, 1024, 2048):
            tb.Button(presets, text=str(value), width=5, command=lambda v=value: self.size_var.set(str(v))).pack(side='left', expand=True, fill='x', padx=1)
        ttk.Label(parent, text='A prévia é o quadrado exportado. As guias e o xadrez não aparecem no PNG. Borda e recorte compartilham o mesmo centro.',
                  style='Muted.TLabel', wraplength=295).pack(fill='x', pady=12)
        tb.Button(parent, text='Exportar token', command=self.save_token, bootstyle='success').pack(fill='x')

    def toggle_advanced(self):
        self.crop_mode.set('square' if self.advanced.get() else 'circle')
        self.fit_mode.set('contain' if self.advanced.get() else 'cover')
        self.notebook.select(2 if self.advanced.get() else 0)
        self.refresh_preview()

    def clamp_slice(self, index, changed):
        start, end, _ = self.slice_vars[index]
        if start.get() + end.get() > 90:
            (end if changed == 'start' else start).set(max(0, 90 - (start if changed == 'start' else end).get()))
        if hasattr(self, 'slice_labels') and index < len(self.slice_labels):
            self.slice_labels[index].configure(text=f'Visível: {90 - start.get() - end.get():.0f}° / 90°')
        self.refresh_preview()

    def set_slices(self, visible):
        for start, end, show in self.slice_vars:
            show.set(visible)
            if visible:
                start.set(0)
                end.set(0)
        self.refresh_preview()

    def on_image_loaded(self):
        self.img_zoom.set(1)
        self.center_image()

    def center_image(self):
        self.offset_x = self.offset_y = 0
        self.refresh_preview()

    def fit_image(self, mode):
        self.fit_mode.set(mode)
        self.img_zoom.set(1)
        self.center_image()

    def load_borders(self):
        self.borders = border_paths()
        self.border_combo['values'] = ['Sem borda', *self.borders]
        if self.border_choice.get() not in self.border_combo['values']:
            self.border_choice.set('Sem borda')

    def import_border(self):
        path = filedialog.askopenfilename(parent=self, filetypes=[('Borda', '*.png *.webp')])
        if path:
            self._read_border(path)
            self.border_choice.set('Borda importada')

    def _read_border(self, path):
        try:
            self.border_img = read_image(path)
        except (OSError, ValueError) as error:
            messagebox.showerror('Não foi possível abrir a borda', str(error), parent=self)
        self.refresh_preview()

    def apply_border(self):
        path = self.borders.get(self.border_choice.get())
        if path:
            self._read_border(path)
        else:
            self.border_img = None
            self.refresh_preview()

    def settings(self):
        return TokenSettings(advanced=self.advanced.get(), image_zoom=self.img_zoom.get(),
            border_zoom=self.border_zoom.get(), offset_x=self.offset_x, offset_y=self.offset_y,
            crop=self.crop_mode.get(), crop_scale=self.crop_scale.get(), fit=self.fit_mode.get(),
            trim_transparent=self.trim_transparent.get(), background=self.bg_color if self.bg_mode.get() == 'solid' else None,
            rotation=self.rotation.get(), slices=[Slice(a.get(), b.get(), v.get()) for a, b, v in self.slice_vars])

    def make_token(self, size):
        return render_token(self.source_img, self.border_img, size, self.settings())

    def draw_preview(self):
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        self.canvas.delete('all')
        if min(width, height) < 80:
            return
        size = max(64, min(900, width - 36, height - 36))
        self.preview_size = size
        image = checkerboard(size).copy()
        image.alpha_composite(self.make_token(size))
        self.preview_tk = ImageTk.PhotoImage(image, master=self)
        cx, cy = width / 2, height / 2
        self.canvas.create_image(cx, cy, image=self.preview_tk)
        self.canvas.create_rectangle(cx-size/2, cy-size/2, cx+size/2, cy+size/2, outline='#9caac0')
        if self.show_guides.get() and self.advanced.get():
            radius = size * self.border_zoom.get() / 2
            for i, color in enumerate(SLICE_COLORS):
                angle = math.radians(self.rotation.get() + i * 90)
                self.canvas.create_line(cx, cy, cx+math.sin(angle)*radius, cy-math.cos(angle)*radius, fill=color, dash=(3, 5))
                middle = angle + math.pi / 4
                self.canvas.create_text(cx+math.sin(middle)*(radius+10), cy-math.cos(middle)*(radius+10), text=str(i+1), fill=color, font=('Segoe UI', 11, 'bold'))
        if self.source_img is None:
            self.canvas.create_text(cx, cy, text='Arraste sua imagem aqui\nou use Importar imagem', fill='#354966', font=('Segoe UI', 13), justify='center')

    def start_drag(self, event):
        self.drag_start = (event.x, event.y)

    def do_drag(self, event):
        if self.drag_start and self.source_img is not None:
            self.offset_x += (event.x - self.drag_start[0]) / self.preview_size
            self.offset_y += (event.y - self.drag_start[1]) / self.preview_size
            self.drag_start = (event.x, event.y)
            self.refresh_preview()

    def zoom_wheel(self, event):
        self.img_zoom.set(min(4, max(.1, self.img_zoom.get() * (1.08 if event.delta > 0 else 1 / 1.08))))
        return 'break'

    def save_token(self):
        if self.source_img is None:
            messagebox.showinfo('Importe uma imagem', 'Selecione a imagem do token antes de exportar.', parent=self)
            return
        try:
            size = int(self.size_var.get())
            if not 64 <= size <= 4096:
                raise ValueError
        except (ValueError, tk.TclError):
            messagebox.showerror('Tamanho inválido', 'Use um número inteiro entre 64 e 4096.', parent=self)
            return
        save_image(self, self.make_token(size), 1)
