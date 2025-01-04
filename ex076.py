print('-' * 40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-' * 40)

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)  # Tupla criada com todos os produtos e seus valores

for pos in range(0, len(produtos)):  # Para cada 'pos' no range de zero até o len de 'produtos':
    if pos % 2 == 0:  # Se 'pos' dividido por 2 for igual a zero:
        print(f'{produtos[pos]:.<30}', end=' ') # Mostre 'produtos' na posição 'pos' centralizado 30 casas a direita com pontos
    else:  # Se não:
        print(f'R$ {produtos[pos]:>7.2f}')  # Mostre 'produtos' na posição 'pos' centralizado 7 casas a direita com 2 números depois da virgula
print('-' * 40)