from time import sleep
bateria = int(input('Qual a porcentagem da sua bateria? '))
bateria_cheia = bateria + (100 - bateria)
carregar_ou_nao = int(input('''Você deseja carregar seu celular?
                            
[ 1 ]

[ 2 ]

Escolha: '''))
if carregar_ou_nao == 1:
    print(f'Bateria: {bateria}%')
    for c in range(bateria, bateria_cheia, 5):
        sleep(0.25)
        bateria +=5
        if bateria > 100:
            bateria = 100
        print(f'Bateria: {bateria}%')
    print('Sua bateria está completa!!!')
elif carregar_ou_nao == 2:
    print('''Tome cuidado para não ficar sem bateria.
Você pode precisar usar o celular. Eu recomendo usar o modo
de economia de energia.''')
else:
    print('OPÇÃO INVÁLIDA!!!')
            
        
    