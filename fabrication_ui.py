"""Modificadores opcionais de fabricação; não representa uma ficha de personagem."""
import tkinter as tk
from tkinter import ttk

from fabrication import POWERS, DISTINCTIONS, Creator
from forge_ui import InfoPopup, info_button, set_visible


class CreatorPanel(ttk.Frame):
    def __init__(self, master, app, on_change, *, powers=(), equipment=False, scope=None):
        super().__init__(master)
        self.variables, self.power_vars, self.distinction_vars = {}, {}, {}
        self.distinction_fields = {}
        self.scope = scope or ('equipment' if equipment else 'potion')
        self.info = InfoPopup(self)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        power_host, distinction_host = ttk.Frame(self.notebook), ttk.Frame(self.notebook)
        self.notebook.add(power_host, text='Poderes e raças')
        self.notebook.add(distinction_host, text='Distinções')
        content = app.create_scrollable_panel(power_host, padx=6, pady=6)
        other = app.create_scrollable_panel(distinction_host, padx=6, pady=6)
        ttk.Label(content, text='Compare os modificadores do orçamento.', style='Small.TLabel', wraplength=270).pack(anchor='w', pady=(0,8))
        if self.scope in ('equipment','weapon','armor'):
            row = ttk.Frame(content)
            row.pack(fill='x', pady=(0,8))
            ttk.Label(row, text='Raça').pack(side='left')
            info_button(row, self.info, 'Metalurgia Hobgoblin', 'Hobgoblins com outra habilitação para fabricar superiores pagam ¼ do preço das melhorias em vez de ⅓. Não altera o preço-base nem os encantos. A habilitação é presumida. Ameaças de Arton, p. 84.').pack(side='right')
            self.variables['race'] = tk.StringVar(self, 'Outra')
            ttk.Combobox(content, textvariable=self.variables['race'], values=('Outra','Hobgoblin'), state='readonly').pack(fill='x', pady=(0,8))
        allowed = {
            'potion': {'potion','alchemical'}, 'scroll': {'scroll'},
            'general': {'alchemical','equipment'}, 'equipment': {'equipment'},
            'weapon': {'equipment'}, 'armor': {'equipment'},
        }[self.scope]
        def option(host, name, description, variables):
            row = ttk.Frame(host)
            row.pack(fill='x', pady=4)
            var = variables[name] = tk.BooleanVar(self, name in powers)
            control = ttk.Checkbutton(row, text=name, variable=var)
            control.pack(side='left', fill='x', expand=True)
            info_button(row, self.info, name, description).pack(side='right')
            var.trace_add('write', on_change)
            if 'CD +5' in description:
                ttk.Style(self).configure('Penalty.TCheckbutton', foreground='#b3261e')
                var.trace_add('write', lambda *_: control.configure(style='Penalty.TCheckbutton' if var.get() else 'TCheckbutton'))
        for name, (kind, description) in POWERS.items():
            if kind in allowed and name != 'Gênio Inovador':
                option(content, name, description, self.power_vars)
        if self.scope in ('equipment','weapon','armor'):
            ttk.Label(content, text='Gênio Inovador está nas opções de materiais do item.', style='Small.TLabel', wraplength=270).pack(anchor='w', pady=8)
        scopes = {
            'potion': {'potion','alchemical'}, 'scroll': set(),
            'general': {'alchemical','prepared','food'}, 'equipment': {'weapon','firearm'},
            'weapon': {'weapon','firearm'}, 'armor': set(),
        }[self.scope]
        group = ''
        for name, entry in DISTINCTIONS.items():
            if entry['scope'] not in scopes:
                continue
            if entry['group'] != group:
                group = entry['group']
                ttk.Label(other, text=group, style='Section.TLabel').pack(anchor='w', pady=(10,4))
            option(other, name, entry['description']+'\n\n'+entry['source'], self.distinction_vars)
            self.distinction_fields[name] = ttk.Frame(other)
        if not self.distinction_vars:
            ttk.Label(other, text='Nos livros consultados, nenhuma distinção altera diretamente o orçamento desta categoria.', wraplength=270, style='Small.TLabel').pack(anchor='w', pady=8)
        if 'Forja Devocional' in self.distinction_vars:
            host = self.distinction_fields['Forja Devocional']
            ttk.Label(host,text='Forja Devocional: CD da arma doadora',wraplength=270).pack(anchor='w',pady=(10,3))
            self.variables['transfer_dc']=tk.StringVar(self)
            ttk.Entry(host,textvariable=self.variables['transfer_dc']).pack(fill='x')
            self.distinction_vars['Forja Devocional'].trace_add('write',
                lambda *_: set_visible(host, self.distinction_vars['Forja Devocional'].get()))
        for var in self.variables.values():
            var.trace_add('write', on_change)

    def get_creator(self):
        dc=None
        if 'Forja Devocional' in self.distinction_vars and self.distinction_vars['Forja Devocional'].get():
            text=self.variables['transfer_dc'].get().strip()
            if text:
                try:
                    dc=int(text)
                except ValueError:
                    raise ValueError('A CD da arma doadora deve ser um número inteiro.') from None
        return Creator(race=self.variables['race'].get() if 'race' in self.variables else 'Outra',
            powers=tuple(n for n,v in self.power_vars.items() if v.get()),
            distinctions=tuple(n for n,v in self.distinction_vars.items() if v.get()),transfer_dc=dc)

    def destroy(self):
        self.info.hide()
        super().destroy()
