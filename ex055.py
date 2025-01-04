mais_pesado = 0  # Iniciando o mais_pesado
mais_leve = 0  # Iniciando o mais_leve
for pessoa in range(1, 6):  # Laço pessoa no intervalo de 1 a 6:
    peso = float(input(f'Qual o peso da {pessoa} pessoa? '))
    if pessoa == 1:         # O primeiro laço sempre será
        mais_pesado = peso  # o menor
        mais_leve = peso    # e  o maior simultaneamente
    else:  # Se não for o primeiro laço
        if peso > mais_pesado:  # E se o peso for maior que o mais_pesado:
            mais_pesado = peso  # Mais_pesado passa a ser peso
        if peso < mais_leve:  # E se o peso dor menor que o mais_leve:
            mais_leve = peso  # Mais_leve passa a ser peso
print(f'O maior peso registrado foi {mais_pesado}KG')
print(f'O menor peso registrado foi {mais_leve}KG') 
