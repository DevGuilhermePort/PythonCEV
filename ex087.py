matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criando a lista 'matriz' com três lista com três zeros dentro de cada uma
soma_pares = soma_terceira_coluna = maior = 0  # Iniciando as variàveis 'soma_pares', 'soma_teceira_coluna' e 'maior'


for linha in range(0, 3):  # Para cada 'linha' no range de 0 à 3:
    for coluna in range(0, 3): # Para cada 'coluna' no range de 0 à 3:
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))  # 'matriz[linha][coluna]' passa a ser a entrada do usuário

        if matriz[linha][coluna] % 2 == 0:  # Se 'matriz[linha][coluna]' dividio por 2 for igual à 0:
            soma_pares += matriz[linha][coluna]  # 'soma_pares' passa a ser 'matriz[linha][coluna]'

        if coluna == 2:  # Se 'coluna' for igual à 2:
            soma_terceira_coluna += matriz[linha][coluna]  # 'soma_terceira_coluna' adiciona 'matriz[linha][coluna]'
        
        if linha == 1 and coluna == 0:  # Se 'linha' for igual 1 e 'coluna' igual 0:
            maior = matriz[linha][coluna]  # 'maior' passa a ser 'matriz[linha][coluna]'
        elif linha == 1:  # Se 'linha' for igual 1:
            if matriz[linha][coluna] > maior:  # Se matriz[linha][coluna] for maior que 'maior':
                maior = matriz[linha][coluna]  # 'maior' passa a ser 'matriz[linha][coluna]'
    print('')  # Linha em branco ao final do loop

print('-=' * 15)
for linha in matriz:  # Para cada 'linha' em 'matriz':
    for coluna in linha:  # Para cada 'coluna' em 'linha':
        print(f'[{coluna:^8}]', end='')  # Print 'coluna' centralizado à 8 caracteres, e substituindo o final por nada
    print()  # quebra de linha
print('-=' * 15)

print(f'A soma dos valores pares é: {soma_pares}.')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior}')
