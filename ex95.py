partidas = []
jogador = {}
time = []

while True:
    jogador['nome'] = str(input("Nome: ")).strip().title()
    for jogos in range(0, int(input(f"Quantas partidas {jogador['nome']} jogou? "))):
        partidas.append(int(input(f"Quantos gols na partida {jogos + 1}? ")))
    jogador['gols'] = partidas[:]
    partidas.clear()
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    jogador.clear()

    while True:
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
        if continuar in 'sn':
            break
        print("ERRO!!! Por favor responda apenas com 'S' ou 'N'.")
    if continuar == 'n':
            break
    
print("-" * 60)
print(f"{'Cod':>3}", end=' ')
for key in time[0].keys():
    print(f"{key:<25}", end=' ')
print()
for ind, valor in enumerate(time):
    print(f"{ind:>3}", end=' ')
    for dado in valor.values():
        print(f"{str(dado):<25}", end=' ')
    print()
print("-" * 60)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 interrompe) "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Erro! Não existe jogador com o código da busca.")
    else:
        print(f"{'-=' * 3} Levantamento do jogador {time[busca]['nome']} {'-=' * 3}")
        for indicie, gols in enumerate(time[busca]['gols']):
            print("-" * 60)
        print(f"No jogo {indicie}, fez {gols} gols.")
print("<<< FINALIZANDO >>>")
