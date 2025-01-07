from pacote import moedas

numero = int(input("Digite um preço: R$"))
print(f"A metade de {numero} é {moedas.metade(numero)}")
print(f"O dobro de {numero} é {moedas.dobro(numero)}")
print(f"Aumentando 10% temos {moedas.aumentar(numero, 10)}")
print(f"Reduzindo 13% temos{moedas.diminuir(numero, 13)}")