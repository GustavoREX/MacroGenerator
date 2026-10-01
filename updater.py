import os
import shutil
import subprocess
import sys
import tempfile
import time
import ctypes
from ctypes import wintypes


SYNCHRONIZE = 0x00100000
WAIT_OBJECT_0 = 0x00000000
ERROR_INVALID_PARAMETER = 87
INFINITE = 0xFFFFFFFF


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

        os.replace(
            temporary_target,
            target,
        )

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
        # O Macro Generator ainda está usando o executável.
        wait_for_process(pid)

        # Agora o executável antigo está liberado.
        replace_executable(
            target,
            staged,
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

        return 0

    except Exception as error:
        print(
            f"Falha na atualização: {error}",
            file=sys.stderr,
        )

        # Tenta abrir a versão antiga se ela ainda existir.
        if os.path.isfile(target):
            try:
                subprocess.Popen(
                    [target],
                    cwd=target_dir,
                    close_fds=True,
                )
            except OSError:
                pass

        return 1


if __name__ == "__main__":
    sys.exit(main())
