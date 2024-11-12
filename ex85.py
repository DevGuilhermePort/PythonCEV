numeros = [[],[]]  # Criando uma lista separada em duas outras listas

for i in range (1, 8):  # Laço de repetição no intervalo de 1 a 8
    numero = int(input(f'Digite o {i}o. valor: '))
    if numero % 2 == 0:  # Se o número for divisivel por dois:
        numeros[0].append(numero)  # Adicionar 'numero' na lista 'numeros' na posição '[0]' 
    else:  # Se não:
        numeros[1].append(numero)  # Adicionar 'numero' na lista 'numeros' na posiçãp '[1]'

print(f'Os valores pares digitados foram: {sorted(numeros[0])}.')
print(f'Os calores ímpares digitados foram: {sorted(numeros[1])}.')
