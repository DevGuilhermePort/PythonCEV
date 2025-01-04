from random import randint #Importei a função para aleatorizar um número inteiro dentro do range
from time import sleep #Importei a função pra pausar alguns segundos o código

#Fiz putice com cor printando a mensagem do jogo
print('Irei \033[1;36mpensar\033[m em um \033[1;36mnúmero\033[m de \033[1;36mzero\033[m a \033[1;36mcinco\033[m, tente acertar o \033[1;36mnúmero\033[m que \033[1;36mpensei\033[m para me \033[1;36mVENCER\033[m!')

#Aleatorizei um número e atribuí para a variável num
num = randint(0, 5)

#Fiz putice com cor perguntando ao usuário qual número foi escolhido
win = int(input('Em qual \033[1;36mnúmero\033[m eu \033[1;36mpensei\033[m? '))

#Usando o módulo importado para pausar o tempo
print('\033[1;36mPROCESSANDO\033[m...')
sleep(3)

#Estrutura condicional composta "se" e "se não"
if win == num: #"Se win for igual a num, escreva:"
    print('Você me \033[1;36mVENCEU\033[m!!!')
else:          #"Se não:"
    print(f'Você \033[1;31mPERDEU\033[m... \033[1;32mMais sorte\033[m na próxima. o numero pensado \033[1;31mNÃO\033[m foi \033[1;31m{win}\033[m!')
print(f'O número pensado foi \033[1;36m{num}\033[m')
