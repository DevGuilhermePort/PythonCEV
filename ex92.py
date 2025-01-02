from datetime import datetime  

dados = {}
dados['nome'] = str(input('Nome: ')).strip().lower()
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - datetime.now().year

print('-=' * 15)
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}.')
print('-=' * 15)
