genero = str(input('Informe seu sexo: ')).strip().upper()[0]  # Informe o sexo, remova todos os espaços na frente e atrás e me de apenas a primeira letra
while genero not in 'MF':  # Enquanto genero não estiver e, 'M' ou 'F':
    genero = str(input('Dados inválidos. Por favor informe seu sexo [M/F]:')).strip().upper()[0]  # Informe o sexo, remova todos os espaços na frente e atrás e me de apenas a primeira letra
print(f'Sexo {genero} registrado com sucesso')
