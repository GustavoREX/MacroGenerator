"""Separei a criação das formulas das macros do resto tudo. mesmo assim ainda é uma tripa de coisa..."""
from html import unescape
import re
from dataclasses import dataclass, field
from typing import List
from constants import ADVANCED_QUESTION_ESCAPES, BEST_DIE_FORMULA
from libraries import DAMAGE_SPECIAL_TRACK_BY_DIE, DAMAGE_STEP_TRACKS, DADOSPADRAO, GLOBALMODIFIERS, PERICIASATACK


def render_initiative_macro(extra: str = "", roll_name: str = "Iniciativa") -> str:
    return (
        "&{template:t20}{{character=@{character_name}}}"
        f"{{{{rollname={roll_name.strip() or 'Iniciativa'}}}}}"
        "{{theroll=Iniciativa [[1d20 + [[@{iniciativatotal}]]"
        + extra
        + " &{tracker}]]}}"
    )


def get_damage_step_options() -> list[tuple[str, str]]:
    options = []
    seen_values = set()

    for dice_group in DADOSPADRAO.values():
        for label, value in dice_group.items():
            if value not in seen_values:
                options.append((label, value))
                seen_values.add(value)

    for steps in DAMAGE_STEP_TRACKS.values():
        for value in steps:
            if value not in seen_values:
                options.append((value, value))
                seen_values.add(value)

    return sorted(options, key=lambda option: get_damage_die_max_total(option[1]))


def get_damage_die_max_total(die: str) -> int:
    match = re.fullmatch(r"(\d*)d(\d+)", die, flags=re.IGNORECASE)
    if not match:
        return 0
    count = int(match.group(1) or "1")
    sides = int(match.group(2))
    return count * sides


def get_damage_step_delta(start: str, current: str, steps: tuple[str, ...]) -> tuple[int, int]:
    step_delta = steps.index(current) - steps.index(start)
    total_delta = get_damage_die_max_total(current) - get_damage_die_max_total(start)
    return step_delta, total_delta


def get_damage_step_track(die: str) -> tuple[str, tuple[str, ...]]:
    track_name = DAMAGE_SPECIAL_TRACK_BY_DIE.get(die, "Padrão")
    return track_name, DAMAGE_STEP_TRACKS[track_name]


def build_attack_expression(
    base_formula: str,
    threat_margin: str = "",
    skill: str = "",
    extra_values: list[str] | None = None,
) -> str:
    attack = (base_formula or "").strip()
    margin = (threat_margin or "").strip()
    if attack and margin.isdigit():
        attack += f"cs>{margin}"
    if skill in PERICIASATACK:
        attack += "+" + PERICIASATACK[skill]
    for value in (extra_values or []):
        if value:
            attack += "+" + value
    if attack:
        attack += "+" + GLOBALMODIFIERS["Concatenaçao de ataque"]
    return attack


def build_critical_damage(base_formula: str, repeats: int = 1) -> str:
    formula = (base_formula or "").strip()
    if not formula:
        return ""

    try:
        repeats = int(repeats)
    except (TypeError, ValueError):
        repeats = 1

    if repeats <= 1:
        return formula

    return join_formula_parts(*([formula] * repeats))


def join_formula_parts(*parts: str) -> str:
    formula = ""
    for part in parts:
        value = (part or "").strip()
        if not value:
            continue
        if not formula or value.startswith("-"):
            formula += value
        else:
            formula += "+" + value
    return formula


def simplify_condition_questions(formula: str) -> str:
    parts = []
    cursor = 0

    while True:
        start = formula.find("?{", cursor)
        if start == -1:
            parts.append(formula[cursor:])
            break

        parts.append(formula[cursor:start])
        depth = 1
        pipe = -1
        end = start + 2
        while end < len(formula) and depth:
            if formula.startswith("&#124;", end):
                if depth == 1 and pipe == -1:
                    pipe = end
                end += len("&#124;")
            elif formula.startswith("&#125;", end):
                depth -= 1
                end += len("&#125;")
            elif formula[end] == "|" and depth == 1 and pipe == -1:
                pipe = end
                end += 1
            elif formula[end] == "{":
                depth += 1
                end += 1
            elif formula[end] == "}":
                depth -= 1
                end += 1
            else:
                end += 1

        if depth:
            parts.append(formula[start:])
            break

        if pipe == -1:
            parts.append(formula[start:end])
        else:
            parts.append(f"?{{{formula[start + 2:pipe]}}}")
        cursor = end

    return "".join(parts)


def build_damage_roll_formula(
    base_formula: str,
    attributes: list[str] | None = None,
    universal_conditions: list[str] | None = None,
) -> str:
    formula = join_formula_parts(base_formula, *(attributes or []))
    universal_conditions = [
        condition
        for condition in (universal_conditions or [])
        if condition
    ]
    if formula or universal_conditions:
        damage_suffix = GLOBALMODIFIERS["Concatenaçao de Dano"]
        roll_bonus = GLOBALMODIFIERS["Bonus Rolagem"]
        if universal_conditions and roll_bonus in damage_suffix:
            roll_bonus_index = damage_suffix.rfind(roll_bonus)
            before_roll_bonus = damage_suffix[:roll_bonus_index].rstrip("+")
            formula = join_formula_parts(
                formula,
                before_roll_bonus,
                *universal_conditions,
                roll_bonus,
            )
        elif universal_conditions:
            formula = join_formula_parts(
                formula,
                *universal_conditions,
                damage_suffix,
            )
        else:
            formula += f"+{damage_suffix}"
    return formula


def build_damage_expression(
    base_formula: str,
    extra_values: list[str] | None = None,
    attributes: list[str] | None = None,
    universal_conditions: list[str] | None = None,
) -> str:
    formula = build_damage_roll_formula(
        base_formula,
        attributes,
        universal_conditions,
    )
    return build_roll_expression(formula, extra_values)


def build_critical_expression(
    base_formula: str,
    extra_values: list[str] | None = None,
    attributes: list[str] | None = None,
    universal_conditions: list[str] | None = None,
) -> str:
    return build_damage_expression(
        base_formula, extra_values, attributes, universal_conditions,
    )


def build_roll_expression(formula: str, extra_values: list[str] | None = None) -> str:
    expression = f"[[{formula}]]" if formula else ""
    extras = "".join(value for value in (extra_values or []) if value)
    if expression and extras:
        return expression + extras
    return expression or extras


@dataclass
class QuestionOption:
    label: str
    value: str
    wrap_value: bool | None = None


@dataclass
class MacroQuestion:
    name: str
    options: List[QuestionOption] = field(default_factory=list)

    def build(self) -> str:
        parts = [f"?{{{self.name}"]
        for option in self.options:
            parts.append(f"|{option.label},{option.value}")
        parts.append("}")
        return "".join(parts)


def build_condition_question(
    name: str,
    options: List[QuestionOption],
    wrap_values: bool = True,
) -> str:
    parts = [f"?{{{name}"]
    for option in options:
        label = option.label.strip()
        value = option.value.strip()
        if not value:
            parts.append(f"|{label}")
            continue
        if value and wrap_values and option.wrap_value is not False:
            value = f"[[{value}]]"
        if label:
            parts.append(f"|{label},{value}")
        else:
            parts.append(f"|{value}")
    parts.append("}")
    return "".join(parts)


def build_modified_condition_question(
    name: str,
    options: List[QuestionOption],
    effect_value: str,
    effect_mode: str,
    wrap_values: bool = True,
) -> str:
    modifier = effect_value.strip()
    if not modifier:
        return build_condition_question(name, options, wrap_values)

    question = build_condition_question(name, options, wrap_values=False)
    operator = "*" if effect_mode == "multiplicativo" else "+"
    return f"[[({question}{operator}{modifier})]]"


def parse_result_modified_condition(
    text: str,
) -> tuple[str, str, str] | None:
    source = (text or "").strip()
    if not source.startswith("[[(") or not source.endswith(")]]"):
        return None

    expression = source[3:-3].strip()
    if not expression.startswith("?{"):
        return None

    depth = 0
    index = 0
    question_end = None
    while index < len(expression):
        if expression.startswith("?{", index):
            depth += 1
            index += 2
        elif expression.startswith("&#125;", index) and depth:
            depth -= 1
            index += len("&#125;")
            if depth == 0:
                question_end = index
                break
        elif expression[index] == "}" and depth:
            depth -= 1
            index += 1
            if depth == 0:
                question_end = index
                break
        elif expression.startswith("&#123;", index):
            index += len("&#123;")
        elif expression[index] == "{":
            depth += 1
            index += 1
        else:
            index += 1

    if question_end is None:
        return None

    question = expression[:question_end]
    modifier = expression[question_end:].strip()
    if modifier.startswith("*"):
        return question, modifier[1:].strip(), "multiplicativo"
    if modifier.startswith("+"):
        return question, modifier[1:].strip(), "aditivo"
    return None


def build_advanced_question_value(
    name: str,
    options: List[QuestionOption],
) -> str:
    parts = [f"?{{{name.translate(ADVANCED_QUESTION_ESCAPES)}"]
    for option in options:
        label = option.label.translate(ADVANCED_QUESTION_ESCAPES)
        value = option.value.translate(ADVANCED_QUESTION_ESCAPES)
        if not value.strip():
            parts.append(f"&#124;{label}")
        elif label.strip():
            parts.append(f"&#124;{label}&#44;{value}")
        else:
            parts.append(f"&#124;{value}")
    parts.append("&#125;")
    return "".join(parts)


def _split_roll20_parts(text: str, separator: str) -> list[str]:
    parts = []
    start = 0
    index = 0
    nested_depth = 0

    while index < len(text):
        if text.startswith("?{", index):
            nested_depth += 1
            index += 2
        elif text.startswith("&#125;", index) and nested_depth:
            nested_depth -= 1
            index += len("&#125;")
        elif text[index] == "}" and nested_depth:
            nested_depth -= 1
            index += 1
        elif text.startswith("&#123;", index):
            index += len("&#123;")
        elif text[index] == "{" and nested_depth:
            nested_depth += 1
            index += 1
        elif nested_depth == 0 and text.startswith(separator, index):
            parts.append(text[start:index])
            index += len(separator)
            start = index
        else:
            index += 1

    parts.append(text[start:])
    return parts


def infer_named_condition_option(value: str, numeric_label_width: int = 1):
    value = value.strip()
    if not value:
        return "x", ""

    first_digit = re.search(r"\d", value)
    if first_digit and first_digit.start() > 0:
        label = value[:first_digit.start()].strip()
        option_value = value[first_digit.start():].strip()
        if label and re.match(r"\d", option_value):
            return label, option_value

    if value.isdigit():
        return "x", value

    dice_match = re.match(r"\d+d\d+", value, flags=re.IGNORECASE)
    if dice_match:
        label_width = max(1, min(numeric_label_width, len(value) - 1))
        remainder = value[label_width:]
        if re.match(r"\d+d\d+", remainder, flags=re.IGNORECASE):
            return value[:label_width], remainder

    return "x", value


def looks_like_roll20_condition(text: str) -> bool:
    source = (text or "").strip()
    source = source.replace("&lbrack;", "&#91;")
    source = source.replace("&rbrack;", "&#93;")
    while source.startswith("[") or source.startswith("&#91;"):
        source = (
            source[1:]
            if source.startswith("[")
            else source[len("&#91;"):]
        )
    return bool(
        re.match(r"^\?\{.*?(?:\||&#124;)", source)
        or re.match(r"^\?.+?(?:\||&#124;)", source)
    )


def close_advanced_questions_before_outer_pipe(source: str) -> tuple[str, bool]:
    stack = []
    repaired = False
    index = 0

    while index < len(source):
        if source.startswith("?{", index):
            stack.append(False)
            index += 2
        elif source.startswith("&#124;", index):
            if stack:
                stack[-1] = True
            index += len("&#124;")
        elif source.startswith("&#125;", index):
            if stack:
                stack.pop()
            index += len("&#125;")
        elif source.startswith("&#123;", index):
            index += len("&#123;")
        elif source[index] == "|" and len(stack) > 1 and stack[-1]:
            source = source[:index] + "&#125;" + source[index:]
            stack.pop()
            index += len("&#125;")
            repaired = True
        elif source[index] == "}" and stack:
            stack.pop()
            index += 1
        else:
            index += 1

    return source, repaired


def parse_roll20_question(text: str):
    source = (text or "").strip()
    source = source.replace("&lbrack;", "&#91;")
    source = source.replace("&rbrack;", "&#93;")
    repaired = False

    if source.startswith("&#91;&#91;"):
        source = source[len("&#91;&#91;"):]
        if source.endswith("&#93;&#93;"):
            source = source[:-len("&#93;&#93;")]
        elif source.endswith("&#93;"):
            source = source[:-len("&#93;")]
            repaired = True
        else:
            repaired = True
    elif source.startswith("&#91;") and source.endswith("&#93;&#93;"):
        source = source[len("&#91;"):-len("&#93;&#93;")]
        repaired = True
    elif source.endswith("&#93;&#93;"):
        source = source[:-len("&#93;&#93;")]
        repaired = True
    elif source.startswith("[["):
        source = source[2:]
        if source.endswith("]]" ):
            source = source[:-2]
        elif source.endswith("]"):
            source = source[:-1]
            repaired = True
        else:
            repaired = True
    elif source.startswith("[") and source.endswith("]]" ):
        source = source[1:-2]
        repaired = True
    elif source.endswith("]]" ):
        source = source[:-2]
        repaired = True

    start = source.find("?{")
    if start == -1:
        missing_opening = re.match(r"^\?([^|]+)(\||&#124;)", source)
        if not missing_opening:
            return None
        source = "?{" + source[1:]
        start = 0
        repaired = True

    if source[:start].strip():
        return None

    source, closed_advanced = close_advanced_questions_before_outer_pipe(
        source[start:]
    )
    start = 0
    repaired = repaired or closed_advanced

    depth = 1
    index = start + 2
    body_end = len(source)
    closed = False
    while index < len(source):
        if source.startswith("?{", index):
            depth += 1
            index += 2
        elif source.startswith("&#125;", index):
            depth -= 1
            if depth == 0:
                body_end = index
                index += len("&#125;")
                closed = True
                break
            index += len("&#125;")
        elif source[index] == "{":
            depth += 1
            index += 1
        elif source[index] == "}":
            depth -= 1
            if depth == 0:
                body_end = index
                index += 1
                closed = True
                break
            index += 1
        else:
            index += 1

    if not closed:
        source += "}" * depth
        body_end = len(source) - 1
        index = len(source)
        closed = True
        repaired = True

    if source[index:].strip():
        return None

    body = source[start + 2:body_end]
    pipe_parts = _split_roll20_parts(body, "|")
    if len(pipe_parts) == 1:
        pipe_parts = _split_roll20_parts(body, "&#124;")
    if len(pipe_parts) == 1 and "," in body:
        comma_parts = _split_roll20_parts(body, ",")
        if len(comma_parts) > 1:
            pipe_parts = [
                comma_parts[0],
                ",".join(comma_parts[1:]),
            ]
        repaired = True

    if len(pipe_parts) > 1:
        first_option_parts = _split_roll20_parts(pipe_parts[0], ",")
        if len(first_option_parts) == 1:
            first_option_parts = _split_roll20_parts(
                pipe_parts[0],
                "&#44;",
            )
        if len(first_option_parts) > 1:
            condition_name = first_option_parts[0].strip()
            first_value = ",".join(first_option_parts[1:]).strip()
            if condition_name and first_value:
                pipe_parts = [
                    condition_name,
                    f"x,{first_value}",
                    *pipe_parts[1:],
                ]
                repaired = True

    name = pipe_parts[0].strip()
    if not name:
        return None

    named_option_labels = []
    for part in pipe_parts[1:]:
        named_parts = _split_roll20_parts(part, ",")
        if len(named_parts) == 1:
            named_parts = _split_roll20_parts(part, "&#44;")
        if len(named_parts) > 1 and named_parts[0].strip():
            named_option_labels.append(named_parts[0].strip())

    numeric_label_width = max(
        (
            len(label)
            for label in named_option_labels
            if label.isdigit()
        ),
        default=1,
    )

    options = []
    for part in pipe_parts[1:]:
        comma_parts = _split_roll20_parts(part, ",")
        if len(comma_parts) == 1:
            comma_parts = _split_roll20_parts(part, "&#44;")
        if len(comma_parts) == 1:
            value = part.strip()
            if named_option_labels:
                label, option_value = infer_named_condition_option(
                    value,
                    numeric_label_width,
                )
                options.append(QuestionOption(label, option_value))
                repaired = True
            else:
                options.append(QuestionOption(value, ""))
            continue

        label = comma_parts[0].strip()
        value = ",".join(comma_parts[1:]).strip()
        if not label:
            repaired = True
            continue

        if len(comma_parts) >= 3:
            first_value = comma_parts[1].strip()
            remaining_values = [part.strip() for part in comma_parts[2:]]
            dice_match = re.search(
                r"\d+d\d+",
                first_value,
                flags=re.IGNORECASE,
            )
            if not dice_match:
                numeric_label_match = re.fullmatch(
                    r"(\d+)([^\d,]+)",
                    first_value,
                )
                if numeric_label_match:
                    options.append(
                        QuestionOption(label, numeric_label_match.group(1))
                    )
                    options.append(
                        QuestionOption(
                            numeric_label_match.group(2).strip(),
                            ",".join(remaining_values),
                        )
                    )
                    repaired = True
                    continue
            if dice_match:
                first_roll = first_value[:dice_match.end()].strip()
                next_label = first_value[dice_match.end():].strip()
                if (
                    first_roll
                    and next_label
                    and re.fullmatch(r"[^\d,]+", next_label)
                    and all(remaining_values)
                ):
                    options.append(QuestionOption(label, first_roll))
                    options.append(
                        QuestionOption(
                            next_label,
                            ",".join(remaining_values),
                        )
                    )
                    repaired = True
                    continue

            next_value = ",".join(remaining_values)
            if (
                first_value.isdigit()
                and re.match(r"\d+d\d+", next_value, flags=re.IGNORECASE)
            ):
                if len(first_value) > 1:
                    first_option_value = first_value[:-1]
                    next_label = first_value[-1]
                else:
                    first_option_value = first_value
                    next_label = "x"
                options.append(
                    QuestionOption(label, first_option_value)
                )
                options.append(
                    QuestionOption(next_label, next_value)
                )
                repaired = True
                continue

            if (
                first_value.isdigit()
                and len(first_value) > 1
                and all(value.isdigit() for value in remaining_values)
            ):
                options.append(
                    QuestionOption(label, first_value[:-1])
                )
                options.append(
                    QuestionOption(
                        first_value[-1],
                        ",".join(remaining_values),
                    )
                )
                repaired = True
                continue

            if first_value and all(remaining_values):
                options.append(QuestionOption(label, first_value))
                options.append(
                    QuestionOption(
                        "x",
                        ",".join(remaining_values),
                    )
                )
                repaired = True
                continue

        left_brackets = len(value) - len(value.lstrip("["))
        right_brackets = len(value) - len(value.rstrip("]"))
        if left_brackets or right_brackets:
            if left_brackets >= 2 and right_brackets >= 2:
                value = value[2:-2].strip()
            else:
                value = value[left_brackets:len(value) - right_brackets if right_brackets else None].strip()
                repaired = True

        options.append(QuestionOption(label, value))

    return name, options, repaired


def extract_roll20_question_names(text: str) -> list[str]:
    names = []
    for component in split_roll20_components(text):
        parsed = parse_roll20_question(component)
        if not parsed:
            continue

        name, options, _ = parsed
        names.append(unescape(name).strip().casefold())
        for option in options:
            names.extend(extract_roll20_question_names(option.value))
    return [name for name in names if name]


def split_roll20_components(expression: str) -> list[str]:
    expression, _ = close_advanced_questions_before_outer_pipe(expression)
    components = []
    start = 0
    index = 0
    question_depth = 0
    roll_depth = 0

    while index < len(expression):
        if question_depth and expression.startswith("+?{", index):
            component = expression[start:index].strip()
            if component:
                components.append(component)
            index += 1
            start = index
            question_depth = 0
            roll_depth = 0
        elif expression.startswith("?{", index):
            question_depth += 1
            index += 2
        elif expression.startswith("&#125;", index) and question_depth:
            question_depth -= 1
            index += len("&#125;")
        elif expression[index] == "}" and question_depth:
            question_depth -= 1
            index += 1
        elif not question_depth and expression.startswith("[[", index):
            roll_depth += 1
            index += 2
        elif not question_depth and expression.startswith("]]", index) and roll_depth:
            roll_depth -= 1
            index += 2
        elif not question_depth and not roll_depth and expression[index] == "+":
            component = expression[start:index].strip()
            if component:
                components.append(component)
            index += 1
            start = index
        else:
            index += 1

    component = expression[start:].strip()
    if component:
        components.append(component)
    return components


def _read_macro_template_group(text: str, cursor: int, name: str):
    prefix = f"{{{{{name}="
    if not text.startswith(prefix, cursor):
        return None

    value_start = cursor + len(prefix)
    index = value_start
    brace_depth = 0
    while index < len(text):
        if brace_depth == 0 and text.startswith("}}", index):
            return text[value_start:index], index + 2
        if text.startswith("&#125;", index) and brace_depth:
            brace_depth -= 1
            index += len("&#125;")
        elif text.startswith("&#123;", index):
            index += len("&#123;")
        elif text[index] == "{":
            brace_depth += 1
            index += 1
        elif text[index] == "}" and brace_depth:
            brace_depth -= 1
            index += 1
        else:
            index += 1
    return None


def _read_bracketed_roll(text: str, cursor: int = 0):
    if not text.startswith("[[", cursor):
        return None

    index = cursor + 2
    roll_depth = 1
    question_depth = 0
    while index < len(text):
        if text.startswith("?{", index):
            question_depth += 1
            index += 2
        elif text.startswith("&#125;", index) and question_depth:
            question_depth -= 1
            index += len("&#125;")
        elif text[index] == "}" and question_depth:
            question_depth -= 1
            index += 1
        elif not question_depth and text.startswith("[[", index):
            roll_depth += 1
            index += 2
        elif not question_depth and text.startswith("]]", index):
            roll_depth -= 1
            if roll_depth == 0:
                return text[cursor + 2:index], index + 2
            index += 2
        else:
            index += 1
    return None


def _read_roll20_question(text: str, cursor: int = 0):
    if not text.startswith("?{", cursor):
        return None

    index = cursor + 2
    depth = 1
    while index < len(text):
        if text.startswith("?{", index):
            depth += 1
            index += 2
        elif text.startswith("&#125;", index):
            depth -= 1
            index += len("&#125;")
            if depth == 0:
                return text[cursor:index], index
        elif text[index] == "{":
            depth += 1
            index += 1
        elif text[index] == "}":
            depth -= 1
            index += 1
            if depth == 0:
                return text[cursor:index], index
        else:
            index += 1
    return None


def _normalize_character_attribute_refs(text: str, character_name: str) -> str:
    if not character_name:
        return text
    pattern = (
        r"@\{"
        + re.escape(character_name)
        + r"\|([^{}|]+)\}"
    )
    return re.sub(pattern, r"@{\1}", text)


def parse_generated_macro(text: str):
    source = (text or "").strip()
    prefix = "&{template:t20-attack}"
    if not source.startswith(prefix):
        return None

    cursor = len(prefix)
    character_group = _read_macro_template_group(source, cursor, "character")
    if not character_group:
        return None
    character_value = character_group[0]
    character_match = re.fullmatch(
        r"@\{([^{}|]+)\|character_name\}((?:\r?\n.*)?)",
        character_value,
        flags=re.DOTALL,
    )
    if character_value == "@{character_name}":
        character_name = ""
        character_display = ""
    elif character_match:
        character_name = character_match.group(1)
        character_display = character_match.group(2).lstrip("\r\n")
    else:
        return None
    cursor = character_group[1]

    attack_name = _read_macro_template_group(source, cursor, "attackname")
    if not attack_name:
        return None
    fields = {"attackname": attack_name[0]}
    cursor = attack_name[1]

    for field_name in (
        "attackroll",
        "damageroll",
        "criticaldamageroll",
        "typeofdamage",
    ):
        while cursor < len(source) and source[cursor].isspace():
            cursor += 1
        if source.startswith(f"{{{{{field_name}=", cursor):
            field = _read_macro_template_group(source, cursor, field_name)
            if not field:
                return None
            fields[field_name] = field[0]
            cursor = field[1]

    while cursor < len(source) and source[cursor].isspace():
        cursor += 1
    description_prefix = "{{description="
    if not source.startswith(description_prefix, cursor):
        return None
    description_start = cursor + len(description_prefix)
    if not source.endswith("}}"):
        return None
    fields["description"] = source[description_start:-2]
    fields["character_name"] = character_name
    fields["character_display"] = character_display
    for field_name in ("attackroll", "damageroll", "criticaldamageroll"):
        if field_name in fields:
            fields[field_name] = _normalize_character_attribute_refs(
                fields[field_name],
                character_name,
            )
            fields[field_name] = fields[field_name].replace(
                "@{Ameaça}",
                "20",
            )
    return fields


def _parse_roll_suffix(text: str):
    values = []
    cursor = 0
    while cursor < len(text):
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        if cursor == len(text):
            break
        if text.startswith("[[", cursor):
            parsed_roll = _read_bracketed_roll(text, cursor)
            if not parsed_roll:
                return None
            value, cursor = parsed_roll
            values.append(value)
        elif text.startswith("?{", cursor):
            parsed_question = _read_roll20_question(text, cursor)
            if not parsed_question:
                return None
            value, cursor = parsed_question
            values.append(value)
        else:
            return None
    return values


def _parse_damage_or_critical_group(text: str):
    modifier = f"+{GLOBALMODIFIERS['Concatenaçao de Dano']}"
    parsed_roll = _read_bracketed_roll(text)
    if parsed_roll:
        roll_formula, cursor = parsed_roll
        if roll_formula.endswith(modifier):
            base_formula = roll_formula[:-len(modifier)]
            extras = _parse_roll_suffix(text[cursor:])
            if extras is None:
                return None
            return base_formula, extras

    extras = _parse_roll_suffix(text)
    if extras is None:
        return None
    return "", extras


def _get_damage_extra_strings(values: list[str]) -> list[str]:
    extras = []
    for value in values:
        value = value.strip()
        if not value:
            continue
        if value.startswith("?{") and value.endswith("}"):
            extras.append(value)
        else:
            extras.append(f"[[{value}]]")
    return extras


def render_generated_macro(
    name: str,
    attack: str,
    damage: str,
    critical: str,
    damage_type: str,
    description: str,
    character_display: str = "",
) -> str:
    character = "@{character_name}"
    if character_display:
        character += f"\n{character_display}"
    macro = "&{template:t20-attack}"
    macro += f"{{{{character={character}}}}}"
    macro += f"{{{{attackname={name}}}}}"
    if attack:
        macro += f"{{{{attackroll=[[{attack}]]}}}}"
    if damage:
        macro += f"{{{{damageroll={damage}}}}}"
    if critical:
        macro += f"{{{{criticaldamageroll={critical}}}}}"
    if damage_type:
        macro += f"{{{{typeofdamage={damage_type}}}}}"
    return macro + f"{{{{description={description}}}}}"


def parse_generated_macro_state(text: str):
    fields = parse_generated_macro(text)
    if fields is None:
        return None

    state = {
        "attack_name": fields["attackname"],
        "character_display": fields["character_display"],
        "attack_roll": "",
        "attack_threat": "",
        "attack_skill": "",
        "attack_extras": [],
        "damage": "",
        "damage_additional": "",
        "damage_extras": [],
        "critical": "",
        "damage_type": fields.get("typeofdamage", ""),
        "description": fields["description"],
    }

    if "attackroll" in fields:
        parsed_roll = _read_bracketed_roll(fields["attackroll"])
        modifier = GLOBALMODIFIERS["Concatenaçao de ataque"]
        if not parsed_roll or parsed_roll[1] != len(fields["attackroll"]):
            return None
        attack_formula = parsed_roll[0]
        attack_temp_suffix = "+@{ataquetemp}"
        if not attack_formula.endswith(attack_temp_suffix):
            return None
        attack_core = attack_formula[:-len(attack_temp_suffix)]

        skill_found = False
        for skill, marker in PERICIASATACK.items():
            skill_marker = f"+{marker}"
            marker_index = attack_core.find(skill_marker)
            if marker_index != -1:
                marker_content_start = marker_index + len(skill_marker)
                bracket_end = attack_core.find("]]", marker_content_start)
                if bracket_end == -1:
                    return None
                condition_modifiers = attack_core[
                    marker_content_start:bracket_end
                ].removeprefix("+").split("+")
                if sorted(condition_modifiers) != sorted((
                    GLOBALMODIFIERS["Bonus de Condição"],
                    GLOBALMODIFIERS["Bonus de Condição2"],
                )):
                    return None

                state["attack_skill"] = skill
                base_attack = attack_core[:marker_index]
                extras_text = attack_core[bracket_end + 2:]
                if extras_text.startswith("+"):
                    extras_text = extras_text[1:]
                elif extras_text:
                    return None
                state["attack_extras"] = (
                    split_roll20_components(extras_text)
                    if extras_text
                    else []
                )
                skill_found = True
                break

        if not skill_found:
            return None
        threat_match = re.search(r"cs>(\d+)$", base_attack)
        if threat_match:
            state["attack_threat"] = threat_match.group(1)
            base_attack = base_attack[:threat_match.start()]
        supported_best_die = (
            "?{melhor dado| Sim,2d20kh1|Não,1d20}"
        )
        if base_attack not in (
            "1d20",
            BEST_DIE_FORMULA,
            supported_best_die,
        ):
            return None
        state["attack_roll"] = base_attack
        if len(state["attack_extras"]) > 3:
            return None

    if "damageroll" in fields:
        parsed_damage = _parse_damage_or_critical_group(fields["damageroll"])
        if parsed_damage is None:
            return None
        state["damage"], state["damage_extras"] = parsed_damage
        if len(state["damage_extras"]) > 3:
            return None

    if "criticaldamageroll" in fields:
        parsed_critical = _parse_damage_or_critical_group(
            fields["criticaldamageroll"]
        )
        if parsed_critical is None:
            return None
        state["critical"] = parsed_critical[0]
        expected_critical_extras = [
            simplify_condition_questions(value)
            for value in _get_damage_extra_strings(state["damage_extras"])
        ]
        actual_critical_extras = [
            simplify_condition_questions(value)
            for value in _get_damage_extra_strings(parsed_critical[1])
        ]
        if actual_critical_extras != expected_critical_extras:
            return None

    damage_extra_values = _get_damage_extra_strings(state["damage_extras"])
    attack = build_attack_expression(
        state["attack_roll"],
        state["attack_threat"],
        state["attack_skill"],
        state["attack_extras"],
    )
    damage = build_damage_expression(
        state["damage"],
        damage_extra_values,
    )
    critical_extras = [
        simplify_condition_questions(value)
        for value in damage_extra_values
    ]
    critical = build_critical_expression(
        state["critical"],
        critical_extras,
    )
    return state


@dataclass
class MacroButton:
    text: str
    action: str

    def build(self) -> str:
        return f"[{self.text}]({self.action})"
