ficha = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2 
    ficha.append([nome, [nota1, nota2], media])

    continuar = str(input('Quer continuar? [S/N] ')).strip().title()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().title()[0]
    if continuar == 'N':
        print('FIM')
        break

print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)

for pos, aluno in enumerate(ficha):
    print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>8}')

while True:
    print('-' * 30)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        break

    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}.')
print('FIM!!!')