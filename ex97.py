def escreva(string):  # Criando a função "escreva()" pedindo como parâmetro um único valor chamado "string"
    tamanho = len(string) + 4
    print("~" * tamanho)  # Printar "~" de acordo com o tamanho de "string"
    print(f"  {string}  ")
    print("~" * tamanho)  # Printar "~" de acordo com o tamanho de "string"


# Código principal
escreva("Guilherme + Melissa == S2")  # Chamando o código para teste
escreva("Projeto: ORION")
escreva("Primeiro passo")