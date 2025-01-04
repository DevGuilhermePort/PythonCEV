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


contador(4, 4, 7, 6, 2)