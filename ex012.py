preço = float(input('Qual é o preço do produto? R$')) #Fiz o usuário informar o preço do produto
print(f'O produto que custava R${preço:.2f}', end=', ') #Formatei o valor que o usuário atribuiu á variavel preço, e interliguei o final desde print com ', ' ao próximo print
preço -= preço * 0.05 #Re-Atribuí o valor desta variável para seu própio valor 5% menor
print(f'na promoção com desconto de 5% vai custar R${preço:.2f}') #Somei o valor da variável com o valor da variável vezes 0.05 para calcular o desconto de 5%
print(f'Pagando a vista receberá um desconto extra de mais 10%, custando apenas R${preço - (preço * 0.10):.2f}!') #Calculei um desconto extra de 10%
print(f'Você pode parcelar o produto em 6, 8 ou até 10 vezes sem juros!')
print(f'Seis de R${preço / 6:.2f}.\nOito de R${preço / 8:.2f}.\nDez de R${preço / 10:.2f}.') #Dei o valor que cada parcela teria
