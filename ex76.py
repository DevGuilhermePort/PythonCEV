listagem = ('Maça', 20.98,
            'Açucar', 19.90,
            'Corante', 4.60,
            'Pipoca', 8.79,
            'Pinhão', 78.90,
            'Rapadura', 23.99)  # Tupla com o nome e o valor dos produtos

print(f'{'-' * 40}')
print(f'{'LISTAGEM DE PREÇOS':^40}')  # Formatando a saída
print(f'{'-' * 40}')
for pos in range(0, len(listagem)):  # para cada pos no range de 0 até o tamanho da tupla:
    if pos % 2 == 0:  # Se o módulo de pos dividido por 2 for igual a 0:
        print(f'{listagem[pos]:.<30}', end='')  # Formatando a saída a esquerda com pontos 
    else:  # Se não
        print(f'R${listagem[pos]:>6.2f}')  
print(f'{'-' * 40}')