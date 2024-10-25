from datetime import date
maiores_de_idade = 0  # Contador
menores_de_idade = 0  # Contador
ano = date.today().year
mes = date.today().month
dia = date.today().day
for pessoa in range(1,8):
    ano_de_nascimento = int(input(f'Em que ano a {pessoa} nasceu? '))
    mes_de_nascimento = int(input(f'Em que mês a {pessoa} nasceu? '))
    dia_de_nascimento = int(input(f'Em que dia a {pessoa} nasceu? '))
    print('')
    if ano - ano_de_nascimento >= 21:
        if mes_de_nascimento <= mes:
            if dia_de_nascimento <= dia:
                maiores_de_idade += 1 
    else:
        menores_de_idade += 1
print(f'Ao todo tivemos {maiores_de_idade} pessoas maiores de idade.')
print(f'E também tivemos {menores_de_idade} pessoas  menores de idade.')