nome = str(input('Qual seu nome completo? ')).title().strip() #Fiz o usuário dar o valor da variável string
if 'silva' in nome.lower():            #"Se tiver silva na variável, escreva:"
    print('Seu nome \033[1;32mPOSSUI\033[m "Silva"')
else:                                 #"Caso contrário:"
    print('Seu nome \033[1;31mNÃO POSSUI\033[m "Silva"')
