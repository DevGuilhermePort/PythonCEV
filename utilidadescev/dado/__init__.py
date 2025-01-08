def leiaDinheiro(msg):
    valido = False
    while not valido:
        numero = str(input(msg)).replace(",", ".").strip()
        if numero.isalpha() or numero == "":
            print(f"\033[31mErro! \"{numero}\" não é um número válido\033[m")
        else:
            valido = True
            return float(numero)


def leiaInt(msg):   # Criando a função leiaInt() recebendo uma mensagem.
    """
    -> Valida a entrada do usuário aceitando apenas números inteiros.
    : param msg: Recebe a mensagem que vai aparecer quando o número for perguntado.
    : return: o número, caso ele seja um inteiro.
    __Função feita por Port nos primeiros do projeto Orion.__
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Por favor digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mO usuário preferiu não continuar o programa.\033[m")
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Por favor digite um número real válido.\033[m")
        except KeyboardInterrupt:
            print("\n\033[31mO usuário preferiu não continuar o programa.\033[m")
            return 0
        else:
            return num
