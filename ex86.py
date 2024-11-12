matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for pilar in range(0, 3):
    for coluna in range(0, 3):
        matriz[coluna][pilar] = int(input(f'Digite um valor para [{coluna}, {pilar}]: '))

print('')
for pilar in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[coluna][pilar]:^5}]', end=' ')
    print()