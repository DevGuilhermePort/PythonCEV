pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'o {pessoa['nome']} tem {pessoa['idade']} anos.')
print('')
print(pessoa.keys())
print('')
print(pessoa.values())
print('')
print(pessoa.items())

for k in pessoa.keys():
    print(k)
print('')
for v in pessoa.values():
    print(v)
print('')
for k, v in pessoa.items():
    print(f'{k} = {k}')
print('')


del pessoa['sexo']
for k, v in pessoa.items():
    print(f'{k} = {v}')
print('')

pessoa['nome'] = 'Leandro'

for k, v in pessoa.items():
    print(f'{k} = {v}')
print('')

pessoa['peso'] = 98.5

for k, v in pessoa.items():
    print(f'{k} = {v}')
print('')
