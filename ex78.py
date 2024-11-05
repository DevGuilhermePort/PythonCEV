lista = list()  # Criando a lista vazia com o método 'list()'
maior = menor = 0  # Iniciando duas variáveis com o mesmo valor
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {cont}: ')))  # Adicionando a entrada do teclado na lista com o método 'append'
    if cont == 0:  # Se for a primeira iteração:
        maior = menor = lista[cont]  # O maior e o menor são iguais a lista[conta]:
    else:  # Se não:
        if lista[cont] > maior:  # Se a lista[cont] for maior que maior:
            maior = lista[cont]  # Maior passa a ser lsita[cont]
        if lista[cont] < menor:  # Se a lista[cont] for menor que menor?:
            menor = lista[cont]
print(f'O maior valor digitado foi {maior} nas posições', end=': ')
for iteracao, valor in enumerate(lista):
    if valor == maior:
        print(f'{iteracao}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=': ')
for iteracao, valor in enumerate(lista):
    if valor == menor:
        print(f'{iteracao}...', end=' ')
