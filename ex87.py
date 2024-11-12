matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criando uma lista com 3 listas com 3 números neutros dentro
somapar = somacoluna = maior = 0  # Iniciando as variáveis 'somapar', 'somacoluna' e 'maior'

for coluna in range(0, 3):  # Laço de repetição no intervalo de 0 a 3
    for linha in range(0, 3):  # Laço de repetição no intervalo de 0 a 3
        matriz[coluna][linha] = int(input(f'Digite um valor para [{coluna},{linha}]: '))  # Atribuíndo o valor dado pelo usuário à 'matriz' na posição '[coluna][linha]'

print('-=' * 15)
for coluna in range(0, 3):  # Laço de repetição no intervalo de 0 a 3
    for linha in range(0, 3):  # Laço de repetição no intervalo de 0 a 3
        print(f'[{matriz[coluna][linha]:^5}]', end='')  # Saída dos dados da matriz na posição pedida
        if matriz[coluna][linha] % 2 == 0:  # Se o valor nesta posição for divisivel por dois:
            somapar += matriz[coluna][linha]  # Somapar soma 'matriz[coluna][linha]'
    print()
print('-=' * 15)

print(f'A soma dos valores pares é {somapar}.')
for coluna in range(0, 3):  # Laço de repetição no intervalo de 0 a 3
    somacoluna += matriz[coluna][2]  # 'somacoluna' recebe 'matriz[coluna][2]'
print(f'A soma dos valores da terceira coluna é {somacoluna}')
maior = max(matriz[1])  # Maior passa a ser 'max(matriz[1])'
print(f'O maior valor da segunda linha é {maior}.')