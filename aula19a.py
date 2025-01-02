brasil = list()  # Criando a lista vazia 'brasil'
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}  # Criando o dicionário 'estado1' com as chaves 'uf' e 'sigla' já definidas
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  # Criando o dicionário 'estado2' com as chaves 'uf' e 'sigla' já definidas
brasil.append(estado1)  # Adicionando 'estado1' na lista 'brasil'
brasil.append(estado2)  # Adicionando 'estado2' na lista 'brasil'

print(brasil[0])  # Acessando o indicie zero da lista 'brasil'
print(brasil[1])  # Acessando o indicie um da lista 'brasil'
print(brasil)  # Printando 'brasil'
print('')
print(brasil[0]['uf'])  # Printando o valor da chave literal 'uf' de 'brasil[0]'
print(brasil[1]['sigla'])  # Printando o valor da chave literal 'sigla' de 'brasil[1]'