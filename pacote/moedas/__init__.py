def metade(num=0, format=False):
    resposta = num / 2
    if format:
        return moeda(resposta)
    else:
        return resposta


def dobro(num=0, format=False):
    resposta = num * 2
    if format:
        return moeda(resposta)
    else:
        return resposta


def aumento(num=0, taxa=0, format=False):
    resposta = num + (num * taxa / 100)
    if format:
        return moeda(resposta)
    else:
        return resposta


def reducao(num=0, taxa=0, format=False):
    resposta = num - (num * taxa / 100)
    if format:
        return moeda(resposta)
    else:
        return resposta


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")


def resumo(num=0, taxa_aumento=10, taxa_reducao=5):
    print("-" * 30)
    print(f"{"RESUMO DO VALOR":^30}")
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(num)}.")
    print(f"Dobro do preço: \t{dobro(num, True)}.")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"Com {taxa_aumento}% de aumento fica \t{aumento(num, taxa_aumento, True)}")
    print(f"Com {taxa_reducao}% de redução fica \t{reducao(num, taxa_reducao, True)}")