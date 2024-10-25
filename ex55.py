mais_pesado = 0
mais_leve = 0
for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa} pessoa? '))
    if pessoa == 1:         # O primeiro laço sempre será
        mais_pesado = peso  # o menor
        mais_leve = peso    # e  o maior simultaneamente
    else:
        if peso > mais_pesado:
            mais_pesado = peso
        if peso < mais_leve:
            mais_leve = peso
print(f'O maior peso registrado foi {mais_pesado}KG')
print(f'O menor peso registrado foi {mais_leve}KG') 
