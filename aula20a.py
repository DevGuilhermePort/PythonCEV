def titulo(texto):  # Definindo a função "titutlo" com o parâmetro "texto"
    print("-" * 30)  # Dando suas instruções; Printar "-" trinta vezes
    print(f"{texto:^30}")  # Printando o parâmetro centralizado em trinta caracteres
    print("-" * 30)  # Printando mais trinta "-"


def contador(*num):
    print(num)
    print("")

    print("Recebi os valores ", end='')
    for valor in num:
        print(f"{valor}", end=' ')
    print("")

    print("")
    tamanho = len(num)
    print(f"Recebi os valores {num} e são ao todo {tamanho} números.")

titulo("Eu te amo, amor")

contador(4, 4, 7, 6, 2)