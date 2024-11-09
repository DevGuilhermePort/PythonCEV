lista = list()  # Criando a lista vazia

while True:  # Enquanto for verdadeiro
     num = int(input('Digite um número: '))  # Pergunta um número para o usuário
     if num not in lista:  # Se o número não estiver na lista:
         lista.append(num)  # Adicionar na lista
     else:  # Se não:
         print('Valor duplicado! Não vou adicionar.')  # Falar que já possui o número

     continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Perguntar se quer continuar, tirar todos os espaços na frente e atrás, passar para o maiúsculo e pegar apenas o indicie zero
     while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]  # Perguntar se quer continuar, tirar todos os espaços na frente e atrás, passar para o maiúsculo e pegar apenas o indicie zero
     if continuar == 'N':  # Se continuar for igual a não:
            break  # Quebre o loop
     
lista.sort()

print({'-='  * 20})
print(f'Você digitou os os valores {lista}')  # Lista dos dados
