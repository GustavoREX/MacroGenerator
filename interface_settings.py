"""Preferências visuais da tela inicial, separadas dos dados do inventário."""
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile


@dataclass(frozen=True)
class HomeOptions:
    village: bool = True
    effects: bool = True


def default_settings_path():
    return Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'MacroGenerator' / 'interface.json'


class InterfaceSettings:
    def __init__(self, path=None):
        self.path = Path(path) if path is not None else None
        self.options = HomeOptions()
        if self.path is not None:
            try:
                data = json.loads(self.path.read_text(encoding='utf-8'))
                if not isinstance(data, dict):
                    return
                self.options = HomeOptions(**{key: data[key] if isinstance(data.get(key), bool) else default
                    for key,default in asdict(self.options).items()})
            except (OSError, ValueError):
                pass

    def save(self, options):
        if not isinstance(options.village, bool) or not isinstance(options.effects, bool):
            raise ValueError('As preferências visuais devem ser booleanas.')
        if self.path is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with NamedTemporaryFile(mode='w', encoding='utf-8', dir=self.path.parent,
                                        prefix='interface-', suffix='.tmp', delete=False) as stream:
                    temporary = Path(stream.name)
                    json.dump(asdict(options), stream, ensure_ascii=False, indent=2)
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, self.path)
            finally:
                if temporary is not None and temporary.exists():
                    temporary.unlink()
        self.options = options
