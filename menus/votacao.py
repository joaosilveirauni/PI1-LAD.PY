from submenu.sistemavotacao import submenu_votacao
from submenu.resultados import resultados
from submenu.auditoria import auditoria

def menu_votacao():
    opcao = ""

    while opcao != "0":
        print("\n=== VOTAÇÃO ===")
        print("1 - Abrir votação")
        print("2 - Resultados")
        print("3 - Auditoria")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "0":
            return
        elif opcao == "1":
            submenu_votacao()
        elif opcao == "2":
            resultados()
        else:
            auditoria()