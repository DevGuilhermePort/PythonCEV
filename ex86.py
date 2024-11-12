matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criando a lista 'matriz' com 3 listas com valores neutros dentro delas

for pilar in range(0, 3):  # Laço de repetição com variável de controle 'pilar' no intervalo de um à três
    for coluna in range(0, 3):  #   Laço de repetição com variável de controle 'coluna' no intervalor de um à três
        matriz[coluna][pilar] = int(input(f'Digite um valor para [{coluna}, {pilar}]: '))  # 'matriz' na posição '[coluna]' e '[pilar]'

print('')
for pilar in range(0, 3):  # Repetir o laço três vezes
    for coluna in range(0, 3):  # Cada iteração ira iterar este laço outras 5 vezes
        print(f'[{matriz[coluna][pilar]:^5}]', end=' ')  # Saída dos dados 'matriz' na posição  '[coluna]' e '[pilar]'
    print()