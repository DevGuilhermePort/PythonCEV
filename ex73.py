brasileirao = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atlético Mineiro', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória', 'Corinthians', 'Atlético-PR', 'Bragantino', 'Juventude', 'Cuiabá', 'Atlético-GO')
print(f'{'=' * 30}')
print(f'Lista de times do Brasileirão: {brasileirao}')
print(f'{'=' * 30}')
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print(f'{'=' * 30}')
print(f'Os 4 últimos são {brasileirao[-4:]}')
print(f'{'=' * 30}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'{'=' * 30}')
if 'Chapecoense' in brasileirao:
    print(f'O Chapecoense está {brasileirao.index('Chapecoense')} na lista')
else:
    print('O Chapecoense não está no brasileirão série A.')
