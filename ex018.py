from math import radians, sin, cos, tan #importei todas as funções que vou usar

ang = int(input('Informe um angulo: ')) #Peço ao usuário dar o valor da variável
print(f'O SENO de {ang} tem o valor de {sin(radians(ang)):.2f}') #Utilizo as funções importadas para dar o seno do valor dado, convertido em radianos
print(f'O COSSENO de {ang} tem o valor de {cos(radians(ang)):.2f}') #Utilizo as funções importadas para dar p cosseno dado, convertido para radianos
print(f'A TANGENTE de {ang} tem o valor de {tan(radians(ang)):.2f}') #Utilozo as funções importadas e repito o processo

#PRESTAR MAIS ATENÇÃO NOS RADIANOS