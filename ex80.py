lista = []  # Criando a lista

for cont in range(0, 5):  # Laço de repetição no intervalo de 0 até 5
    numero = int(input('Digite um valor: '))  # Perguntando um valor para o usuário

    if cont == 0 or numero > lista[-1]:  # Se o cont for igual a zero ou o número for maior que o último valor da lista:
        lista.append(numero)  # Adicionar numero na lista
        print('Adicionado no fim da lista.')
    else:  # Se não:
        pos = 0  # Inicia o contador pos
        while pos < len(lista):  # Enquanto pos for menor que o len de lista:
            if numero <= lista[pos]:  # Se número for menor que lista na posição pos
                lista.insert(pos, numero)  # Inserir na posição pos o valor de numero
                print(f'Adicionado na posição {pos}.')
                break  # Quebre o loop
            pos += 1  # pos recebe um
print(f'Os valores em ordem foram {lista}')  # Saída de dados