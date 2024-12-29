palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f'Na palavra {palavra} temos', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print()
