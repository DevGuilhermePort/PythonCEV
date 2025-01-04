#Pedi pro usuário dar um valor para atribuí-lo à variável vel
vel = float(input('Velocidade atual do carro: '))

#Estrutura condicional composta "Se" e "Se não"
if vel <= 80:       #"Se vel(velocidade) for menor ou igual(<=) 80, escreva:"
    print('Você é um motorista responsável! Tenha um bom dia!')
else:               #"Se não:"
    multa =  (vel - 80) * 7
    print('Você ultrapassou o limite de velocidade 80Km/H')
    print(f'e deverá pagar uma multa de R${multa:.2f}.')

#Sempre vai acontecer
print('Preze sempre ser responsável no volante.')