def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gols.")

ficha(str(input("Nome do jogador: ")).strip().title(), int(input("Númeo de gols: ")))