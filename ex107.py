from pacote import moedas  # Importando o módulo moedas do pacote pacote.

numero = float(input("Digite o preço: R$"))  # Perguntando um valor ao usuário

print(f"A metade de {numero} é {moedas.metade(numero)}.")  # Usando as funções do meu módulo para retornar a metade do número
print(f"O dobro de {numero} é {moedas.dobro(numero)}.")  # O dobro do número
print(f"Aumentando 10% temos {moedas.aumento(numero, 10)}.")  # O número com um aumento de 10%
print(f"Reduzindo 13% temos {moedas.reducao(numero, 13)}.")  # E com uma redução de 13%.
