numero =int(input('Digite um valor: '))
fatorial = 1  # Começar uma multiplicação LIMPA
print(f'{numero}! =', end=' ')
while numero > 0:
    if numero == 1:
        print(numero, end=' = ')
    else:
        print(numero, end=' x ')
    fatorial *= numero
    numero -= 1 
print(f'{fatorial}')
