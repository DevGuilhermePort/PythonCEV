from random import randint
from time import sleep  # Importabdo os módulos necessários

print(f'''{'=-' * 15}
VAMOS JOGAR PAR OU IMPAR!!!
{'=-' * 15}''')  # Formatando a mensagem

contador = 0  # Iniciando o contador
while True:  # Enquando verdadeiro
    escolha_jogador = int(input('Diga um valor: '))  # Informando o valor
    escolha_pc = randint(1, 10)  # Usando o módulo para fazer a escolha do pc
    par_impar = (escolha_pc + escolha_jogador) % 2  # Módulo(resto) da soma das escolhas por 2
    while True:  #Enquanto verdadeiro
        # Definindo par ou impar, jogando para maiúsculo, dando strip, e fatiando a primeira letra
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print(f'{'-' * 30}')
        if escolha in 'PI':  # Se escolha estiver em 'PI':
            break  # Quebra o loop
    if escolha == 'P' and par_impar == 0 or escolha == 'I' and par_impar == 1:  # Se for verdadeuro:
        print(f'Você VENCEU!!! Você jogou {escolha_jogador} e a máquina {escolha_pc}.')
        contador += 1  # Contador mais um
    elif escolha == 'P' and par_impar == 1 or escolha == 'I' and par_impar == 0:  #Se não, se:
        print(f'Game Over!!! Você jogou {escolha_jogador} e a máquina {escolha_pc}.')
        break  # Quebra o código
print(f'Você venceu {contador} vezes até perder')
