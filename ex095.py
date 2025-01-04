partidas = []  # Criando a lista vazia "partidas"
jogador = {}  # Criando o dicionário vazio "jogador"
time = []  # Criando a lista vazia "time"

while True:  # Loop infinito enquanto for verdadeiro
    jogador['nome'] = str(input("Nome: ")).strip().title()  # Criando a chave ['nome'] no dicionário "jogador"
    for jogos in range(0, int(input(f"Quantas partidas {jogador['nome']} jogou? "))):  # Para cada "jogos" no range de zero até a entrada do usuário
        partidas.append(int(input(f"Quantos gols na partida {jogos + 1}? ")))  # Adicionando a entrada do usuário na lista "partidas"
    jogador['gols'] = partidas[:]  # Criando a chave ['gols'] com a cópia da lista "partidas" no dicionário "jogador"
    partidas.clear()  # Limpando a lista "partidas"
    jogador['total'] = sum(jogador['gols'])  # Criando a chave ['total'] com a soma ('sum()') da chave ['gols'] no dicionário "jogador"
    time.append(jogador.copy())  # Adicionando dentro de "time" uma cópia do dicionário "jogador"
    jogador.clear()  # Limpando o dicionário jogador

    while True:  # Loop infinito enquanto for True
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]  # Perguntando se o usuário quer continuar
        if continuar in 'sn':  # Se a responta estiver em "s" ou "n":
            break  # Saía imediatamente do loop
        print("ERRO!!! Por favor responda apenas com 'S' ou 'N'.")
    if continuar == 'n':  # Se continuar for igual "n":
            break  # Quebre o loop também
    
print("-" * 60)
print(f"{'Cod':>3}", end=' ')  # Printar "cod" centralizado três cadas à direita, e remover a quebra de linha por um espaço
for key in time[0].keys():  # Para cada "key" em nas chaves do indicie zero de "time":
    print(f"{key:<25}", end=' ')  # Printar "key" centralizado 25 casas à esquerda, e remover a quebra de linha po um espaço
print()  # Quebra de linha

for ind, valor in enumerate(time):  # Para cada "ind" e "valor" em "time" enumerado:
    print(f"{ind:>3}", end=' ')  # Printar "ind" centralizado três casas à direita, e remover a quebra de linha por um espaço
    for dado in valor.values():  # Para cada "dado" nos valores de "valor":
        print(f"{str(dado):<25}", end=' ')  # Printar "valor" transformado em string, centralizado em 25 casas à esquerda, e substituir a quebra de linha por um espaço
    print()  # Quebra de linha
print("-" * 60)

while True:  # Loop while infinito enquanto for verdadeiro
    busca = int(input("Mostrar dados de qual jogador? (999 interrompe) "))  # Criar a variável de busca com a entrada do usuário
    if busca == 999:  # Se "busca" for 999:
        break  # Quebre o loop
    if busca >= len(time):  # Se "busca" for maior ou igual ao len de "time":
        print("Erro! Não existe jogador com o código da busca.")
    else:  # Se não:
        print(f"{'-=' * 3} Levantamento do jogador {time[busca]['nome']} {'-=' * 3}")  # Fazer o levantamento da chave "nome" dentro do indicie "busca" de "time"
        for indicie, gols in enumerate(time[busca]['gols']):  # Para cada "indicie" e "gols" na chave "gols" do indicie "busca" de "time"
            print("-" * 60)
        print(f"No jogo {indicie}, fez {gols} gols.")
print("<<< FINALIZANDO >>>")
