from random import randint  # Importando a função randint da biblíoteca random
from time import sleep  # Importando a função sleep da biblíoteca time

jogos = []  # Criando a lista vazia 'jogos'
lista = []  # Criando a lista vazia 'lista'

print(f'{'-' * 30}\n{'JOGUE NA MEGA SENA':^30}\n{'-' * 30}')

jogo = int(input('Quer que eu sorteie quantos jogos? '))  # Atribuindo a entrada do usuário na variável 'jogo'
total = 0  # Iniciando a variável 'total'

sleep(0.5)  # Pausa de 0.5 segundos
while total < jogo:  # Enquanto 'total' for menor que 'jogo'
    contador = 0  # Iniciando a variável 'contador'
    while True:  # Loop infinito enquanto for verdadeiro:
        numero = randint(1, 60)  # Randomizando um número de um a sessenta para a varável 'numero'
        if numero not in lista:  # Se 'numero' não estiver em 'lista':
            lista.append(numero)  # Adicione 'numero' na lista 'lista'
            contador += 1  # Contador adiciona um
        
        if contador >= 6:  # Se contador for igual ou maior que seis:
            break  # Quebre o loop
    lista.sort()  # Organizando 'lista' em ordem
    jogos.append(lista[:])  # Adicionando uma cópia de 'lista' dentro de 'jogos'
    lista.clear()  # Limpando a variável 'lista'
    total += 1  # Total recebe mais um
print(f'{'-=' * 3} SORTEANDO {jogo} JOGOS {'-=' * 3}')
sleep(0.5)
for pos, valor in enumerate(jogos):  # Para cada 'pos' e 'valor' dentro de 'jogos' enumerado:
    print(f'Jogo {pos + 1}: {valor}')
    sleep(0.75)  # Pausa de 0.75 segundos
print(f'{'-=' * 4} < BOA SORTE > {'-=' * 4}')
