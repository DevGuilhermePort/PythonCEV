lista = list()  # Iniciando a minha lista
for pos in range(0, 5):  # Para cada pos no intervalo de 0 até 5 (efetivando o 5):
    lista.append(int(input(f'Digite um numero para a Posição {pos}: ')))  # Adicionando um valor a lista 5 vezes
print(f'O menor valor digitado foi {min(lista)} nas Posições: ', end='')  # Informando o menor usando a função `min`
for pos, num in enumerate(lista):  # Para cada pos, num na lista enumerada:
    if lista[pos] == min(lista):  # Se a lista no indicie pos for igual ao menor:
        print(pos, end='...')
print()
print(f'O maior valor digitado foi {max(lista)} nas Posições: ', end='')
for pos, num in enumerate(lista):  # Para cada pos, num na lista enumerada:
    if lista[pos] == max(lista):  # Se a lista no indicie pos for igual ao maior:
        print(pos, end='...')
