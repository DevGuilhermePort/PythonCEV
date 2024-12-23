times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atletico Goianiense', 'Cuiabá')

print(times[0:5])

print(f'{'=-' * 15}')

print(times[-4:])

print(f'{'=-' * 15}')

print(f'{'=-' * 15}')

print(sorted(times))

print(f'{'=-' * 15}')

if 'Chapecoense' in times:
    print(times.index('Chapecoense'))
else:
    print('Chapecoense não esta na tabela.')