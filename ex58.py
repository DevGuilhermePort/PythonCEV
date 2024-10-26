from time import sleep  # Importar a função sleep da biblioteca time
from random import randint  # Importar a função randint da biblioteca random
print('Olá! Eu me chamo computador!')
sleep(1.25)  # Pausando o código por 1.25 segundos
jogar = ' '  # Iniciando a varipavel jogar
while jogar not in 'SN':  # Enquanto jogar for difetente de '
    jogar = str(input('Gostaria jogar um jogo comigo [S/N]? ')).strip().upper()[0]
    if jogar not in 'SN':  # Se jogar for difente de 'S' ou 'N':
        print('OPÇÃO INVÁLIDA!!!')
        print('Tente novamente!')
    elif jogar == 'S':  # Se jogar for igual a 'S':
        print('Irei pensar em um número de zero a dez.')
        sleep(1)  # Pausa de um segundo
        print('Pensando...')
        sleep(1)  # Pausa de um segundo
        print('Pensando...')
        sleep(1)  # Pausa de um segundo
        escolha_cpu = randint(0, 10)  # Definindo escolha_cpu como um número aleatorio inteiro entre 1 e 10
        print('''Pensei!!! Vamos ver quantas tentativas você
precisará para descobrir o número!''')
        sleep(1)  # Pausa de um segundo
        print('Boa sorte!!!')
        sleep(0.75)  # Pausa de 0.75 segundos
        tentativas = 0  # Iniciando o contador de tentativas
        escolha_jogador = ''  # Iniciando a variável escolha_jogador
        while escolha_jogador != escolha_cpu:  # Enquanto escolha_jogador for diferente de escolha_cpu:
            escolha_jogador = int(input('Em que número eu pensei? '))
            print('')
            tentativas += 1  # Tentativa mais um
            if escolha_jogador != escolha_cpu:  # Se escolha_jogador for diferente de escolha_cpu:
                print('Você errou!')
                if escolha_jogador < escolha_cpu:  # Se escolha jogador for maior que escolha_cpu: 
                    print('Mais um pouco')
                elif escolha_jogador > escolha_cpu:  # Se não, se escolha jogador_jogador for maior que escolha_cpu:
                    print('Um pouco menos')
                print('Tente novamente.')
                print('')
        print(f'''Você ACERTOU!!!
{tentativas} tentativas foram necessárias para você acertar!''')
    elif jogar == 'N':  # Se jogar for igual a 'N':
        print('Que pena! Tenha um bom dia!')
print('Fim.')