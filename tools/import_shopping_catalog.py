"""Extrai os catálogos de compras da planilha, sem depender de Excel.

Uso: python tools/import_shopping_catalog.py caminho/compilado.xlsx
"""
import argparse
from pathlib import Path
from pprint import pformat

try:
    from .import_weapon_catalog import read_catalog_sheets
except ImportError:
    from import_weapon_catalog import read_catalog_sheets


SIMPLE = dict(name="A", price="B", numeric_price="C", spaces="D", description="E", source="F", notes="G")
GROUPED = dict(group="A", name="B", price="C", numeric_price="D", spaces="E",
               description="F", source="G", notes="H")
WEAPON = dict(group="A", name="B", price="C", numeric_price="D", damage="E", critical="F",
              range="G", damage_type="H", spaces="I", description="J", source="K", notes="L")
SHOPPING_COLUMNS = {
    **{name: WEAPON for name in ("Armas simples", "Armas marciais", "Armas exóticas", "Armas de fogo")},
    "Munições": SIMPLE,
    "Armaduras e escudos": dict(group="A", name="B", price="C", numeric_price="D", defense="E",
                                 penalty="F", spaces="G", description="H", source="I", notes="J"),
    "Aventura": SIMPLE, "Ferramentas": GROUPED, "Vestuário": SIMPLE, "Esotéricos": SIMPLE,
    "Preparados": GROUPED, "Catalisadores": SIMPLE, "Venenos": SIMPLE,
    "Alimentos e bebidas": GROUPED, "Animais e veículos": GROUPED,
    "Serviços e tatuagens": GROUPED, "Aparatos": SIMPLE,
    "Materiais": dict(name="A", price="B", description="H", source="I", notes="J"),
    "Recursos": SIMPLE, "Armas mágicas": SIMPLE, "Armaduras mágicas": SIMPLE,
    "Esotéricos mágicos": SIMPLE, "Acessórios mágicos": SIMPLE, "Itens litúrgicos": SIMPLE,
    "Poções e pergaminhos": GROUPED, "Simbiontes": SIMPLE, "Artefatos": SIMPLE,
}


def read_shopping_sheets(source):
    catalog = read_catalog_sheets(source, SHOPPING_COLUMNS)
    # Adicionais de materiais e maldições são modificadores do criador, não mercadorias.
    # O fardo é a matéria-prima comercial expressamente vendida por unidade na fonte.
    catalog["Materiais"] = [row for row in catalog["Materiais"] if row["name"].startswith("Fardo de ")]
    for row in catalog["Materiais"]:
        row["spaces"] = "2"  # A própria descrição do fardo informa dois espaços.
    return catalog


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    data = read_shopping_sheets(args.source)
    destination = Path(__file__).resolve().parents[1] / "shopping_data.py"
    destination.write_text(
        '# Catálogo extraído de ' + args.source.name + '\n'
        '# Gerado por tools/import_shopping_catalog.py; preserve os textos da fonte.\n'
        'SHOPPING_DATA = ' + pformat(data, width=100, sort_dicts=False) + '\n', encoding="utf-8")
    print(f"{sum(map(len, data.values()))} itens importados em {len(data)} catálogos.")
