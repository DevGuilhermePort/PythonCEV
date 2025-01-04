from random import shuffle #Importei a função de embaralhamento

al1 = str(input('Primeiro aluno: ')).strip().capitalize() #Fiz o usuário dar o valor da variável e a formatei
al2 = str(input('Segundo aluno: ')).strip().capitalize() #Repeti o processo
al3 = str(input('Terceiro aluno: ')).strip().capitalize() #Repeti o processo
al4 = str(input('Quarto aluno: ')).strip().capitalize() #Repeti o processo
lista = [al1, al2, al3, al4] #Montei uma lista
shuffle(lista) #Embaralhei a lista
print(f'A ordem de apresentação é \n{lista}') #Mostrei a lista embaralhada na tela
