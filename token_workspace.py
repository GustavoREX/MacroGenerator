"""Essa é a parte do TokenForge... magina negra aconteceu aqui"""
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from modes.token_mode import TokenMode
from modes.editor_mode import EditorMode


class TokenWorkspace(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        navigation = ttk.Frame(self, padding=(12, 0, 12, 10))
        navigation.pack(fill='x')
        self.mode_var = tk.StringVar(value='token')
        for value, label in (('token', 'Token Forge'), ('editor', 'Editor de imagem')):
            tb.Radiobutton(navigation, text=label, value=value, variable=self.mode_var,
                           bootstyle='primary-toolbutton', command=self.show_selected).pack(side='left', padx=(0, 8))
        self.content = ttk.Frame(self, padding=(12, 0, 12, 8))
        self.content.pack(fill='both', expand=True)
        self.modes = {}
        self.current = None
        self.show_selected()

    def show_selected(self):
        self.show(TokenMode if self.mode_var.get() == 'token' else EditorMode)

    def show(self, frame_cls):
        self.mode_var.set('token' if frame_cls is TokenMode else 'editor')
        if self.current is not None:
            self.current.pack_forget()
        if frame_cls not in self.modes:
            self.modes[frame_cls] = frame_cls(self.content)
        self.current = self.modes[frame_cls]
        self.current.pack(fill='both', expand=True)
        self.current.refresh_preview()
