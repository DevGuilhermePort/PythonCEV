print(f'''Para usar cores é necessário ulizar \033[1;32m/n033[m\033[m
Entre os COLCHETES e o M comoloca-se EX: 1; 30; 43
0 = nada
\033[1m1 = negrito\033[m
\033[4m4 = underline\033[m
\033[7m7 = negativo\033[m

\033[30m30 = preto\033[m
\033[31m31 = vermelho\033[m
\033[32m32 = verde\033[m
\033[33m33 = amarelo\033[m
\033[34m34 = azul\033[m
\033[35m35 = lilás\033[m
\033[36m36 = ciano\033[m
\033[37m37 = cinza\033[m''')

n = str(input('Qual seu nome? ')).strip().capitalize()
nome = n.split()
if nome[0] == 'Guilherme':
    print('Você é um ótimo programador!!!')
elif nome[0] == 'Melissa':
    print('MOOMEEUU!!!')
elif n in 'Shaolin Monstro Pietro Cigano Japa Iago':
    print('Te larga maconheiro véio!')
elif n in 'Memel Duda':
    print('Te larga maconheira marginal"')
elif 'Nedeff' in n:
    print('Que rabão, amigo')
print(f'Tenha um bom dia, {nome[0]}!!!')

