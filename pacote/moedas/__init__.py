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


def aumentar(num, aumento, format=False):
    if format:
        return moeda(num + (num * (aumento / 100)))
    else:
        return num + (num * (aumento / 100))


def diminuir(num, reducao, format=False):
    if format:
        return moeda(num - (num * (reducao / 100)))
    else:
        return num - (num * (reducao / 100))

def moeda(num):
    return f"R${num:.2f}"