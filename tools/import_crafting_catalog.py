"""Importa as abas de melhorias, materiais e encantamentos sem alterar a planilha."""
import argparse
from pathlib import Path
from pprint import pformat

from import_weapon_catalog import read_catalog_sheets

CRAFTING_COLUMNS = {
    "Melhorias": dict(name="A", application="B", price="C", description="D", source="E", notes="F"),
    "Materiais": dict(name="A", price="B", weapon_price="C", light_price="D", heavy_price="E",
                      shield_price="F", description="H", source="I", notes="J"),
    "Encantamentos": dict(group="A", name="B", price="C", description="F", source="G", notes="H"),
    "Armaduras e escudos": dict(group="A", name="B", price="C", defense="E", penalty="F",
                               spaces="G", description="H", source="I", notes="J"),
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    data = read_catalog_sheets(args.source, CRAFTING_COLUMNS)
    destination = Path(__file__).resolve().parents[1] / "crafting_data.py"
    destination.write_text(
        '# Dados extraídos de ' + args.source.name + '\n'
        '# Gerado por tools/import_crafting_catalog.py.\n'
        'CRAFTING_DATA = ' + pformat(data, width=100, sort_dicts=False) + '\n', encoding="utf-8")
    print({name: len(rows) for name, rows in data.items()})
