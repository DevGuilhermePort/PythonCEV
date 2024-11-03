valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))  # Posso usar input dentro de append

for valor in valores:
    print(valor, end=' - ')
print('\n')

for pos, v in enumerate(valores):
    print(f'Encontrei {v} na posição {pos}')

# PECULIARIDADE DO PYTHON
lista_a = [1, 2, 3, 4, 5]
lista_b = lista_a
lista_b[2] = 2
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
# O Python faz uma ligação sempre que você igualar duas listas
print('')
# Para fazer uma cópia, devo copiar TODOS os elementos de uma lista para outra
lista_a = [1, 2, 3, 4, 5]
lista_b = lista_a[:]
lista_b[2] = 2
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
