from random import randint  # Importando a função randint da biblíoteca random

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  # Criando a tupla com 5 números aleatórios de 1 a 10
print('Os números sorteados foram: ', end='')
for numero in numeros:  # Para cada numero em número:
    print(f'{numero} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')  # A função max retorna o maior valor de uma sequência ou conjunto de valores
print(f'O menor valor sorteado foi: {min(numeros)}')  # A função min retorna o menor valor de uma sequência ou conjunto de valores