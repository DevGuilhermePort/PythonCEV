from random import choice #Importei a função necessária


al1 = str(input('Nome do primeiro aluno: ')).capitalize().strip().split() #Pedi para o usuário falar o nome dos alunos
al2 = str(input('Nome do segundo aluno: ')).capitalize().strip().split() #Formatei todas as variáveis de texto
al3 = str(input('Nome do terceiro aluno: ')).capitalize().strip().split() #Usei strip para remover todos os espaços antes e depois dos nomes
al4 = str(input('Nome do quarto aluno: ')).capitalize().strip().split() #Split para separar todos os nomes refazendo os indicies
lista = [al1, al2, al3, al4] #Formei uma lista
print(f'O aluno sorteado foi {choice(lista)[0]}') #Escolhi um elemento aleatorio da lista, mostrando seu 0