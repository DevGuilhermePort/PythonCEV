ficha = list()  # Criando a lista vazia 'ficha'

while True:  # Loop infinito enquanto for True:
    nome = str(input('Nome: ')).strip().title()  # Criando a variável 'nome'
    nota_um = float(input('Nota um: '))  # Criando a variável 'nota_um'
    nota_dois = float(input('Nota dois: '))  # Crando a variável 'nota_dois'
    media = (nota_um + nota_dois) / 2  # Criando a variável 'media'
    ficha.append([nome, [nota_um, nota_dois], media])  # Adicionando 'nome', 'nota_um', 'nota_dois' e 'media' na lista 'ficha'

    continuar = str(input('Quer continuar?  [S/N] ')).strip().lower()[0]  # Perguntando se o usuário quer continuar, removendo espaços excedentes, jogando para minúsculo e pegando apenas a primeira letra
    while continuar not in 'sn':  # Enquanto 'continuat' não for 's' ou 'n':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] '))  # Perguntar novamente
    if continuar == 'n':  # Se continuar for igual 'n':
        break  # Quebre o loop

print('-' * 30)
print(f'{"No.":<6}{"Nome:":<15}{"Média:":>8}')
for pos, valor in enumerate(ficha):  # Para cada 'pos' e 'valor' na lista numerada 'ficha':
    print(f'{pos:<6}{ficha[pos][0]:<15}{ficha[pos][2]:>8}')
print('-' * 30)

aluno = int(input('Mostrar notas de qual aluno: (999 interrompe): '))  # Perguntar pro usuário qual aluno ele quer ver as notas
print('-' * 30)
while aluno != 999:  # Enquanto 'aluno' for diferente de '999':
    print(f'Notas {ficha[aluno][0]} de são: {ficha[aluno][1]}')
    print('-' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-' * 30)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
