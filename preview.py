import ast
import re
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from constants import MACRO_BUTTON_PATTERN


PREVIEW_COLORS = {
    "background": "#d3e5f5",
    "card": "white",
    "normal_roll": "#FEF68E",
    "critical_roll": "#ffcc80",
    "roll_outline": "#d69e00",
    "critical_outline": "#3fb315",
    "critical_label": "#287a38",
    "description": "#fdf8ab",
    "macro_button": "#d80b9b",
    "text": "#111111",
}


def parse_preview_question(formula: str, start: int):
    parts = []
    part_start = start + 2
    depth = 1

    for index in range(part_start, len(formula)):
        character = formula[index]
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                parts.append(formula[part_start:index])
                return parts, index + 1
        elif character == "|" and depth == 1:
            parts.append(formula[part_start:index])
            part_start = index + 1

    return None, len(formula)


def get_preview_question_choices(*formulas: str) -> dict[str, str]:
    choices = {}
    for formula in formulas:
        cursor = 0
        while True:
            start = formula.find("?{", cursor)
            if start == -1:
                break
            parts, _end = parse_preview_question(formula, start)
            if parts and len(parts) > 1:
                _, separator, value = parts[1].partition(",")
                if separator:
                    choices.setdefault(parts[0], value)
            cursor = start + 2
    return choices


def select_first_preview_options(
    formula: str,
    choices: dict[str, str] | None = None,
) -> str:
    choices = choices or {}
    result = []
    cursor = 0
    while True:
        start = formula.find("?{", cursor)
        if start == -1:
            result.append(formula[cursor:])
            break
        result.append(formula[cursor:start])
        parts, end = parse_preview_question(formula, start)
        if not parts:
            result.append(formula[start:])
            break

        if len(parts) > 1:
            _, separator, value = parts[1].partition(",")
            replacement = value if separator else parts[1]
        else:
            replacement = choices.get(parts[0], formula[start:end])

        if replacement == formula[start:end]:
            result.append(formula[start:end])
        else:
            result.append(select_first_preview_options(replacement, choices))
        cursor = end

    return "".join(result)


def preview_die_value(match: re.Match, force_d20: bool = False) -> str:
    count = int(match.group(1) or "1")
    sides = int(match.group(2))
    modifier = (match.group(3) or "").lower()
    modifier_count = int(match.group(4) or "1") if modifier else 0

    if force_d20 and sides == 20:
        return "20"
    if modifier.startswith("k"):
        count = min(count, modifier_count)
    elif modifier.startswith("d"):
        count = max(0, count - modifier_count)

    value = count * sides / 2
    return str(int(value)) if value.is_integer() else str(value)


def simplify_preview_math(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        return "0"

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return str(node.value), True, node.value
        if isinstance(node, ast.Name):
            return "0", True, 0
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            text, numeric, value = visit(node.operand)
            sign = -1 if isinstance(node.op, ast.USub) else 1
            if numeric:
                result = sign * value
                return str(result), True, result
            return ("-" if sign < 0 else "+") + text, False, None
        if isinstance(node, ast.BinOp) and isinstance(
            node.op,
            (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv),
        ):
            left, left_numeric, left_value = visit(node.left)
            right, right_numeric, right_value = visit(node.right)
            operators = {
                ast.Add: "+",
                ast.Sub: "-",
                ast.Mult: "×",
                ast.Div: "/",
                ast.FloorDiv: "/",
            }
            if left_numeric and right_numeric:
                try:
                    result = {
                        ast.Add: lambda: left_value + right_value,
                        ast.Sub: lambda: left_value - right_value,
                        ast.Mult: lambda: left_value * right_value,
                        ast.Div: lambda: left_value / right_value,
                        ast.FloorDiv: lambda: left_value // right_value,
                    }[type(node.op)]()
                except ZeroDivisionError:
                    return f"{left} {operators[type(node.op)]} {right}", False, None
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return str(result), True, result
            return f"{left} {operators[type(node.op)]} {right}", False, None
        raise ValueError("Unsupported preview expression")

    try:
        result, numeric, value = visit(tree)
    except (ValueError, TypeError):
        return "0"
    if numeric and isinstance(value, float) and value.is_integer():
        return str(int(value))
    return result


def format_roll_preview(
    formula: str,
    force_d20: bool = False,
    choices: dict[str, str] | None = None,
) -> str:
    preview = select_first_preview_options(formula or "", choices)
    preview = preview.replace("[[", "").replace("]]", "")
    preview = re.sub(r"cs>\d+", "", preview, flags=re.IGNORECASE)
    preview = re.sub(r"@\{([^}]+)\}", lambda _match: "0", preview)
    preview = re.sub(
        r"(?<![\w.])(\d*)d(\d+)(?:(kh|kl|dh|dl)(\d*))?",
        lambda match: preview_die_value(match, force_d20),
        preview,
        flags=re.IGNORECASE,
    )
    return simplify_preview_math(preview)


def split_macro_button_markup(text: str) -> list[tuple[str, str]]:
    parts = []
    cursor = 0
    for match in MACRO_BUTTON_PATTERN.finditer(text or ""):
        if match.start() > cursor:
            parts.append(("text", text[cursor:match.start()]))
        parts.append(("button", match.group(1)))
        cursor = match.end()
    if cursor < len(text or ""):
        parts.append(("text", text[cursor:]))
    return parts


class PreviewMixin:
    @staticmethod
    def configure_preview_styles(style: ttk.Style):
        style.configure("Preview.TLabel", font=("Segoe UI", 10, "bold"))

    def build_preview_panel(self, parent):
        ttk.Label(
            parent,
            text="Macro gerada",
            style="Section.TLabel",
        ).pack(anchor="w", pady=(0, 8))

        macro_toolbar = ttk.Frame(parent)
        macro_toolbar.pack(fill="x", pady=(0, 4))
        ttk.Button(
            macro_toolbar,
            text="Atualizar",
            command=self.update_preview,
        ).pack(side="left")
        ttk.Button(
            macro_toolbar,
            text="Copiar macro",
            command=self.copy_macro,
        ).pack(side="left", padx=6)

        self.duplicate_condition_warning_var = tk.StringVar(value="")
        ttk.Label(
            parent,
            textvariable=self.duplicate_condition_warning_var,
            foreground="#b3261e",
            wraplength=460,
        ).pack(anchor="w", fill="x", pady=(0, 4))

        preview_split = ttk.PanedWindow(parent, orient="vertical")
        preview_split.pack(fill="both", expand=True)
        macro_panel = ttk.Frame(preview_split)
        card_panel = ttk.Frame(preview_split)
        preview_split.add(macro_panel, weight=3)
        preview_split.add(card_panel, weight=2)

        self.preview = tk.Text(
            macro_panel,
            wrap="char",
            font=("Consolas", 10),
        )
        self.preview.pack(fill="both", expand=True)

        card_toolbar = ttk.Frame(card_panel)
        card_toolbar.pack(fill="x", pady=(8, 4))
        ttk.Label(
            card_toolbar,
            text="Prévia do Roll20",
            style="Preview.TLabel",
        ).pack(side="left")

        self.roll_preview_critical_var = tk.BooleanVar(value=False)
        preview_mode = ttk.Frame(card_toolbar)
        preview_mode.pack(side="right")
        for label, value in (("Normal", False), ("Crítico", True)):
            ttk.Radiobutton(
                preview_mode,
                text=label,
                variable=self.roll_preview_critical_var,
                value=value,
                command=self.draw_roll_preview,
            ).pack(side="left", padx=(6, 0))

        card_frame = ttk.Frame(card_panel)
        card_frame.pack(fill="both", expand=True)
        self.roll_preview_canvas = tk.Canvas(
            card_frame,
            background=PREVIEW_COLORS["background"],
            highlightthickness=0,
        )
        card_scrollbar = ttk.Scrollbar(
            card_frame,
            orient="vertical",
            command=self.roll_preview_canvas.yview,
        )
        self.roll_preview_canvas.configure(yscrollcommand=card_scrollbar.set)
        self.roll_preview_canvas.pack(side="left", fill="both", expand=True)
        card_scrollbar.pack(side="right", fill="y")
        self.roll_preview_canvas.bind(
            "<Configure>",
            lambda _event: self.draw_roll_preview(),
        )

        bottom = ttk.Frame(parent)
        bottom.pack(fill="x", pady=(8, 0))
        ttk.Button(
            bottom,
            text="Limpar",
            command=self.clear_all,
        ).pack(side="right")

    def draw_roll_preview(self):
        canvas = getattr(self, "roll_preview_canvas", None)
        if canvas is None or not canvas.winfo_exists():
            return

        colors = PREVIEW_COLORS
        canvas.delete("all")
        width = max(canvas.winfo_width(), 260)
        card_width = min(width - 24, 440)
        card_left = max((width - card_width) / 2, 8)
        card_right = card_left + card_width
        center_x = (card_left + card_right) / 2
        top = 14
        content_y = top + 14
        data = self.get_roll_preview_data()
        card_background = canvas.create_rectangle(
            card_left,
            top,
            card_right,
            top + 1000,
            fill=colors["card"],
            outline="",
        )

        def add_text(
            text,
            x,
            y,
            wrap_width,
            font,
            fill=None,
            justify="center",
        ):
            item = canvas.create_text(
                x,
                y,
                text=text,
                width=wrap_width,
                font=font,
                fill=fill or colors["text"],
                justify=justify,
                anchor="n",
            )
            bounds = canvas.bbox(item)
            return bounds[3] if bounds else y

        content_y = add_text(
            data["character"].upper(),
            center_x,
            content_y,
            card_width - 24,
            ("PT Sans", 10, "bold"),
        ) + 3
        content_y = add_text(
            data["name"] or "Ataque",
            center_x,
            content_y,
            card_width - 24,
            ("PT Sans", 11, "italic"),
        ) + 7

        column_width = (card_width - 30) / 2
        left_center = card_left + 10 + column_width / 2
        right_center = card_right - 10 - column_width / 2

        def add_roll_box(
            text,
            center,
            y,
            max_width,
            fill=None,
            outline=None,
        ):
            text_item = canvas.create_text(
                center,
                y + 5,
                text=text,
                width=max_width - 12,
                font=("Helvetica Neue", 15, "bold"),
                fill=colors["text"],
                justify="center",
                anchor="n",
            )
            bounds = canvas.bbox(text_item)
            if not bounds:
                return y + 28
            box_left = max(center - max_width / 2, bounds[0] - 7)
            box_right = min(center + max_width / 2, bounds[2] + 7)
            box_top = bounds[1] - 5
            box_bottom = bounds[3] + 5
            box = canvas.create_rectangle(
                box_left,
                box_top,
                box_right,
                box_bottom,
                fill=fill or colors["normal_roll"],
                outline=outline or colors["roll_outline"],
                width=1,
            )
            canvas.tag_raise(text_item, box)
            return box_bottom

        attack_bottom = add_roll_box(
            data["attack"],
            left_center,
            content_y,
            column_width - 8,
            fill=(
                colors["critical_roll"]
                if data["critical"]
                else colors["normal_roll"]
            ),
            outline=(
                colors["critical_outline"]
                if data["critical"]
                else colors["roll_outline"]
            ),
        )

        damage_left = center_x + 8
        damage_right = card_right - 10
        damage_specs = []
        for roll_value in data["damage_rolls"]:
            probe = canvas.create_text(
                0,
                0,
                text=roll_value,
                font=("Helvetica Neue", 15, "bold"),
                fill=colors["text"],
                anchor="nw",
            )
            bounds = canvas.bbox(probe)
            canvas.delete(probe)
            text_width = bounds[2] - bounds[0] if bounds else 20
            text_height = bounds[3] - bounds[1] if bounds else 18
            damage_specs.append(
                (roll_value, max(36, text_width + 14), text_height + 12)
            )

        gap = 5
        group_width = sum(box_width for _, box_width, _ in damage_specs)
        group_width += gap * max(0, len(damage_specs) - 1)
        damage_x = max(damage_left, right_center - group_width / 2)
        damage_y = content_y
        damage_row_height = 0
        damage_bottom = content_y
        for roll_value, box_width, box_height in damage_specs:
            if damage_x + box_width > damage_right and damage_x > damage_left:
                damage_y += damage_row_height + 7
                damage_x = damage_left
                damage_row_height = 0
            box = canvas.create_rectangle(
                damage_x,
                damage_y,
                damage_x + box_width,
                damage_y + box_height,
                fill=colors["normal_roll"],
                outline=colors["roll_outline"],
                width=1,
            )
            probe = canvas.create_text(
                damage_x + box_width / 2,
                damage_y + 6,
                text=roll_value,
                width=box_width - 14,
                font=("Helvetica Neue", 15, "bold"),
                fill=colors["text"],
                justify="center",
                anchor="n",
            )
            canvas.tag_raise(probe, box)
            damage_row_height = max(damage_row_height, box_height)
            damage_bottom = max(damage_bottom, damage_y + damage_row_height)
            damage_x += box_width + gap

        row_bottom = max(attack_bottom, damage_bottom)
        canvas.create_line(
            center_x,
            content_y + 2,
            center_x,
            row_bottom + 26,
            fill=colors["text"],
        )
        add_text(
            "Ataque",
            left_center,
            row_bottom + 4,
            column_width - 8,
            ("PT Sans", 10),
        )
        damage_label = "Dano (Crítico)" if data["critical"] else "Dano"
        add_text(
            damage_label,
            right_center,
            row_bottom + 4,
            column_width - 8,
            ("PT Sans", 10),
            fill=colors["critical_label"] if data["critical"] else colors["text"],
        )
        content_y = row_bottom + 25

        if data["damage_type"]:
            content_y = add_text(
                data["damage_type"],
                center_x,
                content_y,
                card_width - 24,
                ("PT Sans", 11, "italic"),
            ) + 4

        description = data["description"].strip()
        if description:
            description_left = card_left + 14
            description_width = card_width - 28
            description_y = content_y + 4
            description_background = canvas.create_rectangle(
                description_left,
                description_y,
                description_left + description_width,
                description_y + 1000,
                fill=colors["description"],
                outline="",
            )
            text_font = tkfont.Font(root=canvas, font=("Helvetica Neue", 10))
            button_font = tkfont.Font(
                root=canvas,
                font=("Helvetica Neue", 10, "bold"),
            )
            content_left = description_left + 7
            content_right = description_left + description_width - 7
            cursor_x = content_left
            cursor_y = description_y + 6
            base_line_height = text_font.metrics("linespace") + 2
            row_height = base_line_height

            def next_description_line():
                nonlocal cursor_x, cursor_y, row_height
                cursor_x = content_left
                cursor_y += row_height + 2
                row_height = base_line_height

            for part_type, value in split_macro_button_markup(description):
                if part_type == "button":
                    button_width = min(
                        button_font.measure(value) + 16,
                        content_right - content_left,
                    )
                    button_text = canvas.create_text(
                        0,
                        0,
                        text=value,
                        width=max(1, button_width - 12),
                        font=("Helvetica Neue", 10, "bold"),
                        fill="white",
                        justify="center",
                        anchor="nw",
                    )
                    button_bounds = canvas.bbox(button_text)
                    button_height = max(
                        base_line_height + 4,
                        (button_bounds[3] - button_bounds[1] + 8)
                        if button_bounds
                        else base_line_height + 4,
                    )
                    if (
                        cursor_x + button_width > content_right
                        and cursor_x > content_left
                    ):
                        next_description_line()
                    button_top = cursor_y - 2
                    button_background = canvas.create_rectangle(
                        cursor_x,
                        button_top,
                        cursor_x + button_width,
                        button_top + button_height,
                        fill=colors["macro_button"],
                        outline=colors["macro_button"],
                    )
                    canvas.coords(
                        button_text,
                        cursor_x + 6,
                        button_top + 4,
                    )
                    canvas.tag_raise(button_text, button_background)
                    cursor_x += button_width + 4
                    row_height = max(row_height, button_height + 2)
                    continue

                segments = (
                    value.replace("\r\n", "\n")
                    .replace("\r", "\n")
                    .split("\n")
                )
                for segment_index, segment in enumerate(segments):
                    if segment_index > 0 and cursor_x > content_left:
                        next_description_line()
                    for token in re.findall(r"\s+|\S+", segment):
                        if token.isspace():
                            if cursor_x == content_left:
                                continue
                            token_width = text_font.measure(token)
                            if cursor_x + token_width > content_right:
                                next_description_line()
                            else:
                                cursor_x += token_width
                            continue

                        token_width = text_font.measure(token)
                        if (
                            cursor_x + token_width > content_right
                            and cursor_x > content_left
                        ):
                            next_description_line()
                        text_item = canvas.create_text(
                            cursor_x,
                            cursor_y,
                            text=token,
                            font=("Helvetica Neue", 10),
                            fill=colors["text"],
                            anchor="nw",
                        )
                        bounds = canvas.bbox(text_item)
                        if bounds:
                            row_height = max(
                                row_height,
                                bounds[3] - cursor_y,
                            )
                        cursor_x += token_width

            description_bottom = cursor_y + row_height + 6
            canvas.coords(
                description_background,
                description_left,
                description_y,
                description_left + description_width,
                description_bottom,
            )
            content_y = description_bottom + 6

        card_bottom = max(content_y + 8, top + 100)
        canvas.coords(
            card_background,
            card_left,
            top,
            card_right,
            card_bottom,
        )
        canvas.itemconfigure(card_background, outline="black", width=2)
        canvas.configure(scrollregion=(0, 0, width, card_bottom + 14))
        canvas.yview_moveto(0)
