"""SHOPING: navegação por catálogo e inventário com quantidades e carga."""
import tkinter as tk
from decimal import Decimal
from tkinter import ttk, messagebox

from crafting_core import money, format_money
from shopping_core import CATALOGS, decimal_text, filter_items, item_info, item_characteristics
from weapon_ui import WeaponInfoPopup
from forge_ui import QuoteCards


CATALOG_GROUPS = {
    "Armas": {"Armas simples": "Simples", "Armas marciais": "Marciais", "Armas exóticas": "Exóticas",
              "Armas de fogo": "De fogo", "Armas mágicas": "Mágicas", "Munições": "Munições"},
    "Armaduras e escudos": {"Armaduras e escudos": "Comuns e escudos", "Armaduras mágicas": "Mágicas"},
    "Esotéricos": {"Esotéricos": "Comuns", "Esotéricos mágicos": "Mágicos"},
}


class ShoppingCards(QuoteCards):
    """Resumo do inventário exclusivo do Shopping, com o visual das oficinas."""

    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self._inventory_quote = None
        self.purchase_bargain_var = tk.IntVar(self, 0)
        self.resale_bargain_var = tk.IntVar(self, 0)
        self.bargain_rows = []
        self.bargain_buttons = {}
        for index, variable in ((0, self.purchase_bargain_var), (2, self.resale_bargain_var)):
            row = tk.Frame(self.labels[index].master, bg='#eef3ff')
            self.bargain_rows.append(row)
            for percent in (10, 20):
                button = tk.Checkbutton(row, text=f'Barganha {percent}%', variable=variable,
                    onvalue=percent, offvalue=0, bg='#eef3ff', activebackground='#eef3ff',
                    selectcolor='#eef3ff', font=('Segoe UI', 9), anchor='w')
                button.pack(anchor='w')
                self.bargain_buttons[index, percent] = button
            variable.trace_add('write', self._refresh_bargains)

    def set_mode(self, fabricating):
        super().set_mode(fabricating)
        self._inventory_quote = None
        for row in self.bargain_rows:
            row.pack_forget()

    def _refresh_bargains(self, *_args):
        if self._inventory_quote is not None:
            self.show_inventory(*self._inventory_quote)

    def show_inventory(self, inventory, selected=None):
        self.set_mode(False)
        self.clear()
        self._inventory_quote = inventory, selected
        totals = inventory.totals()
        purchase_percent = self.purchase_bargain_var.get()
        resale_percent = self.resale_bargain_var.get()
        purchase = totals.cost * (Decimal(100) - purchase_percent) / 100
        purchase_hint = (f'Sem barganha: {format_money(totals.cost)} · Desconto de {purchase_percent}%'
                         if purchase_percent else 'Total a pagar pelos itens do inventário')
        if totals.missing_price:
            purchase_hint += f'\n{totals.missing_price} unidade(s) com preço pendente · Total parcial'
        if selected is not None:
            full_price = selected.item.get('full_price')
            reference = money(full_price) if full_price is not None else selected.unit_price
            missing_resale = int(reference is None)
            resale_hint = f"{selected.item['name']} · 1 unidade / pacote"
        else:
            reference = totals.value
            missing_resale = sum(row.quantity for row in inventory.lines
                                if row.unit_price is None and row.item.get('full_price') is None)
            resale_hint = f'Inventário total · {totals.quantity} unidades / pacotes'
        resale = None if reference is None else reference * Decimal('0.5') * (Decimal(100) + resale_percent) / 100
        if reference is not None:
            resale_hint += f'\n50% de {format_money(reference)}'
        if resale_percent:
            resale_hint += f' · Barganha +{resale_percent}%'
        if missing_resale:
            resale_hint += (f'\n{missing_resale} unidade(s) com valor pendente'
                            + (' · Total parcial' if selected is None else ''))
        metrics = (
            ("GASTO CONHECIDO" if totals.missing_price else "GASTO TOTAL",
             format_money(purchase), purchase_hint, bool(totals.missing_price)),
            ("CARGA CONHECIDA" if totals.missing_spaces else "CARGA TOTAL",
             f"{decimal_text(totals.spaces)} espaços",
             f"{totals.missing_spaces} unidade(s) com carga pendente · Total parcial"
             if totals.missing_spaces else "Carga de todos os itens do inventário",
             bool(totals.missing_spaces)),
            ("REVENDA", 'Pendente' if resale is None else format_money(resale),
             resale_hint, bool(missing_resale)),
        )
        for i, (title, value, hint, pending) in enumerate(metrics):
            self.titles[i].set(title)
            self.values[i].set(value)
            self.hints[i].set(hint)
            self.labels[i].configure(font=("Segoe UI", 15, "bold"),
                                     fg="#ae5510" if pending else "#244cc0")
            self.captions[i].configure(fg="#ae5510" if pending else "#52678e")
        for row in self.bargain_rows:
            row.pack(fill='x', pady=(6, 0))


class ShoppingWorkshop(ttk.Frame):
    PAGE_SIZE = 24

    def __init__(self, master, app, on_back):
        super().__init__(master, padding=12)
        self.app = app
        self.inventory = app.get_inventory()
        self.info = WeaponInfoPopup(self.winfo_toplevel())
        self.bind("<Unmap>", lambda e: self.info.hide() if e.widget == self else None)
        self.category = "Todos"
        self.page = 0
        self.catalog_rows = []
        self.category_buttons = {}
        self.group_buttons = {}
        self.group_panels = {}
        self.expanded_groups = set()
        self.category_groups = {category: group for group, categories in CATALOG_GROUPS.items()
                                for category in categories}
        self.search_var = tk.StringVar(self)
        self.quantity_var = tk.StringVar(self, "1")
        self.price_var = tk.StringVar(self)
        self.spaces_var = tk.StringVar(self)
        self.status_var = tk.StringVar(self)
        self.selection_var = tk.StringVar(self, "Selecione um item para editar a quantidade, o preço ou a carga.")

        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 6))
        ttk.Label(header, text="🛒 SHOPING", style="Section.TLabel").pack(side="left")
        ttk.Label(self, text="Monte suas compras e acompanhe o gasto e a carga. Passe o mouse no ⓘ para ver os detalhes.",
                  wraplength=1000).pack(anchor="w", pady=(0, 8))
        self.item_title_var = tk.StringVar(self,'Selecione um item para ver preço e características')
        self.item_title_label = ttk.Label(self,textvariable=self.item_title_var,style='Section.TLabel',wraplength=1000)
        self.item_title_label.pack(anchor='w',pady=(0,4))
        self.item_cards = ShoppingCards(self,expandable=False)
        self.item_cards.effects.configure(height=3)
        self.item_cards.pack(fill='x',pady=(0,8))
        self.status_label = ttk.Label(self, textvariable=self.status_var, wraplength=1100)
        self._catalog_preview_item = None
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        catalog_tab = ttk.Frame(self.notebook)
        inventory_tab = ttk.Frame(self.notebook, padding=8)
        self.notebook.add(catalog_tab, text="Catálogos")
        self.notebook.add(inventory_tab, text="Meu inventário")
        self.notebook.bind("<<NotebookTabChanged>>", self._tab_changed)

        menu_panel = ttk.Frame(catalog_tab, width=218)
        menu_panel.pack(side="left", fill="y", padx=(0, 10))
        menu_panel.pack_propagate(False)
        menu = app.create_scrollable_panel(menu_panel)
        for name in ("Todos", "Customizados", *CATALOGS):
            group = self.category_groups.get(name)
            if group:
                if group in self.group_buttons:
                    continue
                section = ttk.Frame(menu)
                section.pack(fill="x")
                button = ttk.Button(section, text=group, command=lambda g=group: self.toggle_category_group(g))
                button.pack(fill="x", pady=2)
                self.group_buttons[group] = button
                children = ttk.Frame(section, padding=(14, 0, 0, 0))
                self.group_panels[group] = children
                for category, label in CATALOG_GROUPS[group].items():
                    child = ttk.Button(children, text=label, command=lambda n=category: self.choose_category(n))
                    child.pack(fill="x", pady=2)
                    self.category_buttons[category] = child
                continue
            button = ttk.Button(menu, text=name, command=lambda n=name: self.choose_category(n))
            button.pack(fill="x", pady=2)
            self.category_buttons[name] = button
        products = ttk.Frame(catalog_tab, padding=(0, 8, 0, 0))
        products.pack(side="left", fill="both", expand=True)
        search = ttk.Frame(products)
        search.pack(fill="x", pady=(0, 6))
        ttk.Label(search, text="Buscar:").pack(side="left", padx=(0, 6))
        ttk.Entry(search, textvariable=self.search_var).pack(side="left", fill="x", expand=True)
        self.catalog_title = ttk.Label(products, text="", style="Section.TLabel", wraplength=800)
        self.catalog_title.pack(anchor="w")
        ttk.Label(products, text="Clique no item ou no + para adicionar uma unidade/pacote. Itens vermelhos são especiais.",
                  wraplength=800, style="Small.TLabel").pack(anchor="w", pady=(3, 6))
        self.catalog_list = app.create_scrollable_panel(products, padx=(0, 6))
        navigation = ttk.Frame(products)
        navigation.pack(fill="x", pady=(6, 4))
        self.previous_button = ttk.Button(navigation, text="← Anterior", command=lambda: self.change_page(-1))
        self.previous_button.pack(side="left")
        self.page_var = tk.StringVar(self)
        ttk.Label(navigation, textvariable=self.page_var).pack(side="left", padx=10)
        self.next_button = ttk.Button(navigation, text="Próxima →", command=lambda: self.change_page(1))
        self.next_button.pack(side="left")
        self.catalog_clear_button = ttk.Button(navigation, text="Limpar", command=self.clear_inventory)
        self.catalog_clear_button.pack(side="right")

        self.selection_label = ttk.Label(inventory_tab, textvariable=self.selection_var, wraplength=1100)
        self.selection_label.pack(anchor="w", pady=(0, 6))
        tree_panel = ttk.Frame(inventory_tab)
        tree_panel.pack(fill="both", expand=True)
        columns = ("info", "name", "quantity", "price", "subtotal", "spaces", "load")
        self.inventory_tree = ttk.Treeview(tree_panel, columns=columns, show="headings", selectmode="browse", height=12)
        headings = ("ⓘ", "Item", "Qtd.", "A pagar / un.", "Subtotal", "Espaços / un.", "Carga total")
        widths = (35, 290, 65, 135, 135, 105, 105)
        for col, title, width in zip(columns, headings, widths):
            self.inventory_tree.heading(col, text=title)
            self.inventory_tree.column(col, width=width, minwidth=width if col != "name" else 150,
                                       stretch=col == "name", anchor="w" if col == "name" else "center")
        yscroll = ttk.Scrollbar(tree_panel, orient="vertical", command=self.inventory_tree.yview)
        xscroll = ttk.Scrollbar(tree_panel, orient="horizontal", command=self.inventory_tree.xview)
        self.inventory_tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.inventory_tree.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        tree_panel.rowconfigure(0, weight=1)
        tree_panel.columnconfigure(0, weight=1)
        self.inventory_tree.tag_configure("special", foreground="#c13232")
        self.inventory_tree.bind("<<TreeviewSelect>>", self._selected)
        self.inventory_tree.bind("<Button-1>", self._inventory_click)
        self.inventory_tree.bind("<Escape>", self._clear_selection)
        self.inventory_tree.bind("<Motion>", self._tree_info)
        self.inventory_tree.bind("<Leave>", self.info.schedule_hide)
        self.inventory_tree.bind("<ButtonRelease-1>", self._tree_info)
        self._tooltip_key = None

        inventory_controls = ttk.Frame(inventory_tab)
        inventory_controls.pack(side='bottom',fill='x',before=tree_panel)
        form = ttk.Frame(inventory_controls)
        form.pack(fill="x", pady=(8, 0))
        for column, (title, variable, width) in enumerate((("Quantidade", self.quantity_var, 9),
                    ("A pagar por unidade (T$)", self.price_var, 22), ("Espaços por unidade", self.spaces_var, 18))):
            ttk.Label(form, text=title).grid(row=0, column=column, sticky="w", padx=(0, 10))
            ttk.Entry(form, textvariable=variable, width=width).grid(row=1, column=column, sticky="ew", padx=(0, 10))
            form.columnconfigure(column, weight=1)
        actions = ttk.Frame(inventory_controls)
        actions.pack(fill="x", pady=(8, 4))
        self.apply_button = ttk.Button(actions, text="Aplicar alterações", command=self.update_selected)
        self.apply_button.pack(side="left", padx=(0, 6))
        self.minus_button = ttk.Button(actions, text="−1", width=4, command=lambda: self.adjust_quantity(-1))
        self.minus_button.pack(side="left", padx=(0, 4))
        self.plus_button = ttk.Button(actions, text="+1", width=4, command=lambda: self.adjust_quantity(1))
        self.plus_button.pack(side="left", padx=(0, 6))
        self.remove_button = ttk.Button(actions, text="Remover", command=self.remove_selected)
        self.remove_button.pack(side="left", padx=(0, 6))
        self.clear_button = ttk.Button(actions, text="Limpar", command=self.clear_inventory)
        self.clear_button.pack(side="left", padx=(0, 6))
        self.selected_info_button = ttk.Button(actions, text="ⓘ", width=3, command=self.show_selected_info)
        self.selected_info_button.pack(side="left")
        self.selected_info_button.bind("<Leave>", self.info.schedule_hide)
        ttk.Label(inventory_controls, text="Deixe preço ou espaços em branco para manter a pendência. Informe 0 se não houver custo ou carga.",
                  style="Small.TLabel", wraplength=1050).pack(anchor="w", pady=(4, 0))

        self.bind("<Configure>", self._resize, add="+")
        self.search_var.trace_add("write", lambda *_: self.choose_category(self.category))
        self.refresh()
        if self.inventory.lines:
            self.notebook.select(1)

    def _resize(self, event):
        if event.widget == self:
            for label in (self.status_label, self.selection_label, self.item_title_label):
                label.configure(wraplength=max(240, event.width - 40))

    def choose_category(self, name):
        group = self.category_groups.get(name)
        if group and group not in self.expanded_groups:
            self.expanded_groups.add(group)
            self.group_panels[group].pack(fill="x")
        self.category, self.page = name, 0
        self.refresh_catalog()

    def toggle_category_group(self, name):
        if name in self.expanded_groups:
            self.expanded_groups.remove(name)
            self.group_panels[name].pack_forget()
        else:
            self.expanded_groups.add(name)
            self.group_panels[name].pack(fill="x")
        self._refresh_category_buttons()

    def _refresh_category_buttons(self):
        for name, button in self.category_buttons.items():
            count = sum(len(rows) for rows in CATALOGS.values()) + len(self.inventory.custom_items) if name == "Todos" else (
                len(self.inventory.custom_items) if name == "Customizados" else len(CATALOGS[name]))
            group = self.category_groups.get(name)
            label = CATALOG_GROUPS[group][name] if group else name
            button.configure(text=f"{label} ({count})", style="Primary.TButton" if name == self.category else "TButton")
        for name, button in self.group_buttons.items():
            count = sum(len(CATALOGS[category]) for category in CATALOG_GROUPS[name])
            arrow = "▾" if name in self.expanded_groups else "▸"
            button.configure(text=f"{arrow} {name} ({count})",
                             style="Primary.TButton" if self.category in CATALOG_GROUPS[name] else "TButton")

    def change_page(self, delta):
        self.page += delta
        self.refresh_catalog()

    def refresh_catalog(self):
        self.info.hide()
        self._tooltip_key = None
        items = filter_items(self.category, self.search_var.get(), self.inventory.custom_items.values())
        pages = max(1, (len(items) + self.PAGE_SIZE - 1) // self.PAGE_SIZE)
        self.page = max(0, min(self.page, pages - 1))
        for child in self.catalog_list.winfo_children():
            child.destroy()
        self.catalog_rows = []
        self.catalog_title.configure(text=f"{self.category} · {len(items)} itens")
        self._refresh_category_buttons()
        start = self.page * self.PAGE_SIZE
        for item in items[start:start + self.PAGE_SIZE]:
            row = ttk.Frame(self.catalog_list, padding=(0, 6))
            row.pack(fill="x")
            row.columnconfigure(0, weight=1)
            ttk.Label(row, text=item["name"], wraplength=430,
                      foreground="#c13232" if item["special"] else "#24324b").grid(row=0, column=0, sticky="w")
            price = ("ESPECIAL · " + (item.get("price") or "Sem preço") if item["special"] else
                     format_money(money(item["price_value"])))
            if item.get("full_price"):
                price = f"A pagar: {price} · Valor: {item['price']}"
            spaces = "Pendente" if item["spaces_value"] is None else decimal_text(money(item["spaces_value"]))
            ttk.Label(row, text=f"{price} · Espaços: {spaces}", wraplength=430,
                      foreground="#c13232" if item["special"] else "#59677f").grid(row=1, column=0, sticky="w")
            icon = ttk.Button(row, text="ⓘ", width=3)
            icon.grid(row=0, column=1, rowspan=2, padx=(6, 3))
            self.info.attach(icon, item_info(item))
            for widget in (row, *row.winfo_children()):
                widget.bind('<Enter>', lambda _, i=item: self.show_catalog_item(i), add='+')
            add = ttk.Button(row, text="+", width=3, command=lambda i=item: self.add_item(i))
            add.grid(row=0, column=2, rowspan=2)
            # Bindings do contêiner não propagam aos filhos no Tk. Apenas o
            # cartão e seus textos compram; ⓘ mantém sua ação independente.
            for widget in (row, *[w for w in row.winfo_children() if isinstance(w, ttk.Label)]):
                widget.configure(cursor="hand2")
                widget.bind("<Button-1>", lambda _e, i=item: self.add_item(i))
            row.bind("<Configure>", lambda event, r=row: [w.configure(wraplength=max(100, event.width - 110))
                     for w in r.winfo_children() if isinstance(w, ttk.Label)])
            self.catalog_rows.append((item, row, icon, add))
        if not items:
            ttk.Label(self.catalog_list, text="Nenhum item encontrado." if self.category != "Customizados" else
                      "Use Adicionar ao inventário nas oficinas de equipamentos ou no Boticário Arcano.", wraplength=450).pack(anchor="w", pady=12)
        self._refresh_cards()
        self.page_var.set(f"{self.page + 1} / {pages}")
        self.previous_button.configure(state="normal" if self.page else "disabled")
        self.next_button.configure(state="normal" if self.page + 1 < pages else "disabled")
        canvas = self.catalog_list.master
        canvas.yview_moveto(0)

    def refresh(self):
        self.refresh_catalog()
        self.refresh_inventory()
        if self.inventory.load_error:
            self.set_status(self.inventory.load_error, error=True)

    def refresh_inventory(self):
        selected = self.inventory_tree.selection()
        self.info.hide()
        self._tooltip_key = None
        self.inventory_tree.delete(*self.inventory_tree.get_children())
        for row in self.inventory.lines:
            cost = "Pendente" if row.unit_price is None else format_money(row.unit_price)
            subtotal = "Pendente" if row.unit_price is None else format_money(row.unit_price * row.quantity)
            spaces = "Pendente" if row.unit_spaces is None else decimal_text(row.unit_spaces)
            load = "Pendente" if row.unit_spaces is None else decimal_text(row.unit_spaces * row.quantity)
            self.inventory_tree.insert("", "end", iid=row.key,
                                       values=("ⓘ", row.item["name"], row.quantity, cost, subtotal, spaces, load),
                                       tags=("special",) if row.item.get("special") else ())
        if selected and self.inventory_tree.exists(selected[0]):
            self.inventory_tree.selection_set(selected[0])
        self._selected()
        totals = self.inventory.totals()
        clearable = bool(self.inventory.lines or self.inventory.custom_items)
        for button in (self.clear_button, self.catalog_clear_button):
            button.configure(state="normal" if clearable else "disabled")
        self.notebook.tab(1, text=f"Meu inventário ({totals.quantity})")

    def set_status(self, text, error=False):
        self.status_var.set(text)
        self.status_label.configure(foreground="#b3261e" if error else "#174a75")
        if text:
            self.status_label.pack(fill="x", pady=(0, 6), before=self.notebook)
        else:
            self.status_label.pack_forget()

    def add_item(self, item):
        try:
            self.inventory.add(item)
            self.refresh_inventory()
            if self.notebook.index(self.notebook.select()) == 1:
                self.inventory_tree.selection_set(item['id'])
            self._selected()
            self.set_status(f"{item['name']} adicionado. Inventário salvo automaticamente.")
        except (OSError, ValueError) as error:
            self.set_status(str(error), error=True)

    def selected_line(self):
        selected = self.inventory_tree.selection()
        return next((row for row in self.inventory.lines if selected and row.key == selected[0]), None)

    def show_item(self, item, line=None):
        price = line.unit_price if line else money(item['price_value']) if item.get('price_value') is not None else None
        quantity = line.quantity if line else 1
        spaces = line.unit_spaces if line else money(item['spaces_value']) if item.get('spaces_value') is not None else None
        stats = item_characteristics(item)+'\nEspaços / un.: '+('Pendente' if spaces is None else decimal_text(spaces))
        hint = ('Valor completo / un.: '+format_money(money(item['full_price']))) if item.get('full_price') is not None else ''
        effects = '\n\n'.join(filter(None,(item.get('description',''),item.get('notes',''),
                                            'Fonte: '+item['source'] if item.get('source') else '')))
        self.item_title_var.set(item['name'])
        self.item_cards.show_purchase(price,stats,effects,quantity=quantity,price_hint=hint,stats_hint=item.get('group',''))
        self.item_cards.titles[0].set('GASTO DO ITEM · TOTAL' if line else 'PREÇO DE COMPRA')
        if price is None:
            self.item_cards.labels[0].configure(fg='#b3261e')

    def show_catalog_item(self, item):
        self._catalog_preview_item = item
        if self.notebook.index(self.notebook.select()) != 0:
            return
        line = next((r for r in self.inventory.lines if r.key == item['id']),None)
        self.show_item(item,line)

    def _refresh_cards(self):
        if self.notebook.index(self.notebook.select()) == 1:
            self.item_title_var.set("Resumo do inventário")
            self.item_cards.show_inventory(self.inventory, self.selected_line())
        elif self.catalog_rows:
            chosen = next((item for item, *_ in self.catalog_rows
                           if self._catalog_preview_item and item['id'] == self._catalog_preview_item['id']),
                          self.catalog_rows[0][0])
            self.show_catalog_item(chosen)
        else:
            self.item_title_var.set("Nenhum item corresponde aos filtros")
            self.item_cards.set_mode(False)
            self.item_cards.clear()

    def _tab_changed(self, _event=None):
        self.info.hide()
        self._selected()

    def _selected(self, _event=None):
        row = self.selected_line()
        for button in (self.apply_button, self.minus_button, self.plus_button, self.remove_button, self.selected_info_button):
            button.configure(state="normal" if row else "disabled")
        if row:
            self.quantity_var.set(str(row.quantity))
            self.price_var.set("" if row.unit_price is None else decimal_text(row.unit_price).replace(".", ","))
            self.spaces_var.set("" if row.unit_spaces is None else decimal_text(row.unit_spaces).replace(".", ","))
            self.selection_var.set(f"{row.item['name']} · {row.item['category']}" + (
                f" · Valor completo por unidade: {row.item['price']}" if row.item.get("full_price") else ""))
        else:
            self.selection_var.set("Adicione itens nos catálogos, nas oficinas ou no Boticário Arcano.")
        self._refresh_cards()

    def _clear_selection(self, _event=None):
        self.inventory_tree.selection_remove(*self.inventory_tree.selection())
        self.info.hide()
        self._selected()
        return 'break'

    def _inventory_click(self, event):
        if self.inventory_tree.identify_region(event.x, event.y) == 'nothing':
            return self._clear_selection()

    def update_selected(self):
        row = self.selected_line()
        if row is None:
            return
        try:
            price = money(self.price_var.get()) if self.price_var.get().strip() else None
            spaces = money(self.spaces_var.get()) if self.spaces_var.get().strip() else None
            self.inventory.update(row.key, self.quantity_var.get(), price, spaces)
            self.refresh_inventory()
            self.set_status("Quantidade, preço e carga atualizados. Inventário salvo.")
        except (OSError, ValueError) as error:
            self.set_status(str(error), error=True)

    def adjust_quantity(self, delta):
        row = self.selected_line()
        if row is None:
            return
        try:
            if row.quantity + delta <= 0:
                self.inventory.remove(row.key)
            else:
                self.inventory.update(row.key, row.quantity + delta, row.unit_price, row.unit_spaces)
            self.refresh_inventory()
            self.set_status("Quantidade atualizada. Inventário salvo.")
        except (OSError, ValueError) as error:
            self.set_status(str(error), error=True)

    def remove_selected(self):
        row = self.selected_line()
        if row is not None:
            try:
                self.inventory.remove(row.key)
                self.refresh_inventory()
                self.set_status("Item removido do inventário.")
            except (OSError, ValueError) as error:
                self.set_status(str(error), error=True)

    def clear_inventory(self):
        include_custom = False
        if self.inventory.custom_items or any(row.item["category"] == "Customizados" for row in self.inventory.lines):
            self.info.hide()
            answer = messagebox.askyesnocancel(
                "Limpar inventário",
                "Há itens customizados salvos. Deseja removê-los também?\n\n"
                "Sim: remove todos os itens e esvazia o catálogo Customizados.\n"
                "Não: remove apenas os itens comuns, preservando os customizados.\n"
                "Cancelar: mantém tudo como está.", parent=self)
            if answer is None:
                return
            include_custom = answer
        try:
            self.inventory.clear(include_custom=include_custom)
            self.refresh()
            self.set_status("Inventário limpo, incluindo os customizados." if include_custom else
                            "Itens comuns removidos. Customizados preservados." if self.inventory.custom_items else
                            "Inventário limpo.")
        except (OSError, ValueError) as error:
            self.set_status(str(error), error=True)

    def show_selected_info(self):
        row = self.selected_line()
        if row:
            self.info.show(self.selected_info_button, item_info(row.item))

    def _tree_info(self, event):
        key = self.inventory_tree.identify_row(event.y)
        if key and self.inventory_tree.identify_column(event.x) == "#1":
            if self._tooltip_key != key or self.info.popup is None:
                self.info.hide()
                self._tooltip_key = key
                row = next(row for row in self.inventory.lines if row.key == key)
                bounds = self.inventory_tree.bbox(key, 'info')
                if not bounds:
                    return
                x, y, width, height = bounds
                self.info.show(self.inventory_tree, item_info(row.item), hover_bounds=(
                    self.inventory_tree.winfo_rootx() + x, self.inventory_tree.winfo_rooty() + y, width, height))
            self.info.cancel_hide()
        else:
            self._tooltip_key = None
            self.info.schedule_hide()

    def destroy(self):
        self.info.hide()
        super().destroy()
