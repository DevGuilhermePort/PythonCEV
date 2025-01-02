ficha = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    nota_um = float(input('Nota um: '))
    nota_dois = float(input('Nota dois: '))
    media = (nota_um + nota_dois) / 2
    ficha.append([nome, [nota_um, nota_dois], media])

    continuar = str(input('Quer continuar?  [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] '))
    if continuar == 'n':
        break

print('-' * 30)
print(f'{"No.":<6}{"Nome:":<15}{"Média:":>8}')
for pos, valor in enumerate(ficha):
    print(f'{pos:<6}{ficha[pos][0]:<15}{ficha[pos][2]:>8}')
print('-' * 30)

aluno = int(input('Mostrar notas de qual aluno: (999 interrompe): '))
print('-' * 30)
while aluno != 999:
    print(f'Notas {ficha[aluno][0]} de são: {ficha[aluno][1]}')
    print('-' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-' * 30)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
