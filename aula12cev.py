from time import sleep  # Importar a função sleep da biblioteca time
bateria = int(input('Qual a porcentagem da sua bateria? '))
bateria_cheia = 100
carregar_ou_nao = int(input('''Você deseja carregar seu celular?
                            
[ 1 ]

[ 2 ]

Escolha: '''))
if carregar_ou_nao == 1:  # Se carre_ou_não for igual a 1:
    print(f'Bateria: {bateria}%')
    for c in range(bateria, bateria_cheia, 5):  # Laço c no intervalo bateria até bateria_cheia pulando de 5 em 5:
        sleep(0.25)  # Pausar o código por 0.25 seg
        bateria += 5  # Bateria mais 4
        if bateria > 100:  # Se bateria for maior que 100
            bateria = 100  # Bateria recebe a 100
        print(f'Bateria: {bateria}%')
    print('Sua bateria está completa!!!')
elif carregar_ou_nao == 2:  # Se não, se carregar_ou_não for igual a 2
    print('''Tome cuidado para não ficar sem bateria.
Você pode precisar usar o celular. Eu recomendo usar o modo
de economia de energia.''')
else:  # Se não
    print('OPÇÃO INVÁLIDA!!!')
            
        
    