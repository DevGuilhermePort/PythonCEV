expressao = str(input('Digite a expressão: '))  # Criando a variável 'expressao' para armazenar a entrada do usuário
pilha = []  # Criando a lista vazia 'pilha' 

for simbolo in expressao:  # Para cada 'simbolo' na 'expressao':
    if simbolo == '(':  # Se o 'simbolo' for igual a '(':
        pilha.append('(')  # Adicione '(' na pilha
    elif simbolo == ')':  # Se 'simbolo' for igual a ')':
        if len(pilha) > 0:  # Se o len de 'pilha' for maior do que zero
            pilha.pop()  # Remova o último item de 'pilha'
        else:  # Se não:
            pilha.append(')')  # Adicione ')' na pilha
            break  # Quebre o loop

if len(pilha) == 0:  # Se o len de 'pilha' for igual à zero:
    print('Sua expressão está correta!')
else:  # Se não:
    print('Sua expressão está errada!')
