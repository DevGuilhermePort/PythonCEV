numeros = list()  # Criando a lista 'numeros'
maior = menor = 0  # Iniciando as variáveis 'maior' e 'menor'

print('-' * 35)

for pos in range(0, 5):  # Para cada 'pos' no range de 0 até 5:
    numeros.append(int(input(f'Digite um valor para a posição {pos}: '))) # Adicionar a entrada do usuário na lista
    if pos == 0:  # se 'pos' for igual a zero:
        maior = menor = numeros[pos]  # Maior e menor passam a ser 'numeros' na posição 'pos'
    else:  # Se não
        if numeros[pos] > maior:  # Se 'numeros' na posição 'pos' for maior que 'maior':
            maior = numeros[pos]  # 'maior' passa a ser 'numeros' na posição 'pos'
        if numeros[pos] < menor:  # Se 'numeros' na posição 'pos' for menor que 'menor':
            menor = numeros[pos]  # 'menor' passa a ser 'numeros' na posição 'pos'

print('-' * 35)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, numero in enumerate(numeros):  # Para cada 'posicao' e 'numero' em 'numeros' enumerados:
    if numero == maior:  # Se 'numero' for igual à 'maior':
        print(posicao, end=' ')  # Print 'posicao' e substitua a quebra de linha por espaço

print()  # Quebra de linha

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, numero in enumerate(numeros):  # Para cada 'posicao' e 'numero' em 'numeros' enumerados:
    if numero == menor:  # Se 'numero' for igual à 'menor':
        print(posicao, end=' ')  # Print 'posicao' e sbstitua a quebra de linha por espaço
