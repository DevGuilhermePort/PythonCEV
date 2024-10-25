# Informe o sexo, remova os espaços na frente e atrás, jogue para maiúsculo
# e me de a primeira letra
genero = str(input('Informe seu sexo: ')).strip().upper()[0]
while genero not in 'MF':  # Enquanto genero for diferente de M
                           # e F
    # Informe o sexo, revoma os espaços na frente e atras, jogue para maiúsculo
    # e me de apenas a primeira letra [0]
    genero = str(input('Dados inválidos. Por favor informe seu sexo [M/F]:')).strip().upper()[0]
print(f'Sexo {genero} registrado com sucesso')
