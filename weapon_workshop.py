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
        self.info = WeaponInfoPopup(self.winfo_toplevel())
        self.bind("<Unmap>", lambda event: self.info.hide() if event.widget == self else None)
        header = ttk.Frame(self)
        header.pack(fill="x", pady=(0, 8))
        ttk.Button(header, text="← Macro Generator", command=on_back).pack(side="right")
        ttk.Label(header, text=self.workshop_title, style="Section.TLabel").pack(anchor="w")
        ttk.Label(self, text="Monte a configuração final, incluindo os efeitos que o item já possui. "
                  "Materiais contam como uma melhoria.", wraplength=900).pack(anchor="w", pady=(0, 8))
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
            ttk.Label(settings, text=label).pack(anchor="w", pady=(9, 3))
            if values is None:
                widget = ttk.Entry(settings, textvariable=variable)
            else:
                widget = ttk.Combobox(settings, textvariable=variable, values=values, state="readonly")
            widget.pack(fill="x")
            self.form_fields[label] = widget
            return widget

        # A busca reduz as opções da arma sem permitir que uma arma mágica entre na seleção.
        self.form_fields = {}
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
                                              self.old_improvements_var, tuple(range(5)))
        self.old_enchantments_widget = field(self.old_enchantments_label,
                                              self.old_enchantments_var, tuple(range(4)))
        self.old_material_widget = field("Material especial que ela já possui", self.old_material_var,
                                          ("Nenhum", *self.materials))
        self.old_material_widget.bind("<<ComboboxSelected>>", self._old_material_changed)
        self.material_quote_widget = field("Cotação do material raro (T$; quando exigida)", self.material_price_var)
        self.material_hint_var = tk.StringVar(self)
        ttk.Label(settings, textvariable=self.material_hint_var, wraplength=320,
                  style="Small.TLabel").pack(anchor="w", pady=(3, 0))
        field("Lancinante: efeito escolhido no crítico", self.lancinante_var, ("+10", "Multiplicar bônus"))
        ttk.Checkbutton(settings, text=self.immunity_label,
                        variable=self.red_matter_var).pack(anchor="w", pady=(10, 0))
        field("Dano final manual (opcional; substitui os passos)", self.damage_var)
        ttk.Label(settings, text="Use o dano manual para casos fora da tabela de passos. "
                  "O tamanho altera o dano; ajuste o preço-base se necessário.", wraplength=320,
                  style="Small.TLabel").pack(anchor="w", pady=(4, 8))
        self.build_extra_fields(settings, field)

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
        # O resumo e a ação continuam acessíveis mesmo quando as listas são longas.
        footer = ttk.Frame(self, padding=(0, 8, 0, 0))
        footer.pack(fill="x")
        self.summary_var = tk.StringVar(self)
        self.details_var = tk.StringVar(self)
        self.error_var = tk.StringVar(self)
        self.summary_label = ttk.Label(footer, textvariable=self.summary_var, style="Section.TLabel", wraplength=1100)
        self.summary_label.pack(anchor="w")
        self.details_label = ttk.Label(footer, textvariable=self.details_var, wraplength=1100)
        self.details_label.pack(anchor="w", pady=(3, 0))
        self.error_label = ttk.Label(footer, textvariable=self.error_var, foreground="#b3261e", wraplength=1100)
        self.error_label.pack(anchor="w", pady=(3, 0))
        self.generate_button = ttk.Button(footer, text="Gerar macro de arma", style="Primary.TButton",
                                          command=self.generate)
        self.generate_button.pack(anchor="e", pady=(6, 0))
        self.inventory_button = ttk.Button(footer, text="Adicionar no inventário", command=self.add_to_inventory)
        self.inventory_button.pack(anchor="e", pady=(6, 0))
        self.inventory_status_var = tk.StringVar(self)
        self.inventory_status_label = ttk.Label(footer, textvariable=self.inventory_status_var, wraplength=1100)
        self.inventory_status_label.pack(anchor="w", pady=(3, 0))
        self.bind("<Configure>", self._resize_footer, add="+")
        variables = (self.profile_var, self.name_var, self.size_var, self.construction_var,
                     self.base_price_var, self.material_price_var, self.damage_var, self.owned_var,
                     self.old_improvements_var, self.old_enchantments_var, self.old_material_var,
                     self.material_var, self.lancinante_var, self.red_matter_var, self.search_var,
                     *self.improvement_vars.values(), *self.enchantment_vars.values())
        for variable in variables:
            variable.trace_add("write", self.schedule_refresh)
        self.weapon_search_var.trace_add("write", self._filter_weapons)
        self.material_var.trace_add("write", lambda *_args: self.material_price_var.set(""))
        self._weapon_changed()
        self.refresh()

    def _resize_footer(self, event):
        if event.widget == self:
            for label in (self.summary_label, self.details_label, self.error_label, self.inventory_status_label):
                label.configure(wraplength=max(240, event.width - 36))

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
            red_matter_immune=self.red_matter_var.get(), **self.extra_design_fields())

    def refresh(self):
        if self._update_job is not None:
            self.after_cancel(self._update_job)
            self._update_job = None
        query = search_key(self.search_var.get())
        weapon = self.items[self.weapon_var.get()]
        self._clear_unavailable_options(weapon)
        improvements = tuple(name for name, var in self.improvement_vars.items() if var.get())
        enchantments = tuple(name for name, var in self.enchantment_vars.items() if var.get())
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
                    elif len(improvements) + bool(self.material_var.get()) >= 4:
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
            count = (bool(self.material_var.get()) if kind == "material" else
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
            self.material_hint_var.set("Só um material especial. O material ocupa uma das quatro melhorias.")
        self.material_quote_widget.configure(state="normal" if rare else "disabled")
        self.result_profile = None
        quote = None
        try:
            design = self.get_design()
            quote = self.quote_design(design)
            self.summary_var.set(f"Preço final: {format_money(quote.total_price)}  ·  "
                                 f"A pagar agora: {format_money(quote.due_now)}")
            self.details_var.set(
                f"Base: {format_money(quote.base_price)} · Melhorias {quote.improvement_count}/4: "
                f"{format_money(quote.improvement_price)} · Material: {format_money(quote.material_price)} · "
                f"Encantos {quote.enchantment_count}/3: {format_money(quote.enchantment_price)}\n"
                f"A pagar em melhorias: {format_money(quote.improvement_due)}; "
                f"encantos: {format_money(quote.enchantment_due)}; material: {format_money(quote.material_due)}. "
                f"CD de melhorias +{quote.improvement_dc}; CD de encantamentos +{quote.enchantment_dc}.")
            profile = self.build_profile(design)
            self.result_profile = profile
            self.error_var.set(self.profile_summary(profile))
            self.error_label.configure(foreground="#174a75")
        except (ValueError, KeyError) as error:
            self.error_var.set(str(error))
            self.error_label.configure(foreground="#b3261e")
            # Não deixa valores de uma combinação anterior parecerem válidos.
            if quote is None:
                self.summary_var.set("Confira a configuração da arma.")
                self.details_var.set("")
        self.update_actions()

    def generate(self):
        self.refresh()
        if self.result_profile is not None and self.can_generate(self.result_profile):
            self.info.hide()
            self.on_generate(self.result_profile)

    def add_to_inventory(self):
        self.refresh()
        if self.result_profile is None:
            return
        try:
            design = self.get_design()
            item = self.app.add_custom_to_inventory(design, self.items[design.weapon_name],
                                                    self.quote_design(design), self.result_profile)
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
        self.inventory_button.configure(state="normal" if self.result_profile is not None else "disabled")

    @staticmethod
    def profile_summary(profile):
        return (f"Dano: {profile['damage'] or '—'}" + (f" + {profile['flat_damage']}" if profile['flat_damage'] else "")
                + f" · Crítico: {profile['threat'] or '—'}/x{profile['critical_multiplier']} · "
                f"Tipo: {profile['damage_type'] or '—'}\n"
                + ("Extras: " + " + ".join(profile["extras"]) + ". " if profile["extras"] else "")
                + "A descrição da macro inclui apenas RD ignorada e ativações por PM.")

    def destroy(self):
        if self._update_job is not None:
            self.after_cancel(self._update_job)
        self.info.hide()
        super().destroy()
