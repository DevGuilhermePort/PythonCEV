from random import randint  # Importando a função 'randint' da biblíoteca 'random'
from time import sleep  # Importando a função 'sleep' da biblíoteca 'time'
from operator import itemgetter  # Importando a função 'itemgetter' da biblíoteca 'operator'.

ranking = []  # Criando a lista 'ranking' vazia
jogadores = {  # Criando o dicionário 'jogadores' vazio

    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(0, 6),
    'Jogador4': randint(0, 6)  # Usando a função 'randint' para aleatorizar um número aleatório de um a seis dentro de cada jogador

}

print('-' * 30)
for jogador, valor in jogadores.items():  # Cada 'jogador' e 'valor' dentro de cada  chave e valor dos itens do dicionário 'jogadores'
    print(f'{jogador} tirou {valor}.')
    sleep(0.75)  # Dando uma pausa de 0.75 segundos no código
print('-' * 30)
print('')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # Atribuíndo os itens de 'jogadores', organizados graças ao operador 'itemgetter' de acordo com o segundo item do dicionário ('itemgetter(1)'), em ordem de trás para frente, do maior ao menor 

print('-=' * 15)
for indicie, valor in enumerate(ranking):  # Para cada 'indicie' e 'valor' dentro de 'enumerate(ranking)':
    print(f'{indicie + 1} lugar: {valor[0]} com {valor[1]}')
    sleep(0.75)  # Pausa de 0.75 segundos no código
print('-=' * 15)
