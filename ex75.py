numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')) , int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores: {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'o valor 3 apareceu na {numeros.index(3)} posição')
print(f'Os valores pares digitados foram', end=' ')

for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
    if numero == numeros[len(numeros) - 1]:
        print('\n')