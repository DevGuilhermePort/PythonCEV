def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


lista = [6, 3, 9, 1, 0, 2]
dobra(lista)
print(lista)