pessoas = []
dados = []
pesados = []
leves = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    
    if len(pessoas) == 1:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    dados.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break

for pessoa in pessoas:
    if pessoa[1] == maior:
        pesados.append(pessoa[0])
    elif pessoa[1] == menor:
        leves.append(pessoa[0])


print(f'Ao todo, você cadastrou {"uma pessoa."if len(pessoas) == 1 else f"{len(pessoas)} pessoas."}')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for pessoa in pesados:
    if pessoa == pesados[len(pesados) - 1]:
        print(f'{pessoa}.')
    else:
        print(pessoa, end=', ')
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for pessoa in leves:
    if pessoa == leves[len(leves) - 1]:
        print(f'{pessoa}.')
    else:
        print(pessoa, end=', ')
