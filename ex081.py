numeros = []  # Criando a lista vazia 'numeros'

while True:  # Loop infinito
    numeros.append(int(input('Digite um valor: ')))  # Adicionando a entrada do usuáio na lista
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntando se o usuário deseja continuar, removendo todos os espaços à frente e à trás, jogando para minúsculo e pegando apenas a primeira letra
    while continuar not in 'sn':  # Continuar o loop enquanto 'continuar' não for 's' ou 'n':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntando novamente
    
    if continuar == 'n':  # Se 'continuar' for igual a 'n':
        break  # Quebre o loop

print(f'Você digitou {len(numeros)} elementos.')  # Print o len de 'numeros'
numeros.sort(reverse=True)  # Colocando 'numeros' em ordem decressente
print(f'Os valores em ordem decressente são {numeros}')  # Mostrando 'numeros'

if 5 in numeros:  # Se 5 estiver em 'numeros':
    print('O valor 5 faz parte da lista!')
else:  # Se não:
    print('O valor 5 não foi encontrado na lista!')
