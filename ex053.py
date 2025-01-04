frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # Separa a frase em palavras por espaço
juncao = ''.join(palavras)  # Junta todas as palavras sem  os espaços('')
inverso = ''  # Contadores também podem ser strings
for letra in range(len(juncao) - 1, -1, -1):  # len = quantos indicies, -1 para ir ate o zero(pois o fim corta o último indicie), e -1 para dar o passo(de trás pra frente).
    inverso += juncao[letra]  # Inverço concatena o indicie de juncao de acordo com o numero do loop
print( f'Você escreveu {juncao}, que ao contrario fica {inverso}')
if juncao == inverso:  # Se junção for igual a inverso:
    print('A frase É um PALÍNDROMO!!!')
else:  # Se não
    print('A frase NÃO É um PALÍNDROMO!!!')

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
juncao = ''.join(palavras)
print(f'Você escreveu {juncao}, que ao contrário fica {juncao[::-1]}')  # Junção[Do inicio, ao fim, de trás pra frente] 
if juncao == juncao[::-1]:  # Se junção for igual a junção de trás pra frente: 
    print('A frase É um PALÍNDROMO!!!')
else:  # Se não:
    print('A frase NÃO É um PALÍNDROMO')
