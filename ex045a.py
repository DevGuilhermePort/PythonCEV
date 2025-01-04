#Importando o módulo
from random import randint
from time import sleep

#Informações
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua escolha? '))

#Parte bonita do jogo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(f'{'-=' * 12}')
print(f'Computador jogou {itens[cpu]}')
print(f'Jogador jogou {itens[jogador]}')
print(f'{'-=' * 12}')

#Estrutura condicional aninhada
if cpu == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 1:
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')
    else:
        print('JOGADA INVÁLIDA''')
elif cpu == 2:
    if jogador == 0:
        print('VITÓRIA')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
