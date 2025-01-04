#importar módulo date
from datetime import date

#Perguntar a idade do nadador ao usuário
nas = int(input('Qual a idade do atleta? '))
ano = date.today().year
idade = ano - nas
print(f'''O atleta tem {idade} anos de idade!''')
#Estrutura condicional aninhada
if idade <= 9:
    print('O atleta irá competir na categoria: Mirim')
elif idade <= 14:
    print('O atleta irá competir na categoria: Infantil')
elif idade <= 19:
    print('O atleta irá competir na categoria: Junior')
elif idade <= 25:
    print('O atleta irá competir na categoria: Sênior')
elif idade < 25:
    print('O atleta irá competir na categoria: Master')
