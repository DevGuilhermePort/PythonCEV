aluno = list()
alunos = list()

while True:
    aluno.append(str(input('Nome: ')).strip().title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    alunos.append(aluno[:])
    aluno.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break

print('-' * 30)
print(f'{'No.':<10}{'Nome':<15}{'Média':>10}')
for numero, dados in enumerate(alunos):
    print(f'{numero:<10}{dados[0]:<15}{dados[3]:>10}')
print('-' * 30)

nota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
while nota != 999:
    print('-' * 30)
    print(f'Notas de {alunos[nota][0]} são {alunos[nota][1:3]}')
    nota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')