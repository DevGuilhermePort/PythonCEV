idade_homem = 0
homem_mais_velho = ''
mulheres_com_menos_de_vinte = 0  # Contador
media = 0  # Acumulador
for pessoa in range(1, 5):
    print(f'{'-' * 10}\n{pessoa} PESSOA\n{'-' * 10}')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade? '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    media += idade
    print('')
    if sexo == 'M':
        if pessoa == 1:
            homem_mais_velho = nome
            idade_homem = idade
        else:
            if idade > idade_homem:
                homem_mais_velho = nome
                idade_homem = idade
    elif sexo == 'F':
        if idade < 20:
            mulheres_com_menos_de_vinte += 1
media /= 4
print(f'A média de idade do grupo é {media:.2f} anos de idade.')
print(f'O homem mais velho é o {homem_mais_velho}. Ele tem {idade_homem} anos.')
print(f'E tem {mulheres_com_menos_de_vinte} mulheres com menos de 20 anos')
