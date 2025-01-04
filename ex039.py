#Importar a função pra ler o ano atual
from datetime import date

#Informações do usuário
sexo = str(input('Você é do sexo MASCULINO ou FEMININO? ')).strip().lower()
nas = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nas
#Estrutura condicional aninhada para valor se a pessoa deve se alistar, ja se alistou, ou quanto falta para se alistar
print(f'Você tem {idade} ano de idade!')
if sexo == 'feminino':
     print('Você não precisa fazer alistamento militar obrigatório')
elif sexo == 'masculino':
    if idade == 18:
        print('Você deve se alistar imediatamente!!!')
    elif idade < 18:
        print(f'Você deverá se alistar em {18 - idade} anos, no ano de {nas + 18}')
    elif idade > 18:
        print(f'Seu alistamento foi {nas + 18}')