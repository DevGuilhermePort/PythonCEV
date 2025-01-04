#Importando a função choice para jogar pedra papel ou tesoura com o usuário
from random import choice
from time import sleep

#Atribuíndo a escolha do usuário à variável escolha
e = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua escolha? '''))

#Escolha da máquina
ppt = [0, 1, 2]
edm = choice(ppt)

#Estrutura condicional aninhada
if e == 0:
    escolha = 'Pedra'
elif e == 1:
    escolha = 'Papel'
elif e == 2:
    escolha = 'Tesoura'
else:
    print('Escolha inválida')

if edm == 0:
    escolha_da_maquina = 'Pedra'
elif edm == 1:
    escolha_da_maquina = 'Papel'
elif edm == 2:
    escolha_da_maquina = 'Tesoura'
#Parte bonitinha do jogo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(f'''\033[1m{'-=' * 10}
Computador jogou {escolha_da_maquina}
Jogador jogou {escolha}
{'-=' * 10}\033[m''')

if e == 0 and edm == 2 or e == 1 and edm == 0 or e == 2 and edm == 1:
    print('JOGADOR VENCE')
elif e == edm:
    print('EMPATE')
else:
    print('MÁQUINA VENCE')