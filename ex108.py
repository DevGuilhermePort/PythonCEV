from utilidadescev import moedas  # Impórtando meu módulo

num = float(input("Digite o preço: R$"))  # Perguntando um preço pro usuário

print(f"A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}.")  #Usando a função do meu módulo para mostrar a saída em valor monetário
print(f"O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}.")
print(f"Aumentando 10% temos {moedas.moeda(moedas.aumento(num, 10))}.")
print(f"Reduzindo 13% temos {moedas.moeda(moedas.reducao(num, 13))}.")