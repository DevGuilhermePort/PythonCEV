def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"arquivo '{nome}' criado com sucesso.")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo.")
    else:
        from utilidadescev.menu import cabecalho

        cabecalho("PESSOAS CADASTRADAS")
        print(a.read())
