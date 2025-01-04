dias = int(input('Quantos dias alugados? ')) #Faço o usuário informar quantos dias alugou o carro
km = float(input('Quantos Km rodados? ')) #E informar também quantos km
print(f'O valor do aluguel é de R${(dias *60) + (km * 0.15):.2f}') #Printo as informções
