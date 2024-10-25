frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # Separa a frase em palavras por espaço
juncao = ''.join(palavras)  # Junta todas as palavras sem espaço('')
inverso = ''  # Contadores também podem ser strings
for letra in range(len(juncao) - 1, -1, -1):  # len = quantos indicies, -1 para ir ate o zero(pois
                                              # o fim corta o último indicie), e -1 para dar o
                                              # passo(de trás pra frente).
    inverso += juncao[letra]
print( f'Você escreveu {juncao}, que ao contrario fica {inverso}')
if juncao == inverso:
    print('A frase É um PALÍNDROMO!!!')
else:
    print('A frase NÃO É um PALÍNDROMO!!!')

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
juncao = ''.join(palavras)
print(f'Você escreveu {juncao}, que ao contrário fica {juncao[::-1]}')  # 
if juncao == juncao[::-1]:
    print('A frase É um PALÍNDROMO!!!')
else:
    print('A frase NÃO É um PALÍNDROMO')
