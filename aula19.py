pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}  # Criando o dicionário 'pessoa' com as chaves 'nome', 'sexo' e 'idade' já definidos
print(f'o {pessoa['nome']} tem {pessoa['idade']} anos.')  # Usando a chave literal pra acessar elementos do dicionário
print('')  
print(pessoa.keys())  # A função '.keys()' nos mostra apenas as chaves literais do dicionário, como: 'nome', 'sexo' e 'idade'
print('')
print(pessoa.values())  # A função '.values() nos mostra os valores presentes nas chaves, como: 'Gustavo', 'M' e 22
print('')
print(pessoa.items())  # A função '.items()' mostra tanto os valores('Gustavo', 'M', 22), quanto as chaves ('nome', 'sexo', 'idade')

for k in pessoa.keys():  # Para cada 'k' nas chaves de 'pessoa':
    print(k)  # Print 'k'
print('')
for v in pessoa.values():  # Para cada 'v' nos valores de 'pessoa':
    print(v)  # Print 'v'
print('')
for k, v in pessoa.items():  # Para cada 'k' e 'v' nas chaves e valores de 'pessoa':
    print(f'{k} = {k}')  # Print 'k' e 'v'
print('')


del pessoa['sexo']  # Usar o comando 'del' pode excluir um item do dicionário
for k, v in pessoa.items():  # Para cada 'k' e 'v' nas chaves e valores de 'pessoa':
    print(f'{k} = {v}')  # Print 'k' e 'v'
print('')

pessoa['nome'] = 'Leandro'  # Posso reatribuir valores a chaves, como trocar o valor da chave 'nome' de 'Gustavo para 'Leandro'

for k, v in pessoa.items():  # Para cada 'k' e 'v' nas chaves e valores de 'pessoa':
    print(f'{k} = {v}')
print('')

pessoa['peso'] = 98.5  # Posso adicionar um elemento simplismente escrevendo o nome do dicionário, o nome da chave literal a ser adicionada entre colchetes, e atribuir um valor para a mesma 

for k, v in pessoa.items():  # Para cada 'k' e 'v' nas chaves e valores de 'pessoa':
    print(f'{k} = {v}')  # Print 'k' e 'v'
print('')
