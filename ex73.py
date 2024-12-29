times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atletico Goianiense', 'Cuiabá')  # Criação da tupla com todos os times da serie A do Brasileirão

print(times[0:5])  # Os cinco primeiros colocados

print(f'{'=-' * 15}')

print(times[-4:])  # Os quatro últimos colocados

print(f'{'=-' * 15}')

print(sorted(times))  # Times em ordem alfabética

print(f'{'=-' * 15}')

if 'Chapecoense' in times:  # Se o time da Chapecoense estiver na lista:
    print(f'O Chapecoense está na {times.index('Chapecoense') + 1} posição.')  # Mostrar em qual posição ele esta
else:  # Se não:
    print('Chapecoense não esta na tabela.')  # Falar que ele não esta presente na lista
