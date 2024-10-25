tot18 = totH = totM20 = 0  # Dando o mesmo valor para as três variáveis
while True:  # Enqunato verdadeiro
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # Enquanto sexo não estiver em 'M' ou 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18: # Se idade for maior ou igual a 18:
        tot18 += 1
    if sexo == 'M':  # Se sexo for igual a 'M':
        totH += 1
    if sexo == 'F' and idade < 20:  # Se sexo for igual a 'F' e idade for menor que 20:
        totM20 += 1
    continuar = ' '
    while continuar not in 'SN':  # Se continuar não estiver em 'S' ou 'N'
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':  # Se continuar for igual a 'N':
        break  # Quebre o código
print(f'Total de pessoas com mais de 18: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')