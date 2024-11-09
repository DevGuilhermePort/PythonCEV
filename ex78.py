numeros = []  # Criei a lista vazia
for cont in range(0, 5):  # Laço de repetição no intervalo de 0 a 5:
    numeros.append(int(input('Digite um valor: ')))  # Adicionando a entrada no usuário na lista
print(f'O maior valor digitado foi {max(numeros)} nas posições: ', end='')  # Falando qual foi o maior valor
for pos, num in enumerate(numeros):  # Enumerando os valores da lista
    if num == max(numeros):  # Se o número for igual ao maior valor da lista:
        print(pos, end=' ')  # Sua posição.

print(f'\nO menor valor digitado foi {min(numeros)} nas posições: ', end='')  # Falando qual foi o menor valor
for pos, num in enumerate(numeros):  # Enumerando os valores da lista
    if num == min(numeros):  # Se o número for igual ao menor valor da lista: 
        print(pos, end=' ')  # Sua posição.
