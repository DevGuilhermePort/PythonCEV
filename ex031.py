#Vou perguntar quantos quilometros duram a viagem para atribuir o valor à variável km
km = float(input('Sua viagem durará quantos quilometros? '))

#estrutura condicional composta
if km <= 200:   #"Se km for menor ou igual(<=) que 200, escreva:"
    preço = km * 0.50
else:           #"Se não"
    preço = km * 0.45
print(f'A sua passagem custará R${preço:.2f}!')