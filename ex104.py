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


# Programa principal:
print(f"Você acabou de digitar o número {leiaInt("Digite um número: ")}")  # Informando ao usuário qual número ele digitou e usando a f-string para chamar a função leiaInt() antes que a saída de dados aconteça.
