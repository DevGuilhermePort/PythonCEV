numeros = []  # Criando a lista usando dois colchetes
while True:  # Enquanto dor verdadeiro:
    numero = int(input('Digite um valor: '))  # Perguntando um valor e adicionando o valor a uma variável

    if numero in numeros:  # Se o número perguntado não estiver na lista:
        print('Valor duplicado! Não vou adicionar.')  # Não faz nada
    else:  # Se não:
        numeros.append(numero)  # Adiciona o valor dado a variável simples na variável composta

    repetir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Perguntando se o programa deve ou não continuar
    while repetir not in 'SN':  # Se a resposta não for 'S' ou 'N':
        repetir = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]  # Tente de novo
    
    if repetir == 'N':  # Se a respota for 'N':
        break  # Quebre o loop
print(f'{'-=' * 30}')
print(f'Você digitou os valores: {sorted(numeros)}')  # Colocando os números em ordem na tela