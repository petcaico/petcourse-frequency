import os

def filter_files(name_path):
    for file in os.listdir(name_path):
        if ".docx" not in file:
            old_file: str = os.path.join(name_path, file)
            new_file: str = os.path.join(name_path, f"{file}.docx")
            os.rename(old_file, new_file)
        if "fulano" in file.lower():
            walk_file: str = os.path.join(name_path, file)
            os.remove(walk_file)