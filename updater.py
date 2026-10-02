import os
import shutil
import subprocess
import sys
import tempfile
import time
import ctypes
import hashlib
from ctypes import wintypes


SYNCHRONIZE = 0x00100000
WAIT_OBJECT_0 = 0x00000000
ERROR_INVALID_PARAMETER = 87
INFINITE = 0xFFFFFFFF
REPLACE_RETRY_SECONDS = 30


def write_update_log(message: str) -> None:
    log_path = os.path.join(
        os.path.dirname(os.path.abspath(sys.executable)),
        "updater.log",
    )
    try:
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
    except OSError:
        pass


def show_update_error(message: str) -> None:
    try:
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        user32.MessageBoxW.argtypes = [
            wintypes.HWND,
            wintypes.LPCWSTR,
            wintypes.LPCWSTR,
            wintypes.UINT,
        ]
        user32.MessageBoxW.restype = ctypes.c_int
        user32.MessageBoxW(
            None,
            message,
            "Falha ao atualizar o Macro Generator",
            0x10,
        )
    except (AttributeError, OSError):
        pass


def files_match(first_path: str, second_path: str) -> bool:
    def digest(path: str) -> str:
        checksum = hashlib.sha256()
        with open(path, "rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                checksum.update(chunk)
        return checksum.hexdigest()

    return digest(first_path) == digest(second_path)


def wait_for_process(pid: int) -> None:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

    kernel32.OpenProcess.argtypes = [
        wintypes.DWORD,
        wintypes.BOOL,
        wintypes.DWORD,
    ]
    kernel32.OpenProcess.restype = wintypes.HANDLE

    kernel32.WaitForSingleObject.argtypes = [
        wintypes.HANDLE,
        wintypes.DWORD,
    ]
    kernel32.WaitForSingleObject.restype = wintypes.DWORD

    kernel32.CloseHandle.argtypes = [
        wintypes.HANDLE,
    ]
    kernel32.CloseHandle.restype = wintypes.BOOL

    handle = kernel32.OpenProcess(
        SYNCHRONIZE,
        False,
        pid,
    )

    if not handle:
        error = ctypes.get_last_error()

        # O processo já terminou.
        if error == ERROR_INVALID_PARAMETER:
            return

        raise ctypes.WinError(error)

    try:
        result = kernel32.WaitForSingleObject(
            handle,
            INFINITE,
        )

        if result != WAIT_OBJECT_0:
            raise RuntimeError(
                "Não foi possível aguardar o programa principal."
            )
    finally:
        kernel32.CloseHandle(handle)


def replace_executable(target: str, staged: str) -> None:
    target_dir = os.path.dirname(target)

    fd, temporary_target = tempfile.mkstemp(
        prefix=".MacroGenerator-",
        suffix=".tmp",
        dir=target_dir,
    )

    os.close(fd)

    try:
        # Copiar primeiro para o mesmo diretório do destino.
        # Depois os.replace() faz a troca no mesmo volume.
        shutil.copy2(
            staged,
            temporary_target,
        )

        deadline = time.monotonic() + REPLACE_RETRY_SECONDS
        while True:
            try:
                os.replace(
                    temporary_target,
                    target,
                )
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise
                time.sleep(0.5)

        temporary_target = None

    finally:
        if temporary_target and os.path.exists(
            temporary_target
        ):
            try:
                os.remove(temporary_target)
            except OSError:
                pass


def main() -> int:
    if len(sys.argv) != 4:
        return 2

    target = os.path.abspath(sys.argv[1])
    staged = os.path.abspath(sys.argv[2])

    try:
        pid = int(sys.argv[3])
    except ValueError:
        return 2

    if not os.path.isfile(staged):
        return 3

    target_dir = os.path.dirname(target)

    try:
        write_update_log(
            f"Iniciando troca. destino={target}; staging={staged}; pid={pid}"
        )

        # O Macro Generator ainda está usando o executável.
        wait_for_process(pid)

        # Agora o executável antigo está liberado.
        replace_executable(
            target,
            staged,
        )

        if not files_match(target, staged):
            raise RuntimeError(
                "A verificação do executável instalado não corresponde "
                "ao arquivo baixado."
            )

        # Inicia a versão nova.
        subprocess.Popen(
            [target],
            cwd=target_dir,
            close_fds=True,
        )

        # O arquivo de staging não é mais necessário.
        try:
            os.remove(staged)
        except OSError:
            pass

        write_update_log("Atualização instalada e novo executável iniciado.")
        return 0

    except Exception as error:
        error_message = f"Falha na atualização: {error}"
        write_update_log(error_message)
        show_update_error(
            f"{error_message}\n\n"
            "A versão antiga não foi reiniciada. O arquivo baixado foi "
            "mantido para permitir uma nova tentativa."
        )

        return 1


if __name__ == "__main__":
    sys.exit(main())
