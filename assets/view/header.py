import os

def header():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("╔══════════════════════════════════════════════════════╗")
    print("║                  GERENCIAMENTO DE ATAS               ║")
    print("║     Processamento automático de frequência PET       ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║ [1] ->  Com link de compartilhamento (Google Drive)   ║")
    print("║ [2] ->  Com pasta local zipada                        ║")
    print("║ [0] ->  Encerrar processo                             ║")
    print("╚══════════════════════════════════════════════════════╝")
