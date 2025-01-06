def notas(*nota, sit=False):  # Criando a função notas() pedindo um parâmetro empacotado e um parâmetro opcional
    """
    -> Irá calcular o maior e o menor valor entre as notas, o total de notas, alem da média e da situação(opcional).
    : param notas: Recebe todas as notas que o usuário passar como parâmetro.
    : param sit: (Opcional) Recebe True ou false.
    : return: Um dicionário com as informações.
    __Função feita por Port nos primeiros passos do projeto Orion.__
    """
    dados = {
        # Criando o dicionário dados.
    }
    dados["total"] = len(nota)  # Criando a chave total dentro de dados e atribuindo o valor de len de nota.
    dados["maior"] = max(nota)  # Criando a chave literal maior dentro de dados recebendo o maior valor de nota.
    dados["menor"] = min(nota)  # Criando a chave literal menor dentro de dados recebendo o menor valor de nota.
    dados["media"] = sum(nota) / len(nota)  # Criando a chave literal media dentro de dados recebendo o valor da soma de nota divido pela quantia de notas.

    if sit:  # Se o parâmetro sit for verdadeiro:
        if dados["media"] >= 7:  # Se a media for maior ou igual 7:
            dados["situacao"] = "BOA"  # Cria a chave situacao dentro de dados com a situação da turma ("BOA").
        elif dados["media"] >= 5:  # Se não, se a media for maior ou igual 5 (e obviamente menor que 7):
            dados["situacao"] = "RAZOÁVEL"  # Cria a chave situacao dentro de dados com a situação da turma ("RAZOÁVEL").
        else:  # Se não (obviamente menor que 5):
            dados["situacao"] = "RUIM"  # Cria a chave situacao dentro de dados com a situacao da turma ("RUIM").
    
    return dados  # Retorna o dicionário dados.

print(notas(9.5, 5, 7, 6, 4.5, sit=True))  # Chamando a função e passando seus parâmetros.
