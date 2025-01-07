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
    : return: o número, caso ele seja um número realmente, e inteiro.
    __Função feita por Port nos primeiros do projeto Orion.__
    """
    while True:  # Loop while infinito:
        numero = str(input(msg))  # criando a cariável numero fazendo uma pergunta ao usuário de acordo com a mensagem passada como parâmetro.
        if numero.isnumeric():  # Se numero for um número:
            return numero  # Retorne o valor de numero
            break  # Quebre o loop
        else:  # Se não for um número:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")  # Falar ao usuário que o valor não foi válido.
