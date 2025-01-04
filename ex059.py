n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
menu = 0  # Iniciando a variável menu
while menu != 5:
    menu = int(input('''Menu de operações
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
>>>>>>>>>>Sua escolha: '''))  # Dando input para o usuário escolher a opção do menu
    print('')
    if menu == 1:  # Se menu for igual a 1:
        print(f'O total da soma de {n1} e {n2} é {n1 + n2}')
    elif menu == 2:  # Se não, se menu for igual a 2:
        print(f'O produto de {n1} x {n2} vale {n1 * n2}')
    elif menu == 3:  # Se não, se menu for igual a 3:
        maior = n1  # Maior recebe n1
        if n2 > n1:  # Se n2 for maior que n1:
            maior = n2  # Maior passa a ser n2
        print(f'O maior valor é {maior}')
    elif menu == 4:  # Se não, menu for igual a 4:
        n1 = float(input('Novo número: '))
        n2 = float(input('Novo número: '))
    elif menu == 5:  # Se não, se menu for igual a 5:
        print('Fim')
    else:  # Se não for nenhuma das outras alternativas:
        print('Tente novamente')
    print('')
print('Fim do programa!')