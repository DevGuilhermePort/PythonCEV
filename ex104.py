def leiaInt(msg): 
    while True:
        numero = str(input(msg))   
        if numero.isnumeric():
            return numero
            break
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")

print(f"Você acabou de digitar o número {leiaInt("Digite um número: ")}")
