from random import choices

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sorteados = (choices(numeros, k=5))

print('Os valores sorteados foram: ', end=' ')

for pos, numero in enumerate(sorteados):
    if pos == len(sorteados) - 1:
        print(numero)
    else:
        print(numero, end=' ')
    if pos == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
