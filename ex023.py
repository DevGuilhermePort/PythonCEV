num =  int(input('Digite um valor: ')) #Fiz o usuário informar o valor da variável

print('') #Print em branco para dar espaço no código
print('\033[1;32mAnalisando seu numero...\033[m') #Print da informação para o código fica mais bonito
print('') #print em branco para dar espaço no código

print(f'Unidade = {num // 1 % 10}') #Fiz a divisão inteira do número por 1, e depois peguei seu modulo por 10, para descobrir o valor da unidade
print(f'Dezena = {num // 10 % 10}') #Fiz a divisão inteira do número por 10, e depois peguei seu modulo por 10, para descobrir o valor da dezena
print(f'Centena = {num // 100 % 10}') #Fiz a divisão inteira do número por 100, e depois peguei seu modulo por 10, para descobrir o valor da centena
print(f'Milhar = {num // 1000 % 10}') #Fiz a divisão inteira do número por 1000, e depois peguei seu modulo por 10, para descobrir o valor do milhar
