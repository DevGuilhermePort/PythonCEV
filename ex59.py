n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
menu = 0
while menu != 5:
    menu = int(input('''Menu de operações
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
>>>>>>>>>>Sua escolha: '''))
    print('')
    if menu == 1:
        print(f'O total da soma de {n1} e {n2} é {n1 + n2}')
    elif menu == 2:
        print(f'O produto de {n1} x {n2} vale {n1 * n2}')
    elif menu == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor é {maior}')
    elif menu == 4:
        n1 = float(input('Novo número: '))
        n2 = float(input('Novo número: '))
    elif menu == 5:
        print('Fim')
    else:
        print('Tente novamente')
    print('')
print('Fim do programa!')