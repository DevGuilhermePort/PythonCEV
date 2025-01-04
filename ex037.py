#Escolher o valor e a base de conversão
num = int(input('Digite um valor inteiro: '))
base = int(input(f'''[ 1 ] Converter para binário
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal
Sua opção: 
'''))

#Estrutura condicional aninhada para dar o valor em cada base
if base == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Você escolheu uma base inválida.')