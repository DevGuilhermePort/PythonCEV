from pacote import moedas

num = float(input("Digite um preço: R$"))

print(f"A metade de {moedas.moeda(num)} é {moedas.metade(num, True)}.")
print(f"O dobro de {moedas.moeda(num)} é {moedas.dobro(num, True)}.")
print(f"Aumentando 10% temos {moedas.aumento(num, 10, True)}.")
print(f"Reduzindo 13% temos {moedas.reducao(num, 10, True)}.")
