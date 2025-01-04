#Vou importar a função data time para poder informar o ano atual
import datetime

#Pedindo para o usuário informar o ano para ser atribuído a variável
ano = int(input('Digite um ano para saber se ele é bissexto (Coloque zero para analisar o ano atual): '))

#Estrutura condicional simples
if ano == 0: #"Se o ano for igual a zero, substitua o ano pelo ano atual:"
    ano = datetime.date.today().year

#Estrutura condicional composta
#"Se o resto do ano dividido por 4 for igual a zero
#E dividido por 100 for diferente de zero escreva:
#Ou escreva se o resto do ano dividido por 400 for igual a zero"
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!!!')
else:      #"Se não: "
    print(f'{ano} NÃO é um ano bissexto!')
att = datetime.date.today().year
