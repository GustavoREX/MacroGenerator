"""Seletor de armas e cartões de informação do catálogo."""
import tkinter as tk
from tkinter import ttk

from ui_theme import set_responsive_window_geometry
from weapon_catalog import WEAPON_CATEGORIES, get_weapon_profiles, search_key


class WeaponInfoPopup:
    def __init__(self, owner):
        self.owner = owner
        self.popup = None
        self.icon = None
        self.hide_job = None
        owner.bind("<Destroy>", self._owner_destroyed, add="+")
        owner.bind("<Unmap>", self._owner_unmapped, add="+")

    def attach(self, icon, weapon):
        icon.configure(command=lambda: self.show(icon, weapon))
        icon.bind("<Enter>", lambda _event: self.show(icon, weapon))
        icon.bind("<Leave>", self.schedule_hide)
        icon.bind("<FocusIn>", lambda _event: self.show(icon, weapon))
        icon.bind("<FocusOut>", lambda _event: self.hide())
        icon.bind("<Escape>", lambda _event: self.hide())

    def _owner_destroyed(self, event):
        if event.widget == self.owner:
            self.hide()

    def _owner_unmapped(self, event):
        if event.widget == self.owner:
            self.hide()

    def cancel_hide(self, _event=None):
        if self.hide_job is not None:
            self.owner.after_cancel(self.hide_job)
            self.hide_job = None

    def hide(self):
        self.cancel_hide()
        if self.popup is not None:
            self.popup.destroy()
            self.popup = None
        self.icon = None

    def schedule_hide(self, _event=None):
        self.cancel_hide()
        self.hide_job = self.owner.after(180, self._hide_outside)

    def _hide_outside(self):
        self.hide_job = None
        x, y = self.owner.winfo_pointerxy()
        for widget in (self.icon, self.popup):
            if widget is not None and widget.winfo_exists():
                if (widget.winfo_rootx() <= x < widget.winfo_rootx() + widget.winfo_width()
                        and widget.winfo_rooty() <= y < widget.winfo_rooty() + widget.winfo_height()):
                    return
        self.hide()

    def show(self, icon, weapon):
        self.cancel_hide()
        if self.icon == icon and self.popup is not None:
            return
        self.hide()
        self.icon = icon
        popup = self.popup = tk.Toplevel(self.owner)
        popup.withdraw()
        popup.wm_overrideredirect(True)
        popup.transient(self.owner)
        width = min(480, self.owner.winfo_screenwidth() - 32)
        surface, ink = "#f4f7fc", "#172033"
        card = tk.Frame(popup, bg=surface, highlightbackground="#bccbe4", highlightthickness=1,
                        padx=12, pady=10)
        card.pack(fill="both", expand=True)

        def label(text, **options):
            return tk.Label(card, text=text, bg=surface, fg=ink, anchor="w", justify="left",
                            font=("Segoe UI", 10), **options)

        title = label(f"{weapon.get('info_kind', 'Arma')}: {weapon['name']}", wraplength=width - 30)
        title.configure(font=("Segoe UI", 11, "bold"))
        title.pack(fill="x")
        label(f"Preço: {weapon.get('info_price') or weapon.get('price') or 'Não informado'}",
              wraplength=width - 30).pack(fill="x", pady=(3, 8))
        if weapon.get("base_weapon"):
            label("Dados da arma-base; ajuste os efeitos mágicos no editor.",
                  wraplength=width - 30).pack(fill="x", pady=(0, 6))
        stats = tk.Frame(card, bg=surface)
        stats.pack(fill="x")
        profiles = get_weapon_profiles(weapon) if not weapon.get("catalog_entry") else []
        # Os campos marcados ** na fonte são descritos pelos modos da arma.
        base = weapon.get("base_weapon", weapon)
        damage = base.get("damage", "")
        if damage == "**" or (len(profiles) > 1 and profiles[0]["label"] == "Corpo a corpo"):
            damage = " / ".join(profile["damage"] for profile in profiles)
        threats = " / ".join(dict.fromkeys(p["threat"] or "—" for p in profiles))
        multipliers = " / ".join(dict.fromkeys(
            "x" + p["critical_multiplier"] if p["threat"] else "—" for p in profiles))
        values = (("Dano", damage or "Não informado"),
                                                   ("Crítico", threats),
                                                   ("Multiplicador", multipliers)) if profiles else ()
        for column, (heading, value) in enumerate(values):
            stats.columnconfigure(column, weight=1)
            for row, text in enumerate((heading, value)):
                tk.Label(stats, text=text, bg=surface, fg=ink, anchor="w",
                         font=("Segoe UI", 10, "bold" if row == 0 else "normal")).grid(
                             row=row, column=column, sticky="w", padx=(0, 12))
        label("Descrição").pack(fill="x", pady=(10, 3))
        details = weapon.get("description") or "Sem descrição na planilha."
        if weapon.get("profile_note"):
            details += "\n\n" + weapon["profile_note"]
        if len(profiles) > 1:
            details += "\n\nModos / empunhaduras:\n" + "\n".join(
                f"{p['label']}: {p['damage']} · {p['threat']}/x{p['critical_multiplier']}"
                for p in profiles)
        elif "/" in base.get("damage", ""):
            details += "\n\nArma dupla: a macro aplica um ataque de uma ponta."
        for key, heading in (("application", "Aplicação"), ("group", "Grupo"), ("damage_type", "Tipo de dano"),
                             ("range", "Alcance"), ("spaces", "Espaços"),
                             ("notes", "Observações"), ("source", "Fonte")):
            if weapon.get(key):
                details += f"\n\n{heading}: {weapon[key]}"
        body = tk.Frame(card, bg=surface)
        body.pack(fill="both", expand=True)
        text = tk.Text(body, wrap="word", width=1, height=1, font=("Segoe UI", 10),
                       bg=surface, fg=ink, borderwidth=0, highlightthickness=0,
                       padx=0, pady=0)
        scroll = ttk.Scrollbar(body, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        text.pack(side="left", fill="both", expand=True)
        text.insert("1.0", details)
        text.configure(state="disabled")
        popup.update_idletasks()
        # Reserva espaço para o título e mantém descrições extensas roláveis.
        available = self.owner.winfo_screenheight() - 100
        height = min(560, available)
        x = icon.winfo_rootx() + icon.winfo_width() + 8
        if x + width > self.owner.winfo_screenwidth() - 12:
            x = icon.winfo_rootx() - width - 8
        x = max(8, min(x, self.owner.winfo_screenwidth() - width - 8))
        y = max(8, min(icon.winfo_rooty(), self.owner.winfo_screenheight() - height - 48))
        popup.geometry(f"{width}x{height}+{x}+{y}")
        popup.bind("<Enter>", self.cancel_hide)
        popup.bind("<Leave>", self.schedule_hide)
        popup.bind("<Escape>", lambda _event: self.hide())
        popup.deiconify()
        popup.lift()


class WeaponBrowser(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.title("Armas")
        set_responsive_window_geometry(self, 860, 640, 660, 380)
        self.transient(app.root)
        self.grab_set()
        self.bind("<Escape>", lambda _event: self.destroy())
        self.info = WeaponInfoPopup(self)
        ttk.Label(self, text="Escolha uma arma", style="Section.TLabel").pack(
            anchor="w", padx=15, pady=(15, 5))
        ttk.Label(self, text="Clique na arma para preencher a macro. Passe o mouse em ⓘ para ver os detalhes.",
                  wraplength=600).pack(anchor="w", padx=15, pady=(0, 10))
        search = ttk.Frame(self)
        search.pack(fill="x", padx=15, pady=(0, 10))
        ttk.Label(search, text="Buscar:").pack(side="left", padx=(0, 8))
        self.search_var = tk.StringVar(self)
        entry = ttk.Entry(search, textvariable=self.search_var)
        entry.pack(side="left", fill="x", expand=True)
        ttk.Button(search, text="Limpar", command=lambda: self.search_var.set("")).pack(
            side="left", padx=(8, 0))
        self.count_var = tk.StringVar(self)
        ttk.Label(self, textvariable=self.count_var, style="Small.TLabel").pack(
            anchor="w", padx=15, pady=(0, 5))
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=(0, 12))
        self.panels = {}
        for category in WEAPON_CATEGORIES:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=category)
            if category == "Armas mágicas":
                ttk.Label(tab, text="São aplicados os dados da arma-base quando identificada. "
                          "Ajuste os efeitos mágicos no editor.", wraplength=620,
                          style="Small.TLabel").pack(anchor="w", padx=10, pady=(8, 0))
            self.panels[category] = app.create_scrollable_panel(tab, padx=8, pady=8)
        self.notebook.bind("<<NotebookTabChanged>>", lambda _event: self.info.hide())
        self.search_var.trace_add("write", self.refresh)
        self.refresh()
        entry.focus_set()

    def refresh(self, *_args):
        self.info.hide()
        query = search_key(self.search_var.get().strip())
        total = 0
        for index, (category, weapons) in enumerate(WEAPON_CATEGORIES.items()):
            content = self.panels[category]
            for child in content.winfo_children():
                child.destroy()
            matches = [weapon for weapon in weapons if query in search_key(
                " ".join((weapon["name"], weapon.get("group", ""), weapon.get("source", ""))))]
            total += len(matches)
            self.notebook.tab(index, text=category + (f" ({len(matches)})" if query else ""))
            previous_group = None
            for weapon in matches:
                group = weapon.get("group", "")
                if group and group != previous_group:
                    heading = ttk.Label(content, text=group, style="Section.TLabel")
                    heading.pack(anchor="w", pady=(10, 4))
                    self._bind_scroll(heading, content.master)
                    previous_group = group
                row = ttk.Frame(content)
                row.pack(fill="x", pady=3)
                button = ttk.Button(row, text=weapon["name"],
                                    command=lambda w=weapon: self.select_weapon(w))
                button.pack(side="left", fill="x", expand=True)
                icon = ttk.Button(row, text="ⓘ", width=3, cursor="question_arrow")
                icon.pack(side="right", padx=(6, 0))
                self.info.attach(icon, weapon)
                for widget in (row, button, icon):
                    self._bind_scroll(widget, content.master)
            if not matches:
                ttk.Label(content, text="Nenhuma arma encontrada nesta aba.").pack(
                    anchor="w", pady=15)
            content.master.yview_moveto(0)
        count = sum(len(weapons) for weapons in WEAPON_CATEGORIES.values())
        self.count_var.set(f"{total} de {count} armas" if query else f"{count} armas disponíveis")

    def _bind_scroll(self, widget, canvas):
        def scroll(event):
            self.info.hide()
            self.app.scroll_canvas_by_units(canvas, self.app.get_scroll_direction(event))
            return "break"
        for event in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            widget.bind(event, scroll)

    def select_weapon(self, weapon):
        self.info.hide()
        profiles = get_weapon_profiles(weapon)
        if len(profiles) == 1:
            self.app.apply_weapon(weapon["name"], profiles[0], self)
            return
        choice = tk.Toplevel(self)
        choice.title("Empunhadura / modo de ataque")
        set_responsive_window_geometry(choice, 510, 270, 340, 220)
        choice.transient(self)
        choice.grab_set()
        ttk.Label(choice, text=weapon["name"], style="Section.TLabel", wraplength=460).pack(
            anchor="w", padx=15, pady=15)
        ttk.Label(choice, text="Escolha como a arma será usada nesta macro:", wraplength=460).pack(
            anchor="w", padx=15, pady=(0, 8))

        def apply(profile):
            choice.destroy()
            self.app.apply_weapon(weapon["name"], profile, self)

        def cancel(_event=None):
            choice.destroy()
            self.grab_set()
            return "break"

        for profile in profiles:
            ttk.Button(choice, text=f"{profile['label']} — {profile['damage']} · "
                       f"crítico {profile['threat']}/x{profile['critical_multiplier']}",
                       command=lambda p=profile: apply(p)).pack(fill="x", padx=15, pady=4)
        choice.protocol("WM_DELETE_WINDOW", cancel)
        choice.bind("<Escape>", cancel)
