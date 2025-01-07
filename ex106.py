from time import sleep

def mensagem(msg, fonte=0, cor=30):
    tamanho = len(msg)
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")
    print(f"\033[{cor}m  {msg}  \033[m")
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")


def ajuda(comando):
    mensagem(f"Acessando o manual do comando '{comando}'", cor=32)
    sleep(2)
    help(comando)

while True:
    mensagem("SISTEMA DE AJUDA PyHELP", 1, 32)
    resposta = str(input("Função ou biblíoteca: ")).strip().lower()
    if resposta == "fim":
            break
    else:
        ajuda(resposta)
    sleep(1)
    print('')
mensagem("Adeus!", cor=31)