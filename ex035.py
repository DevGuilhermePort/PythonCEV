#Vou pedir para o usuário dar o valor de três retas de um triângulo
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

#"Se a soma de dois lados for menor que o terceiro, escreva:"
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As três retas FORMAM um triângulo!!!')
else:
    print('As retas NÃO formam um triângulo')
