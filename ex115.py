from utilidadescev.menu import menu, cabecalho
from utilidadescev.arquivo import *
from time import sleep

arq = "ex115.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])

    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("\033[36mOpção 2\033[m")
    elif resposta == 3:
        cabecalho("\033[34mSaindo do sistema... Adeus.\033[m")
        break
    else:
        print("\033[31mErro! Escolha uma opção válida.\033[m")
    
    sleep(1)