nome = str(input('Qual seu nome completo? ')).strip() #Pedi para usuário informar a variável nome e formatei ela

print('') #Print em branco para espaçar o código

print('\033[1;32mAnalisando seu nome...\033[m') #Botei a informção na tela para ficar mais bonito

print(f'Seu nome ocm todas as letras maiúsculas é {nome.upper()}') #Usei a função upper para printar o nome completamente em maiúsculo

print(f'Seu nome com todas as letras minúsculas é {nome.lower()}') #Usei a função lower para printar com todas as letras em minúsculo


espaços = nome.count(' ') #Contei quantos espaços a string tem ao todo
print(f'Seu nome tem ao todo {len(nome) - espaços}') #Medi o cumprimento da string e subtraí a quantidade de espaços


dividido = nome.split() #Dividi o nome com split
print(f'Seu primeiro nome tem ao todo {len(dividido[0])} letras') #Medi o cumprimento do indicie zero
