numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))

    repetir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while repetir not in 'SN':
        repetir = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    
    if repetir == 'N':
        break
print(f'{'-=' * 30}')
print(f'Você digitou os valores: {sorted(numeros)}')
