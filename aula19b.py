estado = {}  # Criando o dicionário vazio 'estado'
brasil = []  # Criando a lista vazia 'brasil'

for contador in range(0, 3):  # Para cada 'contador' no range de 0 à 3:
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()  # Atruibuindo a entrada do usuário à chave 'uf' do dicionário 'estado'
    estado['sigla'] = str(input('Sigla: ')).strip().upper()  # Atribruindo a entrada do usuário à chave 'sigla' do dicionário 'estado'
    brasil.append(estado.copy())  # Dicionários, diferentes de listas ou tuplas, não podem ser fatiados, portando, não se pode fazer uma cópia de um dicionário usando o fatiamento ( [:] ). Para isso, deve-se usar a função '.copy()'

print(brasil)
print('')

for est in brasil:  # Para cada 'est' na LISTA 'brasil':
    for v in est.values():  # Paraca cada 'v' nos VALORES do DICIONÁRIO 'est'
        print(v, end=' ')  # Print 'v' e substituir a quebra de linha no final por um espaço
    print()  # Quebra de linha ao final de cada laço referente à **LISTA**
