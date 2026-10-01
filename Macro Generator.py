import ast
import hashlib
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, messagebox
from dataclasses import dataclass, field
from typing import List
from urllib.request import Request, urlopen


VERSAO = "0.01.5.0"  # 0-Versão oficial. 01-Versão funcional. 5-Teste. 0-Correção.

RELEASE_API_URL = "https://api.github.com/repos/GustavoREX/MacroGenerator/releases/tags/Newest"


# ============================================================
# Auto-Updater
# ============================================================
# O programa continua sendo distribuído como um único .exe.
#
# Durante uma atualização:
#   1. O executável consulta a release do GitHub.
#   2. A nova versão é baixada para LOCALAPPDATA.
#   3. O updater auxiliar, incorporado ao .exe, é extraído
#      para LOCALAPPDATA\MacroGenerator.
#   4. O programa encerra.
#   5. O updater espera o processo terminar e substitui o .exe.
#   6. A nova versão é iniciada.
#
# Estou tentando retirar o PowerShell da jogada para tentar evitar que o Windows Defender bloqueie a atualização.
# ============================================================


def parse_version(version: str) -> tuple[int, ...] | None:
    if not re.fullmatch(r"\d+(?:\.\d+)+", version):
        return None
    return tuple(int(part) for part in version.split("."))


def get_update_directory() -> str:
    local_app_data = os.environ.get("LOCALAPPDATA")
    if not local_app_data:
        local_app_data = os.path.expanduser("~")

    directory = os.path.join(local_app_data, "MacroGenerator")
    os.makedirs(directory, exist_ok=True)
    return directory


def get_bundled_updater() -> str | None:
    if not getattr(sys, "frozen", False):
        return None

    meipass = getattr(sys, "_MEIPASS", None)
    if not meipass:
        return None

    updater = os.path.join(meipass, "updater.exe")
    return updater if os.path.isfile(updater) else None


def update_frozen_app() -> bool:
    if not getattr(sys, "frozen", False) or sys.platform != "win32":
        return False

    events = queue.Queue()
    executable_path = os.path.abspath(sys.executable)
    executable_folder = os.path.dirname(executable_path)
    update_directory = get_update_directory()

    downloaded_file = None
    install_requested = False

    def check_for_update():
        try:
            request = Request(
                RELEASE_API_URL,
                headers={"User-Agent": "MacroGenerator-Updater"},
            )

            with urlopen(request, timeout=10) as response:
                release = json.load(response)

            current_version = parse_version(VERSAO)

            asset = next(
                (
                    item
                    for item in release.get("assets", [])
                    if re.search(
                        r"\.V(\d+(?:\.\d+)+)\.exe$",
                        item.get("name", ""),
                        re.IGNORECASE,
                    )
                ),
                None,
            )

            if not current_version or not asset:
                events.put(
                    (
                        "finished",
                        ("error", "Não foi possível ler a versão da release."),
                    )
                )
                return

            version_match = re.search(
                r"\.V(\d+(?:\.\d+)+)\.exe$",
                asset["name"],
                re.IGNORECASE,
            )

            latest_version = (
                parse_version(version_match.group(1))
                if version_match
                else None
            )

            if not latest_version or latest_version <= current_version:
                events.put(("finished", "current"))
                return

            events.put(
                ("available", asset, version_match.group(1))
            )

        except (
            OSError,
            ValueError,
            KeyError,
            TypeError,
            json.JSONDecodeError,
        ) as error:
            events.put(("finished", ("error", str(error))))

    def download_update(asset):
        temporary_path = None

        try:
            # O download fica fora da pasta do executável.
            final_path = os.path.join(
                update_directory,
                asset["name"],
            )
            temporary_path = final_path + ".download"

            if os.path.exists(temporary_path):
                os.remove(temporary_path)

            events.put(
                (
                    "download",
                    asset.get("size", 0),
                    asset["name"],
                )
            )

            digest = hashlib.sha256()
            downloaded = 0

            request = Request(
                asset["browser_download_url"],
                headers={"User-Agent": "MacroGenerator-Updater"},
            )

            with (
                urlopen(request, timeout=60) as response,
                open(temporary_path, "wb") as output,
            ):
                while chunk := response.read(256 * 1024):
                    output.write(chunk)
                    digest.update(chunk)
                    downloaded += len(chunk)
                    events.put(("progress", downloaded))

            expected_digest = asset.get("digest", "")

            if expected_digest.startswith("sha256:"):
                expected_hash = expected_digest.removeprefix(
                    "sha256:"
                ).lower()

                if digest.hexdigest().lower() != expected_hash:
                    raise ValueError(
                        "A verificação do arquivo baixado falhou."
                    )

            elif downloaded != asset.get("size", downloaded):
                raise ValueError(
                    "O download do arquivo ficou incompleto."
                )

            events.put(
                (
                    "finished",
                    ("update", temporary_path),
                )
            )

            temporary_path = None

        except (
            OSError,
            ValueError,
            KeyError,
            TypeError,
            json.JSONDecodeError,
        ) as error:
            events.put(("finished", ("error", str(error))))

        finally:
            if temporary_path and os.path.exists(temporary_path):
                try:
                    os.remove(temporary_path)
                except OSError:
                    pass

    window = tk.Tk()
    window.title("Macro Generator - Atualizador")
    window.geometry("410x155")
    window.resizable(False, False)
    window.attributes("-topmost", True)

    status_label = ttk.Label(
        window,
        text="Iniciando verificação...",
        anchor="center",
    )
    status_label.pack(
        fill="x",
        padx=18,
        pady=(18, 10),
    )

    progress_bar = ttk.Progressbar(
        window,
        mode="indeterminate",
        maximum=100,
    )
    progress_bar.pack(
        fill="x",
        padx=18,
        pady=(0, 10),
    )
    progress_bar.start(12)

    button_frame = ttk.Frame(window)
    button_frame.pack(
        fill="x",
        padx=18,
        pady=(0, 14),
    )

    def close_updater(install=False):
        nonlocal install_requested
        install_requested = install
        window.destroy()

    install_button = ttk.Button(
        button_frame,
        text="Instalar e reiniciar",
        command=lambda: close_updater(install=True),
    )

    later_button = ttk.Button(
        button_frame,
        text="Agora não",
        command=close_updater,
    )

    def begin_download(asset):
        status_label.configure(
            text=f"Baixando {asset['name']}..."
        )

        progress_bar.stop()
        progress_bar.configure(
            mode="determinate",
            maximum=max(asset.get("size", 0), 1),
            value=0,
        )

        threading.Thread(
            target=download_update,
            args=(asset,),
            daemon=True,
        ).start()

    def center_window():
        window.update_idletasks()

        x = (
            window.winfo_screenwidth()
            - window.winfo_width()
        ) // 2

        y = (
            window.winfo_screenheight()
            - window.winfo_height()
        ) // 2

        window.geometry(f"+{x}+{y}")

    def check_events():
        nonlocal downloaded_file

        try:
            while True:
                event = events.get_nowait()

                if event[0] == "available":
                    _, asset, latest_version = event

                    progress_bar.stop()
                    progress_bar.configure(
                        mode="determinate",
                        value=0,
                    )

                    should_download = messagebox.askyesno(
                        "Atualização disponível",
                        (
                            f"A versão {latest_version} está disponível.\n\n"
                            "Deseja baixar agora?"
                        ),
                        parent=window,
                    )

                    if should_download:
                        begin_download(asset)
                    else:
                        status_label.configure(
                            text=(
                                "Download cancelado. "
                                "Abrindo a versão atual..."
                            )
                        )

                        window.after(
                            500,
                            window.destroy,
                        )
                        return

                elif event[0] == "download":
                    _, total_size, file_name = event

                    status_label.configure(
                        text=f"Baixando {file_name}"
                    )

                    progress_bar.stop()
                    progress_bar.configure(
                        mode="determinate",
                        maximum=max(total_size, 1),
                        value=0,
                    )

                elif event[0] == "progress":
                    progress_bar.configure(
                        value=event[1]
                    )

                elif event[0] == "finished":
                    result = event[1]

                    if (
                        isinstance(result, tuple)
                        and result[0] == "update"
                    ):
                        # Guardamos somente o arquivo baixado.
                        # O destino final será decidido pelo updater.
                        downloaded_file = result[1]

                        status_label.configure(
                            text=(
                                "Download concluído. "
                                "Instalar e reiniciar o programa?"
                            )
                        )

                        progress_bar.configure(
                            value=progress_bar.cget("maximum")
                        )

                        install_button.pack(
                            side="left",
                            expand=True,
                            padx=(0, 6),
                        )

                        later_button.pack(
                            side="left",
                            expand=True,
                            padx=(6, 0),
                        )

                        return

                    if result == "current":
                        status_label.configure(
                            text=(
                                "Versão atualizada. "
                                "Abrindo programa..."
                            )
                        )
                    else:
                        status_label.configure(
                            text=(
                                "Falha ao atualizar. "
                                "Abrindo a versão atual..."
                            )
                        )

                    window.after(
                        500,
                        window.destroy,
                    )
                    return

        except queue.Empty:
            pass

        window.after(
            100,
            check_events,
        )

    center_window()

    window.protocol(
        "WM_DELETE_WINDOW",
        close_updater,
    )

    status_label.configure(
        text="Verificando versão..."
    )

    threading.Thread(
        target=check_for_update,
        daemon=True,
    ).start()

    window.after(
        100,
        check_events,
    )

    window.mainloop()

    if not downloaded_file or not install_requested:
        if downloaded_file:
            try:
                os.remove(downloaded_file)
            except OSError:
                pass

        return False

    updater_source = get_bundled_updater()

    if not updater_source:
        try:
            os.remove(downloaded_file)
        except OSError:
            pass

        messagebox.showerror(
            "Atualização",
            (
                "O componente de atualização não está "
                "presente nesta versão do programa."
            ),
        )
        return False

    updater_path = os.path.join(
        update_directory,
        "updater.exe",
    )

    updater_staging = updater_path + ".new"

    try:
        # Copia o updater incorporado para LOCALAPPDATA.
        # Ele permanece lá para as próximas atualizações.
        shutil.copy2(
            updater_source,
            updater_staging,
        )

        os.replace(
            updater_staging,
            updater_path,
        )

        subprocess.Popen(
            [
                updater_path,
                executable_path,
                downloaded_file,
                str(os.getpid()),
            ],
            cwd=update_directory,
            close_fds=True,
        )

        return True

    except OSError as error:
        for path in (
            downloaded_file,
            updater_staging,
        ):
            try:
                os.remove(path)
            except OSError:
                pass

        messagebox.showerror(
            "Atualização",
            f"Não foi possível iniciar a atualização:\n\n{error}",
        )

        return False



# ============================================================
# Roll20 Macro Builder
# ============================================================
# Gerador simples e extensível de macros de ataque para Roll20.
#
# A ideia é permitir montar macros sem precisar digitar
# manualmente os comandos mais comuns, e auxiliar nos mais complexos.
# ============================================================


# ------------------------------------------------------------
# Biblioteca geral de atributos da ficha
# ------------------------------------------------------------
ATTRIBUTES = {
    "Força": "@{for_mod}",
    "Destreza": "@{des_mod}",
    "Constituição": "@{con_mod}",
    "Inteligência": "@{int_mod}",
    "Sabedoria": "@{sab_mod}",
    "Carisma": "@{car_mod}",
}
COMMON_WEAPONS = {
    "Arco Longo": {
        "threat": "20",
        "skill": "Pontaria",
        "damage": "1d8",
        "attributes": (),
        "critical_multiplier": "3",
        "damage_type": "Perfurante",
    },
    "Espada Longa": {
        "threat": "19",
        "skill": "Luta",
        "damage": "?{estilo|uma mão,1d8|duas mãos,1d10}",
        "attributes": ("Força",),
        "critical_multiplier": "2",
        "damage_type": "Corte",
    },
    "Machado de Guerra": {
        "threat": "20",
        "skill": "Luta",
        "damage": "1d12",
        "attributes": ("Força",),
        "critical_multiplier": "3",
        "damage_type": "Corte",
    },
    "Martelo de Guerra": {
        "threat": "20",
        "skill": "Luta",
        "damage": "1d8",
        "attributes": ("Força",),
        "critical_multiplier": "3",
        "damage_type": "Esmagamento",
    },
    "Montante": {
        "threat": "19",
        "skill": "Luta",
        "damage": "2d6",
        "attributes": ("Força",),
        "critical_multiplier": "2",
        "damage_type": "Corte",
    },
}
GLOBALMODIFIERS = {
    "Bonus de Ataque": "@{ataquetemp}",
    "Bonus de Condição": "@{condicaomodataque}",    
    "Bonus de Condição2": "@{condicaomodataquecc}",
    "Bonus dano Temporario":"@{danotemp}",
    "Bonus Rolagem":"@{rolltemp}",
    "Concatenaçao de ataque":"@{condicaomodataque}+@{condicaomodataquecc}]]+@{ataquetemp}",
    "Concatenaçao de Dano":"@{danotemp}+@{rolltemp}"
}
PERICIASATACK = {
    "Luta":"[[@{lutatotal}",
    "Pontaria":"[[@{pontariatotal}",
    "Atuação":"[[@{atuacaototal}",
    "Furtividade":"[[@{furtividadetotal}"
}
DADOSCOMUNS = {
    "d4": "1d4",
    "d6": "1d6",
    "d8": "1d8",
    "d10": "1d10",
    "d12": "1d12",
    "2d6": "2d6",
}

DADOSEXOTICOS = {
    "Min": "1d1",
    "d2": "1d2",
    "d3": "1d3",
    "2d4": "2d4",
    "3d4": "3d4",
    "3d6": "3d6",
    "2d8": "2d8",
    "2d10": "2d10",
    "4d6": "4d6",
    "4d8": "4d8",
    "3d10": "3d10",
    "4d10": "4d10",
    "Max": "4d12",
}

DADOSPADRAO = {
    "Comuns": DADOSCOMUNS,
    "Exóticos": DADOSEXOTICOS,
}

DAMAGE_STEP_TRACKS = {
    "Padrão": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "1d8", "1d10", "1d12",
        "3d6", "4d6", "4d8", "4d10", "4d12"
    ),
    "Especial: 2d4": ("1d1", "1d2", "1d3", "1d4","1d6", "2d4", "1d10","1d12",
        "3d6", "4d6", "4d8", "4d10", "4d12"),
    "Especial: 2d8": ("1d1", "1d2", "1d3", "1d4", "1d6", "1d8","1d10", "2d6", "2d8", "3d8", "4d8", "4d10", "4d12",
    ),
    "Especial: 3d4": ("1d1", "1d2", "1d3", "1d4", "1d6", "1d8","1d10", "3d4", "3d6", "4d6", "4d8", "4d10", "4d12"),
    "Especial: 2d10": ("1d1", "1d2", "1d3", "1d4", "1d6", "1d8","1d10", "2d6","2d8", "2d10", "3d10", "4d10", "4d12"),
}

DAMAGE_SPECIAL_TRACK_BY_DIE = {
    "2d4": "Especial: 2d4",
    "2d6": "Especial: 2d8",
    "3d4": "Especial: 3d4",
    "2d8": "Especial: 2d10",
    "2d10": "Especial: 2d10",
    "3d10": "Especial: 2d10",
}
BEST_DIE_FORMULA = "?{melhor dado|Não,1d20|Sim,2d20kh1}"
MACRO_BUTTON_PATTERN = re.compile(
    r"\[([^\]\r\n]+)\]\(~@\{character_name\}\|([^\)\r\n]+)\)",
    flags=re.IGNORECASE,
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
            if formula[end] == "|" and depth == 1 and pipe == -1:
                pipe = end
            elif formula[end] == "{":
                depth += 1
            elif formula[end] == "}":
                depth -= 1
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


def build_damage_roll_formula(base_formula: str, attributes: list[str] | None = None) -> str:
    formula = join_formula_parts(base_formula, *(attributes or []))
    if formula:
        formula += f"+{GLOBALMODIFIERS['Concatenaçao de Dano']}"
    return formula


def build_damage_expression(
    base_formula: str,
    extra_values: list[str] | None = None,
    attributes: list[str] | None = None,
) -> str:
    formula = build_damage_roll_formula(base_formula, attributes)
    return build_roll_expression(formula, extra_values)


def build_critical_expression(
    base_formula: str,
    extra_values: list[str] | None = None,
    attributes: list[str] | None = None,
) -> str:
    formula = build_damage_roll_formula(base_formula, attributes)
    return build_roll_expression(formula, extra_values)


def build_roll_expression(formula: str, extra_values: list[str] | None = None) -> str:
    expression = f"[[{formula}]]" if formula else ""
    extras = "+".join(value for value in (extra_values or []) if value)
    if expression and extras:
        return f"{expression}+{extras}"
    return expression or extras


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
            parts, end = parse_preview_question(formula, start)
            if parts and len(parts) > 1:
                _, separator, value = parts[1].partition(",")
                if separator:
                    choices.setdefault(parts[0], value)
            cursor = start + 2
    return choices


def select_first_preview_options(formula: str, choices: dict[str, str] | None = None) -> str:
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

    def replace_attribute(match):
        return "0"

    preview = re.sub(r"@\{([^}]+)\}", replace_attribute, preview)
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


@dataclass
class QuestionOption:
    label: str
    value: str


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
        value = option.value.strip()
        if value and wrap_values:
            value = f"[[{value}]]"
        elif not value:
            value = " "
        parts.append(f"|{option.label},{value}")
    parts.append("}")
    return "".join(parts)


@dataclass
class MacroButton:
    text: str
    action: str

    def build(self) -> str:
        return f"[{self.text}]({self.action})"


class MacroBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roll20 Macro Builder")
        self.root.geometry("1100x720")
        self.root.minsize(950, 620)

        self.setup_style()
        self.build_ui()
        self.update_preview()

    # ========================================================
    # Interface
    # ========================================================

    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))
        style.configure("Section.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Small.TLabel", font=("Segoe UI", 9))
        style.configure("DamageStep.TButton", font=("Segoe UI", 18, "bold"), padding=(18, 12))
        style.configure("DamageDie.TButton", padding=(4, 5))

    def build_ui(self):
        # ----------------------------------------------------
        # Topo
        # ----------------------------------------------------
        header = ttk.Frame(self.root, padding=(12, 10))
        header.pack(fill="x")

        ttk.Label(
            header,
            text="Roll20 Macro Builder",
            style="Title.TLabel"
        ).pack(side="left")

        ttk.Label(
            header,
            text= "V"+VERSAO,
            style="Small.TLabel"
        ).pack(side="left", padx=(12, 0))

        # ----------------------------------------------------
        # Nome da macro
        # ----------------------------------------------------
        name_frame = ttk.Frame(self.root, padding=(12, 0, 12, 8))
        name_frame.pack(fill="x")

        ttk.Label(name_frame, text="Nome do ataque:").pack(side="left")

        self.attack_name_var = tk.StringVar(value="Nome Ataque")
        name_entry = ttk.Entry(
            name_frame,
            textvariable=self.attack_name_var,
            width=45
        )
        name_entry.pack(side="left", padx=(8, 0))
        name_entry.bind("<KeyRelease>", lambda e: self.update_preview())

        # ----------------------------------------------------
        # Corpo principal
        # ----------------------------------------------------
        body = ttk.PanedWindow(self.root, orient="horizontal")
        body.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # Painel esquerdo - componentes
        left = ttk.Frame(body, padding=8)
        body.add(left, weight=1)

        # Painel central - campos
        center = ttk.Frame(body, padding=8)
        body.add(center, weight=2)

        # Painel direito - preview
        right = ttk.Frame(body, padding=8)
        body.add(right, weight=3)

        self.build_component_panel(left)
        self.build_editor_panel(center)
        self.build_preview_panel(right)

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
            wraplength=190
        ).pack(anchor="w", pady=(0, 12))

        buttons = [
            ("Armas comuns", self.open_common_weapons_dialog),
            ("Calculador de Passos de Dano", self.insert_fixed_bonus),
            ("Pergunta Roll20", self.insert_question),
            ("Botão de macro", self.insert_button),
            ("Código personalizado", self.insert_custom),
        ]

        for text, command in buttons:
            ttk.Button(
                parent,
                text=text,
                command=command
            ).pack(fill="x", pady=3)

        ttk.Separator(parent).pack(fill="x", pady=12)

        ttk.Label(
            parent,
            text="Atributos disponíveis",
            style="Section.TLabel"
        ).pack(anchor="w", pady=(0, 6))

        attr_frame = ttk.Frame(parent)
        attr_frame.pack(fill="x")

        for name, code in ATTRIBUTES.items():
            ttk.Button(
                attr_frame,
                text=name,
                command=lambda c=code: self.insert_text(c)
            ).pack(fill="x", pady=2)

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

        button = ttk.Button(
            section,
            text=f"- {title}" if expanded else f"+ {title}",
            command=toggle,
        )
        button.pack(fill="x")

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

        for idx, var in enumerate(self.attack_extra_vars):
            field_frame = ttk.Frame(self.attack_extra_frame)
            field_frame.grid(
                row=0,
                column=idx,
                sticky="ew",
                padx=(0, 6),
            )
            ttk.Entry(
                field_frame,
                textvariable=var,
                width=20,
            ).pack(fill="x")
            ttk.Button(
                field_frame,
                text="Condicional?",
                command=lambda index=idx: self.insert_attack_conditional(index),
            ).pack(fill="x", pady=(3, 0))
            var.trace_add("write", lambda *_: self.update_preview())

        for idx in range(len(self.attack_extra_vars)):
            self.attack_extra_frame.columnconfigure(idx, weight=1)

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
            sticky="w"
        )

        for attribute in [
            "Luta",
            "Pontaria",
            "Atuação",
            "Furtividade"
        ]:
            ttk.Radiobutton(
                attribute_frame,
                text=attribute,
                variable=self.attack_attribute_var,
                value=attribute
            ).pack(
                side="left",
                padx=(0, 8)
            )

        self.attack_attribute_var.trace_add(
            "write",
            lambda *_: self.update_preview()
        )

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

        for index, (label, value) in enumerate(DADOSCOMUNS.items()):
            ttk.Button(
                common_dice_frame,
                text=label,
                width=6,
                command=lambda v=value: self.add_to_entry(
                    self.damage_entry,
                    self.damage_var,
                    v
                )
            ).grid(
                row=0,
                column=index,
                sticky="w",
                padx=(0, 4),
                pady=2
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
        for index, (label, value) in enumerate(exotic_values):
            ttk.Button(
                self.damage_exotic_frame,
                text=label,
                width=6,
                command=lambda v=value: self.add_to_entry(
                    self.damage_entry,
                    self.damage_var,
                    v
                )
            ).grid(
                row=index // 7,
                column=index % 7,
                sticky="w",
                padx=(0, 4),
                pady=2
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
            sticky="w"
        )

        for attribute in ATTRIBUTES.keys():
            ttk.Checkbutton(
                damage_attr_frame,
                text=attribute,
                variable=self.damage_attribute_vars[attribute],
            ).pack(side="left", padx=(0, 8), anchor="w")

        for attribute_var in self.damage_attribute_vars.values():
            attribute_var.trace_add("write", lambda *_: self.update_preview())

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

        for idx, var in enumerate(self.damage_extra_vars):
            field_frame = ttk.Frame(self.damage_extra_frame)
            field_frame.grid(
                row=0,
                column=idx,
                sticky="ew",
                padx=(0, 6)
            )
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

        for idx in range(len(self.damage_extra_vars)):
            self.damage_extra_frame.columnconfigure(idx, weight=1)

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

    def build_preview_panel(self, parent):
        ttk.Label(
            parent,
            text="Macro gerada",
            style="Section.TLabel"
        ).pack(anchor="w", pady=(0, 8))

        preview_split = ttk.PanedWindow(parent, orient="vertical")
        preview_split.pack(fill="both", expand=True)

        macro_panel = ttk.Frame(preview_split)
        card_panel = ttk.Frame(preview_split)
        preview_split.add(macro_panel, weight=3)
        preview_split.add(card_panel, weight=2)

        self.preview = tk.Text(
            macro_panel,
            wrap="char",
            font=("Consolas", 10)
        )
        self.preview.pack(
            fill="both",
            expand=True
        )

        card_toolbar = ttk.Frame(card_panel)
        card_toolbar.pack(fill="x", pady=(8, 4))
        ttk.Label(
            card_toolbar,
            text="Prévia do Roll20",
            style="Section.TLabel",
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
            background="#d3e5f5",
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
            text="Atualizar",
            command=self.update_preview
        ).pack(side="left")

        ttk.Button(
            bottom,
            text="Copiar macro",
            command=self.copy_macro
        ).pack(side="left", padx=6)

        ttk.Button(
            bottom,
            text="Limpar",
            command=self.clear_all
        ).pack(side="right")

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
        damage_choices = get_preview_question_choices(
            damage_formula,
            *damage_extras,
        )
        damage_base_formula = build_damage_roll_formula(
            damage_formula,
            damage_attributes,
        )

        critical_var = getattr(self, "critical_var", None)
        critical_formula = critical_var.get().strip() if critical_var else ""
        critical_extras = [
            simplify_condition_questions(value)
            for value in damage_extras
        ]
        critical_base_formula = build_damage_roll_formula(
            critical_formula,
            damage_attributes if critical_formula else [],
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

    def draw_roll_preview(self):
        canvas = getattr(self, "roll_preview_canvas", None)
        if canvas is None or not canvas.winfo_exists():
            return

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
            fill="white",
            outline="",
        )

        def add_text(text, x, y, wrap_width, font, fill="#111111", justify="center"):
            item = canvas.create_text(
                x,
                y,
                text=text,
                width=wrap_width,
                font=font,
                fill=fill,
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
        def add_roll_box(text, center, y, max_width, fill="#FEF68E", outline="#d69e00"):
            text_item = canvas.create_text(
                center,
                y + 5,
                text=text,
                width=max_width - 12,
                font=("Helvetica Neue", 15, "bold"),
                fill="#111111",
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
                fill=fill,
                outline=outline,
                width=1,
            )
            canvas.tag_raise(text_item, box)
            return box_bottom

        attack_fill = "#ffcc80" if data["critical"] else "#FEF68E"
        attack_outline = "#3fb315" if data["critical"] else "#d69e00"
        attack_bottom = add_roll_box(
            data["attack"],
            left_center,
            content_y,
            column_width - 8,
            fill=attack_fill,
            outline=attack_outline,
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
                fill="#111111",
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
                fill="#FEF68E",
                outline="#d69e00",
                width=1,
            )
            probe = canvas.create_text(
                damage_x + box_width / 2,
                damage_y + 6,
                text=roll_value,
                width=box_width - 14,
                font=("Helvetica Neue", 15, "bold"),
                fill="#111111",
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
            fill="#111111",
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
            fill="#287a38" if data["critical"] else "#111111",
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
                fill="#fdf8ab",
                outline="",
            )
            text_font = tkfont.Font(root=canvas, font=("Helvetica Neue", 10))
            button_font = tkfont.Font(root=canvas, font=("Helvetica Neue", 10, "bold"))
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
                        if button_bounds else base_line_height + 4,
                    )
                    if cursor_x + button_width > content_right and cursor_x > content_left:
                        next_description_line()
                    button_top = cursor_y - 2
                    button_background = canvas.create_rectangle(
                        cursor_x,
                        button_top,
                        cursor_x + button_width,
                        button_top + button_height,
                        fill="#d80b9b",
                        outline="#d80b9b",
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

                segments = value.replace("\r\n", "\n").replace("\r", "\n").split("\n")
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
                        if cursor_x + token_width > content_right and cursor_x > content_left:
                            next_description_line()
                        text_item = canvas.create_text(
                            cursor_x,
                            cursor_y,
                            text=token,
                            font=("Helvetica Neue", 10),
                            fill="#111111",
                            anchor="nw",
                        )
                        bounds = canvas.bbox(text_item)
                        if bounds:
                            row_height = max(row_height, bounds[3] - cursor_y)
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
        )

        critical_var = getattr(self, "critical_var", None)
        critical_formula = critical_var.get().strip() if critical_var else ""
        critical_extra_values = [
            simplify_condition_questions(value)
            for value in extra_values
        ]
        critical = build_critical_expression(
            critical_formula,
            critical_extra_values,
            damage_attributes if critical_formula else [],
        )

        damage_type_var = getattr(self, "damage_type_var", None)
        damage_type = damage_type_var.get().strip() if damage_type_var else ""

        description = self.get_description()

        macro = (
            "&{template:t20-attack}"
            "{{character=@{character_name}}}"
            f"{{{{attackname={name}}}}}"
        )

        if attack:
            macro += f"{{{{attackroll=[[{attack}]]}}}}"

        if damage:
            macro += f"{{{{damageroll={damage}}}}}"

        if critical:
            macro += f"{{{{criticaldamageroll={critical}}}}}"

        if damage_type:
            macro += f"{{{{typeofdamage={damage_type}}}}}"

        macro += f"{{{{description={description}}}}}"

        return macro

    def update_preview(self):
        if not hasattr(self, "preview"):
            return

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

        if isinstance(widget, tk.Entry) and widget.cget("state") != "readonly":
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
        win.geometry("320x300")
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Escolha uma arma:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 8))

        for weapon_name in COMMON_WEAPONS:
            ttk.Button(
                win,
                text=weapon_name,
                command=lambda name=weapon_name: self.apply_common_weapon(
                    name,
                    win,
                ),
            ).pack(fill="x", padx=15, pady=3)

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
        win.geometry("760x400")
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

        for column in range(7):
            dice_frame.columnconfigure(column, weight=1)

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
        )

    def insert_question(
        self,
        target_var=None,
        conditional=False,
        wrap_conditional_values=True,
    ):
        win = tk.Toplevel(self.root)
        win.title("Condição" if conditional else "Pergunta Roll20")
        win.geometry("500x430")
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Nome da condição:" if conditional else "Nome da pergunta:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 4))

        name_var = tk.StringVar(value="Condição" if conditional else "Pergunta")

        ttk.Entry(
            win,
            textvariable=name_var
        ).pack(fill="x", padx=15)

        ttk.Label(
            win,
            text="Opções (nome = valor):",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(12, 4))

        options_frame = ttk.Frame(win)
        options_frame.pack(fill="both", expand=True, padx=15)

        rows = []

        def add_row(label="", value=""):
            row = ttk.Frame(options_frame)
            row.pack(fill="x", pady=2)

            label_var = tk.StringVar(value=label)
            value_var = tk.StringVar(value=value)

            ttk.Entry(
                row,
                textvariable=label_var,
                width=22
            ).pack(side="left", fill="x", expand=True)

            ttk.Entry(
                row,
                textvariable=value_var,
                width=18
            ).pack(side="left", padx=(5, 0))

            rows.append((label_var, value_var))

        add_row("SIM", "1")
        add_row("NÃO", "0")

        ttk.Button(
            win,
            text="+ Adicionar opção",
            command=add_row
        ).pack(pady=5)

        def insert():
            name = name_var.get().strip()
            options = []

            for label_var, value_var in rows:
                label = label_var.get().strip()
                value = value_var.get().strip()

                if label:
                    options.append(QuestionOption(label, value))

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
        win.geometry("500x240")
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

    def insert_custom(self):
        win = tk.Toplevel(self.root)
        win.title("Código personalizado")
        win.geometry("600x300")
        win.transient(self.root)
        win.grab_set()

        ttk.Label(
            win,
            text="Código Roll20:",
            style="Section.TLabel"
        ).pack(anchor="w", padx=15, pady=(15, 5))

        text = tk.Text(
            win,
            height=10,
            font=("Consolas", 10)
        )
        text.pack(fill="both", expand=True, padx=15)

        def insert():
            value = text.get("1.0", "end-1c")

            if value.strip():
                self.insert_text(value)

            win.destroy()

        ttk.Button(
            win,
            text="Inserir",
            command=insert
        ).pack(pady=10)

        text.focus_set()

    def insert_description_text(self):
        win = tk.Toplevel(self.root)
        win.title("Texto da descrição")
        win.geometry("500x260")
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