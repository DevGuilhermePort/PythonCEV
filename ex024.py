cid = str(input('Qual o nome da sua cidade? ')).title().strip() #Fiz o usuário dar o valor para a variável
dividido = cid.lower().split() #Usei split para dividir a string
if 'santo' in dividido[0]:                #"se tiver santo no indicie zero, escreva:"
    print(f'{cid} começa com "Santo".')
else:                                     #"Caso contrário:"
    print(f'{cid} não começa com "Santo"')
