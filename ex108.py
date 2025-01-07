from pacote import moedas

num = float(input("Digite um preço: R$"))

print(f"A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}.")
print(f"O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}.")
print(f"Aumentando 10% temos {moedas.moeda(moedas.aumentar(num, 10))}.")
print(f"Reduzindo 13% temos {moedas.moeda(moedas.diminuir(num, 13))}.")