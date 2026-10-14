from html import unescape
import tkinter as tk
from tkinter import ttk, messagebox

from constants import (
    ATTACK_PRIDE_EFFECT,
    BEST_DIE_FORMULA,
    RESISTANCE_MACRO_BASE,
    SKILL_MACRO_BASE,
    SKILL_MACRO_CLOSING,
    VERSAO,
)
from libraries import (
    ATTRIBUTES,
    COMMON_WEAPONS,
    DAMAGE_STEP_TRACKS,
    DADOSCOMUNS,
    DADOSEXOTICOS,
    PERICIAS_ESPECIALISTA,
)
from ui_theme import configure_theme, update_canvas_scroll_region

from preview import PreviewMixin, format_roll_preview, get_preview_question_choices

from auto_update import update_frozen_app
from ui_theme import set_responsive_window_geometry

from macro_core import (
    get_damage_step_options,
    get_damage_step_delta,
    get_damage_step_track,
    build_attack_expression,
    build_critical_damage,
    join_formula_parts,
    simplify_condition_questions,
    build_damage_roll_formula,
    build_damage_expression,
    build_critical_expression,
    QuestionOption,
    MacroQuestion,
    build_condition_question,
    build_modified_condition_question,
    parse_result_modified_condition,
    build_advanced_question_value,
    looks_like_roll20_condition,
    close_advanced_questions_before_outer_pipe,
    parse_roll20_question,
    extract_roll20_question_names,
    split_roll20_components,
    render_generated_macro,
    parse_generated_macro_state,
    MacroButton,
)



class MacroBuilderApp(PreviewMixin):
    def __init__(self, root):
        self.root = root
        self.skill_macro_extra = ""
        self.skill_macro_question_name = "Pergunta"
        self.skill_macro_question_options = []
        self.skill_macro_pride_enabled = False
        self.skill_macro_effect_enabled = True
        self.skill_macro_effect_value = ""
        self.skill_macro_effect_mode = "multiplicativo"
        self.skill_macro_specialist_enabled = False
        self.skill_macro_specialist_skills = []
        self.skill_macro_specialist_intelligence = "1"
        self.skill_macro_button = None
        self.skill_macro_gear_button = None
        self.resistance_macro_extra = ""
        self.resistance_macro_question_name = "Pergunta"
        self.resistance_macro_question_options = []
        self.resistance_macro_pride_enabled = False
        self.resistance_macro_effect_enabled = True
        self.resistance_macro_effect_value = ""
        self.resistance_macro_effect_mode = "multiplicativo"
        self.resistance_macro_button = None
        self.resistance_macro_gear_button = None
        self.root.title("Roll20 Macro Builder")
        set_responsive_window_geometry(self.root, 1280, 820, 560, 480)

        self.setup_style()
        self.build_ui()
        self.update_preview()

    # ========================================================
    # Interface
    # ========================================================

    def setup_style(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        configure_theme(self.root, style)
        self.configure_preview_styles(style)

    def build_ui(self):
        page_viewport = ttk.Frame(self.root)
        page_viewport.pack(fill="both", expand=True)
        page_viewport.columnconfigure(0, weight=1)
        page_viewport.rowconfigure(0, weight=1)

        self.page_canvas = tk.Canvas(
            page_viewport,
            highlightthickness=0,
        )
        self.page_canvas.grid(row=0, column=0, sticky="nsew")
        self.page_scrollbar = ttk.Scrollbar(
            page_viewport,
            orient="vertical",
            command=self.page_canvas.yview,
        )
        self.page_canvas.configure(
            yscrollcommand=self.page_scrollbar.set,
        )
        self.page_content = ttk.Frame(self.page_canvas)
        self.page_canvas_window = self.page_canvas.create_window(
            (0, 0),
            window=self.page_content,
            anchor="nw",
        )
        self.page_content.bind(
            "<Configure>",
            lambda _event: self.schedule_page_scrollbar_update(),
        )
        self.page_canvas.bind(
            "<Configure>",
            self.resize_page_content,
        )
        self.root.bind_all("<MouseWheel>", self.scroll_main_page, add="+")
        self.root.bind_all("<Button-4>", self.scroll_main_page, add="+")
        self.root.bind_all("<Button-5>", self.scroll_main_page, add="+")

        # ----------------------------------------------------
        # Topo
        # ----------------------------------------------------
        header = ttk.Frame(self.page_content, padding=(12, 10))
        header.pack(fill="x", pady=(8, 4))

        ttk.Label(
            header,
            text="Macro Generator",
            style="Title.TLabel"
        ).pack(side="left")

        ttk.Label(
            header,
            text= "V"+VERSAO,
            style="Small.TLabel"
        ).pack(side="left", padx=(12, 0))

        build_info = [None]
        build_info_button = ttk.Label(
            header,
            text="ⓘ",
            cursor="question_arrow",
            foreground="#286090",
        )
        build_info_button.pack(side="left", padx=(6, 0))
        build_info_text = (
            "Build 0.01.8\n"
            "- Adicionados novos módulos\n"
            "- Adicionadas macros básicas de Perícias e Resistências, "
            "com alternadores para condicionais\n"
            "- Adicionado módulo para alterar e adicionar novos efeitos às "
            "condicionais, como efeitos multiplicativos e modularidade de dados\n"
            "- Adicionado o efeito de Macro Universal para ataques "
            "(para habilidades aplicadas a tudo)\n"
            "  - Mini revamp na interface para tentar evitar que componentes "
            "sejam cortados da tela\n"
            "  - Início da adição de botões que geram efeitos de habilidades "
            "de classe e os adicionam diretamente às macros "
            "(Orgulho do Nobre foi o primeiro a ser testado)"
        )

        def show_build_info(_event):
            if build_info[0] is not None:
                return
            tooltip = tk.Toplevel(self.root)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(
                f"+{build_info_button.winfo_rootx()}+"
                f"{build_info_button.winfo_rooty() + build_info_button.winfo_height()}"
            )
            tk.Label(
                tooltip,
                text=build_info_text,
                justify="left",
                wraplength=520,
                background="#fff8dc",
                foreground="#333333",
                relief="solid",
                borderwidth=1,
                padx=8,
                pady=6,
            ).pack()
            build_info[0] = tooltip

        def hide_build_info(_event):
            if build_info[0] is not None:
                build_info[0].destroy()
                build_info[0] = None

        build_info_button.bind("<Enter>", show_build_info)
        build_info_button.bind("<Leave>", hide_build_info)

        # ----------------------------------------------------
        # Nome da macro
        # ----------------------------------------------------
        name_frame = ttk.Frame(self.page_content, padding=(16, 0, 16, 12))
        name_frame.pack(fill="x")
        name_frame.columnconfigure(0, weight=3)
        name_frame.columnconfigure(1, weight=2)
        ttk.Label(name_frame, text="NOME DO ATAQUE", style="Small.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 5))
        ttk.Label(name_frame, text="NOME EXIBIDO", style="Small.TLabel").grid(row=0, column=1, sticky="w", padx=(12, 0), pady=(0, 5))
        self.attack_name_var = tk.StringVar(value="Nome Ataque")
        self.character_display_var = tk.StringVar(value="")
        ttk.Entry(name_frame, textvariable=self.attack_name_var, width=20).grid(row=1, column=0, sticky="ew")
        ttk.Entry(name_frame, textvariable=self.character_display_var, width=16).grid(row=1, column=1, sticky="ew", padx=(12, 0))
        for variable in (self.attack_name_var, self.character_display_var):
            variable.trace_add("write", lambda *_: self.update_preview())

        self.workspace_nav = ttk.Frame(self.page_content, padding=(16, 0, 16, 10))
        self.workspace_section = tk.StringVar(value="editor")
        for value, label in (("components", "Componentes"), ("editor", "Montar ataque"), ("preview", "Macro e prévia")):
            ttk.Radiobutton(self.workspace_nav, text=label, value=value,
                            variable=self.workspace_section, style="Nav.TRadiobutton",
                            command=self.layout_workspace).pack(side="left", padx=(0, 8))

        self.workspace = ttk.Frame(self.page_content, padding=(12, 10, 12, 12), style="App.TFrame")
        self.workspace.pack(fill="both", expand=True)
        self.workspace.rowconfigure(0, weight=1)
        self.workspace_panels = {}
        for key in ("components", "editor", "preview"):
            self.workspace_panels[key] = ttk.Frame(self.workspace, padding=12, style="Card.TFrame")
        self.workspace_panels["components"].configure(width=205)
        self.workspace_panels["components"].pack_propagate(False)
        self.build_component_panel(self.create_scrollable_panel(self.workspace_panels["components"]))
        self.build_editor_panel(self.create_scrollable_panel(self.workspace_panels["editor"]))
        self.build_preview_panel(self.workspace_panels["preview"])
        self._workspace_compact = None
        self.layout_workspace()
        self.schedule_page_scrollbar_update()

    def layout_workspace(self):
        compact = self.page_canvas.winfo_width() < 1120
        if compact:
            self.workspace_nav.pack(fill="x", before=self.workspace)
        else:
            self.workspace_nav.pack_forget()
        for panel in self.workspace_panels.values():
            panel.grid_remove()
        for column in range(3):
            self.workspace.columnconfigure(column, weight=0, minsize=0)
        if compact:
            self.workspace.columnconfigure(0, weight=1)
            self.workspace_panels[self.workspace_section.get()].grid(row=0, column=0, sticky="nsew")
        else:
            for column, key in enumerate(("components", "editor", "preview")):
                self.workspace.columnconfigure(column, weight=(0, 3, 4)[column], minsize=(195, 400, 390)[column])
                self.workspace_panels[key].grid(row=0, column=column, sticky="nsew", padx=(0, 8) if column < 2 else 0)
        self._workspace_compact = compact

    def resize_page_content(self, event):
        self.page_canvas.itemconfigure(
            self.page_canvas_window,
            width=event.width,
        )
        if hasattr(self, "workspace") and (event.width < 1120) != self._workspace_compact:
            self.layout_workspace()
        self.schedule_page_scrollbar_update()

    def schedule_page_scrollbar_update(self):
        if getattr(self, "_page_scroll_update_pending", False):
            return
        self._page_scroll_update_pending = True
        self.root.after_idle(self.update_page_scrollbar)

    def update_page_scrollbar(self):
        self._page_scroll_update_pending = False
        viewport_height = self.page_canvas.winfo_height()
        content_height = max(560, viewport_height)
        self.page_canvas.itemconfigure(self.page_canvas_window, height=content_height)
        needs_scrollbar = content_height > viewport_height + 1
        scrollbar_visible = bool(self.page_scrollbar.winfo_manager())
        if needs_scrollbar != scrollbar_visible:
            if needs_scrollbar:
                self.page_scrollbar.grid(row=0, column=1, sticky="ns")
            else:
                self.page_scrollbar.grid_remove()

        self.page_canvas.configure(
            scrollregion=(0, 0, self.page_canvas.winfo_width(), content_height)
        )
        if not needs_scrollbar:
            self.page_canvas.yview_moveto(0)

    def scroll_main_page(self, event):
        widget = event.widget
        scroll_canvas = None
        if isinstance(widget, ttk.Scrollbar):
            scroll_canvas = next(
                (
                    child
                    for child in widget.master.winfo_children()
                    if isinstance(child, tk.Canvas)
                ),
                None,
            )
        else:
            current = widget
            while current is not None and current is not self.root:
                if isinstance(current, tk.Canvas):
                    scroll_canvas = current
                    break
                current = current.master

        if scroll_canvas is not None and scroll_canvas is not self.page_canvas:
            direction = self.get_scroll_direction(event)
            self.scroll_canvas_by_units(scroll_canvas, direction)
            return "break"

        widget_path = str(widget)
        content_path = str(self.page_content)
        if not (
            widget_path == content_path
            or widget_path.startswith(content_path + ".")
        ):
            return None

        direction = self.get_scroll_direction(event)
        self.scroll_canvas_by_units(self.page_canvas, direction)
        return "break"

    @staticmethod
    def get_scroll_direction(event):
        if getattr(event, "num", None) == 4:
            return -1
        if getattr(event, "num", None) == 5:
            return 1
        direction = int(-event.delta / 120)
        if direction == 0:
            direction = -1 if event.delta > 0 else 1
        return direction

    @staticmethod
    def scroll_canvas_by_units(canvas, direction):
        top, bottom = canvas.yview()
        if bottom - top >= 0.98:
            return False
        at_top = direction < 0 and top <= 0.01
        at_bottom = direction > 0 and bottom >= 0.99
        if at_top or at_bottom:
            return False
        canvas.yview_scroll(direction, "units")
        return True

    # ========================================================
    # Painel de componentes
    # ========================================================

    def build_component_panel(self, parent):
        ttk.Label(
            parent,
            text="Componentes",
            style="Section.TLabel"
        ).pack(anchor="w", pady=(0, 8))

        ttk.Label(
            parent,
            text="Insira elementos Roll20 nos campos.",
            wraplength=130
        ).pack(anchor="w", pady=(0, 12))

        buttons = [
            ("Armas comuns", self.open_common_weapons_dialog),
            ("Passos de Dano", self.insert_fixed_bonus),
            ("Pergunta Roll20", self.insert_question),
            ("Botão de macro", self.insert_button),
            ("Importar macro", self.insert_custom),
        ]

        for text, command in buttons:
            ttk.Button(
                parent,
                text=text,
                command=command,
                padding=(4, 8),
            ).pack(fill="x", pady=3)

        ttk.Separator(parent).pack(fill="x", pady=12)

        ttk.Label(
            parent,
            text="Macros Base",
            style="Section.TLabel"
        ).pack(anchor="w", pady=(0, 6))

        attr_frame = ttk.Frame(parent)
        attr_frame.pack(fill="x")

        for name, code in ATTRIBUTES.items():
            if name == "Força":
                skill_frame = ttk.Frame(attr_frame)
                skill_frame.pack(fill="x", pady=2)
                self.skill_macro_button = ttk.Button(
                    skill_frame,
                    text="⚒ Perícias",
                    command=self.copy_skill_macro,
                    padding=(4, 8),
                )
                self.skill_macro_button.pack(
                    side="left",
                    fill="x",
                    expand=True,
                )
                self.skill_macro_gear_button = ttk.Button(
                    skill_frame,
                    text="⚙",
                    width=3,
                    command=self.open_skill_macro_editor,
                )
                self.skill_macro_gear_button.pack(side="left", padx=(4, 0))
                self.update_skill_macro_gear_style()
                continue

            if name == "Destreza":
                resistance_frame = ttk.Frame(attr_frame)
                resistance_frame.pack(fill="x", pady=2)
                self.resistance_macro_button = ttk.Button(
                    resistance_frame,
                    text="💪 Resistências",
                    command=self.copy_resistance_macro,
                    padding=(4, 8),
                )
                self.resistance_macro_button.pack(
                    side="left",
                    fill="x",
                    expand=True,
                )
                self.resistance_macro_gear_button = ttk.Button(
                    resistance_frame,
                    text="⚙",
                    width=3,
                    command=lambda: self.open_skill_macro_editor("resistance"),
                )
                self.resistance_macro_gear_button.pack(
                    side="left",
                    padx=(4, 0),
                )
                self.update_resistance_macro_gear_style()
                continue

            ttk.Button(
                attr_frame,
                text=name,
                command=lambda c=code: self.insert_text(c),
                padding=(4, 8),
            ).pack(fill="x", pady=2)

    def create_scrollable_panel(
        self,
        parent,
        padx=0,
        pady=0,
        canvas_height=None,
    ):
        container = ttk.Frame(parent)
        container.pack(
            fill="both",
            expand=True,
            padx=padx,
            pady=pady,
        )
        canvas = tk.Canvas(container, highlightthickness=0)
        if canvas_height is not None:
            canvas.configure(height=canvas_height)
        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview,
        )
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def update_scroll_region(_event=None):
            update_canvas_scroll_region(canvas, scrollbar)

        def scroll_panel(event):
            self.scroll_canvas_by_units(
                canvas,
                self.get_scroll_direction(event),
            )
            return "break"

        canvas.bind("<MouseWheel>", scroll_panel)
        canvas.bind("<Button-4>", scroll_panel)
        canvas.bind("<Button-5>", scroll_panel)

        content = ttk.Frame(canvas)
        canvas_window = canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw",
        )
        content.bind(
            "<Configure>",
            update_scroll_region,
        )
        canvas.bind(
            "<Configure>",
            lambda event: (
                canvas.itemconfigure(
                    canvas_window,
                    width=event.width,
                ),
                canvas.after_idle(update_scroll_region),
            ),
        )
        return content

    def add_result_modifier_warning(self, parent, value_var):
        warning_text = (
            "Para macros com alterador de valor final, são aconselhadas "
            "habilidades modulares, cujo uso depende de quanto está disposto "
            "a investir. Dessa maneira, recomenda-se colocar apenas o efeito "
            "que será multiplicado ou adicionado pelo gasto. Se optar por "
            "valores fixos, faça um para cada gasto."
        )
        tooltip = [None]
        icon = ttk.Label(
            parent,
            text="⚠",
            foreground="#8a5a00",
            cursor="question_arrow",
        )

        def hide_tooltip(_event=None):
            if tooltip[0] is not None:
                tooltip[0].destroy()
                tooltip[0] = None

        def show_tooltip(_event):
            if tooltip[0] is not None:
                return
            popup = tk.Toplevel(parent.winfo_toplevel())
            popup.wm_overrideredirect(True)
            popup.wm_geometry(
                f"+{icon.winfo_rootx()}+"
                f"{icon.winfo_rooty() + icon.winfo_height()}"
            )
            tk.Label(
                popup,
                text=warning_text,
                justify="left",
                wraplength=420,
                background="#fff3cd",
                foreground="#8a5a00",
                relief="solid",
                borderwidth=1,
                padx=8,
                pady=6,
            ).pack()
            tooltip[0] = popup

        def update_warning(*_args):
            if value_var.get().strip():
                if not icon.winfo_manager():
                    icon.pack(side="right", padx=(8, 0))
            else:
                hide_tooltip()
                icon.pack_forget()

        icon.bind("<Enter>", show_tooltip)
        icon.bind("<Leave>", hide_tooltip)
        value_var.trace_add("write", update_warning)
        update_warning()
        return icon

    def make_responsive_grid(
        self,
        frame,
        widgets,
        minimum_cell_width,
        maximum_columns=None,
    ):
        previous_columns = 0

        def layout(event):
            nonlocal previous_columns
            columns = max(1, event.width // minimum_cell_width)
            if maximum_columns is not None:
                columns = min(columns, maximum_columns)
            if columns == previous_columns:
                return
            for column in range(max(columns, previous_columns)):
                frame.columnconfigure(column, weight=1 if column < columns else 0)
            for index, widget in enumerate(widgets):
                widget.grid_configure(row=index // columns, column=index % columns, sticky="ew")
            previous_columns = columns

        frame.bind("<Configure>", layout)

    # ========================================================
    # Painel editor
    # ========================================================

    def toggle_best_attack_die(self):
        formula = BEST_DIE_FORMULA if self.attack_best_die_var.get() == "sim" else "1d20"
        self.attack_roll_var.set(formula)
        self.update_preview()

    def toggle_attack_extra_field(self):
        if hasattr(self, "attack_extra_frame"):
            if self.attack_extra_enabled_var.get():
                self.attack_extra_frame.grid()
            else:
                self.attack_extra_frame.grid_remove()
        self.update_preview()

    def toggle_damage_extra_field(self):
        if hasattr(self, "damage_extra_frame"):
            if self.damage_extra_enabled_var.get():
                self.damage_extra_frame.grid()
            else:
                self.damage_extra_frame.grid_remove()
        self.update_preview()

    def toggle_exotic_dice_field(self):
        if hasattr(self, "damage_exotic_frame"):
            if self.damage_exotic_enabled_var.get():
                self.damage_exotic_frame.grid()
            else:
                self.damage_exotic_frame.grid_remove()

    def get_damage_extra_values(self):
        values = []
        for var in getattr(self, "damage_extra_vars", []):
            value = var.get().strip()
            if value:
                if value.startswith("?{") and value.endswith("}"):
                    values.append(value)
                else:
                    values.append(f"[[{value}]]")
        return values

    def get_attack_extra_values(self):
        values = []
        for var in getattr(self, "attack_extra_vars", []):
            value = var.get().strip()
            if value:
                values.append(value)
        return values

    def set_attack_universal_flags(self, index, flags):
        if index >= len(self.attack_extra_universal_flags):
            return
        self.attack_extra_universal_flags[index] = list(flags)
        self.update_preview()

    def get_attack_universal_conditions(self):
        conditions = []
        flags_by_field = getattr(self, "attack_extra_universal_flags", [])
        for field_index, variable in enumerate(
            getattr(self, "attack_extra_vars", [])
        ):
            flags = (
                flags_by_field[field_index]
                if field_index < len(flags_by_field)
                else []
            )
            condition_index = 0
            for component in split_roll20_components(variable.get()):
                modified = parse_result_modified_condition(component)
                question = modified[0] if modified else component
                if not looks_like_roll20_condition(question):
                    continue
                is_universal = (
                    flags[condition_index]
                    if condition_index < len(flags)
                    else False
                )
                condition_index += 1
                if is_universal:
                    conditions.append(simplify_condition_questions(question))
        return conditions

    def select_attack_attribute(self, attribute):
        self.attack_attribute_var.set(attribute)

    def on_attack_attribute_changed(self):
        self.update_attack_attribute_buttons()
        self.update_preview()

    def update_attack_attribute_buttons(self):
        for attribute, button in getattr(
            self,
            "attack_attribute_buttons",
            {},
        ).items():
            button.configure(
                style=(
                    "Selected.TButton"
                    if self.attack_attribute_var.get() == attribute
                    else "TButton"
                )
            )

    def toggle_damage_attribute(self, attribute):
        variable = self.damage_attribute_vars[attribute]
        variable.set(not variable.get())

    def update_damage_attribute_button(self, attribute):
        button = getattr(self, "damage_attribute_buttons", {}).get(attribute)
        if button is not None:
            button.configure(
                style=(
                    "Selected.TButton"
                    if self.damage_attribute_vars[attribute].get()
                    else "TButton"
                )
            )

    def render_attack_extra_field(self, index):
        value = self.attack_extra_vars[index].get().strip()
        is_pride = value == ATTACK_PRIDE_EFFECT
        entry = self.attack_extra_entries[index]
        pride_button = self.attack_extra_pride_buttons[index]
        conditional_button = self.attack_extra_conditional_buttons[index]
        if is_pride:
            entry.pack_forget()
            pride_button.pack(fill="x", before=conditional_button)
            conditional_button.configure(state="disabled")
        else:
            pride_button.pack_forget()
            entry.pack(fill="x", before=conditional_button)
            conditional_button.configure(state="normal")

    def remove_attack_pride_effect(self, index):
        self.attack_extra_vars[index].set("")

    def on_attack_extra_changed(self, index):
        if index < len(self.attack_extra_universal_flags):
            self.attack_extra_universal_flags[index] = []
        if self.attack_extra_vars[index].get().strip() == ATTACK_PRIDE_EFFECT:
            for other_index, variable in enumerate(self.attack_extra_vars):
                if (
                    other_index != index
                    and variable.get().strip() == ATTACK_PRIDE_EFFECT
                ):
                    variable.set("")
        self.render_attack_extra_field(index)
        self.update_preview()

    def sync_critical_from_damage(self):
        if not hasattr(self, "critical_var"):
            return

        try:
            repeats = int(self.critical_repeat_var.get().strip() or "2")
        except ValueError:
            repeats = 2

        damage_formula = simplify_condition_questions(
            (self.damage_var.get() or "").strip()
        )
        additional_formula = simplify_condition_questions(
            (self.damage_additional_var.get() or "").strip()
        )
        critical_parts = []
        if damage_formula:
            critical_parts.append(build_critical_damage(damage_formula, repeats))
        if additional_formula:
            critical_parts.append(additional_formula)
        critical_formula = join_formula_parts(*critical_parts)
        self.critical_var.set(critical_formula)
        if hasattr(self, "update_preview"):
            self.update_preview()

    def create_toggle_section(
        self,
        parent,
        title,
        expanded=False,
        expand_on_open=False,
        pady=(0, 8),
        header_action_variable=None,
    ):
        section = ttk.Frame(parent)
        section.pack(fill="x", pady=pady)
        content = ttk.Frame(section, padding=8, relief="groove", borderwidth=1)

        def toggle():
            if content.winfo_manager():
                content.pack_forget()
                button.configure(text=f"+ {title}")
                section.pack_configure(fill="x", expand=False)
            else:
                content.pack(
                    fill="both" if expand_on_open else "x",
                    expand=expand_on_open,
                    pady=(2, 0),
                )
                button.configure(text=f"- {title}")
                section.pack_configure(
                    fill="both" if expand_on_open else "x",
                    expand=expand_on_open,
                )

        button_parent = section
        if header_action_variable is not None:
            button_parent = ttk.Frame(section)
            button_parent.pack(fill="x")
        button = ttk.Button(
            button_parent,
            text=f"- {title}" if expanded else f"+ {title}",
            command=toggle,
        )
        button.pack(
            side="left" if button_parent is not section else "top",
            fill="x",
            expand=button_parent is not section,
        )
        if header_action_variable is not None:
            ttk.Checkbutton(
                button_parent,
                text="Condição Universal",
                variable=header_action_variable,
            ).pack(side="right", padx=(8, 0))

        if expanded:
            content.pack(fill="x", pady=(2, 0))

        return content

    def build_editor_panel(self, parent):
        ttk.Label(
            parent,
            text="Montagem do ataque",
            style="Section.TLabel"
        ).pack(anchor="w", pady=(0, 8))

        # ----------------------------------------------
        # Ataque
        # ----------------------------------------------
        attack_box = self.create_toggle_section(
            parent,
            "Rolagem de ataque",
            expanded=True,
        )

        self.attack_roll_var = tk.StringVar(value="1d20")
        self.attack_threat_var = tk.StringVar(value="18")
        self.attack_best_die_var = tk.StringVar(value="nao")

        ttk.Label(
            attack_box,
            text="Fórmula:"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        best_die_frame = ttk.Frame(attack_box)
        best_die_frame.grid(row=0, column=1, sticky="e")
        ttk.Label(best_die_frame, text="Melhor dado:").pack(side="left", padx=(0, 4))
        for label, value in [("Não", "nao"), ("Sim", "sim")]:
            ttk.Radiobutton(
                best_die_frame,
                text=label,
                variable=self.attack_best_die_var,
                value=value,
                command=self.toggle_best_attack_die,
            ).pack(side="left", padx=(0, 4))

        self.attack_entry = ttk.Entry(
            attack_box,
            textvariable=self.attack_roll_var,
            state="readonly",
        )
        self.attack_entry.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(4, 6)
        )

        ttk.Label(
            attack_box,
            text="Margem de ameaça:",
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=(0, 4),
        )

        numeric_validation = (
            self.root.register(lambda value: value.isdigit() or value == ""),
            "%P",
        )
        ttk.Spinbox(
            attack_box,
            textvariable=self.attack_threat_var,
            from_=0,
            to=99,
            width=5,
            validate="key",
            validatecommand=numeric_validation,
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=(0, 6),
        )

        self.attack_extra_enabled_var = tk.BooleanVar(value=False)
        self.attack_extra_vars = [
            tk.StringVar(),
            tk.StringVar(),
            tk.StringVar(),
        ]
        self.attack_extra_universal_flags = [[], [], []]
        ttk.Checkbutton(
            attack_box,
            text="Efeito extra",
            variable=self.attack_extra_enabled_var,
            command=self.toggle_attack_extra_field,
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=(8, 2),
        )

        self.attack_extra_frame = ttk.Frame(attack_box)
        self.attack_extra_frame.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="ew",
        )

        attack_extra_fields = []
        self.attack_extra_entries = []
        self.attack_extra_pride_buttons = []
        self.attack_extra_conditional_buttons = []
        for idx, var in enumerate(self.attack_extra_vars):
            field_frame = ttk.Frame(self.attack_extra_frame)
            field_frame.grid(row=0, column=idx, sticky="ew", padx=(0, 6))
            attack_extra_fields.append(field_frame)
            entry = ttk.Entry(
                field_frame,
                textvariable=var,
                width=20,
            )
            entry.pack(fill="x")
            pride_button = ttk.Button(
                field_frame,
                text="👑 Orgulho",
                style="Pride.TButton",
                command=lambda index=idx: self.remove_attack_pride_effect(
                    index
                ),
            )
            conditional_button = ttk.Button(
                field_frame,
                text="Condicional?",
                command=lambda index=idx: self.insert_attack_conditional(index),
            )
            conditional_button.pack(fill="x", pady=(3, 0))
            self.attack_extra_entries.append(entry)
            self.attack_extra_pride_buttons.append(pride_button)
            self.attack_extra_conditional_buttons.append(
                conditional_button
            )
            var.trace_add(
                "write",
                lambda *_args, index=idx: self.on_attack_extra_changed(
                    index
                ),
            )
            self.render_attack_extra_field(idx)

        self.make_responsive_grid(
            self.attack_extra_frame,
            attack_extra_fields,
            minimum_cell_width=190,
        )

        self.attack_extra_frame.grid_remove()
        self.toggle_attack_extra_field()

        self.attack_roll_var.trace_add(
            "write",
            lambda *_: self.update_preview()
        )
        self.attack_threat_var.trace_add(
            "write",
            lambda *_: self.update_preview()
        )

        # ----------------------------------------------
        # Atributo do ataque
        # ----------------------------------------------
        self.attack_attribute_var = tk.StringVar(value="Luta")

        ttk.Label(
            attack_box,
            text="Pericia:"
        ).grid(
            row=6,
            column=0,
            sticky="w",
            pady=(0, 4)
        )

        attribute_frame = ttk.Frame(attack_box)
        attribute_frame.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="ew",
        )

        attack_attribute_buttons = []
        self.attack_attribute_buttons = {}
        for attribute in [
            "Luta",
            "Pontaria",
            "Atuação",
            "Furtividade"
        ]:
            button = ttk.Button(
                attribute_frame,
                text=attribute,
                command=lambda selected=attribute: self.select_attack_attribute(
                    selected
                ),
                padding=(10, 6),
            )
            attack_attribute_buttons.append(button)
            self.attack_attribute_buttons[attribute] = button
        self.make_responsive_grid(
            attribute_frame,
            attack_attribute_buttons,
            minimum_cell_width=100,
        )

        self.attack_attribute_var.trace_add(
            "write",
            lambda *_: self.on_attack_attribute_changed(),
        )
        self.update_attack_attribute_buttons()

        attack_box.columnconfigure(
            0,
            weight=1
        )
        attack_box.columnconfigure(1, weight=1)

        # ----------------------------------------------
        # Dano
        # ----------------------------------------------
        damage_box = self.create_toggle_section(
            parent,
            "Dano",
            expanded=True,
        )

        self.damage_var = tk.StringVar(
            value="1d8"
        )
        self.damage_additional_var = tk.StringVar()

        self.damage_exotic_enabled_var = tk.BooleanVar(value=False)

        common_dice_frame = ttk.LabelFrame(
            damage_box,
            text="Comuns",
            padding=6
        )
        common_dice_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 6)
        )

        common_dice_buttons = []
        for index, (label, value) in enumerate(DADOSCOMUNS.items()):
            button = ttk.Button(
                common_dice_frame,
                text=label,
                width=6,
                command=lambda v=value: self.add_to_entry(
                    self.damage_entry,
                    self.damage_var,
                    v
                )
            )
            button.grid(
                row=0,
                column=index,
                sticky="w",
                padx=(0, 4),
                pady=2
            )
            common_dice_buttons.append(button)
        self.make_responsive_grid(
            common_dice_frame,
            common_dice_buttons,
            minimum_cell_width=58,
        )

        ttk.Checkbutton(
            damage_box,
            text="Exóticos",
            variable=self.damage_exotic_enabled_var,
            command=self.toggle_exotic_dice_field
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=(0, 4)
        )

        self.damage_exotic_frame = ttk.LabelFrame(
            damage_box,
            text="Exóticos",
            padding=6
        )
        self.damage_exotic_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 6)
        )

        exotic_values = list(DADOSEXOTICOS.items())
        exotic_dice_buttons = []
        for index, (label, value) in enumerate(exotic_values):
            button = ttk.Button(
                self.damage_exotic_frame,
                text=label,
                width=6,
                command=lambda v=value: self.add_to_entry(
                    self.damage_entry,
                    self.damage_var,
                    v
                )
            )
            button.grid(
                row=index // 7,
                column=index % 7,
                sticky="w",
                padx=(0, 4),
                pady=2
            )
            exotic_dice_buttons.append(button)
        self.make_responsive_grid(
            self.damage_exotic_frame,
            exotic_dice_buttons,
            minimum_cell_width=58,
        )

        self.toggle_exotic_dice_field()

        damage_fields = ttk.Frame(damage_box)
        damage_fields.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(0, 6),
        )
        damage_fields.columnconfigure(0, weight=1, uniform="damage-fields")
        damage_fields.columnconfigure(1, weight=1, uniform="damage-fields")

        ttk.Label(damage_fields, text="Dano:").grid(
            row=0, column=0, sticky="w", padx=(0, 6)
        )
        self.damage_entry = ttk.Entry(
            damage_fields,
            textvariable=self.damage_var,
        )
        self.damage_entry.grid(
            row=1, column=0, sticky="ew", padx=(0, 6), pady=(4, 2)
        )
        ttk.Button(
            damage_fields,
            text="Condicional?",
            command=lambda: self.insert_damage_field_conditional(self.damage_var),
        ).grid(row=2, column=0, pady=(0, 4))

        ttk.Label(damage_fields, text="Dano adicional:").grid(
            row=0, column=1, sticky="w", padx=(6, 0)
        )
        self.damage_additional_entry = ttk.Entry(
            damage_fields,
            textvariable=self.damage_additional_var,
        )
        self.damage_additional_entry.grid(
            row=1, column=1, sticky="ew", padx=(6, 0), pady=(4, 2)
        )
        ttk.Button(
            damage_fields,
            text="Condicional?",
            command=lambda: self.insert_damage_field_conditional(self.damage_additional_var),
        ).grid(row=2, column=1, pady=(0, 4))

        self.damage_var.trace_add(
            "write",
            lambda *_: self.sync_critical_from_damage()
        )
        self.damage_additional_var.trace_add(
            "write",
            lambda *_: self.sync_critical_from_damage()
        )
        self.damage_entry.bind(
            "<KeyRelease>",
            lambda e: self.update_preview()
        )

        self.damage_attribute_vars = {
            attribute: tk.BooleanVar(value=attribute == "Força")
            for attribute in ATTRIBUTES
        }
        ttk.Label(
            damage_box,
            text="Atributos do dano:"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=(0, 4)
        )

        damage_attr_frame = ttk.Frame(damage_box)
        damage_attr_frame.grid(
            row=5,
            column=0,
            sticky="ew"
        )

        damage_attribute_buttons = []
        self.damage_attribute_buttons = {}
        for attribute in ATTRIBUTES.keys():
            button = ttk.Button(
                damage_attr_frame,
                text=attribute,
                command=lambda selected=attribute: self.toggle_damage_attribute(
                    selected
                ),
                padding=(10, 6),
            )
            damage_attribute_buttons.append(button)
            self.damage_attribute_buttons[attribute] = button
        self.make_responsive_grid(
            damage_attr_frame,
            damage_attribute_buttons,
            minimum_cell_width=100,
        )

        for attribute, attribute_var in self.damage_attribute_vars.items():
            attribute_var.trace_add(
                "write",
                lambda *_args, selected=attribute: (
                    self.update_damage_attribute_button(selected),
                    self.update_preview(),
                ),
            )
        for attribute in self.damage_attribute_vars:
            self.update_damage_attribute_button(attribute)

        self.damage_extra_enabled_var = tk.BooleanVar(value=False)
        self.damage_extra_vars = [
            tk.StringVar(),
            tk.StringVar(),
            tk.StringVar(),
        ]

        ttk.Checkbutton(
            damage_box,
            text="Efeito extra",
            variable=self.damage_extra_enabled_var,
            command=self.toggle_damage_extra_field
        ).grid(
            row=7,
            column=0,
            sticky="w",
            pady=(10, 2)
        )

        self.damage_extra_frame = ttk.Frame(damage_box)
        self.damage_extra_frame.grid(
            row=8,
            column=0,
            sticky="ew"
        )

        damage_extra_fields = []
        for idx, var in enumerate(self.damage_extra_vars):
            field_frame = ttk.Frame(self.damage_extra_frame)
            field_frame.grid(row=0, column=idx, sticky="ew", padx=(0, 6))
            damage_extra_fields.append(field_frame)
            ttk.Entry(
                field_frame,
                textvariable=var,
                width=20
            ).pack(fill="x")
            ttk.Button(
                field_frame,
                text="Condicional?",
                command=lambda index=idx: self.insert_damage_conditional(index)
            ).pack(fill="x", pady=(3, 0))
            var.trace_add("write", lambda *_: self.update_preview())

        self.make_responsive_grid(
            self.damage_extra_frame,
            damage_extra_fields,
            minimum_cell_width=190,
        )

        self.damage_extra_frame.grid_remove()
        self.toggle_damage_extra_field()

        damage_box.columnconfigure(
            0,
            weight=1
        )

        # ----------------------------------------------
        # Crítico
        # ----------------------------------------------
        critical_box = self.create_toggle_section(
            parent,
            "Dano crítico (Multiplicador crítico)",
        )

        critical_controls = ttk.Frame(critical_box)
        critical_controls.pack(fill="x")

        ttk.Label(
            critical_controls,
            text="Multiplicador:"
        ).pack(side="left")

        self.critical_repeat_var = tk.StringVar(value="2")
        ttk.Entry(
            critical_controls,
            textvariable=self.critical_repeat_var,
            width=8
        ).pack(side="left", padx=(8, 0))

        self.critical_repeat_var.trace_add(
            "write",
            lambda *_: self.sync_critical_from_damage()
        )

        self.damage_type_var = tk.StringVar(
            value="Tipo Dano"
        )

        self.critical_var = tk.StringVar(value="")
        self.critical_var.trace_add(
            "write",
            lambda *_: self.update_preview()
        )
        self.sync_critical_from_damage()

        ttk.Entry(
            critical_box,
            textvariable=self.critical_var
        ).pack(
            fill="x",
            pady=(8, 0)
        )

        # ----------------------------------------------
        # Tipo de dano
        # ----------------------------------------------
        type_box = self.create_toggle_section(
            parent,
            "Tipo de dano",
            expanded=True,
        )

        ttk.Entry(
            type_box,
            textvariable=self.damage_type_var
        ).pack(
            fill="x"
        )
    
        self.damage_type_var.trace_add(
            "write",
            lambda *_: self.update_preview()
        )
    
        # ----------------------------------------------
        # Descrição
        # ----------------------------------------------
        desc_box = self.create_toggle_section(
            parent,
            "Descrição",
            expand_on_open=True,
        )
    
        self.description_text = tk.Text(
            desc_box,
            height=6,
            wrap="word"
        )
        self.description_text.pack(
            fill="both",
            expand=True
        )
    
        self.description_text.bind(
            "<KeyRelease>",
            lambda e: self.update_preview()
        )
    
        desc_buttons = ttk.Frame(desc_box)
        desc_buttons.pack(
            fill="x",
            pady=(6, 0)
        )
    
        ttk.Button(
            desc_buttons,
            text="Adicionar texto",
            command=self.insert_description_text
        ).pack(
            side="left"
        )
    
        ttk.Button(
            desc_buttons,
            text="Adicionar botão",
            command=self.insert_button
        ).pack(
            side="left",
            padx=5
        )

    # ========================================================
    # Painel preview
    # ========================================================

    def get_roll_preview_data(self):
        attack_var = getattr(self, "attack_roll_var", None)
        attack_formula = attack_var.get().strip() if attack_var else ""
        threat_var = getattr(self, "attack_threat_var", None)
        threat_margin = threat_var.get() if threat_var else ""
        attack_attribute_var = getattr(self, "attack_attribute_var", None)
        attack_attribute = attack_attribute_var.get() if attack_attribute_var else ""
        attack = build_attack_expression(
            attack_formula,
            threat_margin,
            attack_attribute,
            self.get_attack_extra_values(),
        ) if attack_var else ""
        attack_choices = get_preview_question_choices(
            attack_formula,
            *self.get_attack_extra_values(),
        )

        damage_var = getattr(self, "damage_var", None)
        damage_formula = damage_var.get().strip() if damage_var else ""
        additional_var = getattr(self, "damage_additional_var", None)
        additional_formula = additional_var.get().strip() if additional_var else ""
        damage_formula = join_formula_parts(damage_formula, additional_formula)
        damage_attributes = [
            ATTRIBUTES[attribute]
            for attribute, variable in getattr(self, "damage_attribute_vars", {}).items()
            if variable.get()
        ]
        damage_extras = self.get_damage_extra_values()
        universal_conditions = self.get_attack_universal_conditions()
        damage_choices = get_preview_question_choices(
            damage_formula,
            *damage_extras,
            *self.get_attack_extra_values(),
        )
        damage_base_formula = build_damage_roll_formula(
            damage_formula,
            damage_attributes,
            universal_conditions,
        )

        critical_var = getattr(self, "critical_var", None)
        critical_formula = critical_var.get().strip() if critical_var else ""
        critical_universal_conditions = (
            universal_conditions if critical_formula else []
        )
        critical_extras = [
            simplify_condition_questions(value)
            for value in damage_extras
        ]
        critical_base_formula = build_damage_roll_formula(
            critical_formula,
            damage_attributes if critical_formula else [],
            critical_universal_conditions,
        )
        name_var = getattr(self, "attack_name_var", None)
        type_var = getattr(self, "damage_type_var", None)
        is_critical = self.roll_preview_critical_var.get()
        selected_damage_formula = (
            critical_base_formula if is_critical else damage_base_formula
        )
        selected_extras = critical_extras if is_critical else damage_extras
        damage_rolls = []
        if selected_damage_formula:
            damage_rolls.append(
                format_roll_preview(
                    selected_damage_formula,
                    choices=damage_choices,
                )
            )
        damage_rolls.extend(
            format_roll_preview(value, choices=damage_choices)
            for value in selected_extras
            if value
        )

        return {
            "character": "PERSONAGEM",
            "name": name_var.get().strip() if name_var else "Ataque",
            "attack": format_roll_preview(
                attack,
                force_d20=is_critical,
                choices=attack_choices,
            ),
            "damage_rolls": damage_rolls or ["—"],
            "critical": is_critical,
            "damage_type": type_var.get().strip() if type_var else "",
            "description": self.get_description(),
        }

    # ========================================================
    # Construção da macro
    # ========================================================

    def get_description(self):
        description_widget = getattr(self, "description_text", None)
        if description_widget is None:
            return ""
        return description_widget.get("1.0", "end-1c")

    def build_macro(self):
        name_var = getattr(self, "attack_name_var", None)
        name = name_var.get().strip() if name_var else "Ataque"
        if not name:
            name = "Ataque"

        attack_var = getattr(self, "attack_roll_var", None)
        attack_formula = attack_var.get().strip() if attack_var else ""
        threat_var = getattr(self, "attack_threat_var", None)
        threat_margin = threat_var.get() if threat_var else ""
        attack_attribute_var = getattr(self, "attack_attribute_var", None)
        attack_attribute = attack_attribute_var.get() if attack_attribute_var else ""
        attack = build_attack_expression(
            attack_formula,
            threat_margin,
            attack_attribute,
            self.get_attack_extra_values(),
        ) if attack_var else ""

        damage_var = getattr(self, "damage_var", None)
        damage_formula = damage_var.get().strip() if damage_var else ""
        additional_damage_var = getattr(self, "damage_additional_var", None)
        additional_damage_formula = (
            additional_damage_var.get().strip() if additional_damage_var else ""
        )
        damage_formula = join_formula_parts(
            damage_formula,
            additional_damage_formula,
        )
        extra_values = self.get_damage_extra_values()
        universal_conditions = self.get_attack_universal_conditions()
        damage_attribute_vars = getattr(self, "damage_attribute_vars", {})
        damage_attributes = [
            ATTRIBUTES[attribute]
            for attribute, variable in damage_attribute_vars.items()
            if variable.get()
        ]
        damage = build_damage_expression(
            damage_formula,
            extra_values,
            damage_attributes,
            universal_conditions,
        )

        critical_var = getattr(self, "critical_var", None)
        critical_formula = critical_var.get().strip() if critical_var else ""
        critical_universal_conditions = (
            universal_conditions if critical_formula else []
        )
        critical_extra_values = [
            simplify_condition_questions(value)
            for value in extra_values
        ]
        critical = build_critical_expression(
            critical_formula,
            critical_extra_values,
            damage_attributes if critical_formula else [],
            critical_universal_conditions,
        )

        damage_type_var = getattr(self, "damage_type_var", None)
        damage_type = damage_type_var.get().strip() if damage_type_var else ""

        description = self.get_description()

        character_display_var = getattr(self, "character_display_var", None)
        character_display = (
            character_display_var.get()
            if character_display_var is not None
            else ""
        )
        return render_generated_macro(
            name,
            attack,
            damage,
            critical,
            damage_type,
            description,
            character_display,
        )

    def update_duplicate_condition_warning(self):
        warning_var = getattr(
            self,
            "duplicate_condition_warning_var",
            None,
        )
        if warning_var is None:
            return

        fields = []
        if getattr(self, "attack_extra_enabled_var", None) and self.attack_extra_enabled_var.get():
            fields.extend(getattr(self, "attack_extra_vars", []))

        fields.extend(
            variable
            for variable in (
                getattr(self, "damage_var", None),
                getattr(self, "damage_additional_var", None),
            )
            if variable is not None
        )

        if getattr(self, "damage_extra_enabled_var", None) and self.damage_extra_enabled_var.get():
            fields.extend(getattr(self, "damage_extra_vars", []))

        seen_names = set()
        duplicate_found = False
        for variable in fields:
            for name in extract_roll20_question_names(variable.get()):
                if name in seen_names:
                    duplicate_found = True
                    break
                seen_names.add(name)
            if duplicate_found:
                break

        warning_var.set(
            "Aviso: condicionais com a mesma nomenclatura identificadas. "
            "Tome cuidado, pois apenas o valor da primeira será adicionado "
            "a rolagem pelo padrão de prioridade do Roll20"
            if duplicate_found
            else ""
        )

    def update_preview(self):
        if not hasattr(self, "preview") or getattr(self, "_preview_job", None):
            return
        self._preview_job = self.root.after_idle(self._refresh_preview)

    def _refresh_preview(self):
        self._preview_job = None
        self.update_duplicate_condition_warning()
        macro = self.build_macro()

        self.preview.delete("1.0", "end")
        self.preview.insert("1.0", macro)
        self.draw_roll_preview()

    # ========================================================
    # Inserções
    # ========================================================

    def insert_text(self, text):
        # Insere no campo que estiver com foco.
        widget = self.root.focus_get()

        if isinstance(widget, (tk.Entry, ttk.Entry)) and str(widget.cget("state")) not in ("readonly", "disabled"):
            widget.insert(tk.INSERT, text)
            widget.event_generate("<KeyRelease>")
        elif isinstance(widget, tk.Text):
            widget.insert(tk.INSERT, text)
            self.update_preview()
        else:
            # Se nenhum campo estiver focado, adiciona na descrição.
            self.description_text.insert(tk.INSERT, text)
            self.update_preview()

    def add_to_entry(self, entry, variable, text):
        current = variable.get()

        if current and not current.endswith(("+", "-", "*", "/")):
            current += "+"

        variable.set(current + text)
        entry.focus_set()
        self.update_preview()

    def open_common_weapons_dialog(self):
        win = tk.Toplevel(self.root)
        win.title("Armas comuns")
        set_responsive_window_geometry(win, 320, 300, 280, 220)
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Escolha uma arma:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 8))

        weapon_buttons_frame = self.create_scrollable_panel(
            win,
            padx=15,
            pady=(0, 12),
        )
        for weapon_name in COMMON_WEAPONS:
            ttk.Button(
                weapon_buttons_frame,
                text=weapon_name,
                command=lambda name=weapon_name: self.apply_common_weapon(
                    name,
                    win,
                ),
            ).pack(fill="x", pady=3)

    def apply_common_weapon(self, weapon_name, window):
        weapon = COMMON_WEAPONS[weapon_name]

        self.attack_name_var.set(weapon_name)
        self.attack_best_die_var.set("nao")
        self.attack_roll_var.set("1d20")
        self.attack_threat_var.set(weapon["threat"])
        self.attack_attribute_var.set(weapon["skill"])
        self.damage_var.set(weapon["damage"])
        self.damage_additional_var.set("")
        self.critical_repeat_var.set(weapon["critical_multiplier"])
        self.damage_type_var.set(weapon["damage_type"])

        for attribute, variable in self.damage_attribute_vars.items():
            variable.set(attribute in weapon["attributes"])

        self.attack_extra_enabled_var.set(False)
        self.toggle_attack_extra_field()
        for variable in self.attack_extra_vars:
            variable.set("")

        self.damage_extra_enabled_var.set(False)
        self.toggle_damage_extra_field()
        for variable in self.damage_extra_vars:
            variable.set("")

        self.damage_exotic_enabled_var.set(False)
        self.toggle_exotic_dice_field()
        self.sync_critical_from_damage()
        self.update_preview()
        window.destroy()

    def insert_fixed_bonus(self):
        win = tk.Toplevel(self.root)
        win.title("Calculador de Passos de Dano")
        set_responsive_window_geometry(win, 760, 400, 480, 300)
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Escolha um dado:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=18, pady=(14, 4))

        dice_frame = ttk.Frame(win)
        dice_frame.pack(fill="x", padx=18)
        die_var = tk.StringVar(value="1d6")
        die_choice_buttons = []

        for index, (label, value) in enumerate(get_damage_step_options()):
            button = ttk.Button(
                dice_frame,
                text=label,
                style="DamageDie.TButton",
                command=lambda die=value: select_die(die),
            )
            button.grid(
                row=index // 7,
                column=index % 7,
                sticky="ew",
                padx=3,
                pady=3,
            )
            die_choice_buttons.append((button, value))

        self.make_responsive_grid(
            dice_frame,
            [button for button, _value in die_choice_buttons],
            minimum_cell_width=78,
            maximum_columns=7,
        )

        controls = ttk.Frame(win)
        controls.pack(fill="x", expand=True, padx=18, pady=(16, 14))

        previous_button = ttk.Button(controls, text="Regredir passo")
        previous_button.pack(side="left", expand=True, fill="x")

        current_frame = ttk.Frame(controls)
        current_frame.pack(side="left", padx=12)
        track_var = tk.StringVar(value=get_damage_step_track(die_var.get())[0])
        start_die_var = tk.StringVar(value=die_var.get())
        change_label = ttk.Label(
            current_frame,
            text="Passos: 0 | Sem alteração",
            anchor="center",
        )
        change_label.pack(fill="x", pady=(0, 4))

        current_die = ttk.Button(
            current_frame,
            textvariable=die_var,
            style="DamageStep.TButton",
            state="disabled",
        )
        current_die.pack()

        next_button = ttk.Button(controls, text="Aumentar passo")
        next_button.pack(side="left", expand=True, fill="x")

        def update_navigation(*_):
            steps = DAMAGE_STEP_TRACKS[track_var.get()]
            current_index = steps.index(die_var.get())
            previous_button.configure(
                state="normal" if current_index > 0 else "disabled"
            )
            next_button.configure(
                state="normal" if current_index < len(steps) - 1 else "disabled"
            )
            for button, value in die_choice_buttons:
                button.configure(
                    state="disabled" if value == die_var.get() else "normal"
                )
            step_delta, total_delta = get_damage_step_delta(
                start_die_var.get(),
                die_var.get(),
                steps,
            )
            if step_delta > 0:
                summary = f"Passos: +{step_delta} | Aumento máximo: +{total_delta}"
            elif step_delta < 0:
                summary = f"Passos: {step_delta} | Redução máxima: {total_delta}"
            else:
                summary = "Passos: 0 | Sem alteração"
            change_label.configure(text=summary)

        def change_step(offset):
            steps = DAMAGE_STEP_TRACKS[track_var.get()]
            current_index = steps.index(die_var.get())
            new_index = current_index + offset
            if 0 <= new_index < len(steps):
                die_var.set(steps[new_index])
            update_navigation()

        def select_die(die):
            die_var.set(die)
            start_die_var.set(die)
            track_var.set(get_damage_step_track(die)[0])
            update_navigation()

        previous_button.configure(command=lambda: change_step(-1))
        next_button.configure(command=lambda: change_step(1))
        update_navigation()

    def insert_damage_conditional(self, index):
        self.insert_question(
            target_var=self.damage_extra_vars[index],
            conditional=True,
            wrap_advanced_values=True,
        )

    def insert_damage_field_conditional(self, target_var):
        self.insert_question(
            target_var=target_var,
            conditional=True,
            wrap_conditional_values=False,
        )

    def insert_attack_conditional(self, index):
        self.insert_question(
            target_var=self.attack_extra_vars[index],
            conditional=True,
            allow_pride=True,
            universal_flags=self.attack_extra_universal_flags[index],
            on_universal_flags=lambda flags: self.set_attack_universal_flags(
                index,
                flags,
            ),
        )

    def insert_condition_components(
        self,
        target_var,
        wrap_conditional_values,
        wrap_advanced_values,
        allow_pride=False,
        universal_flags=None,
        on_universal_flags=None,
    ):
        source = target_var.get().strip() if target_var is not None else ""
        source, recovered_syntax = close_advanced_questions_before_outer_pipe(
            source
        )
        components = []
        syntax_error = False

        for component_text in split_roll20_components(source):
            result_modifier = parse_result_modified_condition(component_text)
            effect_value = ""
            effect_mode = "multiplicativo"
            if result_modifier is not None:
                component_text, effect_value, effect_mode = result_modifier

            if not looks_like_roll20_condition(component_text):
                components.append({"type": "fixed", "value": component_text})
                continue

            parsed = parse_roll20_question(component_text)
            if parsed is None:
                syntax_error = True
                break

            name, options, was_repaired = parsed
            recovered_syntax = recovered_syntax or was_repaired
            loaded_options = []
            for option in options:
                advanced_data = None
                if looks_like_roll20_condition(option.value):
                    nested = parse_roll20_question(option.value)
                    if nested is None:
                        syntax_error = True
                        break
                    nested_name, nested_options, nested_repaired = nested
                    recovered_syntax = recovered_syntax or nested_repaired
                    advanced_data = (
                        unescape(nested_name),
                        [
                            QuestionOption(
                                unescape(nested_option.label),
                                unescape(nested_option.value),
                            )
                            for nested_option in nested_options
                        ],
                    )
                loaded_options.append((option, advanced_data))

            if syntax_error:
                break
            condition_index = sum(
                item["type"] == "condition"
                for item in components
            )
            components.append({
                "type": "condition",
                "name": name,
                "options": loaded_options,
                "effect_value": effect_value,
                "effect_mode": effect_mode,
                "universal": (
                    universal_flags[condition_index]
                    if universal_flags
                    and condition_index < len(universal_flags)
                    else False
                ),
            })

        if syntax_error:
            components = []
            status_text = (
                "Erro de sintaxe da condicional anterior, impossível "
                "exibir valores originais"
            )
        elif recovered_syntax:
            status_text = (
                "Sintaxe anterior parcialmente errada, valores corrigidos "
                "para valores possíveis"
            )
        else:
            status_text = ""

        has_condition = any(
            component["type"] == "condition"
            for component in components
        )
        if not has_condition:
            fixed_components = [
                component
                for component in components
                if component["type"] == "fixed"
            ]
            components = [{
                "type": "condition",
                "name": "Condição",
                "options": None,
                "effect_value": "",
                "effect_mode": "multiplicativo",
                "universal": False,
            }]
            components.extend(fixed_components)

        win = tk.Toplevel(self.root)
        win.title("Condição")
        set_responsive_window_geometry(win, 760, 620, 520, 400)
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Condicionais e valores adicionais:",
            style="Section.TLabel",
        ).pack(anchor="w", padx=15, pady=(15, 4))

        if allow_pride:
            ttk.Button(
                win,
                text="👑 Orgulho",
                style="Pride.TButton",
                command=lambda: insert_pride_effect(),
            ).pack(anchor="w", padx=15, pady=(0, 6))

        if status_text:
            ttk.Label(
                win,
                text=status_text,
                foreground="#8a5a00" if recovered_syntax and not syntax_error else "#b3261e",
                wraplength=720,
            ).pack(anchor="w", padx=15, pady=(0, 6))

        scroll_frame = ttk.Frame(win)
        scroll_frame.pack(fill="both", expand=True, padx=15)
        canvas = tk.Canvas(scroll_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            scroll_frame,
            orient="vertical",
            command=canvas.yview,
        )
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        component_frame = ttk.Frame(canvas)
        canvas_window = canvas.create_window(
            (0, 0),
            window=component_frame,
            anchor="nw",
        )
        condition_frame = ttk.Frame(component_frame)
        condition_frame.pack(fill="x")
        fixed_section = ttk.Frame(component_frame, padding=(8, 5))
        fixed_section.pack(fill="x", pady=(4, 0))
        ttk.Label(
            fixed_section,
            text="Valores/dados fora das condicionais:",
        ).pack(anchor="w")
        fixed_fields_frame = ttk.Frame(fixed_section)
        fixed_fields_frame.pack(fill="x", pady=(2, 0))

        def update_condition_scroll_region(_event=None):
            update_canvas_scroll_region(canvas, scrollbar)

        component_frame.bind(
            "<Configure>",
            update_condition_scroll_region,
        )
        canvas.bind(
            "<Configure>",
            lambda event: (
                canvas.itemconfigure(canvas_window, width=event.width),
                canvas.after_idle(update_condition_scroll_region),
            ),
        )

        editor_components = []

        def update_condition_component_titles():
            condition_number = 0
            for component in editor_components:
                if component["type"] != "condition":
                    continue
                condition_number += 1
                prefix = (
                    "+"
                    if component["header_button"].cget("text").startswith("+")
                    else "-"
                )
                component["header_button"].configure(
                    text=f"{prefix} Condição {condition_number}"
                )

        def remove_condition_component(component):
            component["frame"].destroy()
            editor_components.remove(component)
            update_condition_component_titles()

        def add_condition_component(initial=None):
            universal_var = tk.BooleanVar(
                value=initial.get("universal", False) if initial else False
            )
            content = self.create_toggle_section(
                condition_frame,
                "Condição",
                expanded=True,
                pady=(0, 5),
                header_action_variable=(
                    universal_var if allow_pride else None
                ),
            )
            section = content.master
            header_button = next(
                header_child
                for child in section.winfo_children()
                for header_child in child.winfo_children()
                if isinstance(header_child, ttk.Button)
            ) if allow_pride else next(
                child
                for child in section.winfo_children()
                if isinstance(child, ttk.Button)
            )
            initial_options = initial["options"] if initial else None
            name_var = tk.StringVar(
                value=initial["name"] if initial else "Condição"
            )
            ttk.Label(content, text="Nome da condição:").pack(anchor="w")
            ttk.Entry(content, textvariable=name_var).pack(
                fill="x",
                pady=(2, 6),
            )
            ttk.Label(content, text="Opções (nome = valor):").pack(anchor="w")
            options_frame = ttk.Frame(content)
            options_frame.pack(fill="x", pady=(2, 2))
            rows = []
            effect_value_var = tk.StringVar(
                value=initial.get("effect_value", "") if initial else ""
            )
            effect_mode_var = tk.StringVar(
                value=(
                    initial.get("effect_mode", "multiplicativo")
                    if initial
                    else "multiplicativo"
                )
            )

            component = {
                "type": "condition",
                "name": name_var,
                "rows": rows,
                "frame": section,
                "header_button": header_button,
                "effect_value": effect_value_var,
                "effect_mode": effect_mode_var,
                "universal": universal_var,
            }
            editor_components.append(component)
            ttk.Button(
                content,
                text="×",
                width=2,
                command=lambda: remove_condition_component(component),
            ).pack(anchor="e", before=next(iter(content.winfo_children())))

            effect_frame = ttk.LabelFrame(
                content,
                text="Condicional com alterador de resultado",
                padding=8,
            )
            effect_frame.pack(fill="x", pady=(8, 0))
            ttk.Label(effect_frame, text="Valor:").pack(side="left")
            ttk.Entry(
                effect_frame,
                textvariable=effect_value_var,
                width=16,
            ).pack(side="left", padx=(5, 10))
            ttk.Radiobutton(
                effect_frame,
                text="Multiplicativo",
                variable=effect_mode_var,
                value="multiplicativo",
            ).pack(side="left", padx=(0, 8))
            ttk.Radiobutton(
                effect_frame,
                text="Aditivo",
                variable=effect_mode_var,
                value="aditivo",
            ).pack(side="left")

            modifier_tooltip = [None]
            info_button = ttk.Label(
                effect_frame,
                text="ⓘ",
                cursor="question_arrow",
                foreground="#286090",
            )
            info_button.pack(side="right", padx=(8, 0))
            tooltip_text = (
                "Valor multiplicativo irá multiplicar a quantidade "
                "adicionada, pelo valor adicionado, seja em dados, ou valor "
                "fixo. Valor Aditivo é recomendado para modularidade de "
                'Dados, onde é dado um dado "d6" e esse dado será rolado '
                "quantas vezes forem investidos ao usar a macro."
            )

            def show_modifier_tooltip(_event):
                if modifier_tooltip[0] is not None:
                    return
                tooltip = tk.Toplevel(win)
                tooltip.wm_overrideredirect(True)
                tooltip.wm_geometry(
                    f"+{info_button.winfo_rootx()}+"
                    f"{info_button.winfo_rooty() + info_button.winfo_height()}"
                )
                tk.Label(
                    tooltip,
                    text=tooltip_text,
                    justify="left",
                    wraplength=380,
                    background="#fff8dc",
                    foreground="#333333",
                    relief="solid",
                    borderwidth=1,
                    padx=8,
                    pady=6,
                ).pack()
                modifier_tooltip[0] = tooltip

            def hide_modifier_tooltip(_event):
                if modifier_tooltip[0] is not None:
                    modifier_tooltip[0].destroy()
                    modifier_tooltip[0] = None

            info_button.bind("<Enter>", show_modifier_tooltip)
            info_button.bind("<Leave>", hide_modifier_tooltip)
            self.add_result_modifier_warning(effect_frame, effect_value_var)
            def remove_row(row_data):
                rows.remove(row_data)
                row_data["container"].destroy()

            def add_row(label="", value="", advanced_data=None):
                row_container = ttk.Frame(options_frame)
                row_container.pack(fill="x", pady=2)
                row = ttk.Frame(row_container)
                row.pack(fill="x")
                option_number = len(rows) + 1
                normal_value = (
                    f"Valor {option_number}"
                    if advanced_data is not None
                    else value
                )
                label_var = tk.StringVar(value=label)
                value_var = tk.StringVar(value=normal_value)
                normal_value_var = tk.StringVar(value=normal_value)
                advanced_var = tk.BooleanVar(value=False)
                advanced_name_var = tk.StringVar(value="Segunda condição")
                ttk.Entry(
                    row,
                    textvariable=label_var,
                    width=22,
                ).pack(side="left", fill="x", expand=True)
                value_entry = ttk.Entry(
                    row,
                    textvariable=value_var,
                    width=18,
                )
                value_entry.pack(side="left", padx=(5, 0))
                advanced_name_entry = ttk.Entry(
                    row,
                    textvariable=advanced_name_var,
                    width=18,
                )
                nested_frame = ttk.Frame(row_container)
                nested_options = []
                nested_rows = []
                nested_add_button = ttk.Button(
                    nested_frame,
                    text="+ Campo",
                    command=lambda: add_nested_option(),
                )

                def remove_nested_option(nested_option):
                    nested_options.remove(nested_option["variables"])
                    nested_rows.remove(nested_option)
                    nested_option["frame"].destroy()

                def add_nested_option():
                    nested_row = ttk.Frame(nested_frame)
                    nested_row.pack(
                        fill="x",
                        pady=(2, 0),
                        before=nested_add_button,
                    )
                    option_number = len(nested_options) + 1
                    nested_label_var = tk.StringVar(
                        value=f"Nome {option_number}"
                    )
                    nested_value_var = tk.StringVar(
                        value=f"Valor {option_number}"
                    )
                    nested_option = {
                        "frame": nested_row,
                        "variables": (nested_label_var, nested_value_var),
                    }
                    ttk.Button(
                        nested_row,
                        text="×",
                        width=2,
                        command=lambda: remove_nested_option(nested_option),
                    ).pack(side="left", padx=(0, 4))
                    ttk.Entry(
                        nested_row,
                        textvariable=nested_label_var,
                        width=15,
                    ).pack(side="left")
                    ttk.Entry(
                        nested_row,
                        textvariable=nested_value_var,
                        width=15,
                    ).pack(side="left", padx=(5, 0))
                    nested_options.append(nested_option["variables"])
                    nested_rows.append(nested_option)

                nested_add_button.pack(anchor="w", pady=(2, 0))
                add_nested_option()
                advanced_check = ttk.Checkbutton(
                    row,
                    text="Condicional avançada",
                    variable=advanced_var,
                    command=lambda: toggle_advanced(),
                )
                advanced_check.pack(side="left", padx=(8, 0))

                def toggle_advanced():
                    if advanced_var.get():
                        normal_value_var.set(value_var.get())
                        value_entry.pack_forget()
                        advanced_name_entry.pack(
                            side="left",
                            padx=(5, 0),
                            before=advanced_check,
                        )
                        nested_frame.pack(
                            fill="x",
                            padx=(24, 0),
                            pady=(2, 4),
                        )
                    else:
                        advanced_name_entry.pack_forget()
                        value_var.set(
                            normal_value_var.get()
                            or f"Valor {option_number}"
                        )
                        value_entry.pack(
                            side="left",
                            padx=(5, 0),
                            before=advanced_check,
                        )
                        nested_frame.pack_forget()

                row_data = {
                    "label": label_var,
                    "value": value_var,
                    "advanced": advanced_var,
                    "advanced_name": advanced_name_var,
                    "nested_options": nested_options,
                    "container": row_container,
                }
                rows.append(row_data)
                ttk.Button(
                    row,
                    text="×",
                    width=2,
                    command=lambda: remove_row(row_data),
                ).pack(side="left", before=next(iter(row.winfo_children())))
                if advanced_data:
                    advanced_name, advanced_options = advanced_data
                    advanced_var.set(True)
                    advanced_name_var.set(advanced_name)
                    if not advanced_options:
                        nested_options[0][0].set("")
                        nested_options[0][1].set("")
                    for index, nested_option in enumerate(advanced_options):
                        if index:
                            add_nested_option()
                        nested_options[index][0].set(nested_option.label)
                        nested_options[index][1].set(nested_option.value)
                    toggle_advanced()

            if initial_options is None:
                add_row("SIM", "1")
                add_row("NÃO", "0")
            else:
                for option, advanced_data in initial_options:
                    add_row(option.label, option.value, advanced_data)

            ttk.Button(
                content,
                text="+ Adicionar opção",
                command=add_row,
            ).pack(anchor="w", pady=(3, 0))
            update_condition_component_titles()
            return component

        def add_fixed_component(value=""):
            fixed_frame = ttk.Frame(fixed_fields_frame)
            fixed_frame.pack(side="left", padx=(0, 6), pady=(0, 3))
            value_var = tk.StringVar(value=value)
            component = {
                "type": "fixed",
                "value": value_var,
            }
            ttk.Entry(
                fixed_frame,
                textvariable=value_var,
                width=14,
            ).pack(
                fill="x",
            )
            ttk.Button(
                fixed_frame,
                text="X",
                width=2,
                command=lambda: remove_fixed_component(
                    fixed_frame,
                    component,
                ),
            ).pack(side="right", padx=(3, 0))
            editor_components.append(component)

        def remove_fixed_component(frame, component):
            frame.destroy()
            if component in editor_components:
                editor_components.remove(component)

        for component in components:
            if component["type"] == "fixed":
                add_fixed_component(component["value"])
            else:
                add_condition_component(component)

        action_frame = ttk.Frame(win)
        action_frame.pack(fill="x", padx=15, pady=(6, 0))
        ttk.Button(
            action_frame,
            text="+ Adicionar valor fixo/dado",
            command=add_fixed_component,
        ).pack(side="left")
        ttk.Button(
            action_frame,
            text="+ Adicionar outra condicional",
            command=add_condition_component,
        ).pack(side="left", padx=(6, 0))

        def insert():
            conditional_components = []
            fixed_components = []
            for component in editor_components:
                if component["type"] == "fixed":
                    value = component["value"].get().strip()
                    if value:
                        fixed_components.append(value)
                    continue

                name = component["name"].get().strip()
                if not name:
                    messagebox.showwarning(
                        "Condição",
                        "Digite um nome para a condição.",
                        parent=win,
                    )
                    return

                options = []
                for row in component["rows"]:
                    label = row["label"].get().strip()
                    value = row["value"].get().strip()
                    if row["advanced"].get():
                        advanced_name = row["advanced_name"].get().strip()
                        if not advanced_name:
                            messagebox.showwarning(
                                "Condição",
                                "Digite um nome para a condição avançada.",
                                parent=win,
                            )
                            return
                        advanced_options = [
                            QuestionOption(
                                nested_label.get().strip(),
                                nested_value.get().strip(),
                            )
                            for nested_label, nested_value
                            in row["nested_options"]
                        ]
                        value = build_advanced_question_value(
                            advanced_name,
                            advanced_options,
                        )
                    options.append(
                        QuestionOption(
                            label,
                            value,
                            wrap_value=(
                                wrap_advanced_values
                                if row["advanced"].get()
                                else None
                            ),
                        )
                    )

                conditional_components.append(
                    build_modified_condition_question(
                        name,
                        options,
                        component["effect_value"].get().strip(),
                        component["effect_mode"].get(),
                        wrap_values=wrap_conditional_values,
                    )
                )

            if target_var is not None:
                target_var.set(
                    "+".join(conditional_components + fixed_components)
                )
                if on_universal_flags is not None:
                    on_universal_flags([
                        component["universal"].get()
                        for component in editor_components
                        if component["type"] == "condition"
                    ])
                self.update_preview()
            win.destroy()

        ttk.Button(
            win,
            text="Inserir condição",
            command=insert,
        ).pack(pady=(6, 12))

        def insert_pride_effect():
            if target_var is not None:
                target_var.set(ATTACK_PRIDE_EFFECT)
                if on_universal_flags is not None:
                    on_universal_flags([])
                self.update_preview()
            win.destroy()

    def insert_question(
        self,
        target_var=None,
        conditional=False,
        wrap_conditional_values=True,
        wrap_advanced_values=False,
        allow_pride=False,
        universal_flags=None,
        on_universal_flags=None,
    ):
        if conditional:
            self.insert_condition_components(
                target_var,
                wrap_conditional_values,
                wrap_advanced_values,
                allow_pride=allow_pride,
                universal_flags=universal_flags,
                on_universal_flags=on_universal_flags,
            )
            return

        win = tk.Toplevel(self.root)
        win.title("Condição" if conditional else "Pergunta Roll20")
        set_responsive_window_geometry(
            win,
            700 if conditional else 650,
            540 if conditional else 460,
            500,
            340,
        )
        win.transient(self.root)
        win.grab_set()

        previous_question = (
            target_var.get().strip()
            if conditional and target_var is not None
            else ""
        )
        previous_is_condition = looks_like_roll20_condition(previous_question)
        parsed_question = (
            parse_roll20_question(previous_question)
            if previous_is_condition
            else None
        )
        loaded_options = None
        recovered_syntax = False
        status_message = ""
        if previous_is_condition and parsed_question is None:
            status_message = (
                "Erro de sintaxe da condicional anterior, "
                "impossível exibir valores originais"
            )
        elif parsed_question:
            parsed_name, parsed_options, recovered_syntax = parsed_question
            loaded_options = []
            for option in parsed_options:
                advanced_data = None
                nested_question = parse_roll20_question(option.value)
                if looks_like_roll20_condition(option.value):
                    if nested_question is None:
                        status_message = (
                            "Erro de sintaxe da condicional anterior, "
                            "impossível exibir valores originais"
                        )
                        loaded_options = None
                        break
                    nested_name, nested_options, nested_recovered = nested_question
                    recovered_syntax = recovered_syntax or nested_recovered
                    advanced_data = (
                        unescape(nested_name),
                        [
                            QuestionOption(
                                unescape(nested.label),
                                unescape(nested.value),
                            )
                            for nested in nested_options
                        ],
                    )
                loaded_options.append((option, advanced_data))

            if loaded_options is not None:
                name_var = tk.StringVar(value=parsed_name)
                if recovered_syntax:
                    status_message = (
                        "Sintaxe anterior parcialmente errada, valores "
                        "corrigidos para valores possíveis"
                    )
        if status_message and loaded_options is None:
            name_var = tk.StringVar(value="Condição")
        elif not parsed_question:
            name_var = tk.StringVar(
                value="Condição" if conditional else "Pergunta"
            )

        ttk.Label(
            win,
            text="Nome da condição:" if conditional else "Nome da pergunta:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 4))

        if status_message:
            ttk.Label(
                win,
                text=status_message,
                foreground=(
                    "#8a5a00"
                    if loaded_options is not None
                    else "#b3261e"
                ),
                wraplength=660,
            ).pack(anchor="w", padx=15, pady=(0, 6))

        ttk.Entry(
            win,
            textvariable=name_var
        ).pack(fill="x", padx=15)

        ttk.Label(
            win,
            text="Opções (nome = valor):",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(12, 4))

        options_frame = self.create_scrollable_panel(win, padx=15)

        rows = []

        def add_row(label="", value="", advanced_data=None):
            row_container = ttk.Frame(options_frame)
            row_container.pack(fill="x", pady=2)

            row = ttk.Frame(row_container)
            row.pack(fill="x")

            option_number = len(rows) + 1
            normal_value = (
                f"Valor {option_number}"
                if advanced_data is not None
                else value
            )
            label_var = tk.StringVar(value=label)
            value_var = tk.StringVar(value=normal_value)
            normal_value_var = tk.StringVar(value=normal_value)
            advanced_var = tk.BooleanVar(value=False)
            advanced_name_var = tk.StringVar(value="Segunda condição")

            remove_button = ttk.Button(
                row,
                text="×",
                width=2,
                command=lambda: remove_row(row_data),
            )
            remove_button.pack(side="left", padx=(0, 4))

            ttk.Entry(
                row,
                textvariable=label_var,
                width=22
            ).pack(side="left", fill="x", expand=True)

            value_entry = ttk.Entry(
                row,
                textvariable=value_var,
                width=18
            )
            value_entry.pack(side="left", padx=(5, 0))

            advanced_name_entry = ttk.Entry(
                row,
                textvariable=advanced_name_var,
                width=18,
            )

            nested_frame = ttk.Frame(row_container)
            nested_options = []

            def remove_nested_option(nested_option):
                nested_options.remove(nested_option)
                nested_option["frame"].destroy()

            def add_nested_option():
                nested_row = ttk.Frame(nested_frame)
                nested_row.pack(
                    fill="x",
                    pady=(2, 0),
                    before=nested_add_button,
                )

                option_number = len(nested_options) + 1
                nested_label_var = tk.StringVar(
                    value=f"Nome {option_number}"
                )
                nested_value_var = tk.StringVar(
                    value=f"Valor {option_number}"
                )
                nested_option = {
                    "frame": nested_row,
                    "label": nested_label_var,
                    "value": nested_value_var,
                }
                ttk.Button(
                    nested_row,
                    text="×",
                    width=2,
                    command=lambda: remove_nested_option(nested_option),
                ).pack(side="left", padx=(0, 4))
                ttk.Entry(
                    nested_row,
                    textvariable=nested_label_var,
                    width=15,
                ).pack(side="left")
                ttk.Entry(
                    nested_row,
                    textvariable=nested_value_var,
                    width=15,
                ).pack(side="left", padx=(5, 0))

                nested_options.append(nested_option)

            nested_add_button = ttk.Button(
                nested_frame,
                text="+ Campo",
                command=add_nested_option,
            )
            nested_add_button.pack(anchor="w", pady=(2, 0))
            add_nested_option()

            advanced_check = ttk.Checkbutton(
                row,
                text="Condicional avançada",
                variable=advanced_var,
                command=lambda: toggle_advanced(),
            )
            advanced_check.pack(side="left", padx=(8, 0))

            def toggle_advanced():
                if advanced_var.get():
                    normal_value_var.set(value_var.get())
                    value_entry.pack_forget()
                    advanced_name_entry.pack(
                        side="left",
                        padx=(5, 0),
                        before=advanced_check,
                    )
                    nested_frame.pack(
                        fill="x",
                        padx=(24, 0),
                        pady=(2, 4),
                    )
                else:
                    advanced_name_entry.pack_forget()
                    value_var.set(
                        normal_value_var.get()
                        or f"Valor {option_number}"
                    )
                    value_entry.pack(
                        side="left",
                        padx=(5, 0),
                        before=advanced_check,
                    )
                    nested_frame.pack_forget()

            row_data = {
                "label": label_var,
                "value": value_var,
                "advanced": advanced_var,
                "advanced_name": advanced_name_var,
                "nested_options": nested_options,
                "container": row_container,
            }
            rows.append(row_data)

            if advanced_data is not None:
                advanced_name, options = advanced_data
                advanced_var.set(True)
                advanced_name_var.set(advanced_name)
                if not options:
                    nested_options[0]["label"].set("")
                    nested_options[0]["value"].set("")
                for index, nested_option in enumerate(options):
                    if index:
                        add_nested_option()
                    nested_options[index]["label"].set(nested_option.label)
                    nested_options[index]["value"].set(nested_option.value)
                toggle_advanced()

            return row_data

        def remove_row(row_data):
            rows.remove(row_data)
            row_data["container"].destroy()

        if loaded_options is None:
            add_row("SIM", "1")
            add_row("NÃO", "0")
        else:
            for option, advanced_data in loaded_options:
                add_row(option.label, option.value, advanced_data)

        ttk.Button(
            win,
            text="+ Adicionar opção",
            command=add_row
        ).pack(pady=5)

        def insert():
            name = name_var.get().strip()
            options = []

            for row in rows:
                label = row["label"].get().strip()

                if label:
                    value = row["value"].get().strip()
                    if row["advanced"].get():
                        advanced_name = row["advanced_name"].get().strip()
                        if not advanced_name:
                            messagebox.showwarning(
                                "Pergunta Roll20",
                                "Digite um nome para a condição avançada.",
                                parent=win,
                            )
                            return

                        advanced_options = [
                            QuestionOption(
                                nested_option["label"].get().strip(),
                                nested_option["value"].get().strip(),
                            )
                            for nested_option in row["nested_options"]
                            if nested_option["label"].get().strip()
                        ]
                        value = build_advanced_question_value(
                            advanced_name,
                            advanced_options,
                        )

                    options.append(
                        QuestionOption(
                            label,
                            value,
                            wrap_value=(
                                wrap_advanced_values
                                if row["advanced"].get()
                                else None
                            ),
                        )
                    )

            if not name:
                messagebox.showwarning(
                    "Condição" if conditional else "Pergunta",
                    "Digite um nome para a condição." if conditional else "Digite um nome para a pergunta.",
                    parent=win
                )
                return

            if conditional:
                question_code = build_condition_question(
                    name,
                    options,
                    wrap_values=wrap_conditional_values,
                )
            else:
                question_code = MacroQuestion(name, options).build()

            if target_var is not None:
                target_var.set(question_code)
                self.update_preview()
            else:
                self.insert_text(question_code)
            win.destroy()

        ttk.Button(
            win,
            text="Inserir pergunta",
            command=insert
        ).pack(pady=(5, 15))

    def insert_button(self):
        win = tk.Toplevel(self.root)
        win.title("Botão de macro")
        set_responsive_window_geometry(win, 500, 240, 380, 200)
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Texto exibido:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 4))

        text_var = tk.StringVar(value="Botão para chamar outra macro")
        ttk.Entry(
            win,
            textvariable=text_var
        ).pack(fill="x", padx=15)

        ttk.Label(
            win,
            text="Ação do botão:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(12, 4))

        action_var = tk.StringVar(
            value="~@{character_name}|Nome da habilidade/macro"
        )
        ttk.Entry(
            win,
            textvariable=action_var
        ).pack(fill="x", padx=15)

        def insert():
            text = text_var.get().strip()
            action = action_var.get().strip()

            if not text or not action:
                messagebox.showwarning(
                    "Botão",
                    "Preencha o texto e a ação.",
                    parent=win
                )
                return

            button = MacroButton(text, action)
            self.insert_text(button.build())
            win.destroy()

        ttk.Button(
            win,
            text="Inserir botão",
            command=insert
        ).pack(pady=15)

    def load_custom_macro(self, macro_text: str):
        state = parse_generated_macro_state(macro_text)
        if state is None:
            return False

        self.attack_name_var.set(state["attack_name"])
        self.character_display_var.set(state["character_display"])
        self.attack_roll_var.set(state["attack_roll"])
        self.attack_best_die_var.set(
            "sim"
            if "2d20kh1" in state["attack_roll"]
            else "nao"
        )
        self.attack_threat_var.set(state["attack_threat"])
        self.attack_attribute_var.set(state["attack_skill"])
        for index, variable in enumerate(self.attack_extra_vars):
            variable.set(
                state["attack_extras"][index]
                if index < len(state["attack_extras"])
                else ""
            )
        self.attack_extra_enabled_var.set(bool(state["attack_extras"]))
        self.toggle_attack_extra_field()

        self.damage_var.set(state["damage"])
        self.damage_additional_var.set(state["damage_additional"])
        for variable in self.damage_attribute_vars.values():
            variable.set(False)
        for index, variable in enumerate(self.damage_extra_vars):
            variable.set(
                state["damage_extras"][index]
                if index < len(state["damage_extras"])
                else ""
            )
        self.damage_extra_enabled_var.set(bool(state["damage_extras"]))
        self.toggle_damage_extra_field()

        self.critical_repeat_var.set("1")
        self.critical_var.set(state["critical"])
        self.damage_type_var.set(state["damage_type"])
        self.description_text.delete("1.0", "end")
        self.description_text.insert("1.0", state["description"])
        self.update_preview()
        return True

    def insert_custom(self):
        win = tk.Toplevel(self.root)
        win.title("Importe sua Macro")
        set_responsive_window_geometry(win, 720, 370, 520, 280)
        win.transient(self.root)
        win.grab_set()

        warning = tk.Frame(
            win,
            background="#fff3cd",
            highlightbackground="#d69e00",
            highlightthickness=1,
            padx=8,
            pady=6,
        )
        warning.pack(fill="x", padx=15, pady=(14, 10))
        warning_message = (
            "Ainda em fase de teste. funciona melhor com codigos do "
            "porprio programa, mas é possivel importar ataques mais "
            "basicos e com um pouco de sorte alguns mais complexos"
        )
        tk.Label(
            warning,
            text="⚠",
            font=("Segoe UI Symbol", 14, "bold"),
            foreground="#8a5a00",
            background="#fff3cd",
        ).pack(side="left", padx=(0, 8))
        tk.Label(
            warning,
            text=warning_message,
            justify="left",
            anchor="w",
            wraplength=610,
            foreground="#6b4e00",
            background="#fff3cd",
        ).pack(side="left", fill="x", expand=True)
        tk.Label(
            warning,
            text="⚠",
            font=("Segoe UI Symbol", 14, "bold"),
            foreground="#8a5a00",
            background="#fff3cd",
        ).pack(side="right", padx=(8, 0))

        ttk.Label(
            win,
            text="Cole uma macro gerada pelo programa:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(0, 5))

        text = tk.Text(
            win,
            height=10,
            font=("Consolas", 10)
        )
        text.pack(fill="both", expand=True, padx=15)

        def insert():
            value = text.get("1.0", "end-1c")
            if self.load_custom_macro(value):
                win.destroy()
                return

            messagebox.showwarning(
                "Importe sua Macro",
                (
                    "Macro não suportada, tente recriar suas funções no "
                    "programa ou revise ela novamente"
                ),
                parent=win,
            )

        ttk.Button(
            win,
            text="Carregar macro",
            command=insert
        ).pack(pady=10)

        text.focus_set()

    def insert_description_text(self):
        win = tk.Toplevel(self.root)
        win.title("Texto da descrição")
        set_responsive_window_geometry(win, 500, 260, 380, 200)
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Texto:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 5))

        text = tk.Text(win, height=8)
        text.pack(fill="both", expand=True, padx=15)

        def insert():
            value = text.get("1.0", "end-1c")

            if value:
                self.description_text.insert(
                    tk.INSERT,
                    value
                )
                self.update_preview()

            win.destroy()

        ttk.Button(
            win,
            text="Inserir",
            command=insert
        ).pack(pady=10)

    # ========================================================
    # Utilidades
    # ========================================================

    def update_skill_macro_gear_style(self):
        if self.skill_macro_button is not None:
            self.skill_macro_button.configure(
                text=(
                    "⚒\nEspecialista"
                    if self.skill_macro_specialist_enabled
                    else "⚒ Perícias"
                ),
                style=(
                    "Modified.TButton"
                    if self.skill_macro_specialist_enabled
                    else "TButton"
                ),
            )
        if self.skill_macro_gear_button is not None:
            self.skill_macro_gear_button.configure(
                style=(
                    "Modified.TButton"
                    if (
                        self.skill_macro_extra
                        or self.skill_macro_specialist_enabled
                    )
                    else "TButton"
                )
            )

    def update_resistance_macro_gear_style(self):
        if self.resistance_macro_gear_button is not None:
            self.resistance_macro_gear_button.configure(
                style=(
                    "Modified.TButton"
                    if self.resistance_macro_extra
                    else "TButton"
                )
            )

    def build_skill_macro(self):
        if self.skill_macro_specialist_enabled:
            skills = [
                skill
                for skill in PERICIAS_ESPECIALISTA
                if skill in self.skill_macro_specialist_skills
            ]
            skill_options = "".join(
                (
                    f"|{skill},{'Oficio' if skill == 'Ofício' else skill}"
                    f"[[1d20+[[{PERICIAS_ESPECIALISTA[skill]}]]"
                )
                for skill in skills
            )
            skill_macro_base = (
                "&{template:t20}{{character=@{character_name}}}"
                "{{rollname=Teste de Perícia}}"
                f"{{{{theroll=?{{Perícia: {skill_options}}}"
                "+[[@{bonus_treino}]]"
            )
        else:
            skill_macro_base = SKILL_MACRO_BASE

        return (
            skill_macro_base
            + self.skill_macro_extra
            + SKILL_MACRO_CLOSING
        )

    def build_resistance_macro(self):
        return (
            RESISTANCE_MACRO_BASE
            + self.resistance_macro_extra
            + SKILL_MACRO_CLOSING
        )

    def build_skill_question_extra(
        self,
        name,
        options,
        effect_value,
        effect_mode,
        effect_enabled,
        pride_enabled,
    ):
        question = MacroQuestion(name, options).build()
        if not options:
            question = f"?{{{name}|}}"

        if not options and not effect_value:
            question = f"?{{{name}|0}}"

        if not effect_enabled:
            return "+[[(?{Orgulho|0}*2)]]" if pride_enabled else ""

        if pride_enabled:
            pride_macro = "(?{Orgulho|0}*2)"
            if effect_mode == "multiplicativo" and effect_value:
                effect = f"({question}*{effect_value})"
            elif effect_value:
                effect = f"{question[:-1]}{effect_value}}}"
            else:
                effect = question
            return f"+[[{pride_macro}+{effect}]]"

        if effect_mode == "multiplicativo" and effect_value:
            return f"+[[({question}*{effect_value})]]"
        if effect_value:
            return f"+[[({question}{effect_value})]]"
        return f"+[[({question})]]"

    def copy_skill_macro(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.build_skill_macro())
        self.root.update()
        messagebox.showinfo(
            "Macro de Perícias copiada",
            "A macro de Perícias foi copiada para a área de transferência.",
        )

    def copy_resistance_macro(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.build_resistance_macro())
        self.root.update()
        messagebox.showinfo(
            "Macro de Resistências copiada",
            "A macro de Resistências foi copiada para a área de transferência.",
        )

    def open_skill_macro_editor(self, macro_type="skill"):
        is_skill_macro = macro_type == "skill"
        state_prefix = (
            "skill_macro" if is_skill_macro else "resistance_macro"
        )
        section_name = "Perícias" if is_skill_macro else "Resistências"
        get_setting = lambda name: getattr(
            self,
            f"{state_prefix}_{name}",
        )
        set_setting = lambda name, value: setattr(
            self,
            f"{state_prefix}_{name}",
            value,
        )
        win = tk.Toplevel(self.root)
        win.title(f"Pergunta Roll20 - {section_name}")
        set_responsive_window_geometry(
            win,
            760,
            700 if is_skill_macro else 560,
            560,
            420,
        )
        win.transient(self.root)
        win.grab_set()

        editor_viewport = ttk.Frame(win)
        editor_viewport.pack(fill="both", expand=True)
        editor_canvas = tk.Canvas(editor_viewport, highlightthickness=0)
        editor_scrollbar = ttk.Scrollbar(
            editor_viewport,
            orient="vertical",
            command=editor_canvas.yview,
        )
        editor_canvas.configure(yscrollcommand=editor_scrollbar.set)
        editor_viewport.columnconfigure(0, weight=1)
        editor_viewport.columnconfigure(1, minsize=16)
        editor_viewport.rowconfigure(0, weight=1)
        editor_canvas.grid(row=0, column=0, sticky="nsew")
        editor_scrollbar.grid(row=0, column=1, sticky="ns")
        editor_content = ttk.Frame(editor_canvas)
        editor_content_window = editor_canvas.create_window(
            (0, 0),
            window=editor_content,
            anchor="nw",
        )

        def update_editor_scroll_region(_event=None):
            bounds = editor_canvas.bbox("all")
            content_height = bounds[3] if bounds else 0
            editor_canvas.configure(
                scrollregion=(
                    0,
                    0,
                    max(editor_canvas.winfo_width(), bounds[2] if bounds else 0),
                    content_height,
                )
            )
            needs_scrollbar = (
                content_height > editor_canvas.winfo_height() + 1
            )
            if needs_scrollbar:
                editor_scrollbar.state(["!disabled"])
            else:
                editor_scrollbar.state(["disabled"])
                editor_canvas.yview_moveto(0)

        editor_content.bind(
            "<Configure>",
            update_editor_scroll_region,
        )
        editor_canvas.bind(
            "<Configure>",
            lambda event: (
                editor_canvas.itemconfigure(
                    editor_content_window,
                    width=event.width,
                ),
                editor_canvas.after_idle(update_editor_scroll_region),
            ),
        )

        ttk.Label(
            editor_content,
            text="Nome da pergunta:",
            style="Section.TLabel",
        ).pack(anchor="w", padx=15, pady=(15, 4))

        name_var = tk.StringVar(value=get_setting("question_name"))
        ttk.Entry(
            editor_content,
            textvariable=name_var,
        ).pack(fill="x", padx=15)

        ttk.Label(
            editor_content,
            text="Opções (nome = valor):",
            style="Section.TLabel",
        ).pack(anchor="w", padx=15, pady=(12, 4))

        options_frame = self.create_scrollable_panel(
            editor_content,
            padx=15,
        )
        options_canvas = options_frame.master
        options_frame_container = options_canvas.master
        options_frame_container.pack_configure(
            fill="x",
            expand=False,
        )
        options_canvas.configure(height=1)
        options_scrollbar = next(
            child
            for child in options_frame_container.winfo_children()
            if isinstance(child, ttk.Scrollbar)
        )
        option_rows = []

        def resize_options_list(_event=None):
            options_frame.update_idletasks()
            content_height = options_frame.winfo_reqheight()
            max_visible_height = 5 * 34
            visible_height = min(content_height, max_visible_height)
            options_canvas.configure(height=max(1, visible_height))
            options_canvas.configure(
                scrollregion=options_canvas.bbox("all")
            )
            if content_height > visible_height + 1:
                options_scrollbar.state(["!disabled"])
            else:
                options_scrollbar.state(["disabled"])
                options_canvas.yview_moveto(0)
            editor_canvas.after_idle(update_editor_scroll_region)

        options_frame.bind("<Configure>", resize_options_list)

        def remove_option(option_row):
            option_rows.remove(option_row)
            option_row["frame"].destroy()
            resize_options_list()

        def add_option(label="", value=""):
            row_frame = ttk.Frame(options_frame)
            row_frame.pack(fill="x", pady=2)
            option_row = {
                "frame": row_frame,
                "label": tk.StringVar(value=label),
                "value": tk.StringVar(value=value),
            }
            ttk.Button(
                row_frame,
                text="×",
                width=2,
                command=lambda: remove_option(option_row),
            ).pack(side="left", padx=(0, 4))
            ttk.Entry(
                row_frame,
                textvariable=option_row["label"],
                width=22,
            ).pack(side="left", fill="x", expand=True)
            ttk.Entry(
                row_frame,
                textvariable=option_row["value"],
                width=22,
            ).pack(side="left", padx=(5, 0), fill="x", expand=True)
            option_rows.append(option_row)
            resize_options_list()

        for label, value in get_setting("question_options"):
            add_option(label, value)

        editor_actions = ttk.Frame(win)
        editor_actions.pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=(5, 10),
        )
        ttk.Button(
            editor_actions,
            text="Cancelar",
            command=win.destroy,
            style="EditorCancel.TButton",
        ).pack(side="right")
        ttk.Button(
            editor_actions,
            text="Salvar",
            command=lambda: save(),
            style="EditorSave.TButton",
        ).pack(side="right", padx=(0, 6))

        def resize_editor_to_content():
            if not win.winfo_exists():
                return
            win.update_idletasks()
            bounds = editor_canvas.bbox("all")
            content_height = bounds[3] if bounds else 0
            requested_height = (
                content_height
                + editor_actions.winfo_reqheight()
                + 24
            )
            available_height = max(240, win.winfo_screenheight() - 80)
            set_responsive_window_geometry(
                win,
                760,
                min(available_height, max(420, requested_height)),
                560,
                420,
            )

        options_container = ttk.LabelFrame(
            editor_content,
            text="Opções",
            padding=8,
        )
        options_container.pack(fill="x", padx=15, pady=(8, 0))

        effect_frame = ttk.LabelFrame(
            options_container,
            text="Condicional com alterador de resultado",
            padding=8,
        )
        effect_frame.pack(fill="x")

        effect_value_var = tk.StringVar(
            value=get_setting("effect_value")
        )
        ttk.Entry(
            effect_frame,
            textvariable=effect_value_var,
            width=12,
        ).pack(side="left", padx=(0, 10))
        self.add_result_modifier_warning(effect_frame, effect_value_var)

        effect_mode_var = tk.StringVar(
            value=get_setting("effect_mode")
        )
        ttk.Radiobutton(
            effect_frame,
            text="Multiplicativo",
            variable=effect_mode_var,
            value="multiplicativo",
        ).pack(side="left", padx=(0, 8))
        ttk.Radiobutton(
            effect_frame,
            text="Aditivo",
            variable=effect_mode_var,
            value="aditivo",
        ).pack(side="left")

        ttk.Button(
            effect_frame,
            text="+ Adicionar opções",
            command=add_option,
        ).pack(side="right")

        macro_effect_controls = ttk.Frame(options_container)
        macro_effect_controls.pack(fill="x", pady=(8, 0))
        pride_frame = ttk.Frame(macro_effect_controls)
        pride_frame.pack(side="left")
        effect_control_frame = ttk.Frame(macro_effect_controls)
        effect_control_frame.pack(side="left", padx=(8, 0))
        effect_active_var = tk.BooleanVar(
            value=get_setting("effect_enabled")
        )

        def render_effect_control():
            for child in effect_control_frame.winfo_children():
                child.destroy()
            if effect_active_var.get():
                ttk.Button(
                    effect_control_frame,
                    text="EFEITO DE PERGUNTA (ativo)",
                    command=lambda: set_effect_active(False),
                    style="EffectActive.TButton",
                    padding=(6, 4),
                ).pack(side="left")
            else:
                ttk.Button(
                    effect_control_frame,
                    text="EFEITO DE PERGUNTA",
                    command=lambda: set_effect_active(True),
                    style="EffectInactive.TButton",
                    padding=(6, 4),
                ).pack(side="left")

        def set_effect_active(active):
            effect_active_var.set(active)
            render_effect_control()

        render_effect_control()

        pride_active_var = tk.BooleanVar(
            value=get_setting("pride_enabled")
        )

        def render_pride_control():
            for child in pride_frame.winfo_children():
                child.destroy()
            if pride_active_var.get():
                ttk.Button(
                    pride_frame,
                    text="👑 ORGULHO (ativo)",
                    command=lambda: set_pride_active(False),
                    style="PrideActive.TButton",
                    padding=(6, 4),
                ).pack(side="left")
            else:
                ttk.Button(
                    pride_frame,
                    text="👑 ORGULHO",
                    command=lambda: set_pride_active(True),
                    style="PrideInactive.TButton",
                    padding=(6, 4),
                ).pack(side="left")

        def set_pride_active(active):
            pride_active_var.set(active)
            render_pride_control()

        render_pride_control()

        specialist_control_frame = ttk.Frame(macro_effect_controls)
        if is_skill_macro:
            specialist_control_frame.pack(
                side="left",
                padx=(8, 0),
            )
        specialist_active_var = tk.BooleanVar(
            value=(
                get_setting("specialist_enabled")
                if is_skill_macro
                else False
            )
        )
        specialist_options_frame = ttk.LabelFrame(
            options_container,
            text="Configuração do Especialista",
            padding=8,
        )
        intelligence_var = tk.StringVar(
            value=(
                get_setting("specialist_intelligence")
                if is_skill_macro
                else "1"
            )
        )
        skill_vars = {
            skill: tk.BooleanVar(
                value=(
                    is_skill_macro
                    and skill in get_setting("specialist_skills")
                )
            )
            for skill in PERICIAS_ESPECIALISTA
        }
        skill_buttons = {}

        ttk.Label(
            specialist_options_frame,
            text="Inteligência do personagem (mínimo de seleções):",
        ).grid(row=0, column=0, columnspan=3, sticky="w")
        ttk.Entry(
            specialist_options_frame,
            textvariable=intelligence_var,
            width=8,
        ).grid(row=0, column=3, sticky="w", padx=(6, 0))
        specialist_skills_panel = ttk.Frame(specialist_options_frame)
        specialist_skills_panel.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="nsew",
            pady=(6, 0),
        )
        specialist_skills_frame = self.create_scrollable_panel(
            specialist_skills_panel,
            canvas_height=220,
        )

        def get_specialist_skill_limit():
            try:
                return max(1, int(intelligence_var.get().strip()))
            except ValueError:
                return 1

        def refresh_specialist_skill_buttons(*_args):
            selected_count = sum(
                variable.get() for variable in skill_vars.values()
            )
            selection_limit = get_specialist_skill_limit()
            for skill, button in skill_buttons.items():
                selected = skill_vars[skill].get()
                if selected:
                    button.configure(
                        state="normal",
                        style="SpecialistSelected.TButton",
                    )
                elif selected_count >= selection_limit:
                    button.configure(
                        state="disabled",
                        style="SpecialistDisabled.TButton",
                    )
                else:
                    button.configure(
                        state="normal",
                        style="TButton",
                    )

        def toggle_specialist_skill(skill):
            variable = skill_vars[skill]
            if (
                not variable.get()
                and sum(item.get() for item in skill_vars.values())
                >= get_specialist_skill_limit()
            ):
                return
            variable.set(not variable.get())
            refresh_specialist_skill_buttons()

        for skill in skill_vars:
            button = ttk.Button(
                specialist_skills_frame,
                text=skill,
                command=lambda selected_skill=skill: toggle_specialist_skill(
                    selected_skill
                ),
            )
            skill_buttons[skill] = button

        self.make_responsive_grid(
            specialist_skills_frame,
            list(skill_buttons.values()),
            minimum_cell_width=125,
            maximum_columns=4,
        )
        specialist_options_frame.columnconfigure(0, weight=1)
        specialist_options_frame.columnconfigure(3, weight=1)
        intelligence_var.trace_add(
            "write",
            refresh_specialist_skill_buttons,
        )
        refresh_specialist_skill_buttons()

        def render_specialist_control():
            for child in specialist_control_frame.winfo_children():
                child.destroy()
            if specialist_active_var.get():
                ttk.Button(
                    specialist_control_frame,
                    text="ESPECIALISTA (ativo)",
                    command=lambda: set_specialist_active(False),
                    style="EffectActive.TButton",
                    padding=(6, 4),
                ).pack(side="left")
                specialist_options_frame.pack(
                    fill="x",
                    pady=(6, 0),
                )
                win.after_idle(resize_editor_to_content)
            else:
                ttk.Button(
                    specialist_control_frame,
                    text="ESPECIALISTA",
                    command=lambda: set_specialist_active(True),
                    style="EffectInactive.TButton",
                    padding=(6, 4),
                ).pack(side="left")
                specialist_options_frame.pack_forget()
                win.after_idle(resize_editor_to_content)

        def set_specialist_active(active):
            specialist_active_var.set(active)
            if is_skill_macro:
                render_specialist_control()
            else:
                win.after_idle(resize_editor_to_content)

        if is_skill_macro:
            render_specialist_control()

        def save():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning(
                    f"Pergunta de {section_name}",
                    "Digite um nome para a pergunta.",
                    parent=win,
                )
                return

            options = [
                QuestionOption(
                    row["label"].get().strip(),
                    row["value"].get().strip(),
                )
                for row in option_rows
                if row["label"].get().strip()
            ]
            specialist_skills = [
                skill
                for skill, variable in skill_vars.items()
                if variable.get()
            ]
            specialist_intelligence = intelligence_var.get().strip()
            if is_skill_macro and specialist_active_var.get():
                try:
                    intelligence_score = int(specialist_intelligence)
                except ValueError:
                    messagebox.showwarning(
                        "Especialista",
                        "Informe a Inteligência do personagem como um número inteiro.",
                        parent=win,
                    )
                    return
                minimum_skills = max(1, intelligence_score)
                if minimum_skills > len(PERICIAS_ESPECIALISTA):
                    messagebox.showwarning(
                        "Especialista",
                        (
                            f"A Inteligência exige pelo menos {minimum_skills} "
                            "seleções, mas existem apenas "
                            f"{len(PERICIAS_ESPECIALISTA)}."
                        ),
                        parent=win,
                    )
                    return
                if len(specialist_skills) < minimum_skills:
                    messagebox.showwarning(
                        "Especialista",
                        (
                            f"Selecione pelo menos {minimum_skills} opção(ões), "
                            "de acordo com a Inteligência informada."
                        ),
                        parent=win,
                    )
                    return

            set_setting("question_name", name)
            set_setting("question_options", [
                (option.label, option.value)
                for option in options
            ])
            set_setting("pride_enabled", pride_active_var.get())
            set_setting("effect_enabled", effect_active_var.get())
            set_setting("effect_value", effect_value_var.get())
            set_setting("effect_mode", effect_mode_var.get())
            if is_skill_macro:
                set_setting("specialist_enabled", specialist_active_var.get())
                set_setting("specialist_skills", specialist_skills)
                set_setting(
                    "specialist_intelligence",
                    specialist_intelligence,
                )
            set_setting("extra", self.build_skill_question_extra(
                name,
                options,
                effect_value_var.get(),
                effect_mode_var.get(),
                effect_active_var.get(),
                pride_active_var.get(),
            ))
            if is_skill_macro:
                self.update_skill_macro_gear_style()
            else:
                self.update_resistance_macro_gear_style()
            win.destroy()

    def copy_macro(self):
        macro = self.build_macro()

        self.root.clipboard_clear()
        self.root.clipboard_append(macro)
        self.root.update()

        messagebox.showinfo(
            "Macro copiada",
            "A macro foi copiada para a área de transferência."
        )

    def clear_all(self):
        if not messagebox.askyesno(
            "Limpar",
            "Tem certeza que deseja limpar a macro?"
        ):
            return

        self.attack_name_var.set("Ataque")
        if hasattr(self, "attack_best_die_var"):
            self.attack_best_die_var.set("nao")
        self.attack_roll_var.set("1d20")
        if hasattr(self, "attack_threat_var"):
            self.attack_threat_var.set("")
        if hasattr(self, "attack_extra_enabled_var"):
            self.attack_extra_enabled_var.set(False)
            self.toggle_attack_extra_field()
        if hasattr(self, "attack_extra_vars"):
            for var in self.attack_extra_vars:
                var.set("")
        self.damage_var.set("")
        if hasattr(self, "damage_additional_var"):
            self.damage_additional_var.set("")
        self.critical_var.set("")
        self.damage_type_var.set("")
        if hasattr(self, "attack_attribute_var"):
            self.attack_attribute_var.set("Luta")
        for variable in getattr(self, "damage_attribute_vars", {}).values():
            variable.set(False)
        if hasattr(self, "damage_extra_enabled_var"):
            self.damage_extra_enabled_var.set(False)
            self.toggle_damage_extra_field()
        if hasattr(self, "damage_extra_vars"):
            for var in self.damage_extra_vars:
                var.set("")

        self.description_text.delete("1.0", "end")

        self.update_preview()


def main():
    if update_frozen_app():
        return

    root = tk.Tk()
    app = MacroBuilderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
