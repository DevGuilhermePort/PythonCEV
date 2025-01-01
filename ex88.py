from random import randint
from time import sleep

jogos = []
lista = []

print(f'{'-' * 30}\n{'JOGUE NA MEGA SENA':^30}\n{'-' * 30}')

jogo = int(input('Quer que eu sorteie quantos jogos? '))
total = 0

sleep(0.5)
while total < jogo:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'{'-=' * 3} SORTEANDO {jogo} JOGOS {'-=' * 3}')
sleep(0.5)
for pos, valor in enumerate(jogos):
    print(f'Jogo {pos}: {valor}')
    sleep(0.75)
print(f'{'-=' * 4} < BOA SORTE > {'-=' * 4}')
