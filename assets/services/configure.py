import zipfile
import csv
from lxml import etree
import os
from ..utils.dates import extract_date_from_name

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def frequency_list(path):
    with zipfile.ZipFile(path) as docx:
        xml_content = docx.read("word/document.xml")
    
    root = etree.fromstring(xml_content)  # type: ignore
    tables = root.findall(".//w:tbl", NS)

    for tabela in tables:
        if "LISTA DE FREQUÊNCIA" in etree.tostring(tabela, encoding="unicode", method="text").upper():  # type: ignore
            frequency = []
            linhas = tabela.findall(".//w:tr", NS)
            for linha in linhas[2:]:  # ignora cabeçalhos
                celulas = linha.findall(".//w:tc", NS)
                if len(celulas) >= 2:
                    name = "".join(celulas[0].itertext()).strip()
                    status = "".join(celulas[1].itertext()).strip()
                    if name:  # ignora linhas vazias
                        frequency.append((name, status))
            return frequency
    return []

def process_atas(path, out_csv) -> None:
    data = []

    for file in os.listdir(path):
        if file.lower().endswith(".docx"):
            walk = os.path.join(path, file)
            date_ata = extract_date_from_name(file)
            
            if not date_ata:
                print(f"[!] Data inválida no nome: {file}")
                continue
        
            frequency = frequency_list(walk)
            for name, status in frequency:
                data.append(
                    {
                    "Nome": name,
                    "Status": status,
                    "Data": date_ata}
                )
    
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Nome", "Status", "Data"])
        writer.writeheader()
        writer.writerows(data)

    print(f"-> CSV gerado com sucesso: {out_csv}")

if __name__ == "__main__":
    process_atas("6 - Junho", "frequencia.csv")