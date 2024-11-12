from random import sample  # Importando a função sample da biblíoteca ramdom
from time import sleep  # Importando a função sleep da biblíoteca time

mega = list()  # Criando a lista 'mega'

print('-' * 30)  
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)

for numero in range(0, 61):  # Laço de repetição com variável de controle no intervalo de 0 à 61
    mega.append(numero)  # Adicionar a variável de repetição na lista 'mega' em cada iteração

jogos = int(input('Quantos jogos você quer que eu sorteie? '))  # Pedindo para o usuário a entrada de quantos palpites de jogos ele quer ver

for cont in range(jogos):  # Laço de repetição com variável de controle no interválo dado pelo usuário
    print(f'Jogo {cont + 1}: {sorted(sample(mega, k=6))}')  # Escolhedo 6 valores aleátorios da lista 'mega', mostrando em ordem crescente
    sleep(1)

print(f'{'-=' * 5} < BOA SORTE! > {'-=' * 5}')