import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb


def configure_style(root):
    style = tb.Style('bootstrap-light')
    style.configure('TButton', padding=(12, 8), font=('Segoe UI', 10))
    style.configure('TLabel', font=('Segoe UI', 10))
    style.configure('Heading.TLabel', font=('Segoe UI', 22, 'bold'), foreground='#20304c')
    style.configure('Subheading.TLabel', font=('Segoe UI', 11, 'bold'), foreground='#20304c')
    style.configure('Muted.TLabel', foreground='#687991', font=('Segoe UI', 9))
    style.configure('TNotebook.Tab', padding=(9, 8), font=('Segoe UI', 9))
    root.configure(background='#eef2f8')
    return style


class ScrollFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, highlightthickness=0, background='white', width=320)
        scrollbar = tb.Scrollbar(self, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.content = ttk.Frame(self.canvas, padding=12)
        self.window = self.canvas.create_window(0, 0, window=self.content, anchor='nw')
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfigure(self.window, width=e.width))
        self.content.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.bind('<Map>', self._bind_wheel, add='+')

    def _bind_wheel(self, _event=None):
        def attach(widget):
            widget.bind('<MouseWheel>', self._wheel, add='+')
            for child in widget.winfo_children():
                attach(child)
        attach(self.content)
        self.canvas.bind('<MouseWheel>', self._wheel)

    def _wheel(self, event):
        if self.canvas.yview() != (0.0, 1.0):
            self.canvas.yview_scroll(-1 if event.delta > 0 else 1, 'units')
        return 'break'


def responsive_buttons(parent, buttons, cell=170):
    last = [0]
    def layout(event):
        columns = max(1, min(len(buttons), event.width // cell))
        if columns == last[0]:
            return
        for i in range(max(columns, last[0])):
            parent.columnconfigure(i, weight=1 if i < columns else 0)
        for i, button in enumerate(buttons):
            button.grid(row=i // columns, column=i % columns, sticky='ew', padx=3, pady=3)
        last[0] = columns
    for i, button in enumerate(buttons):
        button.grid(row=0, column=i, padx=3, pady=3)
    parent.bind('<Configure>', layout)


def labeled_scale(parent, title, variable, low, high, callback, digits=2):
    row = ttk.Frame(parent)
    row.pack(fill='x', pady=(9, 2))
    ttk.Label(row, text=title).pack(side='left')
    value = ttk.Label(row, style='Muted.TLabel')
    value.pack(side='right')
    def changed(*_):
        value.configure(text=f'{variable.get():.{digits}f}')
        callback()
    variable.trace_add('write', changed)
    tb.Scale(parent, from_=low, to=high, variable=variable).pack(fill='x')
    value.configure(text=f'{variable.get():.{digits}f}')


class ImageMode(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.source_img = None
        self.original_img = None
        self.current_path = None
        self.image_revision = 0
        self.ai_busy = False
        self._preview_job = None
        self.status_var = tk.StringVar(value='Importe uma imagem ou arraste um arquivo para a prévia.')

    def set_status(self, text):
        self.status_var.set(text)

    def refresh_preview(self):
        if self._preview_job is None:
            self._preview_job = self.after(20, self._draw_preview)

    def _draw_preview(self):
        self._preview_job = None
        self.draw_preview()

    def destroy(self):
        if self._preview_job is not None:
            self.after_cancel(self._preview_job)
        super().destroy()
