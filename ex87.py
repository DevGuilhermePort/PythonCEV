matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior = 0


for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        
        if linha == 1 and coluna == 0:
            maior = matriz[linha][coluna]
        elif linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
    print('')

print('-=' * 15)
for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^8}]', end='')
    print()
print('-=' * 15)

print(f'A soma dos valores pares é: {soma_pares}.')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior}')