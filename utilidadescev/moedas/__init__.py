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
    print("-" * 40)
    print(f"{"RESUMO DO VALOR":^40}")
    print("-" * 40)
    print(f"{"Preço analisado:":<30}{moeda(num)}.")
    print(f"{"Dobro do preço:":<30}{dobro(num, True)}.")
    print(f"{"Metade do preço:":<30}{metade(num, True)}")
    print(f"{f"Com {taxa_aumento}% de aumento fica":<30}{aumento(num, taxa_aumento, True)}")
    print(f"{f"Com {taxa_reducao}% de redução fica":<30}{reducao(num, taxa_reducao, True)}")
    print("-" * 40)
