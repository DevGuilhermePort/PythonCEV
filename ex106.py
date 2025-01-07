def mensagem(msg, fonte=0, cor=30):
    tamanho = len(msg)
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")
    print(f"\033[{cor}m  {msg}  \033[m")
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")


while True:
    mensagem("SISTEMA DE AJUDA PyHELP", 1, 32)
    resposta = str(input("Função ou biblíoteca: ")).strip().lower()
    if resposta == "fim":
            break
    else:
        print(f"\033[7m{help(resposta)}\033[m",)
    print('')
