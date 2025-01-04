print(f'''{'=' * 30}
{'BANCO ORION':^30}
{'=' * 30}''')

valor = int(input('Quer sacar quanto? R$'))
total = valor  # Acumulador
nota = 50  # Valor da nota
total_notas = 0  # Total de notas
while True:  # Enquanto for verdadeiro:
    if total >= nota:  # Se o total for igual ou menor que nota:
        total -= nota  # Total perde o valor de nota
        total_notas += 1  # Total de notas mais um
    else:  # Se não:
        if total_notas > 0:  # Se o total_notas for maior que zero
            print(f'Total de {total_notas} de cédulas de R${nota:.2f}')  # Mostre
        if nota == 50:  # Se nota for igual a 50:
            nota = 20  # Nota passa a ser vinte
        elif nota == 20:  # Se nota for igual a 20:
            nota = 10  # Nota passa a ser dez
        elif nota == 10:  # Se nota for igual a dez:
            nota = 1  # Nota passa a ser 1
        total_notas = 0  # Redefine total_notas para 0
        if total == 0:  # Se o total for igual a 0:
            break  # Quebre o loop
print('Obrigado pela preferência! Volte sempre!')
