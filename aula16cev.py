lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')  # Criando uma tupla
for comida in lanche:  # Mostrar cada item na tupla dentro do indicie da variável de controle
    print(comida, end=' -> ')
print('\n')  # Quebrando a linha

for cont in range(0, len(lanche)):  # Criando um loop no renge de zero até o len de lanche
    print(lanche[cont], end=' -> ')  # Fatiar um item da tupla no indicie do contador
print('\n')

for posicao, comida in enumerate(lanche):  # Indicado para usar quando precisa mostrar a posição do elemento.
    print(f'{comida}-{posicao}', end=' -> ')
print('\n')

a = (4, 5, 4, 8, 9)
b = (2, 3, 2, 4, 5)
c = a + b  # Irá concatenar o a no b
d = b + a  # Irá concatenas o b no a
print(f'{c}\n{d}')