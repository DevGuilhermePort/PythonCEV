acumulador = 0
contador = 0
for numero in range(0, 6):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        acumulador += valor
        contador += 1
print(f'A soma dos {contador} PARES vale {acumulador}')