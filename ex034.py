#Vou perguntar o salário do funcionário
sal = float(input('Quanto é o seu salário? R$'))

#Se o salário for superior a R$1250.00, recebe um aumento de 15%, se for menor, recebe um aumento de 10%
if sal <= 1250:
    novo = sal * 0.15 + sal
    porcent = 100 * 0.15
else:
    novo = sal * 0.10 + sal
    porcent = 100 * 0.10
print(F'Quem ganhava R${sal}, passa a receber R${novo} com um aumento de {porcent}%.')