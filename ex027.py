nome = str(input('Qual seu nome completo? ')).title().strip() #Pedi para o usuário informar seu nome
separado = nome.split() #Usei split no nome para separalo pelos espaços
print('') #Print em branco para o codigo ser mais bonito
print(f'Seu primeiro nome é {separado[0]}.\nE seu ultimo nome é {separado[-1]}.') #Informei o nome no indicie zero e no indicie menos um, quebrando a linha com \n
