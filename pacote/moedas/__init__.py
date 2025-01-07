def metade(num=0, format=False):
    resposta = num / 2
    return resposta


def dobro(num=0, format=False):
    resposta = num * 2
    return resposta


def aumento(num=0, taxa=0, format=False):
    resposta = num + (num * taxa / 100)
    return resposta


def reducao(num=0, taxa=0, format=False):
    resposta = num - (num * taxa / 100)
    return resposta


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")
