# As funções "def" (definição de função) são usadas para otimizar tempo e recursos na escrita do código. Uma linha (ou linhas) que se repete uma ou mais vezes dentro de um código pode ser chamada de "ROTINA". Linhas iguais ou semelhantes (Rotinas) podem ser escritas dentro de uma FUNÇÃO antes do código ser escrito, e ser usada dentro do seu código sempre que necessário, não sendo necessário escrever o mesmo código duas vezes, ou até mesmo colá-lo

def soma(a, b):  # Aqui definimos a função "soma" que recebe dois valores como parâmetro, "a" e "b"
    print(f"A = {a} B = {b} ")  # Aqui começa o bloco de instruções da função, onde printamos uma mensagem.
    s = a + b  # Aqui "s" recebe o valor do parâmetro "a" mais o valor do parâmetro "b"
    print(f"A soma de A + B tem valor de {s}")  # Aqui printamos o valor de "s"


    # Codigo principal || Sempre se é recomendado deixar duas linhas de distância entre o código principal e as definições das funções, assim como se é recomendado deixar duas linhas de distância entre uma função e a outra.
soma(4, 5)  # Aqui chamamos a função antes definida "soma", e damos a ela os valores "4" como parâmetro "a" e "5" como parâmetro "b"
soma(5, 5)  # Aqui chamamos a função e damos a ela "5" como ambos os parâmetros, "a" e "b"
soma(b=10, a=7)  # Pode-se mudar a ordem definida deixando explicita a mudança quando a função é chamada
''' "soma(5)" resultaria em um erro, pode que a função "soma()", no início do código foi declarada recebendo apenas dois parâmetros, não mais, e nem menor do que isso '''
