dicionario = {'nome': 'Melissa', 'sexo': 'F', 'idade': 19}
print(f'A {dicionario['nome']} tem {dicionario['idade']} anos.')

dicionario['tamanho'] = 1.60
print(dicionario.values())

del dicionario['tamanho']
print(dicionario.values())

