dado = list()
pessoas = list()
leves = list()
pesados = list()
pesado = 0
leve = 0
while True:
    dado.append(str(input('Nome: ')).strip().capitalize())
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        leve = pesado = pessoa[1]
    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        elif pessoa[1] < leve:
            leve = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == pesado:
        pesados.append(pessoa[0])
    elif pessoa[1] == leve:
        leves.append(pessoa[0])
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesado:.2f}Kg. Peso de {pesados}.')
print(f'O menor peso doi de {leve:.2f}Kg. Peso de {leves}.')
