lista = {'nome': 'Melissa', 'sexo': 'F', 'idade': 19}
print(lista)

lista['samaho'] = 1.60
print(lista)

del lista['tamanho']
print(lista)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
