from random import randint  # Importando a função "randint" da biblíoteca "random"
from time import sleep  # Importando a função "sleep" da biblíoteca

def aleatorizar(sorteio):  # Definindo a função "aleatorizar" recebendo o parâmetro "sorteio"
    print("Sorteando 5 valores da lista: ", end="", flush=True)  # Printando, removendo a quebra de linha e atualizando o fluxo para True, para uma saída de dados imediata
    sleep(1.5)  # Pausar o código por 1.5 segundos
    for cont in range(0, 5):  # Para cada "cont" no range de 0 à 5:
        sorteio.append(randint(1, 10))  # Adicionando um número aleatório dentro de "sorteio"
        print(sorteio[cont], end=" ", flush=True)  # Printando  o valor na posição "cont" de "sorteio"
        sleep(0.5)  # Pausando o código por 0.5 segundos
    print("Pronto!")

def soma_par(lista):  # Definindo a função "soma_par" recebendo o parâmetro "lista":
    somapar = 0  # Iniciando a variável "somapar" com zero
    for par in lista:  # Para cada "par" em "lista":
        if par % 2 == 0:  # Se o resto de "par" dividido por dois for zero:
            somapar += par  # "somapar" soma mais "par"
    
    print(f"Somando os valores pares de {lista}, temos {somapar}.")  # Saída dos dados


# Código principal
numeros = []  # Iniciando uma lista vazia
aleatorizar(numeros)  # Chamando as funções
soma_par(numeros)