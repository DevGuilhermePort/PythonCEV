#Coletando o valor das variáveis
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

#Parcelas e limites das parcelas
parcelas = anos * 12 #12 parcelas por ano
limite_das_parcelas = sal * 0.30 #Limite de 30% do salário do comprador
valor_das_parcelas = casa / parcelas

#Estrutura condicional composta aprovando ou recusando o pedido de empréstimo
if valor_das_parcelas > limite_das_parcelas:
    print('Pedido de empréstimo NEGADO!!!')
    print(f'As parcelas de R${valor_das_parcelas:.2f} excederam o limite de R${limite_das_parcelas:.2f}')
else:
    print('Pedido de empréstimo APROVADO!')
    print(f'Dividá será paga em {parcelas} parcelas de R${valor_das_parcelas:.2f}!!!')