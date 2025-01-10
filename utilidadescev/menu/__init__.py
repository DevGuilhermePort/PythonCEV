def linha(tam=42):
    return "-" * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    from utilidadescev.dado import leiaInt
    
    cabecalho("MENU PRINCIPAL")
    for ind, valor in enumerate(lista):
        print(f"\033[33m{ind + 1:<5}\033[m{"-":<5}\033[34m{valor}\033[m")
    print(linha())
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc