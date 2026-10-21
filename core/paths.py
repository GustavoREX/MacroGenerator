from pathlib import Path
import os
import sys

ROOT = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parents[1]))
APP_DIR = Path(sys.executable).resolve().parent if getattr(sys, 'frozen', False) else ROOT
USER_DIR = Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'TokenForge'


def border_paths():
    """Bordas do usuário têm prioridade sobre as portáteis e as incluídas no programa."""
    found = {}
    for folder in (ROOT / 'borders', APP_DIR / 'borders', USER_DIR / 'borders'):
        if folder.is_dir():
            for path in sorted(folder.iterdir()):
                if path.suffix.lower() in ('.png', '.webp'):
                    found[path.name] = path
    return dict(sorted(found.items(), key=lambda item: item[0].casefold()))
