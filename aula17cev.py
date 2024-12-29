valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for pos, valor in enumerate(valores):
    print(f'Na posução {pos} eu encontrei o valor {valor}')


a = [12, 7, 2024]
b = a[:]
b[1] = 6
print(f'Lista B:{b}')
print(f'Lista A: {a}')
