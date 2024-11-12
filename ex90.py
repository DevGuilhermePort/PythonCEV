dados = dict()  # Criando o dicionário 'dados'

dados['nome'] = str(input('Nome: ')).strip().title()  # Criando o elemento 'nome' com o valor dado pela entrada do usuário
dados['média'] = float(input(f'Média de {dados['nome']}: '))  # Criando o elemento 'média' com o valor dado pela entrada do usuário

if dados['média'] >= 6:  # Se 'média' for maio ou igual a seis:
    dados['situação'] = 'Aprovado'  # Criar o elemento 'situação' com o valor de 'Aprovado'
else:  # Se não
    dados['situação'] = 'Reprovado'  # Criar o elemento 'situação' com o valor de 'Reprovado'

for chave, valor in dados.items():  # Para cada 'chave' e 'valor' nos itens de 'dados'
    print(f'{chave.title()} é igual a {valor}')  # Saída de dados
