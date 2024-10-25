contador, acumulador, flag = 0, 0, 0  # Dando valor a três variáveis ao mesmo tempo
while flag != 999:  # Enquanto flag for diferente de 999, repira:
    flag = int(input('Digite um número [999 para parar]: '))  # Flag é o valor dado pelo usuário
    if flag != 999:  # Se flag for diferente de 999:
        contador += 1  # Contador soma um
        acumulador += flag  # Acumulador soma o valor dado pelo usuário
print(f'Foram somados {contador} números.')  # Total de somas
print(f'O total da soma foi {acumulador}')  # Total das somas
