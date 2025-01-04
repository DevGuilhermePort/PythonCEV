acumulador = contador = 0  # Se duas variáveis são iguais posso fazer isso
maior = menor = None  # Maior e menor iguais a 'nada'
repetir = 'S'  # Repetir igual a string S
while repetir in 'S':  #Enquanto repetir for igual a S, repita: 
    numero = int(input('Digite um número: '))
    acumulador += numero  # Acumulador igual acumulador mais número
    contador += 1  # Contador igual contador mais um
    if contador == 1:  # Se o contador for 1
        maior = menor = numero  # Maior é igual a menor que é igual a numero
    else:  # se não:
        if numero > maior:  # Se numero for maior que o maior:
            maior = numero  # maior passa a ser numero
        if numero < menor:  # Se o numero for menor que o menor:
            menor = numero  # menor passa a ser numero
    repetir = str(input('Quer continuar?')).strip().upper()[0]
    while repetir not in 'SN':  # Se repetir estiver em 'S' ou 'N' repita:
        print('Opção inválida! Tente novametne!')
        repetir = str(input('Quer continuar? [s/n] ')).strip().upper()[0]
media = acumulador / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}.')
print(f'O maior número é {maior}, e o menor é {menor}.')
