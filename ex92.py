from datetime import datetime  # Importando a função 'datetime' da biblíoteca 'datetime'

dados = {}  # Criando o dcionário 'dados' vazio
dados['nome'] = str(input('Nome: ')).strip().lower()  # Criando a chave 'nome' e atribuíndo a entrada do usuário
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))  # Criando a chave 'idade' e atribuíndo a entrada do usuário
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))  # Criando a chave 'ctps' e atribuíndo a entrada do usuário

if dados['ctps'] != 0:  # Se a chave ['ctps'] de 'dados' for diferente de zero:  
    dados['contratação'] = int(input('Ano de contratação: '))  # Criando a chave 'contratação' e atribuíndo a entrada do usuário a ela
    dados['salário'] = float(input('Salário: R$'))  # Criando a chave 'salário' e atribuíndo a entrada do usuário pra ela
    dados['aposentadoria'] = (dados['contratação'] + 35) - datetime.now().year  # Criando a chave 'aposentadoria' e atribuíndo o valor de 'dados['contratação']' mais 35, menor o valor do ano atual ('datetime.now().year')

print('-=' * 15)
for chave, valor in dados.items():  # Para cada 'chave' e 'valor' em 'dados.items()':
    print(f'{chave} tem o valor {valor}.')
print('-=' * 15)
