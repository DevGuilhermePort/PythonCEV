time = []
partidas = []
jogador = {

}
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input("Nome: ")).strip().title()
    jogos = int(input(f"Quantos jogos {jogador['nome']} jogou? "))
    for jogo in range(0, jogos):
        partidas.append(int(input(f"Quantos gols na partida {jogo + 1}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar in 'sn':
            break
        print("ERRO!!! Por favor, responda apenas com 'S' ou 'N'.")
    if continuar == 'n':
        break

print("-" * 40)
print("cod", end='')
for elemento in jogador.keys():
    print(f"{elemento:<15}", end='')
print()

print("-" * 40)
for indicie, valor in enumerate(time):
    print(f"{indicie:>3}", end='')
    for dado in valor.values():
        print(f"{str(dado):<15}", end=' ')
    print()
print("-" * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 interrompe) "))
    if busca == 999:
        break
    if busca > len(time):
        print(f"Não existe jogador com o código {busca}")
    else:
        for indicie, valor in time[busca]['gols']:
            print(f"No jogo {indicie + 1} fez {valor} gols.")
