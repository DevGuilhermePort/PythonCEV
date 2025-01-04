print(f'''{'=' * 27}
    10 TERMOS DE UMA PA
{'=' * 27}''')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for termos in range(0, 10):  # Laço termos no intervalo 0 a 10:
    print(primeiro_termo, end=' -> ')  # Definindo o final do print como ' -> '
    primeiro_termo += razao  # Primeiro_termo mais razão
print('ACABOU')

# Outra forma de fazer

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao  # Formula de resolver a PA
for termos in range(primeiro_termo, decimo_termo + 1, razao):  # Laço termos no intervalo primeiro_termo a decimo_termo mais um pulando de razão em razão:
    print(f'{termos}', end=' -> ')  # Definindo o final do print como ' -> '
print('ACABOU')