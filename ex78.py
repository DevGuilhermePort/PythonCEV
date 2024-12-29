numeros = list()
maior = menor = 0

print('-' * 35)

for pos in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = numeros[pos]
    else:
        if numeros[pos] > maior:
            maior = numeros[pos]
        if numeros[pos] < menor:
            menor = numeros[pos]

print('-' * 35)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == maior:
        print(posicao, end=' ')

print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == menor:
        print(posicao, end=' ')
