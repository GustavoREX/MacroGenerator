"""E seguimos tentanto manter o programa autos suficiente e quem tem ele atualizado"""
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
from tkinter import ttk, messagebox
from urllib.request import Request, urlopen
from constants import RELEASE_API_URL, VERSAO
from ui_theme import set_responsive_window_geometry


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
    window.title("Macro x Token - Atualizador")
    set_responsive_window_geometry(window, 410, 155, 320, 130)
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
