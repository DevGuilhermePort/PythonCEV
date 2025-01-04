# Como "desempacotar" nos permite trabalhar apenas com tuplas, nós acabamos tento uma funcionalidade um tanto quanto limitada, justamente pela regra das tuplas. "Tuplas são imutáveis". Como alternativa para isso, nós podemos declarar uma lista inteira como um parâmetro, nos permitindo trabalhar com listas, agora "mutáveis"

def dobra(list):  # Definindo a função "dobra" recebendo um único parametro:
    pos = 0  # Iniciando a variàvel "pos" com zero
    while pos < len(list):  # Enquanto "pos" for menor que o tamanho de "list":
        list[pos] *= 2  # "list" na posição "pos" recebe o dobro
        pos += 1  # Pos recebe mais um
    print(list)  # Printando a lista dobrada


lista = [12, 7, 20, 24]  # Declarando uma lista de números
dobra(lista)  # Chamando a função "dobra" e passando como parâmetro a lista "lista"
