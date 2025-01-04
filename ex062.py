primeiro = int(input('Primeiro termo: '))  # Primeiro termo da PA 
razao = int(input('Razão: '))  # Razão para calcular a PA
contador = 0  # Contador para poder acabar com o loop
termo = 10  # Contar inicialmente até 10 termos
while contador < termo:  # Enquanto contador for menor ou igual a termo, repita
    contador += 1  # Adicionando 1 a variável para não gerar um loop infinito
    print(primeiro, end='-> ')  # Atribuindo '-> ' ao fim do print
    primeiro += razao  # A progressão aritimétca, somando o valor da razao em cada loop realizado
    if contador == termo:  # Quando o contador se tornar maior que termo
        print('PAUSA')
        termo += int(input('\nMostrar mais quantos termos?')) # Somando o valor desejado à termo
print(f'A progressão foi finalizada com {contador} mostrados.')
