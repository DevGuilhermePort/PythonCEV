ficha = list()  # Criando uma lista chamda 'ficha'

while True:  # Loop infinito
    nome = str(input('Nome: ')).strip().title()  # Criando a variável 'nome'
    nota1 = float(input('Nota 1: '))  # 'nota1'
    nota2 = float(input('Nota 2: '))  # e 'nota2'
    media = (nota1 + nota2) / 2   # 'media' igual 'nota1' mais 'nota2' dividido por 2
    ficha.append([nome, [nota1, nota2], media])  # Adicionando todas essas variáveis dentro de uma lista para adicionar a 'ficha'

    continuar = str(input('Quer continuar? [S/N] ')).strip().title()[0]  # Pedindo uma entrada do usuário, tirando todos os espaços adjacentes, passando para maiúsculo e pegando apenas a primeira letra
    while continuar not in 'SN':  # Enquanto continuar não for 'S' ou 'N':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().title()[0]  # Repetir a pergunta até que a resposta seja válida
    if continuar == 'N':  # Se continuar for igual a 'N'
        print('FIM')
        break  # Quebre o loop

print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)

for pos, aluno in enumerate(ficha):  # para cada posição e aluno na lista enumerada
    print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>8}')  # Numero do aluno centralizado em 4 espaços a esquerda, nome do aluno centralizado 10 espaços a esquerda, media do aluno centralizada 8 espaços a direita

while True:  # Loop infinito
    print('-' * 30)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))  # Perguntar de qual anluno deseja ver as notas
    if opcao == 999:  # Se a resposta do usuário for '999':
        break  # Quebre o loop

    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}.')
print('FIM!!!')