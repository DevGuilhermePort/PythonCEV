from time import sleep
from random import randint
print('Olá! Eu me chamo computador!')
sleep(1.25)
jogar = ''
while jogar != 'S' != 'N' and jogar != 'N' != 'S':
    jogar = str(input('Deseja jogar um jogo comigo [S/N]? ')).strip().upper()
    if jogar != 'S' != 'N' and jogar != 'N' != 'S':
        print('OPÇÃO INVÁLIDA!!!')
        print('Tente novamente!')
    elif jogar == 'S':
        print('Irei pensar em um número de zero a dez.')
        sleep(1)
        print('Pensando...')
        sleep(1)
        print('Pensando...')
        sleep(1)
        escolha_cpu = randint(0, 10)
        print('''Pensei!!! Vamos ver quantas tentativas você
precisará para descobrir o número!''')
        sleep(1)
        print('Boa sorte!!!')
        sleep(0.75)
        tentativas = 0
        escolha_jogador = ...
        while escolha_jogador != escolha_cpu:
            escolha_jogador = int(input('Em que número eu pensei? '))
            print('')
            tentativas += 1
            if escolha_jogador != escolha_cpu:
                print('Você errou!')
                if escolha_jogador < escolha_cpu:
                    print('Mais um pouco')
                elif escolha_jogador > escolha_cpu:
                    print('Um pouco menos')
                print('Tente novamente.')
                print('')
        print(f'''Você ACERTOU!!!
{tentativas} tentativas foram necessárias para você acertar!''')
    elif jogar == 'N':
        print('Que pena! Tenha um bom dia!')
print('Fim.')