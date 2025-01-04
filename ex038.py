#Escolher o valor dos dois números
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

#Estrutura condicional aninhada para dar o valor maior
if n1 > n2:
    print(f'O PRIMEIRO({n1}) valor é maior!.')
elif n2 > n1:
    print(f'O SEGUNDO({n2}) valor é maior.')
else:
    print('Os dois valores são idênticos.')