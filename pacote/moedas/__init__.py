def metade(num, format=False):
    if format:
        return moeda(num / 2)
    else:
        return num / 2


def dobro(num, format=False):
    if format:
        return moeda(num * 2)
    else:
        return num * 2


def aumentar(num, aumento=0, format=False):
    if format:
        return moeda(num + (num * (aumento / 100)))
    else:
        return num + (num * (aumento / 100))


def diminuir(num, reducao=0, format=False):
    if format:
        return moeda(num - (num * (reducao / 100)))
    else:
        return num - (num * (reducao / 100))

def moeda(num):
    return f"R${num:.2f}"


def resumo(num, aumento=0, reducao=0):
    print("-" * 30)
    print(f"{"Resumo do valor":^30}")
    print("-" * 30)
    
    print(f"{"Preço analisado:":<20}{moeda(num)}.")
    print(f"{"Dobro do preço:":<20}{dobro(num, True)}.")
    print(f"{"Metade do preço:":<20}{metade(num, True)}.")
    print(f"{f"{aumento}% de aumento:":<20}{aumentar(num, aumento, True)}.")
    print(f"{f"{reducao}% de redução:":<20}{diminuir(num, reducao, True)}.")
    print("-" * 30)