import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="BD-ACD",
            user="BD250226110",
            password="Abhrg5",
            database="BD250226110"
        )
        return conexao
    except Exception as e:
        print(f"\n[ERRO] Não foi possível conectar ao banco: {e}")
        print("Verifique se a VPN está ativa!")
        return None

def menu_principal():
    opcao = ""

    while opcao != "0":
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gerenciamento")
        print("2 - Votação")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            menu_gerenciamento()
        elif opcao == "2":
            menu_votacao()
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida")


def menu_gerenciamento():
    opcao = ""

    while opcao != "0":
        print("\n=== GERENCIAMENTO ===")
        print("1 - Cadastrar Eleitor")
        print("2 - Listar Eleitores")
        print("0 - Voltar")

        opcao = input("Escolha: ")
      
        if opcao == "2":
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT nome, titulo_eleitor FROM eleitores")

            eleitores = cursor.fetchall()

            print("\n--- LISTA DE ELEITORES NO BANCO ---")
            for e in eleitores:
                print(f"Nome: {e['nome']} | Título: {e['titulo_eleitor']}")

            conexao.close()

        if opcao == "0":
            return


        if opcao == "0":
            return


def menu_votacao():
    opcao = ""

    while opcao != "0":
        print("\n=== VOTAÇÃO ===")
        print("1 - Abrir votação")
        print("2 - Resultados")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "0":
            return


menu_principal()
