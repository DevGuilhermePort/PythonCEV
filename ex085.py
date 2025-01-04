numeros =[[], []]  # Criando a lista 'numeros' com duas listas vazias dentro dela

for pos in range(1, 8):  # Para cada 'pos' no range de 1 à 8:
    numero = int(input(f'Digite o {pos}o. valor: '))  # Criando a variável 'numero' com a entrada do usuário
    
    if numero % 2 == 0:  # Se 'numero' dividido por 2 for igual à zero:
        numeros[0].append(numero)  # Adicionar 'numero' em 'numeros[0]'
    else:  # Se não:
        numeros[1].append(numero)  # Adicionar 'numero' em 'numeros[1]'

numeros[0].sort()  # Colocando 'numeros[0]' em ordem
print('Os valores pares digitados foram: ', end='')
for par in numeros[0]:  # Printando os números pares de maneira mais limpa usando o loop for
    if par == numeros[0][len(numeros[0]) - 1]:
        print(f'{par}.')
    else:
        print(par, end=', ')

numeros[1].sort()  # Colocando 'numeros[1]' em ordem
print('Os valores ímpares digitados foram: ', end='')
for impar in numeros[1]:  # Printando os números pares de maneira mais limpa usando o loop for
    if impar == numeros[1][len(numeros[1]) - 1]:
        print(f'{impar}.')
    else:
        print(impar, end=', ')
