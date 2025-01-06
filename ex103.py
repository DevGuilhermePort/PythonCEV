def ficha(nome="<desconhecido>", gols=0):  # Definindo a função "ficha()" pedindo dois .parâmetros opcionais
    """
    -> Cria um dicionário recebendo os parâmetros "nome" e "gols.
    : param nome: (Opcional) recebe o nome do jogador.
    : param gols: (Opcional) recebe a quantidade de gols feita pelo jogador.
    : return: Retorna um dicionário com as chaves "nome" e "gols".
    __Função feita por Port nos primeiros passos do projeto Orion.__
    """
    return {"nome": nome, "gols": gols}  # Retornando um dicionário com as chaves "nome" e "gols" recebendo os parâmetros opcionais "nome" e "gols".


# Programa principal:
nome = str(input("Nome do jogador: ")).title().strip()  # Criando a cariável "nome" pedindo a entrada do usuário.
gol = str(input("Número de gols: "))  # Criando a variável "gol" pedindo a entrada do usuário dando o número de gols convertido pra strings.

if gol.isnumeric():  # Se gol é um número:
    int(gol)  # Converter gol pra um número inteiro.
else:  # Se não for um número:
    gol = 0  # Gol recebe zero.

if nome == "":  # Se o nome estiver vazio:
    jogador = ficha(gols=gol)  # Criar a variável jogador recebendo o valor da função ficha() passando apenas o parâmetro gols recebendo o valor de gol.
else:  # Se o nome não estiver vazio:
    jogador = ficha(nome, gol)  # Criar a variável jogador recebendo o valor da função ficha() recebendo seus dois parâmetros.

print(f"O jogador {jogador["nome"]} fez {jogador["gols"]} gols.")  # Acessando os valores do dicionário através das suas chaves literais.