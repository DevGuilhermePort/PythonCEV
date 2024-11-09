lista = list()
while True:
    num = int(input('Digite um número: '))

    if num not in lista:
         lista.append(num)
    else:
         print('Valor duplicado! Não vou adicionar.')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
            break
print({'-='  * 20})
print(f'Você digitou os os valores {lista}')