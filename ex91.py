from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogadores = {

    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(0, 6),
    'Jogador4': randint(0, 6)

}

print('-' * 30)
for jogador, dado in jogadores.items():
    print(f'{jogador} tirou {dado}.')
    sleep(0.75)
print('-' * 30)
print('')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-=' * 15)
for indicie, valor in enumerate(ranking):
    print(f'{indicie + 1} lugar: {valor[0]} com {valor[1]}')
    sleep(0.75)
print('-=' * 15)
