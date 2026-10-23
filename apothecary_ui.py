"""🍀 Boticário Arcano: receitas de poções, óleos, granadas e pergaminhos."""
import tkinter as tk
from tkinter import ttk

from apothecary_core import (SPELLS, FORMS, find_spells, potion_forms, eligibility_text,
    ConsumableDesign, quote_consumable, consumable_description, consumable_item, consumable_macro,
    potion_enhancement_allowed)
from crafting_core import money, format_money
from fabrication_ui import CreatorPanel
from fabrication import Creator
from forge_ui import InfoPopup, info_button, QuoteCards, ModeToggle

BOOKS = {'Todos': 'Todos', 'Tormenta20 — Jogo do Ano': 'jda', 'Heróis de Arton': 'herois',
         'Deuses de Arton': 'deuses', 'Ameaças de Arton': 'ameacas', 'Guia de NPCs': 'npcs'}


class ApothecaryWorkshop(ttk.Frame):
    def __init__(self, master, app, on_back):
        super().__init__(master, padding=12)
        header = ttk.Frame(self)
        header.pack(fill='x', pady=(0, 8))
        ttk.Label(header, text='🍀 Boticário Arcano', style='Section.TLabel').pack(anchor='w')
        intro = ttk.Label(self, text='Poções incorporam aprimoramentos na fabricação. Pergaminhos guardam a magia básica; '
                  'os aprimoramentos são aplicados ao ler.', wraplength=1100)
        intro.pack(anchor='w', pady=(0,8))
        self.bind('<Configure>', lambda e: intro.configure(wraplength=max(240,e.width-24)) if e.widget == self else None, add='+')
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        self.potions = RecipePanel(self.notebook, app, scroll=False)
        self.scrolls = RecipePanel(self.notebook, app, scroll=True)
        self.notebook.add(self.potions, text='Poções')
        self.notebook.add(self.scrolls, text='Pergaminhos')
        from general_workshop_ui import GeneralWorkshopPanel
        self.general = GeneralWorkshopPanel(self.notebook, app)
        self.notebook.add(self.general, text='Oficina Geral')


class RecipePanel(ttk.Frame):
    def __init__(self, master, app, *, scroll):
        super().__init__(master, padding=(0, 6))
        self.app, self.scroll = app, scroll
        self._job = None
        self.result = None
        self._building = True
        self.fabricate_var = tk.BooleanVar(self, True)
        self.fabrication_widgets = []
        self.enhancement_vars, self.repeat_vars = {}, {}
        self.vars = {}
        self.info = InfoPopup(self)
        body = ttk.Panedwindow(self, orient='horizontal')
        body.pack(fill='both', expand=True)
        left, right = ttk.Frame(body, width=310), ttk.Frame(body)
        body.add(left, weight=1)
        body.add(right, weight=3)
        self.settings_tabs = ttk.Notebook(left)
        self.settings_tabs.pack(fill='both', expand=True)
        recipe_host = ttk.Frame(self.settings_tabs)
        self.settings_tabs.add(recipe_host, text='Receita')
        self.creator_panel = CreatorPanel(self.settings_tabs, app, self.schedule,
            scope='scroll' if scroll else 'potion')
        self.settings_tabs.add(self.creator_panel, text='Modificadores')
        settings = app.create_scrollable_panel(recipe_host, padx=4, pady=4)
        def field(key, label, default='', values=None):
            ttk.Label(settings, text=label, wraplength=280).pack(anchor='w', pady=(7, 2))
            var = self.vars[key] = tk.StringVar(self, default)
            widget = ttk.Combobox(settings, textvariable=var, values=values, state='readonly') if values else ttk.Entry(settings, textvariable=var)
            widget.pack(fill='x')
            return widget
        def check(key, label, default=False):
            self.vars[key] = tk.BooleanVar(self, default)
            widget = ttk.Checkbutton(settings, text=label, variable=self.vars[key])
            widget.pack(anchor='w', pady=4)
            self.fabrication_widgets.append(widget)
            ttk.Style(self).configure('Penalty.TCheckbutton',foreground='#b3261e')
            self.vars[key].trace_add('write',lambda *_: widget.configure(style='Penalty.TCheckbutton' if self.vars[key].get() else 'TCheckbutton'))
        field('name', 'Nome personalizado (opcional)')
        self.form_combo = field('kind', 'Tipo do item', 'Pergaminho' if scroll else 'Poção',
                               ('Pergaminho',) if scroll else FORMS)
        field('quantity', 'Quantidade de unidades', '1')
        if scroll:
            field('tradition', 'Tradição usada (escolha para Universal)', 'Arcana', ('Arcana', 'Divina'))
        check('double_batch', 'Produzir duas unidades por teste (–5)')
        field('extra_cost', 'Gasto adicional por unidade (T$)', '0')
        ttk.Label(settings, text='Gasto adicional: informe componentes, bebida especial e outros custos variáveis. '
                  'Confira também sacrifícios e requisitos escritos na magia. O preço mostrado usa o custo em PM sem descontos pessoais de conjuração.',
                  wraplength=280, style='Small.TLabel').pack(anchor='w', pady=8)
        self.mode_toggle = ModeToggle(self, self.fabricate_var)
        self.mode_toggle.pack(fill='x', before=body)
        self.cards = QuoteCards(self)
        self.cards.pack(fill='x', pady=(0,10), before=body)
        self.comparison_var = tk.StringVar(self)
        comparison = ttk.Label(self, textvariable=self.comparison_var, style='Small.TLabel', wraplength=850)
        comparison.pack(anchor='w', pady=(0,8), before=body)
        self.bind('<Configure>',lambda e: comparison.configure(wraplength=max(240,e.width-24)) if e.widget == self else None,add='+')
        filters = ttk.Frame(right)
        filters.pack(fill='x')
        self.search = tk.StringVar(self)
        ttk.Label(filters, text='Buscar magia:').pack(side='left')
        ttk.Entry(filters, textvariable=self.search).pack(side='left', fill='x', expand=True, padx=4)
        self.circle_filter = tk.StringVar(self, 'Todos')
        ttk.Combobox(filters, textvariable=self.circle_filter, values=('Todos', '1', '2', '3', '4', '5'),
                     state='readonly', width=7).pack(side='left')
        filter2 = ttk.Frame(right)
        filter2.pack(fill='x', pady=4)
        self.book_filter = tk.StringVar(self, 'Todos')
        book_combo = ttk.Combobox(filter2, textvariable=self.book_filter, values=tuple(BOOKS), state='readonly', width=16)
        self.type_filter = tk.StringVar(self, 'Todos')
        type_combo = ttk.Combobox(filter2, textvariable=self.type_filter, values=('Todos', 'Arcana', 'Divina'), state='readonly', width=12)
        filter_widgets = [book_combo,type_combo]
        self.form_filter = tk.StringVar(self, 'Todas')
        if not scroll:
            form_combo = ttk.Combobox(filter2, textvariable=self.form_filter,
                values=('Todas', *FORMS, 'Não permite poção'), state='readonly', width=16)
            filter_widgets.append(form_combo)
        def layout_filters(event):
            columns = max(1,min(len(filter_widgets),event.width//180))
            for column in range(len(filter_widgets)):
                filter2.columnconfigure(column,weight=1 if column<columns else 0)
            for index,widget in enumerate(filter_widgets):
                widget.grid(row=index//columns,column=index%columns,sticky='ew',padx=2,pady=2)
        for index,widget in enumerate(filter_widgets):
            widget.grid(row=0,column=index,sticky='ew',padx=2)
        filter2.bind('<Configure>',layout_filters)
        catalog = ttk.Panedwindow(right, orient='horizontal')
        catalog.pack(fill='both', expand=True)
        list_host = ttk.Frame(catalog, width=230)
        details_host = ttk.Frame(catalog)
        catalog.add(list_host, weight=1)
        catalog.add(details_host, weight=3)
        self.tree = ttk.Treeview(list_host, show='tree', selectmode='browse')
        self.tree.tag_configure('circle_header',font=('Segoe UI',10,'bold'),foreground='#315ee7')
        bar = ttk.Scrollbar(list_host, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=bar.set)
        bar.pack(side='right', fill='y')
        self.tree.pack(fill='both', expand=True)
        self.count_var = tk.StringVar(self)
        ttk.Label(list_host, textvariable=self.count_var, style='Small.TLabel').pack(anchor='w')
        self.detail_tabs = ttk.Notebook(details_host)
        self.detail_tabs.pack(fill='both', expand=True)
        details = ttk.Frame(self.detail_tabs)
        self.detail_tabs.add(details, text='Magia e aprimoramentos')
        self.details = app.create_scrollable_panel(details, padx=8, pady=6)
        preview_host = ttk.Frame(self.detail_tabs)
        self.detail_tabs.add(preview_host, text='Resultado / regras de uso')
        self.preview = tk.Text(preview_host, wrap='word', width=30, height=8, font=('Segoe UI', 10))
        preview_bar = ttk.Scrollbar(preview_host, command=self.preview.yview)
        self.preview.configure(yscrollcommand=preview_bar.set)
        preview_bar.pack(side='right', fill='y')
        self.preview.pack(fill='both', expand=True)
        footer = ttk.Frame(self, padding=(0, 6, 0, 0))
        footer.pack(side='bottom',fill='x',before=body)
        footer_details = ttk.Frame(footer)
        footer_details.pack(fill='x')
        self.summary_var = tk.StringVar(self)
        self.error_var = tk.StringVar(self)
        self.summary_label = ttk.Label(footer_details, textvariable=self.summary_var, wraplength=1150)
        self.error_label = ttk.Label(footer_details, textvariable=self.error_var, wraplength=1150, foreground='#b3261e')
        actions = ttk.Frame(footer)
        actions.pack(fill='x')
        self.add_button = ttk.Button(actions, text='Adicionar ao inventário', style='Primary.TButton', command=self.add_inventory)
        self.add_button.pack(side='right')
        self.copy_button = ttk.Button(actions, text='Copiar macro do item', command=self.copy_macro)
        self.copy_button.pack(side='right', padx=5)
        self.status_var = tk.StringVar(self)
        ttk.Label(actions, textvariable=self.status_var, wraplength=600).pack(side='left')
        self.tree.bind('<<TreeviewSelect>>', self.select_spell)
        for var in (self.search, self.circle_filter, self.book_filter, self.type_filter, self.form_filter):
            var.trace_add('write', self.filter_spells)
        for var in self.vars.values():
            var.trace_add('write', self.schedule)
        self.fabricate_var.trace_add('write', self.schedule)
        self._building = False
        self.spell_id = ''
        self.filter_spells()

    def filter_spells(self, *_):
        rows = find_spells(self.search.get(), self.circle_filter.get(), BOOKS[self.book_filter.get()], self.type_filter.get())
        shape = self.form_filter.get()
        if shape != 'Todas':
            rows = [s for s in rows if (shape in potion_forms(s) if shape != 'Não permite poção' else not potion_forms(s))]
        previous = self.tree.selection()
        self.tree.delete(*self.tree.get_children())
        for circle in range(1,6):
            group = [s for s in rows if s['circle'] == circle]
            if not group:
                continue
            parent = f'circle:{circle}'
            self.tree.insert('', 'end', iid=parent, text=f'{circle}º círculo · {len(group)} magias', open=True,tags=('circle_header',))
            for s in group:
                self.tree.insert(parent, 'end', iid=s['id'], text=s['name'], tags=(s['book'],))
        self.count_var.set(f'{len(rows)} de {len(SPELLS)} magias')
        chosen = previous[0] if previous and previous[0] in SPELLS and self.tree.exists(previous[0]) else rows[0]['id'] if rows else ''
        if chosen:
            self.tree.selection_set(chosen)
            self.select_spell()
        else:
            self.spell_id = ''
            self.result = None
            for w in self.details.winfo_children():
                w.destroy()
            self.refresh()

    def select_spell(self, _event=None):
        selection = self.tree.selection()
        if not selection or selection[0] not in SPELLS or selection[0] == self.spell_id:
            return
        self.spell_id = selection[0]
        spell = SPELLS[self.spell_id]
        if self.scroll and spell['tradition'] != 'Universal':
            self.vars['tradition'].set(spell['tradition'])
        for w in self.details.winfo_children():
            w.destroy()
        self.enhancement_vars, self.repeat_vars = {}, {}
        ttk.Label(self.details, text=spell['name'], style='Section.TLabel', wraplength=430).pack(anchor='w')
        def label(text):
            widget = ttk.Label(self.details, text=text, wraplength=430, justify='left')
            widget.pack(anchor='w', fill='x', pady=5)
            widget.bind('<Configure>', lambda e: widget.configure(wraplength=max(120, e.width-12)))
        label(f"{spell['tradition']} {spell['circle']} · {spell['school']}\n{spell['source']}\n{spell['stats']}")
        label(spell['description'])
        self.eligibility_var = tk.StringVar(self)
        ttk.Label(self.details, textvariable=self.eligibility_var, wraplength=430, style='Small.TLabel').pack(anchor='w', pady=6)
        label('Aprimoramentos na ativação (não alteram o pergaminho fabricado)' if self.scroll else 'Aprimoramentos incorporados à poção')
        for e in spell['enhancements']:
            if not self.scroll and not potion_enhancement_allowed(e):
                continue
            row = ttk.Frame(self.details)
            row.pack(fill='x', pady=5)
            var = self.enhancement_vars[e['id']] = tk.BooleanVar(self, False)
            ttk.Checkbutton(row, variable=var).grid(row=0, column=0, sticky='n')
            text = ttk.Label(row, text=e['text'], wraplength=370, cursor='hand2')
            text.grid(row=0, column=1, sticky='ew')
            row.columnconfigure(1, weight=1)
            info_button(row, self.info, 'Aprimoramento', e['text']).grid(row=0, column=2, sticky='ne', padx=(3,0))
            text.bind('<Button-1>', lambda _, v=var: v.set(not v.get()))
            text.bind('<Configure>', lambda event, widget=text: widget.configure(wraplength=max(120, event.width-8)))
            if e['repeatable']:
                repeat = self.repeat_vars[e['id']] = tk.StringVar(self, '1')
                ttk.Spinbox(row, from_=1, to=100, textvariable=repeat, width=5).grid(row=1, column=1, sticky='w')
                repeat.trace_add('write', self.schedule)
            var.trace_add('write', self.schedule)
        label('Aprimoramentos de poderes gerais')
        for name, cost in (('Magia Ampliada', 2), ('Magia Acelerada', 4), ('Magia Discreta', 2)):
            if not self.scroll and name in ('Magia Acelerada','Magia Discreta'):
                continue
            var = self.enhancement_vars[name] = tk.BooleanVar(self, False)
            row = ttk.Frame(self.details)
            row.pack(fill='x', pady=3)
            ttk.Checkbutton(row, text=f'{name} (+{cost} PM)', variable=var).pack(side='left')
            description = {'Magia Ampliada':'Aumenta o alcance em um passo ou dobra a área.',
                           'Magia Acelerada':'Muda a execução para livre, uma vez por rodada.',
                           'Magia Discreta':'Sem gestos nem palavras.'}[name]
            info_button(row, self.info, name, description+f' Acréscimo de {cost} PM à receita. T20, p. 131.').pack(side='right')
            var.trace_add('write', self.schedule)
        forms = potion_forms(spell)
        if forms and not self.scroll:
            self.vars['kind'].set(forms[0])
        self.vars['extra_cost'].set('0')
        self.schedule()

    def get_design(self):
        v = self.vars
        try:
            quantity = int(v['quantity'].get())
            selections = tuple((key, int(self.repeat_vars[key].get()) if key in self.repeat_vars else 1)
                               for key, var in self.enhancement_vars.items() if var.get())
        except ValueError:
            raise ValueError('Quantidade e repetições devem ser números inteiros.') from None
        return ConsumableDesign(self.spell_id, kind=v['kind'].get(), name=v['name'].get(),
            enhancements=selections, quantity=quantity,
            double_batch=v['double_batch'].get() if self.fabricate_var.get() else False, extra_cost=money(v['extra_cost'].get()),
            magic_tradition=v['tradition'].get() if self.scroll else SPELLS[self.spell_id]['tradition'])

    def schedule(self, *_):
        if not self._building and self._job is None:
            self._job = self.after_idle(self.refresh)

    def item_characteristics(self, design, quote):
        from apothecary_core import effective_parameters
        s = quote.spell
        params = effective_parameters(s, quote.selected)
        stats = f'{design.kind} · {s["circle"]}º círculo · {s["tradition"]}'
        stats += '\n'+('Magia básica: ' if self.scroll else 'Fórmula: ')+f'{quote.pm} PM'
        stats += '\n'+' · '.join(params[k] for k in ('target','area','duration') if params[k])
        effects = ''
        if quote.selected:
            effects = 'Plano de ativação:\n' if self.scroll else 'Aprimoramentos incorporados:\n'
            effects += '\n\n'.join(f"{e['repeats']}× {e['text']}" for e in quote.selected)
            effects += '\n\nMagia básica:\n'
        effects += s['description']
        hint = (f'Aprimoramentos na leitura: +{quote.activation_pm} PM' if self.scroll
                else 'Aprimoramentos incluídos na fórmula')
        return stats, effects, hint

    def refresh(self):
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None
        self.result = None
        preview = ''
        fabricating = self.fabricate_var.get()
        self.cards.set_mode(fabricating)
        if not fabricating:
            self.settings_tabs.select(0)
        self.settings_tabs.tab(self.creator_panel, state='normal' if fabricating else 'disabled')
        self.settings_tabs.tab(0, text='Receita' if fabricating else 'Item')
        for widget in self.fabrication_widgets:
            widget.configure(state='normal' if fabricating else 'disabled')
        try:
            if not self.spell_id:
                raise ValueError('Nenhuma magia corresponde aos filtros.')
            design = self.get_design()
            creator = self.creator_panel.get_creator() if fabricating else Creator()
            from apothecary_core import selected_enhancements
            selected = selected_enhancements(SPELLS[self.spell_id], design, creator)
            self.eligibility_var.set(eligibility_text(SPELLS[self.spell_id], selected))
            quote = quote_consumable(design, creator, purchase=not fabricating)
            f = quote.fabrication
            characteristics, effects, stats_hint = self.item_characteristics(design, quote)
            if fabricating:
                self.cards.show_quote(f, quote.unit_cost, quote.market_price, design.quantity)
                self.cards.set_characteristics(characteristics, effects, stats_hint=stats_hint)
                self.summary_var.set(f'Fabricando · Lote de {design.quantity}: {format_money(f.cost)} · Fórmula: {quote.pm} PM'
                    + (f' · Lote duplo: {f.penalty:+d} no teste' if f.penalty else ''))
                from dataclasses import replace
                base = quote_consumable(replace(design, unstable=False, special_drink=False), Creator())
                if f.dc is not None and base.fabrication.dc is not None:
                    self.cards.highlight_dc_increase(f.dc-base.fabrication.dc)
                self.comparison_var.set('Sem modificadores: '+format_money(base.unit_cost)+
                    f' / unidade · CD {base.fabrication.dc_label} · {base.fabrication.time_label}')
            else:
                self.cards.show_purchase(quote.market_price, characteristics, effects, quantity=design.quantity,
                    stats_hint=stats_hint)
                self.summary_var.set(f'Comprando · {design.quantity}× {design.kind} · Total: {format_money(quote.market_price*design.quantity)}')
                self.comparison_var.set('O pergaminho contém a magia básica; escolha os aprimoramentos para planejar a leitura.' if self.scroll else '')
            self.error_var.set('')
            preview = consumable_description(design, quote, purchase=not fabricating)
            self.result = design, creator, quote
        except ValueError as error:
            self.result = None
            self.cards.clear()
            self.comparison_var.set('')
            self.summary_var.set('Confira a composição da receita.')
            self.error_var.set(str(error))
            if self.spell_id:
                self.eligibility_var.set(eligibility_text(SPELLS[self.spell_id]))
        self.summary_label.pack_forget()
        self.error_label.pack_forget()
        if not fabricating:
            self.summary_label.pack(anchor='w')
        if self.error_var.get():
            self.error_label.pack(anchor='w', pady=3)
        self.preview.configure(state='normal')
        self.preview.delete('1.0', 'end')
        self.preview.insert('1.0', preview)
        self.preview.configure(state='disabled')
        self.add_button.configure(state='normal' if self.result else 'disabled')
        self.copy_button.configure(state='normal' if self.result else 'disabled')


    def add_inventory(self):
        self.refresh()
        if not self.result:
            return
        d, c, q = self.result
        try:
            item = consumable_item(d, c, q, purchase=not self.fabricate_var.get())
            self.app.add_inventory_item(item, d.quantity)
            self.status_var.set(f'{d.quantity}× {item["name"]}: inventário salvo.' + (' Expira no fim da cena.' if q.fabrication.temporary else ''))
        except (OSError, ValueError) as error:
            self.status_var.set(str(error))

    def copy_macro(self):
        self.refresh()
        if self.result:
            d, c, q = self.result
            self.clipboard_clear()
            self.clipboard_append(consumable_macro(d, q, purchase=not self.fabricate_var.get()))
            self.status_var.set('Macro do item copiada.')

    def destroy(self):
        self.info.hide()
        if self._job is not None:
            self.after_cancel(self._job)
        super().destroy()
