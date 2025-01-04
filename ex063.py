termo1, termo2 = 0, 1  # Posso atribuir dois valores por vez à variaveis diferentes
fibon = int(input('Deseja ver quantos elementos da sequencia de Fibonacci? '))  # Quantos termos ver
contador = 0  # Contador inicial em 0
while contador < fibon:  # Enquanto o contador for menor que fibon, repita:
    print(termo1, end='-> ')  # Mostrar na tela o termo1, e substituir o fim da linha por '-> '
    termo3 = termo1 + termo2  # Calculando o terceiro termo da sequência de fibonacci
    termo1 = termo2  # Re atribuir o valor do termo1 para o próximo loop
    termo2 = termo3  # Re atribuir o valor do termo2 para o próximo loop
    contador += 1  # Somando um ao contador para não gerar um loop infinito