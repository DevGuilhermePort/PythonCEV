#importar o função de raiz quadrada
from math import pow

#Pegar informações sobre peso e altura do usuário
peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (pow(altura, 2))

print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você esta obeso!')
else:
    print('Você esta com obesidade mórbida!')
