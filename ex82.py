numeros = list()  # Criando a lista vazia 'numeros'
pares = list()  # Criando a lista vazia 'pares'
impares = list()  # Criando a lista vazia 'impares'

while True:  # Loop infinito
    numero = int(input('Digite um número: '))  # Criando a variável 'numero' recebendo a entrada do usuário
    numeros.append(numero)  # Adicionando 'numero' em 'numeros'

    if numero % 2 == 0:  # Se 'numero' for divisível por 2:
        pares.append(numero)  # Adicionar 'numero' em 'pares'
    else:  # Se não:
        impares.append(numero)  # Adicionar 'numero' em 'impares'

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntando se o usuário deseja continuar, removendo todos os espaços à frente e à trás, jogando para minúsculo e pegando apenas a primeira letra
    while continuar not in 'sn':  # Enquanto 'continuar' não for s' ou 'n':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntar de novo

    if continuar == 'n':  # Se 'continuar' for igual à 'n':
        break  # Quebre o loop

print()  # Linha em branco

print('A lisca completa é: ', end='')
for numero in numeros:
    if numero == numeros[-1]:
        print(numero, end='.\n')
    else:
        print(numero, end=', ')  # Esquema para a visualização da resposta ser mais limpa

print()

print('A lista de pares é: ', end='')
for par in pares:
    if par == pares[-1]:
        print(par, end='.\n')
    else:
        print(par, end=', ')

print()

print('A lista de ímpares é: ', end='')
for impar in impares:
    if impar == impares[-1]:
        print(impar, end='.\n')
    else:
        print(impar, end=', ')
