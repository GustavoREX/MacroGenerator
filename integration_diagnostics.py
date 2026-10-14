"""Offline smoke check for both tools in the distributed executable."""
import json
from pathlib import Path
import sys
import traceback


def run_self_test(app_class, destination):
    result = {}
    root = None
    try:
        from PIL import Image
        from constants import VERSAO
        from core.paths import border_paths
        from core.rendering import read_image
        from modes.editor_mode import EditorMode
        from auto_update import get_bundled_updater
        root = app_class()
        root.withdraw()
        errors = []
        root.report_callback_exception = lambda *args: errors.append(str(args))
        root.update()
        root.macro.attack_name_var.set('Teste integrado')
        macro = root.macro.build_macro()
        assert 'Teste integrado' in macro
        root.show_tool('token')
        token = root.token_workspace.current
        token.source_img = Image.new('RGBA', (100, 200), 'red')
        borders = border_paths()
        assert len(borders) >= 320
        token.border_img = read_image(next(iter(borders.values())))
        token.advanced.set(True)
        token.toggle_advanced()
        token.slice_vars[0][0].set(40)
        image = token.make_token(256)
        assert image.size == (256, 256)
        root.token_workspace.show(EditorMode)
        root.token_workspace.current.source_img = token.source_img.copy()
        assert root.token_workspace.current.make_image(256).size == (256, 256)
        root.show_tool('macro')
        root.update()
        assert root.macro.build_macro() == macro
        assert not errors, errors
        updater = get_bundled_updater()
        if getattr(sys, 'frozen', False):
            assert updater and Path(updater).is_file()
        import rembg
        import onnxruntime
        result.update(success=True, version=VERSAO, macro='ok', token='ok', editor='ok',
                      state_preserved=True, border_count=len(borders), ai_imports='ok',
                      bundled_updater=bool(updater))
    except Exception:
        result.update(success=False, error=traceback.format_exc())
    finally:
        if root is not None:
            root.destroy()
    Path(destination).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return 0 if result['success'] else 1
