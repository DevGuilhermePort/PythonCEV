#Informações do usuário
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua MÉDIA é {media:.1f}!')
if media == 10:
    print('SUA NOTA FOI PERFEITA!!!')
elif media < 5:
    print('Você foi REPROVADO!!!')
elif 5 <= media < 7:
    print('Você está de RECUPERAÇÃO!!!')
elif media > 7:
    print('Você foi APROVADO!!! Parabéns!')