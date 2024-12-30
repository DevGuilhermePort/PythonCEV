numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]
    
    if continuar == 'n':
        break

print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decressente são {numeros}')

if numeros.count(5) >= 1:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')