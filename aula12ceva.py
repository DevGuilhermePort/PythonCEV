itens = int(input('Quantos itens você quer calcular? '))
soma = 0
for c in range(0, itens):
    item = float(input(f'Preço do produto {c+1}: R$'))
    soma += item
print(f'Seus produtos ao todo custam R${soma:.2f}')