from assets.services.drive import get_frequency
from assets.utils.unzip import unzip_path
from assets.view.header import header
from datetime import date
import pandas as pd

def create_excel(out_csv):
    try:
        df = pd.read_csv(out_csv)
        adjust_df = df.pivot(index='Nome', columns='Data', values='Status')
        adjust_df = adjust_df.sort_index().sort_index(axis=1)

        with pd.ExcelWriter(f"PET_Frequencias_{date.today().strftime('%d-%m-%Y')}.xlsx") as writer:
            adjust_df.to_excel(writer, sheet_name="Frequencias")

        print("✅ Planilha Excel criada com sucesso.")

    except Exception as e:
        print(f"❌ [!] Erro ao criar arquivo Excel: {e}")
        exit(1)


if __name__ == "__main__":
    try:
        out_csv = f"frequencia_{date.today().strftime('%d-%m-%Y')}.csv"

        mode = ''
        while (mode != '0'):
            header()
            mode = input();

            match mode:
                case '1':
                    print("Insira o link do arquivo 'CTRL + SHIFT + V': ")
                    url = input("")
                    try:
                        get_frequency(url=url, out_csv=out_csv)
                        create_excel(out_csv=out_csv)
                        input()
                    except Exception as e:
                        print(f"❌ [!] Falha ao obter frequências: {e}")
                        exit(1)
                case '2':
                    print("Informe o nome da pasta (sem .zip):")
                    path = input("")
                    try:
                        if unzip_path(path=f"./{path}.zip", out_csv=out_csv):
                            create_excel(out_csv=out_csv)
                            input()
                        else:
                            input()
                    except Exception as e:
                        print(f"❌ [!] Falha ao obter frequências: {e}")
                        input()
                case '0':
                    print("Encerrando o processo. Até mais!")
                    break
                case _:
                    print("[!] Opção inválida para esse processo.")
                    input("[!] Enter para continuar ou 'CTRL + C' para encerrar o processo ")

    except KeyboardInterrupt:
        print("\n[!] Processo encerrado pelo usuário com CTRL + C.")
