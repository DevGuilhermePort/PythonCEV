print(f'''{'=' * 27}
    10 TERMOS DE UMA PA
{'=' * 27}''')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for termos in range(0, 10):
    print(f'{primeiro_termo}', end=' -> ')
    primeiro_termo += razao
print('ACABOU')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for termos in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{termos}', end=' -> ')
print('ACABOU')