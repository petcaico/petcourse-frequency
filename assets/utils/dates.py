import re

def extract_date_from_name(file: str) -> str:
    date: list[str] = re.findall(r'\d+', file)
    if len(date[2]) == 2:
        date[2] = f'20{date[2]}'

    return f'{date[0]}-{date[1]}-{date[2]}'
