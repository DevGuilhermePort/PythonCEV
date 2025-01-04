partidas = []  # Criando a lista vazia "partidas"
jogador = {
    
}  # Criando o dicionário vazio "jogador"

jogador['nome'] = str(input("Nome: ")).strip().title()  # Criando a chave "nome" no dicionário
jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))  # Criando a variável "jogos"
for count in range(0, jogos):  # Para cada "count" no range de zero à "jogos"
    partidas.append(int(input(f"Quantos gols na partida {count + 1}: ")))  # Adicionar na lista "partidas" o valor da entrada do usuário
jogador['gols'] = partidas[:]  # Criar a chave "gols" com o valor de "partida" no diconário "jogador"
jogador['total'] = sum(partidas)  # Criando a chave "total" com o valor da soma dos valores de "partidas" dentro de "jogador"

print(f"{'-' * 45}\n{jogador}\n{'-' * 45}")
print("")

print("-" * 45)
for chave, valor in jogador.items():  # Para cada "chave" e "valor" em "jogador.items()":
    print(f"O campo {chave} tem valor {valor}")
print("-" * 45)
print('')

print(f"{'-' * 45}\nO jogador {jogador['nome']} jogou {jogos} partidas.")
for count in range(0, jogos):  # Para cada "count" no range de zero à "jogos"
    print(f" => Na partida {count + 1}, fez {jogador['gols'][count]}.")
print(f"Foi um total de {jogador['total']} gols.")
print("-" * 45)
