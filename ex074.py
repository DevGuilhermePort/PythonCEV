from random import randint  # Importando a função randint da biblíoteaca random

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))  # Colocando 5 números aleatórios entre 0 e 10 dentro da tupla

print('Os valores sorteados foram: ', end=' ')  # Transformando a quebra de linha do final em um espaço

for numero in numeros:  # Para cada 'numero' em 'numeros': 
    if numero == numeros[len(numeros) - 1]:  # Se o 'numero' for igual à 'numeros' na última posição:
        print(numero)  # Mostre 'numero' na tela
    else:  # Se não:
        print(numero, end=' ')  # Mostre 'numero' na tela e troque a quebra de linha final por um espaço

    if numero == numeros[0]:  # Se 'numero' for igual a 'numeros' na posição 0:
        maior = menor = numero  # Criar as variáveis 'maior' e 'menor' e atribuir à ambas o valor de 'numero'
    else:  # Se não:
        if numero > maior:  # Se 'numero' for maior que 'maior':
            maior = numero  # 'maior' passa a ser 'numero'
        elif numero < menor:  # Se não, se 'numero' for menor que 'menor':
            menor = numero  # 'menor' passa a ser 'numero'

print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
