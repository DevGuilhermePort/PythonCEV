from time import sleep
cores = {'limpo': '\033[m',
        'negrito': '\033[1m',
        'sublinhado': '\033[4m',
        'invertido':  '\033[7m',
        'preto': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'lilas': '\033[35m',
        'ciano':  '\033[36m',
        'cinza': '\033[37m'}

print(f'{cores['azul']}Olá mundo{cores['limpo']}!')
nome = str(input(f'{cores['vermelho']}Informe seu {cores['negrito']}nome{cores['limpo']}{cores['vermelho']} para continuar o programa{cores['limpo']}... ')).capitalize().split()
print(f'{cores['negrito']}{cores['vermelho']}Processando{cores['limpo']}...')
sleep(2)
if nome[0] == 'Guilherme':
    print(f'''Meu nome é \033[32m{cores['negrito']}{cores['sublinhado']}{nome[0]}{cores['limpo']}!\nSou o programador que escreveu este código''')
    print('Meu sonho é me tornar um programador completo!')
else:
        print(f'{cores['vermelho']}Você {cores['negrito']}NÃO{cores['limpo']}{cores['vermelho']} é meu programador!!!')
