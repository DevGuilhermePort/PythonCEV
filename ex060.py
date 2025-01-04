numero =int(input('Digite um valor: '))
fatorial = 1  # Começar uma multiplicação LIMPA para um acumulador
print(f'{numero}! =', end=' ')  # Definindo o fim como ' '
while numero > 0:  # Se o número for maior que zero:
    if numero == 1:  # Se número for igual a 1:
        print(numero, end=' = ')  # Definindo o fim como ' = '
    else:  # Se não:
        print(numero, end=' x ')  # Definindo o fim como ' x '
    fatorial *= numero  # Fatorial recebe fatorial vezes número
    numero -= 1 #  Número menos um
print(f'{fatorial}')
