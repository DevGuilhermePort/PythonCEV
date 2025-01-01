matriz = [[ 0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criar uma lista 'matriz' com 3 listas com 3 zeros dentro de cada uma

for linha in range(0, 3):  # Para cada 'linha' no range de 0 à 3:
    for coluna in range(0, 3):  # Para cada 'coluna' no range de 0 à 3:
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))  # 'matriz[linha][coluna]' passa a ser a entrada do usuário
    print('')  # Linha em branco a cada final de loop

print('-=' * 15)
for linha in matriz:  # Para cada 'linha' em 'matriz':
    for coluna in linha:  # Para cada 'coluna' em 'linha':
        print(f'[{coluna:^7}]', end=' ')  # Print 'coluna'
    print()  # Quebra de linha a cada fim de loop
print('-=' * 15)