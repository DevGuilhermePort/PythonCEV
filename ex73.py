brasileirao = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo',
               'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro',
               'Vasco da Gama', 'Atlético Mineiro', 'Grêmio', 'Criciúma',
               'Fluminense', 'Vitória', 'Corinthians', 'Atlético-PR',
               'Bragantino', 'Juventude', 'Cuiabá', 'Atlético-GO')  # Criando a tupla com os 20 colocados do campeonato brasileiro de futebol
print(f'{'=' * 30}')
print(f'Lista de times do Brasileirão: {brasileirao}')  # Mostrando a tupla no terminal
print(f'{'=' * 30}')
print(f'Os 5 primeiros são {brasileirao[0:5]}')  # Mostrando os itens de zero a 5 (efetuando o cinco)
print(f'{'=' * 30}')
print(f'Os 4 últimos são {brasileirao[-4:]}')  # Mostrando os itens a partir de menos 4 até o final
print(f'{'=' * 30}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')  # Mostrando os itens da tupla em ordem
print(f'{'=' * 30}')
if 'Chapecoense' in brasileirao:  # Se chapecoense estiver em brasileirao:
    print(f'O Chapecoense está {brasileirao.index('Chapecoense' + 1)} na lista')  # Mostrar onde ocorre o item na primeira vez
else:  # Se não:
    print('O Chapecoense não está no brasileirão série A.')
