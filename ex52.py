numero = int(input('Digite um número: '))
total = 0
for primo in range(1, numero + 1):
    if numero % primo == 0:
        total += 1
        print(f'-> {primo} <-', end=' ')
    else:
        print(primo, end=' ')
print(f'\nFoi dividido {total} vezes.')
if total == 2:
    print('Por isso ele É PRIMO!!!')
else:
    print('Por isso ele NÃO É PRIMO!!!')
    