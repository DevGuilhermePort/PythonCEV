aluno = {}  # Criando o dicionário 'aluno' vazio

aluno['Nome'] = str(input('Nome: ')).strip().title()  # Criando e atribuindo valor à chave 'Nome'
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))  # Criando e atribuindo valor à chave 'Média'

if aluno['Média'] >= 6:  # Se 'Média' for maior ou igual à 6:
    aluno['Situação'] = 'aprovado'  # Cria a chave Situação' e atribui o valor 'aprovado'
else:  # Se não:
    aluno['Situação'] = 'reprovado' # Crua a chave 'Situação' e atribui o calor 'reprovado'

for key, value in aluno.items():  # Para cada 'key' e 'value' nos itens de 'aluno':
    print(f'{key} é igual a {value}')