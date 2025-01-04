def titulo(texto):
    print("-" * 30)
    print(f"{texto:^30}")
    print("-" * 30)


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