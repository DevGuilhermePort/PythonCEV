print(f'''{'=' * 27}
    10 TERMOS DE UMA PA
{'=' * 27}''')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = 1  # Iniciando a variável termos
while termos <= 10:  # Enquanto termos for menor ou igual a 10:
    print(primeiro_termo, end='-> ')  # Definindo o fim como '-> '
    primeiro_termo += razao  # Primeiro termo mais razão
    termos += 1  # Termos mais um
print('ACABOU')
