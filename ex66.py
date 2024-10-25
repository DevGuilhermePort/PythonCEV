contador = soma = 0  # Definindo contador e soma ao mesmo tempo. Contador e acumulador
while True:  # Enquanto verdadeiro, repita:
    valor = int(input('Digite um valor: (999 para parar) '))  # Pedi o número
                                                               # e informei o 
                                                               # flag (999)
    if valor == 999:  # Se valor for igual a 999:
        break  # Quebre
    contador += 1  # Contador mais um
    soma += valor  # Soma mais valor
print(f'Você digitou {contador} números.')
print(f'O total da soma foi {soma}.')
