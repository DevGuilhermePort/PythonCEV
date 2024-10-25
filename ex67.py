print(f'{'Tabuada':=^20}')  # Formatei a mensagem de um jeito bonito
while True:  # Repita
    numero = int(input('Digite um número para ver sua tabuada: '))
    tabuada = 1
    if numero < 0:  # Caso o número seja menor que 0 (negativo)
        break  # Quebre o loop
    while True:
        print(f'{numero} x {tabuada} = {numero * tabuada}')
        if tabuada == 10: # Caso tabuada seja menor que 10
            break  # Quebre o loop
        tabuada += 1  # Dando a variável o valor para parar
print('Programa de tabuada encerrado, volte sempre!')