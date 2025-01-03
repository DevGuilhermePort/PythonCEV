partidas = []
jogador = {

}

jogador['nome'] = str(input("Nome: ")).strip().title()
jogos = int(input(f"Quantos jogos {jogador['nome']} jogou? "))
for jogo in range(0, jogos):
    partidas.append(int(input(f"Quantos gols na partida {jogo + 1}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])

print(jogador)
print("-=" * 15)
for chave, valor in jogador.items():
    print(f'O campo {chave} vale {valor}.')

print("-=" * 15)
for cont in range(0, jogos):
    print(f"    => Na partida {cont + 1}, fez {jogador['gols'][cont]} gols.")
print(f"Foi um total de {jogador['total']} gols.")
