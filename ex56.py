idade_homem = 0  # Iniciando idade_homem
homem_mais_velho = ''  # Iniciando homem_mais_velho
mulheres_com_menos_de_vinte = 0  # Contador
media = 0  # Acumulador
for pessoa in range(1, 5):  # Laço pessoa no intervalo de 1 a 5:
    print(f'{'-' * 10}\n{pessoa} PESSOA\n{'-' * 10}')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade? '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    media += idade # Media mais idade
    print('')
    if sexo == 'M':  # Se o sexo for igual a 'M':
        if pessoa == 1:  # Se pessoa for igual a 1:
            homem_mais_velho = nome  # homem_mais_velho passa a ser nome
            idade_homem = idade  # idade_homem passa a ser idade
        else:  # Se não:
            if idade > idade_homem:  # Se idade for maior que idade_homem:
                homem_mais_velho = nome  # homem_mais_velho passa a ser nome
                idade_homem = idade  # idade_homem passa a ser idade
    elif sexo == 'F':  # Se não, se sexo for igual a 'F':
        if idade < 20:  # Se idade for maior que 20:
            mulheres_com_menos_de_vinte += 1  # mulheres_com_menos_de_vinte mais um
media /= pessoa  # media dividido por pessoa
print(f'A média de idade do grupo é {media:.2f} anos de idade.')
print(f'O homem mais velho é o {homem_mais_velho}. Ele tem {idade_homem} anos.')
print(f'E tem {mulheres_com_menos_de_vinte} mulheres com menos de 20 anos')
