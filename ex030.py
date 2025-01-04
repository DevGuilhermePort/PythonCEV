#Printei p que o código faz
print('\033[1mAnalisador de pares e ímpares\033[m!!!')

#Vou pedir para o usuário dar um valor para atribuí-lo para a variável num
num = int(input('Digite um número: '))
#"Se o módulo(resto) da divisão inteira de num(número) por dois for igual(==) a 0(indicando é divisível por dois), escreva: "
if num % 2 == 0:
    print(f'O número {num} é PAR!')
#"Se não: "
else:
    print(f'O número {num} é ÍMPAR!')
