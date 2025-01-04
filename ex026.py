frase = str(input('Escreva uma frase: ')).strip() #Fiz o usuário dar o valor a variável string

print(f'A letra "A" aparece {frase.lower().count('a')} na frase.') #Pedi para procurar quantas vezes a letra 'a' aparece em minúsculo na frase transformada em minúsculo
print(f'Ela aparece pela primeira vez na letra {frase.lower().find('a') + 1}.') #Pedi para procurar a primeira vez que a letra 'a' em minúsculo aparece na frase passada para o minúsculo
print(f'E aparece pela última dez na {frase.lower().rfind('a') + 1}')#Pedi para procurar a primeira vez que a letra 'a' em minúsculo aparece na frase passada para o minúsculo da direita para a esquerda
