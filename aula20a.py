def titulo(texto):  # Definindo a função "titutlo" com o parâmetro "texto"
    print("-" * 30)  # Dando suas instruções; Printar "-" trinta vezes
    print(f"{texto:^30}")  # Printando o parâmetro centralizado em trinta caracteres
    print("-" * 30)  # Printando mais trinta "-"


def contador(*num):  # Pra criar uma função onde possamos passar como parâmetro quantos valores nós quisermos, o python nos permite usar o "desempacotamento". Ao usar um asterisco antes de declarar o nome do parâmetro "(*num)", nós "empacotamos" todos os valores declarados como parâmetros dentro de uma lista. Ou melhor, uma tupla.
    print(num)  # Printando a tupla "num" como todos os parâmetros atribuídos à ela
    print("")  # Linha em branco

    print("Recebi os valores ", end='')  # Printando e removendo a quebra de linha do fim
    for valor in num:  # Para cada "valor" na tupla "num":
        print(f"{valor}", end=' ')  # Printar o valor e substituir a quebra de linha final por um espaço
    print("")  # Linha em branco

    print("")  # Outra linha em branco
    tamanho = len(num)  # Declarando a variável "tamanho" recebendo o len de "num"
    print(f"Recebi os valores {num} e são ao todo {tamanho} números.")  # Printado quais valores recebeu e quantos valores são ao todo

titulo("Eu te amo, amor")  # A mensagem passada como parâmetro para a função "titulo"

contador(4, 4, 7, 6, 2)  # Os valores passados como parâmetros para a função "contador"