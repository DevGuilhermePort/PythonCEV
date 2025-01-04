from math import trunc
num = float(input('Informe um valor real: ')) #Pedi para informar o valor para atribuir a variável
print(f'A porção inteira de {num}, é igual a {trunc(num)}') #Usei a função da biblíoteca math para mostrar apenas a perte inteira do numero

print('') #Pritei em branco para espaçar o código
num = float(input('Informe um valor real: ')) #Pedi para o usuário informar o número
print(f'A porção inteira de {num}, é igual à {num:.0f}') #Fiz a formatação para remover tudo que vem depois do ponto flutuante

print('') #Mais um espaço
num  = float(input('Informe um valor real: ')) #Pedi para o usuário informar o valor da variável
print(f'A porção inteira de {num}, é igual a {int(num)}') #Usei a função nativa do python sem módulos