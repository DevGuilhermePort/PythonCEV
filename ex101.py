def voto(nascimento):
    """
    -> Retorna o valor literal indicando se a pessoa possui voto negado, obrigatório ou opcional
    : nascimento: O ano de nascimento da pessoa
    : return: Situação do voto
    __Função feita por Port nos primeiros passos do projeto Orion__
    """
    from datetime import date

    idade = date.today().year - nascimento
    if idade < 16:
        voto = "NÃO VOTA"
    elif 16 <= idade < 18 or idade >= 65:
        voto = "VOTO OPCIONAL"
    else:
        voto = "VOTO OBRIGATÓRIO"

    return idade, voto

eleitor = voto(int(input("Em que ano você nasceu? ")))
print(f"Com {eleitor[0]} anos: {eleitor[1]}")