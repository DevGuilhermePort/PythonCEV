numero = int(input('Digite um número: '))
total = 0  # Iniciando o  contador total
for primo in range(1, numero + 1):  # Laço primo no intervalo de 1 a numero mais 1:
    if numero % primo == 0:  # Se o resto da divisão inteira de numero por primo for igual a 0:
        total += 1  # Total recebe mais um
        print(f'-> {primo} <-', end=' ')  # Tranformando o fim em ' '
    else:  # Se não:
        print(primo, end=' ')  # Transformando o fim em ' '
print(f'\nFoi dividido {total} vezes.')
if total == 2:  # Se o total for igual a 2:
    print('Por isso ele É PRIMO!!!')
else:  # Se não:
    print('Por isso ele NÃO É PRIMO!!!')
    