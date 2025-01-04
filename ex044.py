#Dar o valor da variável produto e da variável pagamento
produto = float(input('Preço do produto: '))
print('''Formas de pagamento:
 À vista no dinheiro ou cheque: Digite 1.
 À vista no cartão: Digite 2.
 Em até duas vezes no cartão:  Digite 3.
 Três vezes ou mais no cartão: Digite 4.
 ''')
forma_de_pagamento = int(input('Digite a forma de pagamento: '))

#Estrutura condicional composta para mostrar o preço do produto de acordo com a forma de pagamento
if forma_de_pagamento == 1:
    print(f'O produto à vista no dinheiro ou no cheque custa R${produto - produto * 0.10:.2f}')
elif forma_de_pagamento == 2:
    print(f'O produto à vista no cartão custa {produto - produto * 0.05:.2f}')
elif forma_de_pagamento == 3:
    print(f'O produto parcelado em 2 vezes sem juros será duas parcelas de {produto / 2:.2f}')
elif forma_de_pagamento == 4:
    parcelas = int(input('Deseja parcelar o produto em quantas vezes? '))
    print(f'O produto séra parcelado em {parcelas} parcelas com 20% de juros. \nCada parcela custará R${(produto + produto *0.20) / parcelas:.2f}')
    print(f'O produto no fim custará R${produto + produto * 0.20:.2f} por conta do juros.')
else:
    print('Forma de pagamento inválida.')
