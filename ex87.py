matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maior = 0

for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f'Digite um valor para [{coluna},{linha}]: '))

print('-=' * 15)
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz[coluna][linha]:^5}]', end='')
        if matriz[coluna][linha] % 2 == 0:
            somapar += matriz[coluna][linha]
    print()
print('-=' * 15)

print(f'A soma dos valores pares é {somapar}.')
for coluna in range(0, 3):
    somacoluna += matriz[coluna][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for linha in range(0, 3):
    maior = max(matriz[1])
print(f'O maior valor da segunda linha é {maior}.')