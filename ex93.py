total = 0
gols = []
jogador = {

    'nome': str(input('Nome: ')).strip().title()

}
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for partida in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {partida}? ")))
    total += gols[partida]
jogador['gols'] = gols
jogador['total'] = total

print('-=' * 15)
print(jogador)
print('-=' * 15)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")
print('-=' * 15)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for cont in range(0, partidas):
    print(f'Na partida {cont}, fez {jogador['gols'][cont]}.')
print(f'Foi um total de {total} gols.')