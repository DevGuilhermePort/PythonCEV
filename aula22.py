# Modularização é o ato de criar módulos. Este conceito surgiu no inicio da decada de 60, periodo esse que a computação quebrou barreiras, começou a ser usada em empresas e os programas aumentaram exponencialmente.

# O foco principal é dividir um programa muito grande, com muitas funcionalidadas. Dividindo-o em pequenos pedaços(módulos) para facilitar o manuseio e a LEGIBILIDADE. É muito mais facil encontrar códigos, seja para manutenção ou melhorias, quando eles são separados em pequenas partes de acordo com o assunto.

def fatorial(numero):
    fatorial = 1
    for c in range(numero,1 , -1):
        fatorial *= c
    return fatorial

num = int(input("Digite um número: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")