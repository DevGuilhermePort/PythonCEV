'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''
resposta = 's'  # Iniciando a vaipavel resposta
while resposta == 's':  # Enquanto resposta for igual a 's':
    numero = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]