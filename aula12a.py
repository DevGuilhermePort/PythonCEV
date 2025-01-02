itens = int(input('Quantos itens você quer calcular? '))
soma = 0  # Acumulador
for c in range(0, itens):  # Laço c no intervalo de 0 até o valor de itens: 
    item = float(input(f'Preço do produto {c+1}: R$'))
    soma += item  # Soma mais item
print(f'Seus produtos ao todo custam R${soma:.2f}')