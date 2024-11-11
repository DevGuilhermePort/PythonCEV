dado = list()
pessoas = list()
pesados = list()
leves = list()
cont = leve = pesado = 0

while True:
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    if cont == 0:
        leve = dado[1]
        leves.append(leve)
        pesado = dado[1]
        pesados.append(pesados)
    if dado[1] > pesado:
        pesado = dado[1]
        pesados.append(dado[0])
    elif dado[1] < leve:
        leve = dado[1]
        leves.append(dado[0])
    dado.clear()
    cont += 1

    repetir = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    while repetir not in 'SN':
        repetir = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if repetir == 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesado:.2f}Kg. Peso de {pesados}')
print(f'O menor peso foi {leve:.2f}Kg. Peso de {leves}')