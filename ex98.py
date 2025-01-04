from time import sleep  # Importando a função sleep() da biblíoteca time

def contador(inicio, fim, passo):  # Definindo a função "contador()" recebendo três parâmetros, "inicio", "fim" e "passo":
    if passo < 0:  # Se "passo" for menor que zero (Se "passo" for negativo):
        passo *= 1  # "passo" recebe "passo" vezes um (inverte o sinal)
    if passo == 0:  # Se "passo" for igual à zero:
        passo = 1  # "passo" passa a ser 1

    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} pulando de {passo} em {passo}.")  # Mostrando os valores de "inicio", "fim" e "passo"
    sleep(2)  # Dando uma pausa de 2 segundos no código
    if inicio < fim:  # Se "inicio" for menor que "fim":
        contador = inicio  # Contador recebe "inicio"
        while contador <= fim:  # Enquanto "contador" for menor ou igual a "fim":
            print(contador, end=" ", flush=True)  # Printando o valor de "contador", substituíndo a quebra de linha do fim por um espaço,e por fim usando o ARGUMENTO DE FUNÇÃO "flush=True" para imprimir o valor de contador imediatamente, sem ter que esperar o buffer, fazendo o código aparecer de maneira "gradual" de acordo com o uso do "sleep"
            sleep(0.25)  # Pausando o código por 0.25 segundos
            contador += passo  # "contador" mais igual "passo"
        print("Fim!")
    else:  # Se não:
        contador = inicio  # "contador" recebe "inicio"
        while contador >= fim:  # Enquanto "contador" for menor ou igual que "fim":
            print(contador, end=" ", flush=True)  # Printando o valor de "contador", substituíndo a quebra de linha do fim por um espaço,e por fim usando o ARGUMENTO DE FUNÇÃO "flush=True" para imprimir o valor de contador imediatamente, sem ter que esperar o buffer, fazendo o código aparecer de maneira "gradual" de acordo com o uso do "sleep"
            sleep(0.25)  # Pausando o código por 0.25 segundos
            contador -= passo  # "contador" menos igual "passo"
        print("Fim!")


# Código principal
contador(1, 10, 1)  # Chamando a função "contador" e dando à ela três parâmetros
contador(10, 0, 2)  # Dando um parâmetro de "inicio" menor que o parâmetro de "fim"
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem.")
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))  # Dando três estradas do usuário para os parâmetros "inicio", "fim" e "passo".
