"""Tela de inventário para orçamento e criação de armas."""
import tkinter as tk
from tkinter import ttk

from crafting_core import (WEAPONS, IMPROVEMENTS, MATERIALS, ENCHANTMENTS, SIZE_STEPS,
                           WeaponDesign, quote_weapon, custom_weapon_profile, money,
                           format_money, material_price, default_construction, incompatibility,
                           IMPROVEMENT_COSTS, ENCHANTMENT_COSTS, catalog_hierarchy, prerequisite_reason)
from weapon_catalog import get_weapon_profiles, search_key
from weapon_ui import WeaponInfoPopup


class WeaponWorkshop(ttk.Frame):
    items = WEAPONS
    improvements = IMPROVEMENTS
    materials = MATERIALS
    enchantments = ENCHANTMENTS
    design_type = WeaponDesign
    workshop_title = "Inventário · Crie sua arma"
    item_label = "Arma-base (sem armas mágicas)"
    mode_label = "Empunhadura / modo"
    construction_label = "Construção da parte que causa dano"
    price_label = "Preço-base da arma (T$; ajustável)"
    old_enchantments_label = "Quantos encantamentos ela já possui?"
    owned_label = "Já possuo esta arma"
    immunity_label = "Portador lefou/lefeu (imune à matéria vermelha)"
    incompatible_pairs = {"Maciça": "Precisa", "Precisa": "Maciça"}
    compatibility = staticmethod(incompatibility)
    material_cost = staticmethod(material_price)
    quote_design = staticmethod(quote_weapon)
    build_profile = staticmethod(custom_weapon_profile)
    item_profiles = staticmethod(get_weapon_profiles)
    item_construction = staticmethod(default_construction)

    def __init__(self, master, app, on_back, on_generate):
        super().__init__(master, padding=12)
        self.app, self.on_generate = app, on_generate
        self._update_job = None
        self._pruning = False
        self.result_profile = None
        from forge_ui import InfoPopup, QuoteCards, ModeToggle
        self.forge_info = InfoPopup(self)
        self.info = WeaponInfoPopup(self.winfo_toplevel())
        self.bind("<Unmap>", lambda event: self.info.hide() if event.widget == self else None)
        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 8))
        ttk.Label(header, text=self.workshop_title, style="Section.TLabel").pack(anchor="w")
        self.intro_label = ttk.Label(self, text="Monte a configuração final, incluindo os efeitos que o item já possui. "
                  "Materiais contam como uma melhoria.", wraplength=900)
        self.intro_label.pack(anchor="w", pady=(0, 8))
        self.fabricate_var = tk.BooleanVar(self, False)
        self.mode_toggle = ModeToggle(self, self.fabricate_var)
        self.mode_toggle.pack(fill='x')
        self.forge_cards = QuoteCards(self)
        self.forge_cards.pack(fill="x", pady=(0, 10))
        self.body = ttk.Panedwindow(self, orient="horizontal")
        self.body.pack(fill="both", expand=True)
        settings_panel = ttk.Frame(self.body, width=380)
        catalog_panel = ttk.Frame(self.body)
        self.body.add(settings_panel, weight=2)
        self.body.add(catalog_panel, weight=3)
        settings = app.create_scrollable_panel(settings_panel, padx=(0, 8))
        self.weapon_var = tk.StringVar(self, next(iter(self.items)))
        self.profile_var = tk.StringVar(self)
        self.name_var = tk.StringVar(self)
        self.size_var = tk.StringVar(self, "Padrão")
        self.construction_var = tk.StringVar(self, "Metal")
        self.base_price_var = tk.StringVar(self)
        self.material_price_var = tk.StringVar(self)
        self.damage_var = tk.StringVar(self)
        self.owned_var = tk.BooleanVar(self, False)
        self.old_improvements_var = tk.StringVar(self, "0")
        self.old_enchantments_var = tk.StringVar(self, "0")
        self.old_material_var = tk.StringVar(self, "Nenhum")
        self.material_var = tk.StringVar(self, "")
        self.lancinante_var = tk.StringVar(self, "+10")
        self.red_matter_var = tk.BooleanVar(self, False)
        self.improvement_vars = {name: tk.BooleanVar(self, False) for name in self.improvements}
        self.enchantment_vars = {name: tk.BooleanVar(self, False) for name in self.enchantments}

        def field(label, variable, values=None):
            host = ttk.Frame(settings)
            host.pack(fill='x')
            self.field_rows[label] = host
            ttk.Label(host, text=label).pack(anchor="w", pady=(9, 3))
            if values is None:
                widget = ttk.Entry(host, textvariable=variable)
            else:
                widget = ttk.Combobox(host, textvariable=variable, values=values, state="readonly")
            widget.pack(fill="x")
            self.form_fields[label] = widget
            return widget

        # A busca reduz as opções da arma sem permitir que uma arma mágica entre na seleção.
        self.form_fields = {}
        self.field_rows = {}
        self.weapon_search_var = tk.StringVar(self)
        field("Buscar item-base", self.weapon_search_var)
        self.weapon_combo = field(self.item_label, self.weapon_var, tuple(self.items))
        self.weapon_combo.bind("<<ComboboxSelected>>", self._weapon_changed)
        self.profile_combo = field(self.mode_label, self.profile_var, ())
        field("Nome do item customizado", self.name_var)
        field("Tamanho / passos de dano", self.size_var, tuple(SIZE_STEPS))
        field(self.construction_label, self.construction_var, ("Metal", "Madeira", "Outra"))
        field(self.price_label, self.base_price_var)
        ttk.Checkbutton(settings, text=self.owned_label, variable=self.owned_var).pack(
            anchor="w", pady=(12, 2))
        self.old_improvements_widget = field("Quantas melhorias ela já possui? (inclua material)",
                                              self.old_improvements_var, tuple(range(6)))
        self.old_enchantments_widget = field(self.old_enchantments_label,
                                              self.old_enchantments_var, tuple(range(4)))
        self.old_material_widget = field("Material especial que ela já possui", self.old_material_var,
                                          ("Nenhum", *self.materials))
        self.old_material_widget.bind("<<ComboboxSelected>>", self._old_material_changed)
        self.material_quote_widget = field("Cotação do material raro (T$; quando exigida)", self.material_price_var)
        self.genius_var = tk.BooleanVar(self, False)
        self.second_material_var = tk.StringVar(self, "Nenhum")
        self.second_material_price_var = tk.StringVar(self)
        self.old_second_material_var = tk.StringVar(self, "Nenhum")
        from forge_ui import info_button
        genius_row=ttk.Frame(settings)
        genius_row.pack(fill="x",pady=(8,2))
        ttk.Checkbutton(genius_row, text="Gênio Inovador",variable=self.genius_var).pack(side="left")
        info_button(genius_row,self.forge_info,"Gênio Inovador","Uma melhoria extra gratuita, fora do limite, e dois materiais especiais. A forja presume a habilitação para usar este benefício. Heróis de Arton, p. 71.").pack(side="right")
        self.second_material_widget = field("Gênio Inovador: segundo material", self.second_material_var,
                                           ("Nenhum", *self.materials))
        self.old_second_material_widget = field("Segundo material que o item já possui", self.old_second_material_var,
                                                ("Nenhum", *self.materials))
        self.second_material_price_widget = field("Cotação do segundo material (T$; se exigida)", self.second_material_price_var)
        self.material_hint_var = tk.StringVar(self)
        ttk.Label(settings, textvariable=self.material_hint_var, wraplength=320,
                  style="Small.TLabel").pack(anchor="w", pady=(3, 0))
        field("Lancinante: efeito escolhido no crítico", self.lancinante_var, ("+10", "Multiplicar bônus"))
        field("Dano final manual (opcional; substitui os passos)", self.damage_var)
        ttk.Label(settings, text="Use o dano manual para casos fora da tabela de passos. "
                  "O tamanho altera o dano; ajuste o preço-base se necessário.", wraplength=320,
                  style="Small.TLabel").pack(anchor="w", pady=(4, 8))
        self.build_extra_fields(settings, field)
        # Compra continua usando o orçamento de mercado. Fabricação tem um perfil próprio.
        self.genius_week_var = tk.BooleanVar(self, False)
        self.fabricator_host = ttk.Frame(settings, height=450)
        self.fabricator_host.pack_propagate(False)
        from fabrication_ui import CreatorPanel
        self.creator_panel = CreatorPanel(self.fabricator_host, app, self.schedule_refresh,
                                          scope='weapon' if self.design_type is WeaponDesign else 'armor')
        self.creator_panel.pack(fill="both", expand=True)
        self.fabricate_var.trace_add("write", self.schedule_refresh)
        self.genius_week_var.trace_add("write", self.schedule_refresh)
        self.fabrication_var = tk.StringVar(self)
        ttk.Label(settings, textvariable=self.fabrication_var, wraplength=320).pack(anchor="w", pady=8)

        search_row = ttk.Frame(catalog_panel)
        search_row.pack(fill="x", pady=(0, 8))
        ttk.Label(search_row, text="Buscar no catálogo:").pack(side="left", padx=(0, 6))
        self.search_var = tk.StringVar(self)
        ttk.Entry(search_row, textvariable=self.search_var).pack(side="left", fill="x", expand=True)
        self.notebook = ttk.Notebook(catalog_panel)
        self.notebook.pack(fill="both", expand=True)
        self.rows = []
        self.catalog_layout = []
        catalogs = (("Melhorias", self.improvements, "improvement"), ("Material especial", self.materials, "material"),
                    ("Encantamentos", self.enchantments, "enchantment"))
        self.tab_titles = []
        for title, catalog, kind in catalogs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=title)
            self.tab_titles.append((title, kind))
            content = app.create_scrollable_panel(tab, padx=6, pady=6)
            if kind == "material":
                ttk.Radiobutton(content, text="Sem material especial", variable=self.material_var,
                                value="").pack(anchor="w", pady=5)
            hierarchy = catalog_hierarchy(catalog)
            parents = {parent for name, depth, parent in hierarchy if name}
            for name, depth, parent in hierarchy:
                if name is None:
                    heading = ttk.Label(content, text=parent, style="Small.TLabel")
                    self.catalog_layout.append((kind, None, heading, depth, parent))
                    continue
                entry = catalog[name]
                row = ttk.Frame(content)
                if kind == "material":
                    selector = ttk.Radiobutton(row, variable=self.material_var, value=name, command=self.refresh)
                else:
                    variable = (self.improvement_vars if kind == "improvement" else self.enchantment_vars)[name]
                    selector = ttk.Checkbutton(row, variable=variable, command=self.refresh)
                selector.grid(row=0, column=0, sticky="n")
                label = ttk.Label(row, text=("↳ " if depth else "") + name, wraplength=310, cursor="hand2",
                                  font=("Segoe UI", 10, "bold" if name in parents else "normal"))
                label.grid(row=0, column=1, sticky="w")
                row.columnconfigure(1, weight=1)
                reason = ttk.Label(row, text="", style="Small.TLabel", wraplength=310)
                reason.grid(row=1, column=1, sticky="w")
                icon = ttk.Button(row, text="ⓘ", width=3, cursor="question_arrow")
                icon.grid(row=0, column=2, sticky="ne", padx=(4, 0))
                progression = IMPROVEMENT_COSTS if kind == "improvement" else ENCHANTMENT_COSTS
                info_price = ("Progressão de melhorias" if kind == "improvement" else "Progressão de encantamentos")
                info_price += ": " + "; ".join(f"{i}: {format_money(value)}" for i, value in
                                               enumerate(progression) if i)
                if kind == "material":
                    try:
                        info_price = self.material_info_price(name)
                    except ValueError:
                        info_price = entry["weapon_price"] + " · cotação em T$ necessária"
                self.info.attach(icon, dict(entry, catalog_entry=True, info_kind=title,
                                            info_price=info_price))
                label.bind("<Button-1>", lambda _event, control=selector: control.invoke())
                row.bind("<Configure>", lambda event, l=label, r=reason: (
                    l.configure(wraplength=max(100, event.width - 80)),
                    r.configure(wraplength=max(100, event.width - 80))))
                self.rows.append((kind, name, entry, row, selector, reason))
                self.catalog_layout.append((kind, name, row, depth, parent))
        self.notebook.bind("<<NotebookTabChanged>>", lambda _event: self.info.hide())
        self.innovation_vars, self.innovation_controls = {}, {}
        self.old_innovations_var=tk.StringVar(self,"0")
        if self.design_type is WeaponDesign:
            from innovation_data import INNOVATIONS
            tab=ttk.Frame(self.notebook)
            self.notebook.add(tab,text="Distinções")
            content=app.create_scrollable_panel(tab,padx=8,pady=8)
            ttk.Label(content,text="Mestre de Armearia · Inovações",style="Section.TLabel").pack(anchor="w",pady=(0,8))
            ttk.Label(content,text="Até quatro inovações, em uma progressão própria de preço e CD. Não têm valor comercial e dependem do criador.",wraplength=420).pack(anchor="w",pady=(0,8))
            for name,entry in INNOVATIONS.items():
                row=ttk.Frame(content)
                row.pack(fill="x",pady=4)
                var=self.innovation_vars[name]=tk.BooleanVar(self,False)
                button=ttk.Checkbutton(row,text=name,variable=var)
                button.pack(side="left",fill="x",expand=True)
                info_button(row,self.forge_info,name,entry['description']+" Deuses de Arton, p. 110–111.").pack(side="right")
                reason=ttk.Label(content,style="Small.TLabel",wraplength=420)
                reason.pack(anchor="w")
                self.innovation_controls[name]=(button,reason)
                var.trace_add('write',self.schedule_refresh)
            field("Inovações que o item já possui",self.old_innovations_var,tuple(range(5)))
            self.old_innovations_var.trace_add('write',self.schedule_refresh)
        # Os cartões concentram o orçamento; o rodapé reserva só uma linha às ações.
        footer = self.footer = ttk.Frame(self, padding=(0, 8, 0, 0))
        footer.pack(side='bottom', fill="x", before=self.body)
        footer.columnconfigure(0, weight=1)
        self.error_var = tk.StringVar(self)
        self.error_label = ttk.Label(footer, textvariable=self.error_var, foreground="#b3261e", wraplength=1100)
        self.error_label.grid(row=0, column=0, sticky="w", pady=(0, 6))
        self.error_label.grid_remove()
        actions = ttk.Frame(footer)
        actions.grid(row=1, column=0, sticky="e")
        self.generate_button = ttk.Button(actions, text="Gerar macro de arma", style="Primary.TButton",
                                          command=self.generate)
        self.generate_button.grid(row=0, column=0, padx=(0, 8))
        self.inventory_button = ttk.Button(actions, text="Adicionar no inventário", command=self.add_to_inventory)
        self.inventory_button.grid(row=0, column=1)
        self.inventory_status_var = tk.StringVar(self)
        self.inventory_status_label = ttk.Label(footer, textvariable=self.inventory_status_var, wraplength=1100)
        self.inventory_status_label.grid(row=2, column=0, sticky="w", pady=(3, 0))
        self.inventory_status_label.grid_remove()
        self.inventory_status_var.trace_add("write", self._update_inventory_status)
        self.bind("<Configure>", self._resize_footer, add="+")
        variables = (self.profile_var, self.name_var, self.size_var, self.construction_var,
                     self.base_price_var, self.material_price_var, self.damage_var, self.owned_var,
                     self.old_improvements_var, self.old_enchantments_var, self.old_material_var,
                     self.material_var, self.lancinante_var, self.red_matter_var, self.search_var,
                     self.genius_var, self.second_material_var, self.second_material_price_var, self.old_second_material_var,
                     *self.improvement_vars.values(), *self.enchantment_vars.values())
        for variable in variables:
            variable.trace_add("write", self.schedule_refresh)
        self.weapon_search_var.trace_add("write", self._filter_weapons)
        self.material_var.trace_add("write", lambda *_args: self.material_price_var.set(""))
        self._weapon_changed()
        self.refresh()

    def _resize_footer(self, event):
        if event.widget == self:
            self.intro_label.configure(wraplength=max(240,event.width-36))
            for label in (self.error_label, self.inventory_status_label):
                label.configure(wraplength=max(240, event.width - 36))

    def _update_inventory_status(self, *_args):
        if self.inventory_status_var.get():
            self.inventory_status_label.grid()
        else:
            self.inventory_status_label.grid_remove()

    def _filter_weapons(self, *_args):
        query = search_key(self.weapon_search_var.get())
        self.weapon_combo.configure(values=[name for name in self.items if query in search_key(name)])

    def _weapon_changed(self, _event=None):
        weapon = self.items[self.weapon_var.get()]
        profiles = self.item_profiles(weapon)
        self.profile_combo.configure(values=[p["label"] for p in profiles])
        self.profile_var.set(profiles[0]["label"])
        self.name_var.set(weapon["name"] + " customizada")
        self.construction_var.set(self.item_construction(weapon))
        try:
            self.base_price_var.set(str(money(weapon["price"])))
        except ValueError:
            self.base_price_var.set("")
        self.damage_var.set("")
        self.schedule_refresh()

    def _old_material_changed(self, _event=None):
        name = self.old_material_var.get()
        if name != "Nenhum":
            self.material_var.set(name)
            self.old_improvements_var.set(str(max(1, int(self.old_improvements_var.get()))))

    def schedule_refresh(self, *_args):
        if not self._pruning and self._update_job is None:
            self._update_job = self.after_idle(self.refresh)

    def _clear_unavailable_options(self, weapon):
        self._pruning = True
        try:
            while True:
                changed = False
                improvements = tuple(name for name, var in self.improvement_vars.items() if var.get())
                enchantments = tuple(name for name, var in self.enchantment_vars.items() if var.get())
                for catalog, variables, kind in ((self.improvements, self.improvement_vars, "improvement"),
                                                 (self.enchantments, self.enchantment_vars, "enchantment")):
                    for name, var in variables.items():
                        if not var.get():
                            continue
                        reason = (self.compatibility(weapon, catalog[name], kind, self.construction_var.get())
                                  or prerequisite_reason(catalog[name], kind, improvements,
                                                         enchantments, self.material_var.get()))
                        if reason:
                            var.set(False)
                            changed = True
                if not changed:
                    break
        finally:
            self._pruning = False

    def _filter_catalog(self, query):
        parents = {(kind, name): parent for kind, name, row, depth, parent in self.catalog_layout if name}
        visible = set()
        for kind, name, entry, row, selector, reason in self.rows:
            ancestors = [name]
            parent = parents[(kind, name)]
            while parent:
                ancestors.append(parent)
                parent = parents.get((kind, parent), "")
            if any(query in search_key(text) for text in ancestors):
                visible.update((kind, ancestor) for ancestor in ancestors)
        # Reempacota na ordem da árvore, inclusive ao limpar uma busca anterior.
        for kind, name, widget, depth, parent in self.catalog_layout:
            widget.pack_forget()
        for kind, name, widget, depth, parent in self.catalog_layout:
            if (kind, name or parent) in visible:
                widget.pack(fill="x", padx=(depth * 20, 0),
                            pady=(1, 1) if depth else (8, 1))

    def get_design(self):
        owned = self.owned_var.get()
        if not self.base_price_var.get().strip():
            raise ValueError("Preço-base não informado na planilha. Informe o valor em T$ (0 se gratuito).")
        profiles = self.item_profiles(self.items[self.weapon_var.get()])
        profile_index = next((i for i, p in enumerate(profiles) if p["label"] == self.profile_var.get()), 0)
        return self.design_type(
            weapon_name=self.weapon_var.get(), profile_index=profile_index, name=self.name_var.get(),
            size=self.size_var.get(), construction=self.construction_var.get(),
            improvements=tuple(n for n, v in self.improvement_vars.items() if v.get()),
            enchantments=tuple(n for n, v in self.enchantment_vars.items() if v.get()),
            material=self.material_var.get(), owned=owned,
            existing_improvements=int(self.old_improvements_var.get()) if owned else 0,
            existing_enchantments=int(self.old_enchantments_var.get()) if owned else 0,
            existing_material=self.old_material_var.get() if owned and self.old_material_var.get() != "Nenhum" else "",
            base_price_override=money(self.base_price_var.get()),
            material_price_override=money(self.material_price_var.get()) if self.material_price_var.get().strip() else None,
            damage_override=self.damage_var.get().strip(), lancinante_mode=self.lancinante_var.get(),
            red_matter_immune=self.red_matter_var.get(), genius_innovator=self.genius_var.get(),
            second_material=self.second_material_var.get() if self.genius_var.get() and self.second_material_var.get() != "Nenhum" else "",
            second_material_price_override=money(self.second_material_price_var.get()) if self.genius_var.get() and self.second_material_price_var.get().strip() else None,
            existing_second_material=self.old_second_material_var.get() if owned and self.genius_var.get() and self.old_second_material_var.get() != "Nenhum" else "",
            innovations=tuple(n for n,v in self.innovation_vars.items() if v.get()),
            existing_innovations=int(self.old_innovations_var.get()) if owned else 0,
            **self.extra_design_fields())

    def refresh(self):
        if self._update_job is not None:
            self.after_cancel(self._update_job)
            self._update_job = None
        query = search_key(self.search_var.get())
        weapon = self.items[self.weapon_var.get()]
        if self.fabricate_var.get():
            self.fabricator_host.pack(fill="x", pady=4)
        else:
            self.fabricator_host.pack_forget()
        self.fabrication_quote = None
        self.fabrication_var.set("")
        self.forge_cards.set_mode(self.fabricate_var.get())
        self.forge_cards.clear()
        from forge_ui import set_visible
        for label in ('Quantas melhorias ela já possui? (inclua material)', self.old_enchantments_label,
                      'Material especial que ela já possui'):
            set_visible(self.field_rows[label], self.owned_var.get())
        for label in ('Gênio Inovador: segundo material', 'Cotação do segundo material (T$; se exigida)'):
            set_visible(self.field_rows[label], self.genius_var.get())
        set_visible(self.field_rows['Segundo material que o item já possui'], self.owned_var.get() and self.genius_var.get())
        set_visible(self.field_rows['Lancinante: efeito escolhido no crítico'],
                    any(v.get() for n,v in self.enchantment_vars.items() if n.startswith('Lancinante')))
        if 'Inovações que o item já possui' in self.field_rows:
            set_visible(self.field_rows['Inovações que o item já possui'],
                        self.owned_var.get() and any(v.get() for v in self.innovation_vars.values()))
        self.second_material_widget.configure(state="readonly" if self.genius_var.get() else "disabled")
        self.old_second_material_widget.configure(state="readonly" if self.genius_var.get() and self.owned_var.get() else "disabled")
        self.second_material_price_widget.configure(state="normal" if self.genius_var.get() else "disabled")
        self._clear_unavailable_options(weapon)
        improvements = tuple(name for name, var in self.improvement_vars.items() if var.get())
        enchantments = tuple(name for name, var in self.enchantment_vars.items() if var.get())
        if self.innovation_controls:
            from innovation_data import innovation_reason
            selected=tuple(n for n,v in self.innovation_vars.items() if v.get())
            firearm=weapon.get('category')=='Armas de fogo' or 'híbrida' in weapon.get('description','') and 'fogo' in weapon.get('description','')
            for name,(control,hint) in self.innovation_controls.items():
                reason=innovation_reason(name,selected,improvements,firearm=firearm)
                if not reason and name not in selected and len(selected)>=4:
                    reason='Limite de quatro inovações atingido.'
                control.configure(state='normal' if name in selected or not reason else 'disabled')
                hint.configure(text=reason)
        for kind, name, entry, row, selector, reason_widget in self.rows:
            reason = (self.compatibility(weapon, entry, kind, self.construction_var.get())
                      or prerequisite_reason(entry, kind, improvements, enchantments, self.material_var.get()))
            selected = (self.material_var.get() == name if kind == "material" else
                        (self.improvement_vars if kind == "improvement" else self.enchantment_vars)[name].get())
            if not selected and not reason:
                if kind == "improvement":
                    opposite = self.incompatible_pairs.get(name)
                    if opposite in improvements:
                        reason = f"Incompatível com {opposite}."
                    elif (len(improvements) + bool(self.material_var.get()) + (self.genius_var.get() and self.second_material_var.get() != "Nenhum")
                          >= (5 if self.genius_var.get() else 4)):
                        reason = "Limite de quatro melhorias atingido."
                elif kind == "enchantment":
                    if name.startswith("Lancinante") and any(n.startswith("Lancinante") for n in enchantments):
                        reason = "Escolha apenas uma versão de Lancinante."
                    elif self.enchantment_count(enchantments) + self.enchantment_count((name,)) > 3:
                        reason = "Limite de três encantamentos atingido."
            selector.configure(state="disabled" if reason else "normal")
            label = row.grid_slaves(row=0, column=1)[0]
            label.configure(foreground="#9299a5" if reason else "#24324b",
                            cursor="arrow" if reason else "hand2")
            reason_widget.configure(text=reason)
        self._filter_catalog(query)
        for index, (title, kind) in enumerate(self.tab_titles):
            count = ((int(bool(self.material_var.get())) + int(self.genius_var.get() and self.second_material_var.get() != 'Nenhum')) if kind == "material" else
                     (len(improvements) if kind == "improvement" else self.enchantment_count(enchantments)))
            self.notebook.tab(index, text=f"{title} ({count})")
        for widget in (self.old_improvements_widget, self.old_enchantments_widget, self.old_material_widget):
            widget.configure(state="readonly" if self.owned_var.get() else "disabled")
        selected_material = self.material_var.get()
        rare = False
        if selected_material:
            try:
                price = self.material_cost(selected_material)
                self.material_hint_var.set(f"Adicional do material: {format_money(price)}. "
                                           "Troca: cobra o novo material inteiro, sem crédito do antigo.")
            except ValueError:
                rare = True
                self.material_hint_var.set(f"Exige {self.material_requirement(selected_material)}. "
                                           "Informe a cotação total das peças; não há preço publicado em T$.")
        else:
            self.material_hint_var.set("Material ocupa uma melhoria. Gênio Inovador permite dois materiais e uma melhoria extra gratuita.")
        self.material_quote_widget.configure(state="normal" if rare else "disabled")
        self.result_profile = None
        quote = None
        try:
            design = self.get_design()
            quote = self.quote_design(design)
            profile = self.build_profile(design)
            self.result_profile = profile
            stats, effects = self.purchase_details(design, profile, weapon)
            if self.fabricate_var.get():
                from fabrication import equipment_fabrication
                self.fabrication_quote = equipment_fabrication(design, weapon, quote,
                    self.creator_panel.get_creator(), genius_week=self.genius_week_var.get())
                self.forge_cards.show_quote(self.fabrication_quote)
                self.forge_cards.set_characteristics(stats, effects,
                    stats_hint='Bônus do item; acrescente os valores da ficha ao usar.')
                self.fabrication_var.set('\n'.join(self.fabrication_quote.notes))
            else:
                self.forge_cards.show_purchase(None if quote.innovation_count else quote.due_now, stats, effects,
                    price_hint=('Inovações sem valor comercial' if quote.innovation_count else
                                f'A pagar pelas alterações · Item completo: {format_money(quote.total_price)}' if design.owned else 'Item pronto · Valor por unidade'),
                    stats_hint='Bônus do item; acrescente os valores da ficha ao usar.')
            self.error_var.set("")
        except (ValueError, KeyError) as error:
            self.result_profile = None
            self.forge_cards.clear()
            self.error_var.set(str(error))
        if self.result_profile is None:
            self.error_label.grid()
        else:
            self.error_label.grid_remove()
        self.update_actions()

    def generate(self):
        self.refresh()
        if self.result_profile is not None and self.can_generate(self.result_profile):
            self.info.hide()
            self.on_generate(self.result_profile)

    def add_to_inventory(self):
        self.refresh()
        if self.result_profile is None or (not self.fabricate_var.get() and self.get_design().innovations):
            return
        try:
            design = self.get_design()
            quote = self.quote_design(design)
            _, effects = self.purchase_details(design, self.result_profile, self.items[design.weapon_name])
            profile = dict(self.result_profile, description=effects,
                           acquisition='fabrication' if self.fabricate_var.get() else 'purchase')
            if self.fabricate_var.get() and self.fabrication_quote is not None:
                from dataclasses import replace
                quote = replace(quote, due_now=self.fabrication_quote.cost)
                profile = dict(profile, description=profile["description"] + "\nFabricação: " + self.fabrication_quote.summary())
            else:
                profile = dict(profile, description=profile['description']+'\nComprando · Preço de compra: '+format_money(quote.due_now))
            item = self.app.add_custom_to_inventory(design, self.items[design.weapon_name],
                                                    quote, profile)
            self.inventory_status_var.set(f"{item['name']} adicionado ao SHOPING. Inventário salvo.")
            self.inventory_status_label.configure(foreground="#174a75")
        except (OSError, ValueError) as error:
            self.inventory_status_var.set(str(error))
            self.inventory_status_label.configure(foreground="#b3261e")

    def build_extra_fields(self, settings, field):
        pass

    def extra_design_fields(self):
        return {}

    def material_requirement(self, name):
        return self.materials[name]["weapon_price"]

    def material_info_price(self, name):
        return format_money(self.material_cost(name)) + " + progressão de melhorias"

    @staticmethod
    def enchantment_count(names):
        return len(names)

    @staticmethod
    def can_generate(profile):
        return True

    def update_actions(self):
        enabled = self.result_profile is not None and self.can_generate(self.result_profile)
        self.generate_button.configure(state="normal" if enabled else "disabled")
        purchasable = self.fabricate_var.get() or not any(v.get() for v in self.innovation_vars.values())
        self.inventory_button.configure(state="normal" if self.result_profile is not None and purchasable else "disabled")

    def purchase_details(self, design, profile, item):
        if 'defense_bonus' in profile:
            stats = f"Defesa +{profile['defense_bonus']} · Penalidade {profile['armor_penalty']}"
            rd = '; '.join(f'RD {v}'+('' if k == 'geral' else '/'+k) for k,v in profile['rd'].items())
            stats += '\n' + (rd or 'Sem redução de dano')
            stats += '\n' + '; '.join(profile['bonuses']) if profile['bonuses'] else ''
            if profile.get('can_attack'):
                stats += '\nEscudo: ' + self.weapon_purchase_stats(profile)
        else:
            stats = self.weapon_purchase_stats(profile)
        blocks = ['Lembretes de uso: '+profile['description']] if profile['description'] else []
        for names, catalog in ((design.improvements, self.improvements),
                               ((design.material, design.second_material), self.materials),
                               (design.enchantments, self.enchantments)):
            blocks.extend(name+': '+catalog[name]['description'] for name in names if name)
        if design.innovations:
            from innovation_data import INNOVATIONS
            blocks.extend(name+': '+INNOVATIONS[name]['description'] for name in design.innovations)
        if item.get('description'):
            blocks.append('Item-base: '+item['description'])
        return stats, '\n\n'.join(filter(None, blocks))

    @staticmethod
    def weapon_purchase_stats(profile):
        damage = profile['damage'] or '—'
        flat = profile['flat_damage']
        if flat:
            damage += (' ' if str(flat).startswith('-') else ' + ') + str(flat)
        if profile['extras']:
            damage += ' + ' + ' + '.join(profile['extras'])
        attack = str(profile['attack_bonus'] or '0')
        if not attack.startswith(('+','-')):
            attack = '+'+attack
        return (f'Dano: {damage}\nAcerto: {attack} · Crítico: {profile["threat"] or "20"}/x{profile["critical_multiplier"]}'
                f'\nTipo(s): {profile["damage_type"] or "—"}')

    @staticmethod
    def profile_summary(profile):
        return (f"Dano: {profile['damage'] or '—'}" + (f" + {profile['flat_damage']}" if profile['flat_damage'] else "")
                + f" · Crítico: {profile['threat'] or '—'}/x{profile['critical_multiplier']} · "
                f"Tipo: {profile['damage_type'] or '—'}\n"
                + ("Extras: " + " + ".join(profile["extras"]) + ". " if profile["extras"] else "")
                + "A descrição da macro inclui apenas RD ignorada e ativações por PM.")

    def destroy(self):
        self.forge_info.hide()
        if self._update_job is not None:
            self.after_cancel(self._update_job)
        self.info.hide()
        super().destroy()
