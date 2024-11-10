expressao = str(input('Digite a expressão: ')).strip()  # Atribuindo a entrada do usuário à variável expressao
pilha = []  # Criando a lista pilha
for simbolo in expressao:  # Para cada elemento(simbolo) na lista(pilha):
    if simbolo == '(':  # Se o símbolo for '(':
        pilha.append('(')  # Adicione na lista
    elif simbolo == ')':  # Se não, se o símbolo for ')':
        if len(pilha) > 0:  # Se o len de pilha for maior que zero:
            pilha.pop()  # Remove o último valor
        else:  # Se não
            pilha.append(')')  # Adiciona ')' na pilha
            break  # E quebra o loop

if len(pilha) == 0:  # Se o len de lista for igual a zero:
    print('Sua espressão é válida!!!')  # Válido
else:  # Se não:
    print('Sua expressão está errada!!!')  # Inválido
