palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR',
            'PRAICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')  # Cada palavra dentro da tupla também é uma variável composta
for palavra in palavras:  # Para casa palavra em palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:  # Para cada letra em palavras:
        if letra in 'AÁÃÂÀEÉÊÈIÍÎÌOÓÕÒUÚÛÙ':  # Se a letra dor uma vogal:
            print(f'{letra.lower()}', end='')  # Escreva ela em minúsculo
