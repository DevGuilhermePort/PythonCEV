numeros = []  # Criando a lista 'numeros' vazia

for c in range(0, 5):  # Para cada 'c' no range de zero à cinco:
    num = int(input('Digite um valor: '))  # Criar a variável 'num' com a entrada do usuário
    
    if c == 0 or num > numeros[-1]:  # Se 'c' for igual a zero, ou 'num' for maior que o último item de 'numeros':
        numeros.append(num)  # Adicionar 'num' ao final da lista 'numeros'
        print('Adicionado ao final da lista.')
    else:  # Se não:
        pos = 0  # Iniciar a variável 'pos com zero
        while pos < len(numeros):  # Enquanto 'pos' for menor que o len de 'numeros':
            if num <= numeros[pos]:  # Se 'num' for menor ou igual que 'numeros' na posição 'pos':
                numeros.insert(pos, num)  # Inserir 'num' na posição 'pos' de 'numeros'
                print(f'Adicionado na posição {pos} da lista.')
                break  # Quebre o loop
            pos += 1  # 'Pos' recebe mais um
print(f'Os valores digitados em ordem foram: {numeros}')