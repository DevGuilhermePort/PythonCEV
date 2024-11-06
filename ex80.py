numeros = []  # Criando a lista com colchetes

for cont in range(0, 5):  # Para cada cont no intervalo de 0 até 5(efetuando o 5):
    numero = int(input('Digite um valor: '))  # Criando a variável numero

    if cont == 0 or numero > numeros[-1]:  # Se cont for iguaL a zero ou se numero for maior que o último número:
        numeros.append(numero)  # Adicione número no final da lista
        print('Adicionado ao final da lista.')
        print()
    
    else:  # Se não:
        pos = 0  # Iniciando o contador da posição
        while pos < len(numeros):  # Enquanto este contador for menor que o len de numeros:
            if numero <= numeros[pos]:  # Se numero for menor ou igual a numeros na posição pos: 
                numeros.insert(pos, numero)  # Insere o número na posição de pos
                print(f'Adicionado na posição {pos}.')
                print()
                break  # Quebrando o loop
            pos += 1  # Adicionando mais um ao contador

print(f'Números digitados: {numeros}')
