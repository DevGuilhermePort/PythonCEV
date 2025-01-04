soma = 0  # Acumulador -> Geralmente vai somando valores
somados = 0  #Contador -> Geralmente soma +1
for numeros in range(1, 501, 2):  # Sempre que eu souber o número de iterações eu posso colocar um número a mais no fim e definir o passo desejado
    if numeros % 3 == 0:  # Se o resto da divisão de numeros por 3 for igual a 0:
        soma += numeros  # Soma recebe soma mais número
        somados += 1  # Somados recebe somados mais um
print(f'A soma de todos os {somados} valores solicitados é {soma}')
