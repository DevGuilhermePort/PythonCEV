def leiaInt(msg):   # Criando a função leiaInt() recebendo uma mensagem.
    """
    -> Valida a entrada do usuário aceitando apenas números inteiros.
    : param msg: Recebe a mensagem que vai aparecer quando o número for perguntado.
    : return: o número, caso ele seja um número realmente, e inteiro.
    __.__
    """
    while True:
        numero = str(input(msg))   
        if numero.isnumeric():
            return numero
            break
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")

print(f"Você acabou de digitar o número {leiaInt("Digite um número: ")}")
