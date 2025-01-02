aluno = {}  # Criando o dicionário 'aluno' vazio

aluno['Nome'] = str(input('Nome: ')).strip().title()  # Criando e atribuindo valor à chave 'Nome'
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))  # Criando e atribuindo valor à chave 'Média'

print('-=' * 15)
if aluno['Média'] >= 7:  # Se 'Média' for maior ou igual à 6:
    aluno['Situação'] = 'aprovado'  # Cria a chave Situação' e atribui o valor 'aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'recuperação'  # Crua a chave 'Situação' e atribui o valor 'reprovado'
else:  # Se não:
    aluno['Situação'] = 'reprovado' # Crua a chave 'Situação' e atribui o valor 'reprovado'

for key, value in aluno.items():  # Para cada 'key' e 'value' nos itens de 'aluno':
    print(f'    - {key} é igual a {value}')
