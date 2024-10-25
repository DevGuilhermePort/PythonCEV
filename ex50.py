acumulador = 0  # Iniciando o acumulador
contador = 0  # Iniciando o contador
for numero in range(0, 6):  # Laço numero no intervalo de 0 a 6:
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:  # Se o resto da divisão de valor por 2 for igual a 0:
        acumulador += valor  # Acumulador mais valor
        contador += 1  # Contado mais um
print(f'A soma dos {contador} PARES vale {acumulador}')