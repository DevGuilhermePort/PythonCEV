from datetime import date  # Importando a função date da biblíoteca datetime
maiores_de_idade = 0  # Contador
menores_de_idade = 0  # Contador
ano = date.today().year  # Ano recebe o ano atual
mes = date.today().month  # Mes recebe o mês atual
dia = date.today().day  # Dia recebe o dia atual
for pessoa in range(1,8):  # Laço pessoa no intervalo de 1 a 8:
    ano_de_nascimento = int(input(f'Em que ano a {pessoa} nasceu? '))
    mes_de_nascimento = int(input(f'Em que mês a {pessoa} nasceu? '))
    dia_de_nascimento = int(input(f'Em que dia a {pessoa} nasceu? '))
    print('')
    if ano - ano_de_nascimento >= 21:  # Se ano menos ano_de_nascimento for maior ou igual a 21:
        if mes_de_nascimento <= mes:  # Se mes_de_nascimento for menor ou igual a mes:
            if dia_de_nascimento <= dia:  # Se dia_de_nascimento for menor o igual dia:
                maiores_de_idade += 1   # Maiores de idade mais um
    else:  # Se não:
        menores_de_idade += 1
print(f'Ao todo tivemos {maiores_de_idade} pessoas maiores de idade.')
print(f'E também tivemos {menores_de_idade} pessoas  menores de idade.')