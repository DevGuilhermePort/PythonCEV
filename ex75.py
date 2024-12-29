numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))  # Colocando 4 números dados pelo usuário na tupla 'numeros'

print(f'Você digitou os valores: {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')  # Usando o método count para contar quantas vezes 9 pareceus na tupla

if 3 in numeros:
    print(f'o valor 3 apareceu na {numeros.index(3) + 1} posição')  # Usando o método index para ver onde foi a primeira incidência do número 3
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram', end=' ')  # Substituindo a quebra de linha por um espaço

for numero in numeros:  # Para cada 'numero' in 'números':
    if numero % 2 == 0:  # Se 'numero' dividido por 2 for igual a 0:
        print(f'{numero}', end=' ')  # Print 'numero' e substitua a quebra de linha por um espaço
    if numero == numeros[len(numeros) - 1]:  # Se 'numero' for igual ao último item de 'numeros':
        print('\n')  # Quebre a linha
