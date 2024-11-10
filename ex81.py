numeros = []  # Criando a lista usando colchetes vazios
while True:  # Criando um loop infinito
    numeros.append(int(input('Digite um número: ')))  # Adicionando números dados pela entrada do usuário na lista

    repetir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Perguntando se o usuário deseja continuar adicionando valores
    while repetir not in 'SN':  # Enquanto repetir não ser 'S' ou 'N'
        repetir = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]  # Pergunte novamente ao usuário
    if repetir == 'N':  # Se repetir for 'N' (Não):
        break  # Quebre o loop
print(f'{'-=' * 20}')
print(f'Você digitou {len(numeros)} elementos.')  # Mostrando quantos números foram digitados usando len para medir o tamanho da lista
print(f'Os valores em ordem decressente são {sorted(numeros, reverse= True)}.')  # Mostrando os valores em ordem decrescente
if 5 in numeros:  # Se '5' estiver dentro da lista 'numeros':
    print('O valor 5 faz parte da lista.')  # Falar que 5 faz parte da lista
else:  # Se não
    print('O valor 5 não foi encontrado na lista.')  # Falar que não
