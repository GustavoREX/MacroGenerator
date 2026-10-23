"""Criador de armaduras e escudos com proteção e ataque no mesmo orçamento."""
import tkinter as tk
from tkinter import ttk

from armor_core import (ARMOR_ITEMS, ARMOR_IMPROVEMENTS, ARMOR_ENCHANTMENTS, ARMOR_MATERIALS,
                        ArmorDesign, armor_incompatibility, armor_material_price, armor_material_column,
                        armor_item_profiles, armor_construction, armor_enchantment_count,
                        quote_armor, custom_armor_profile)
from weapon_workshop import WeaponWorkshop
from weapon_catalog import base_name


class ArmorWorkshop(WeaponWorkshop):
    items = ARMOR_ITEMS
    improvements = ARMOR_IMPROVEMENTS
    materials = ARMOR_MATERIALS
    enchantments = ARMOR_ENCHANTMENTS
    design_type = ArmorDesign
    workshop_title = "Inventário · Crie sua Armadura e Escudos"
    item_label = "Armadura ou escudo-base (sem itens mágicos)"
    mode_label = "Uso do item / ataque do escudo"
    construction_label = "Construção do item"
    price_label = "Preço-base da armadura ou escudo (T$; ajustável)"
    old_enchantments_label = "Quantos espaços de encantamento já usa? (inclua duplos)"
    owned_label = "Já possuo esta armadura ou escudo"
    immunity_label = "Portador lefeu (imune à matéria vermelha)"
    incompatible_pairs = {**WeaponWorkshop.incompatible_pairs, "Delicada": "Reforçada", "Reforçada": "Delicada"}
    compatibility = staticmethod(armor_incompatibility)
    quote_design = staticmethod(quote_armor)
    build_profile = staticmethod(custom_armor_profile)
    item_profiles = staticmethod(armor_item_profiles)
    item_construction = staticmethod(armor_construction)
    enchantment_count = staticmethod(armor_enchantment_count)

    def __init__(self, master, app, on_back, on_generate):
        super().__init__(master, app, on_back, on_generate)
        self.generate_button.configure(text="Gerar macro de ataque do escudo")

    def build_extra_fields(self, settings, field):
        self.fitted_var = tk.BooleanVar(self, True)
        self.goblin_var = tk.StringVar(self, "0")
        self.ballistic_var = tk.BooleanVar(self, False)
        self.caustic_var = tk.BooleanVar(self, False)
        self.fitted_button = ttk.Checkbutton(settings, text="Sob Medida: estou usando o item ajustado para mim",
                                            variable=self.fitted_var)
        self.fitted_button.pack(anchor="w", pady=(8, 0))
        self.goblin_combo = field("Engenhoqueiro goblin: espaços extras (0 a 8)", self.goblin_var, tuple(range(9)))
        self.ballistic_button = ttk.Checkbutton(settings, text="Ataque: Balístico ativo (gasta 1 bala)",
                                               variable=self.ballistic_var)
        self.ballistic_button.pack(anchor="w", pady=(8, 0))
        self.caustic_button = ttk.Checkbutton(settings, text="Ataque: Cáustica ativada (2 PM, até o fim da cena)",
                                             variable=self.caustic_var)
        self.caustic_button.pack(anchor="w", pady=(4, 0))
        self.base_item_info = ttk.Button(settings, text="ⓘ Dados da armadura / escudo-base")
        self.base_item_info.pack(fill="x", pady=(10, 8))
        ttk.Label(settings, text="Defesa e ataque compartilham 4 melhorias e 3 encantamentos. "
                  "Armaduras, vime e torre exibem apenas informações de proteção e preço.",
                  wraplength=320, style="Small.TLabel").pack(anchor="w", pady=(0, 8))
        for var in (self.fitted_var, self.goblin_var, self.ballistic_var, self.caustic_var):
            var.trace_add("write", self.schedule_refresh)

    def _weapon_changed(self, _event=None):
        super()._weapon_changed(_event)
        item = self.items[self.weapon_var.get()]
        self.info.attach(self.base_item_info, dict(item, catalog_entry=True, info_kind=item["group"],
                          info_price=f"{item['price']} · Defesa {item['defense']} · Penalidade {item['penalty']}"))

    def extra_design_fields(self):
        return dict(fitted=self.fitted_var.get(), goblin_extra_spaces=int(self.goblin_var.get()),
                    ballistic_active=self.ballistic_var.get(), caustic_active=self.caustic_var.get())

    def material_cost(self, name, override=None):
        return armor_material_price(name, self.items[self.weapon_var.get()], override)

    def material_requirement(self, name):
        return self.materials[name][armor_material_column(self.items[self.weapon_var.get()])]

    def material_info_price(self, name):
        item = self.materials[name]
        return (f"Leve: {item['light_price']} · Pesada: {item['heavy_price']} · Escudo: {item['shield_price']} "
                "+ progressão de melhorias")

    @staticmethod
    def can_generate(profile):
        return profile["can_attack"]

    def update_actions(self):
        super().update_actions()
        item = self.items[self.weapon_var.get()]
        attack = item["group"] == "Escudos" and base_name(item["name"]) not in ("Escudo de vime", "Escudo torre")
        if attack:
            self.generate_button.grid()
        else:
            self.generate_button.grid_remove()
        for label in ("Tamanho / passos de dano", "Lancinante: efeito escolhido no crítico"):
            self.form_fields[label].configure(state="readonly" if attack else "disabled")
        self.form_fields["Dano final manual (opcional; substitui os passos)"].configure(
            state="normal" if attack else "disabled")
        selected_improvements = {base_name(n) for n, v in self.improvement_vars.items() if v.get()}
        selected_enchantments = {base_name(n) for n, v in self.enchantment_vars.items() if v.get()}
        self.fitted_button.configure(state="normal" if "Sob Medida" in selected_improvements else "disabled")
        self.goblin_combo.configure(state="readonly" if item["name"].startswith("Armadura de engenhoqueiro") else "disabled")
        self.ballistic_button.configure(state="normal" if attack and "Balístico" in selected_improvements else "disabled")
        self.caustic_button.configure(state="normal" if attack and "Cáustica" in selected_enchantments else "disabled")

    @staticmethod
    def profile_summary(profile):
        summary = profile["protection"]
        if profile["can_attack"]:
            summary += "\nAtaque: " + WeaponWorkshop.profile_summary(profile)
        elif profile["is_shield"]:
            summary += "\nEste escudo não pode ser usado para atacar."
        if profile["description"]:
            summary += "\n" + profile["description"]
        return summary
