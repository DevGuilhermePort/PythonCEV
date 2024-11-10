lista = []  # Criando uma lista geral
pares = []  # de pares
impares = []  # e de ímpares

while True:  # Loop while infinito
    num = int(input('Digite número: '))  # Perguntando um valor para o usuário
    lista.append(num)  # Adicionando esse valor na lista geral
    if num % 2 == 0:  # Se num for divisivel por dois:
        pares.append(num)  # Adicionando num a lista de pares
    else:  # Se não:
        impares.append(num)  # Adicione em ímpares

    continuar = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')
