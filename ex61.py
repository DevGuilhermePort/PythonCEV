print(f'''{'=' * 27}
    10 TERMOS DE UMA PA
{'=' * 27}''')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = 1
while termos <= 10:
    print(primeiro_termo, end='-> ')
    primeiro_termo += razao
    termos += 1
print('ACABOU')
