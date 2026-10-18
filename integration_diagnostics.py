"""Offline smoke check for the macro editor, equipment workshops and TokenForge."""
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
        from shopping_core import Inventory, CATALOGS
        root.macro.inventory = Inventory()  # O diagnóstico não altera os dados reais do usuário.
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
        from crafting_core import quote_weapon
        root.show_tool('weapons')
        workshop = root.weapon_workshop
        workshop.owned_var.set(True)
        workshop.old_improvements_var.set('2')
        for name in ('Certeira', 'Cruel', 'Discreto'):
            workshop.improvement_vars[name].set(True)
        workshop.enchantment_vars['Congelante'].set(True)
        workshop.size_var.set('Aumentada')
        workshop.refresh()
        assert quote_weapon(workshop.get_design()).improvement_due == 6000
        workshop.inventory_button.invoke()
        assert len(root.macro.inventory.lines) == 1
        assert root.macro.inventory.lines[0].unit_price == 24000
        workshop.generate_button.invoke()
        assert root.active_tool == 'macro'
        assert root.macro.damage_var.get() == '1d6'
        assert root.macro.damage_type_var.get() == 'Perfuração | Frio'
        assert root.macro.damage_extra_vars[0].get() == '1d6'
        assert '[Frio]' not in root.macro.build_macro()
        root.show_tool('token')
        root.show_tool('weapons')
        assert workshop.enchantment_vars['Congelante'].get()
        root.show_tool('macro')
        root.update()
        root.show_tool('armor')
        armor = root.armor_workshop
        armor.weapon_var.set('Armadura completa')
        armor._weapon_changed()
        armor.material_var.set('Adamante')
        armor.refresh()
        assert armor.result_profile['rd']['geral'] == 5
        assert armor.result_profile['defense_bonus'] == 10
        armor.inventory_button.invoke()
        assert len(root.macro.inventory.lines) == 2
        armor.weapon_var.set('Escudo leve')
        armor._weapon_changed()
        armor.material_var.set('')
        armor.improvement_vars['Reforçada'].set(True)
        armor.enchantment_vars['Defensor'].set(True)
        armor.enchantment_vars['Congelante'].set(True)
        armor.refresh()
        assert armor.result_profile['defense_bonus'] == 4
        armor.inventory_button.invoke()
        assert len(root.macro.inventory.lines) == 3
        armor.generate_button.invoke()
        assert root.active_tool == 'macro'
        assert root.macro.damage_var.get() == '1d4'
        assert root.macro.damage_type_var.get() == 'Impacto | Frio'
        root.show_tool('token')
        root.show_tool('armor')
        assert root.armor_workshop is armor
        assert armor.enchantment_vars['Congelante'].get()
        root.show_tool('shopping')
        shopping = root.shopping_workshop
        assert len(shopping.inventory_tree.get_children()) == 3
        shopping.choose_category('Armas simples')
        shopping.catalog_rows[0][3].invoke()
        assert root.macro.inventory.totals().quantity == 4
        shopping.choose_category('Customizados')
        assert len(shopping.catalog_rows) == 3
        root.show_tool('token')
        root.show_tool('shopping')
        assert root.shopping_workshop is shopping
        assert root.macro.inventory.totals().quantity == 4
        root.show_tool('macro')
        root.update()
        assert not errors, errors
        updater = get_bundled_updater()
        if getattr(sys, 'frozen', False):
            assert updater and Path(updater).is_file()
        import rembg
        import onnxruntime
        result.update(success=True, version=VERSAO, macro='ok', token='ok', editor='ok',
                      state_preserved=True, border_count=len(borders), ai_imports='ok',
                      bundled_updater=bool(updater), workshop='ok', upgrade_price=6000,
                      elemental_damage='ok', armor='ok', shield_attack='ok', shared_shield_limits=True,
                      shopping='ok', shopping_catalog_count=len(CATALOGS),
                      shopping_item_count=sum(map(len, CATALOGS.values())), custom_inventory='ok')
    except Exception:
        result.update(success=False, error=traceback.format_exc())
    finally:
        if root is not None:
            root.destroy()
    Path(destination).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return 0 if result['success'] else 1
