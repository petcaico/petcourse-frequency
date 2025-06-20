import gdown
import os
from typing import List, Union, Any
from .configure import process_atas

def get_frequency(url: str, out_csv: str):
    try:
        paths: Union[List[str], List[Any], None] = gdown.download_folder(url, quiet=False, use_cookies=False)
        
        if paths is not None:
            name_path: str = os.path.basename(os.path.dirname(paths[0]))

            for file in os.listdir(name_path):
                if ".docx" not in file:
                    old_file: str = os.path.join(name_path, file)
                    new_file: str = os.path.join(name_path, f"{file}.docx")

                    os.rename(old_file, new_file)
                
                if "fulano" in file.lower():
                    walk_file: str = os.path.join(name_path, file)
                    os.remove(walk_file)
            
            try:
                process_atas(path=name_path, out_csv=out_csv)
            except Exception as e:
                raise ValueError(" ❌ [!] Erro ao gerar arquivo CSV.")

        else:
            raise ValueError(" ❌ [!] Lista de ATAS indisponível.")

    except Exception as e:
        raise RuntimeError(f"❌ [!] Erro ao baixar arquivos do Google Drive: {e}")    
