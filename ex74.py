from random import choices  # Importando o método choices da biblíoteca random

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Criando a tupla com os números de 0 a 10

sorteados = (choices(numeros, k=5))  # Escolhendo 5 números aleatórios dessa tupla e os atribuindo a outra tupla

print('Os valores sorteados foram: ', end=' ')  # Mostrando na tela a saída de dados

for pos, numero in enumerate(sorteados):  # A posição e o item dentro de cada indicie da variável composta 'sorteados'
    if pos == len(sorteados) - 1:  # Se a posição for igual ao len de sorteados menos um:
        print(numero)  # Mostre o numero na tela
    else:  # Se não:
        print(numero, end=' ')  # Mostre o numero na tela e troque o fim por um espaço
    if pos == 0:  # Se a pos for igual a 0:
        maior = menor = numero  # Maior e menor passam a ser numero
    else:  # Se não:
        if numero > maior:  # Se numero for maior que maior:
            maior = numero  # Maior passa a ser número
        if numero < menor:  # Se numero for menor que menor:
            menor = numero  # Menor passa a ser numero

print(f'O maior valor sorteado foi {maior}.')  # Mostrar na tela o maior
print(f'O menor valor sorteado foi {menor}.')  # Mostrar na tela o menor
