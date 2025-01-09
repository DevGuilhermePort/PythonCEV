from utilidadescev.menu import menu, cabecalho
while True:
    opcoes = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if opcoes == 1:
        print("opção 1")
    elif opcoes == 2:
        print("Opção 2")
    elif opcoes == 3:
        cabecalho("Saindo do sistema... Adeus")
        break
    else:
        print("\033[31mErro! Digite um opção válida.\033[m")