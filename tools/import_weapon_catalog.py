"""Importa apenas os dados das abas de armas, sem dependências de Excel.

Uso: python tools/import_weapon_catalog.py caminho/compilado.xlsx
O catálogo Python gerado acompanha também o executável do aplicativo.
"""
import argparse
from pathlib import Path
from pprint import pformat
from xml.etree import ElementTree as ET
from zipfile import ZipFile

NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
SHEETS = ("Armas simples", "Armas marciais", "Armas exóticas",
          "Armas de fogo", "Armas mágicas")


def read_catalog_sheets(source, sheet_columns):
    catalog = {}
    with ZipFile(source) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = ["".join(t.text or "" for t in item.findall(".//s:t", NS))
                       for item in ET.fromstring(archive.read("xl/sharedStrings.xml"))]
        relationships = {rel.attrib["Id"]: rel.attrib["Target"] for rel in
                         ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
        sheets = ET.fromstring(archive.read("xl/workbook.xml")).find("s:sheets", NS)
        for sheet in sheets:
            name = sheet.attrib["name"]
            if name not in sheet_columns:
                continue
            target = relationships[sheet.attrib[
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]]
            path = target.lstrip("/") if target.startswith("/") else "xl/" + target
            rows = ET.fromstring(archive.read(path)).findall("s:sheetData/s:row", NS)
            weapons = []
            for row in rows:
                if int(row.attrib["r"]) < 5:
                    continue
                cells = {}
                for cell in row:
                    value = cell.find("s:v", NS)
                    if cell.attrib.get("t") == "s" and value is not None:
                        text = strings[int(value.text)]
                    elif cell.attrib.get("t") == "inlineStr":
                        text = "".join(t.text or "" for t in cell.findall(".//s:t", NS))
                    else:
                        text = value.text if value is not None else ""
                    column = "".join(c for c in cell.attrib["r"] if c.isalpha())
                    cells[column] = text
                columns = sheet_columns[name]
                weapon = {key: cells.get(column, "") for key, column in columns.items()}
                if weapon["name"]:
                    weapons.append(weapon)
            catalog[name] = weapons
    if set(catalog) != set(sheet_columns):
        raise ValueError("A planilha não contém todas as abas esperadas: "
                         + ", ".join(set(sheet_columns) - set(catalog)))
    return {name: catalog[name] for name in sheet_columns}


def read_weapon_sheets(source):
    regular = dict(group="A", name="B", price="C", damage="E", critical="F", range="G",
                   damage_type="H", spaces="I", description="J", source="K", notes="L")
    magic = dict(name="A", price="B", spaces="D", description="E", source="F", notes="G")
    return read_catalog_sheets(source, {name: magic if name == "Armas mágicas" else regular
                                       for name in SHEETS})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    data = read_weapon_sheets(args.source)
    destination = Path(__file__).resolve().parents[1] / "weapon_data.py"
    destination.write_text(
        '# Catálogo extraído de ' + args.source.name + '\n'
        '# Gerado por tools/import_weapon_catalog.py; preserve os textos da fonte.\n'
        'WEAPON_DATA = ' + pformat(data, width=100, sort_dicts=False) + '\n',
        encoding="utf-8")
    print(f"{sum(map(len, data.values()))} armas importadas em {len(data)} abas.")
