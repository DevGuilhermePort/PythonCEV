tp = {'verde': '\033[1;32',
    'vermelho': '\033[1;31m',
    'limpo': '\033[m',
    'azul': '\033[1;34m'}

num = int(input('Digite um valor: '))
print(f'Analizando o valor \033[1;34m{num}\033[m, seu antecessor é \033[1;31m{num - 1}{tp['limpo']} e o seu sucessor é \033[1;32m{num + 1}\033[m')