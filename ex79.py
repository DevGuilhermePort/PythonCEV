numeros = []  # Criando a lista 'numeros' vazia

while True:  # Criando um loop infinito
    n = int(input('Digite um valor: '))  # Criando a variável 'n' para a resposta do usuário
    print()  # Linha em branco

    if n not in numeros:  # Se 'n' não estiver em 'numeros':
        numeros.append(n)  # Adicione 'n' em 'numeros'
        print('Valor adicionado com sucesso...')
    else:  # Se não:
        print('Valor duplicado! Não vou adicionar.')

    print()  # Linha em branco

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntar se o usuário deseja continuar
    print()  # Linha em branco
    while continuar not in 'sn':  # Loop infinito enquanto continuar não for 'n':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntar de novo
        print()  # Linha em branco
    if continuar == 'n':  # Se continuar for igual a 'n':
            break  # Quebre o loop
    
print('Você digitou os valores: ', end='')  # Removendo a quebra de linha
for numero in sorted(numeros):  # Para cada 'numero' em 'numeros' em ordem:
     print(f'{numero} ', end='')  # Print 'numero' e subtitua a quebra de linha final por nada.