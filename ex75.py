numeros = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))  # Perguntando o valor 4 vezes dentro da variável para criar a tupla.

print('Os valores digitados foram: ', end='')  # Definindo o fim como ''
for numero in numeros:  # Para cada número em números:
    print(f'{numero} ', end='')  # Dessa forma a tupla não aparece entre parênteses e vírgulas.
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')  # Contar quantas vezes aparece o nove
if 3 in numeros:  # Se o número 3 estivem em numeros:
    print(f'O três apareceu na {numeros.index(3) + 1} posição.')  # A primeira posição que aparece o número 3
else:  # Se não:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for par in numeros:  # Para cada par em numeros:
    if par % 2 == 0:  # Se o módulo de par dividido por 2 for igual a 0:
        print(f'{par} ', end='')
