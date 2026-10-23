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
from home_screen import HomeScreen
from interface_settings import InterfaceSettings, default_settings_path
from forge_ui import InfoPopup

APP_NAME = 'Macro x Token'
DISPLAY_NAME = 'Macro Generator x TokenForge'
RELEASE_NOTES = (
    'Tela inicial com vila em pixel art, menu simples e efeitos opcionais.\n\n'
    'Boticário Arcano: poções, óleos, granadas e pergaminhos com magias e aprimoramentos dos livros.\n\n'
    'Fabricação com Ofício, Inventor, Alquimista e habilidades de conjuradores; integração com o inventário.'
)


class App(TkinterDnD.Tk):
    def __init__(self, *, preferences_path=None, persist_preferences=True):
        super().__init__()
        self.style = configure_style(self)
        self.title(f'{DISPLAY_NAME} {VERSAO}')
        set_responsive_window_geometry(self, 1320, 900, 640, 640)
        try:
            self.iconbitmap(str(ROOT / 'Token.ico'))
        except tk.TclError:
            pass
        self.active_tool = None
        self.release_info = InfoPopup(self)
        self.header = tk.Frame(self, background='white', padx=16, pady=12)
        self.header.pack(fill='x')
        titles = tk.Frame(self.header, background='white')
        titles.pack(anchor='center')
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
        metadata.pack(anchor='center', pady=(4, 0))
        ttk.Label(metadata, text=VERSAO, style='Muted.TLabel').pack(side='left')
        self.info_button = tk.Button(metadata, text='ⓘ', font=('Segoe UI', 12),
                                    fg='#315ee7', bg='white', activebackground='#edf1f9',
                                    relief='flat', borderwidth=0, cursor='question_arrow')
        self.info_button.pack(side='left', padx=8)
        self.info_button.bind('<Enter>', self.show_release_notes)
        self.info_button.bind('<Leave>', lambda _event: self.release_info.hide())
        self.info_button.bind('<Unmap>', lambda _event: self.release_info.hide())
        self.home_button = tk.Button(metadata,text='⌂ Início',font=('Segoe UI',10,'bold'),
            fg='#315ee7',bg='white',activebackground='#edf1f9',relief='flat',bd=0,
            cursor='hand2',command=lambda: self.show_tool('home'))
        self.home_button.pack(side='left',padx=(12,0))
        self.content = ttk.Frame(self)
        self.content.pack(fill='both', expand=True)
        preferences = InterfaceSettings((preferences_path or default_settings_path()) if persist_preferences else None)
        self.home = HomeScreen(self.content,self.show_tool,preferences)
        self.macro_host = ttk.Frame(self.content)
        self.macro = MacroBuilderApp(self, self.macro_host)
        self.token_workspace = TokenWorkspace(self.content)
        self.weapon_host = ttk.Frame(self.content)
        self.weapon_workshop = None
        self.armor_host = ttk.Frame(self.content)
        self.armor_workshop = None
        self.shopping_host = ttk.Frame(self.content)
        self.shopping_workshop = None
        self.apothecary_host = ttk.Frame(self.content)
        self.apothecary_workshop = None
        self.header.bind('<Configure>', self._resize_header)
        self.show_tool('home')

    def _resize_header(self, event):
        self._style_titles(compact=event.width < 800)

    def _style_titles(self, compact=None):
        if compact is None:
            compact = self.winfo_width() < 800
        for key, button in self.title_buttons.items():
            selected = key == self.active_tool or (key == 'macro' and self.active_tool in ('weapons', 'armor', 'shopping', 'apothecary'))
            size = (20 if selected else 15) if compact else (26 if selected else 19)
            button.configure(font=('Segoe UI', size, 'bold' if selected else 'normal'),
                             fg='#315ee7' if selected else '#8490a3',
                             activeforeground='#254bc3' if selected else '#536681')

    def show_tool(self, tool):
        if tool not in ('home', 'macro', 'token', 'weapons', 'armor', 'shopping', 'apothecary'):
            raise ValueError('Ferramenta desconhecida')
        self.release_info.hide()
        self.home.pack_forget()
        self.macro_host.pack_forget()
        self.token_workspace.pack_forget()
        self.weapon_host.pack_forget()
        self.armor_host.pack_forget()
        self.shopping_host.pack_forget()
        self.apothecary_host.pack_forget()
        self.active_tool = tool
        if tool == 'weapons' and self.weapon_workshop is None:
            from weapon_workshop import WeaponWorkshop
            self.weapon_workshop = WeaponWorkshop(self.weapon_host, self.macro,
                                                  lambda: self.show_tool('macro'), self.use_custom_weapon)
            self.weapon_workshop.pack(fill='both', expand=True)
        if tool == 'armor' and self.armor_workshop is None:
            from armor_workshop import ArmorWorkshop
            self.armor_workshop = ArmorWorkshop(self.armor_host, self.macro,
                                                lambda: self.show_tool('macro'), self.use_custom_weapon)
            self.armor_workshop.pack(fill='both', expand=True)
        if tool == 'shopping':
            if self.shopping_workshop is None:
                from shopping_ui import ShoppingWorkshop
                self.shopping_workshop = ShoppingWorkshop(self.shopping_host, self.macro,
                                                          lambda: self.show_tool('macro'))
                self.shopping_workshop.pack(fill='both', expand=True)
            self.shopping_workshop.refresh()
            if self.macro.get_inventory().lines:
                self.shopping_workshop.notebook.select(1)
        if tool == 'apothecary' and self.apothecary_workshop is None:
            from apothecary_ui import ApothecaryWorkshop
            self.apothecary_workshop = ApothecaryWorkshop(self.apothecary_host, self.macro,
                                                        lambda: self.show_tool('macro'))
            self.apothecary_workshop.pack(fill='both', expand=True)
        target = {'home': self.home, 'macro': self.macro_host, 'token': self.token_workspace,
                  'weapons': self.weapon_host, 'armor': self.armor_host,
                  'shopping': self.shopping_host, 'apothecary': self.apothecary_host}[tool]
        target.pack(fill='both', expand=True)
        self._style_titles()
        if tool == 'macro':
            self.macro.update_preview()
        elif tool == 'token':
            self.token_workspace.current.refresh_preview()

    def use_custom_weapon(self, profile):
        self.macro.apply_custom_weapon(profile)
        self.show_tool('macro')

    def show_release_notes(self, _event=None):
        self.release_info.show(self.info_button, f'{DISPLAY_NAME}\n{VERSAO}', RELEASE_NOTES)


def main():
    multiprocessing.freeze_support()
    if len(sys.argv) == 3 and sys.argv[1] == '--self-test':
        from integration_diagnostics import run_self_test
        return run_self_test(App, sys.argv[2])
    App().mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())
