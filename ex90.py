dados = dict()  # Criando o dicionário 'dados'

dados['nome'] = str(input('Nome: ')).strip().title()  # Criando o elemento 'nome' com o valor dado pela entrada do usuário
dados['média'] = float(input(f'Média de {dados['nome']}: '))  # Criando o elemento 'média' com o valor dado pela entrada do usuário

if dados['média'] >= 7:  # Se 'média' for maior ou igual a seis:
    dados['situação'] = 'Aprovado'  # Criar o elemento 'situação' com o valor de 'Aprovado'
elif dados['média'] >= 5 and dados['média'] < 7:  # Se não, se  'média' for maior que cinco e menor que 7:
    dados['situação'] = 'Recuperação'  # Criar o elemento 'situação' com o valor de 'Recuperação'
else:  # Se não
    dados['situação'] = 'Reprovado'  # Criar o elemento 'situação' com o valor de 'Reprovado'

for chave, valor in dados.items():  # Para cada 'chave' e 'valor' nos itens de 'dados'
    print(f'{chave.title()} é igual a {valor}')  # Saída de dados
