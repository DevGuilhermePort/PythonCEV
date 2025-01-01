from random import sample
from time import sleep

print(f'{'-' * 30}\n{'JOGUE NA SENA':^30}\n{'-' * 30}')

jogos = int(input('Quantos jogos quer que eu sorteie? '))
print(f'{'-=' * 3} SORTEANDO {jogos} JOGOS {'-=' * 3}')
print('')
for sorteio in range(1, jogos + 1):
    sleep(0.75)
    print(f'Jogo {sorteio}: {sample(range(1, 60), 6)}')
    print('')

print(f'{'-=' * 4} < BOA SORTE > {'-='* 4}')