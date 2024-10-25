soma = 0  # Acumulador -> Geralmente vai somando valores
somados = 0  #Contador -> Geralmente soma +1
for numeros in range(1, 501, 2):  # Sempre que eu souber o número de iterações
                                  # eu posso colocar um número a mais no 
                                  # fim e definir o passo desejado
    if numeros % 3 == 0:
        soma += numeros
        somados += 1
print(f'A soma de todos os {somados} valores solicitados é {soma}')
