import zipfile
from ..services.configure import process_atas

def unzip_path(path, out_csv) -> bool:
    try:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            file_parent = zip_ref.namelist()[0].split('/')[0]
            zip_ref.extractall("./")
            process_atas(path=file_parent, out_csv=out_csv)
        return True
    except FileNotFoundError:
        print(f"❌ [!] Pasta não encontrada: {path}")
        return False
    except zipfile.BadZipFile:
        print(f"❌ [!] Arquivo corrompido {path}")
        return False
    except Exception as e:
        print(f"❌ [!] Erro ao descompactar: {e}")
        return False
