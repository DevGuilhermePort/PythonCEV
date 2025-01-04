palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')  # Criação da tupla com todas as palavras desejadas

for palavra in palavras:  # Para cada 'palavra' em 'palavras':
    print(f'Na palavra {palavra} temos', end=' ')  # Trocar a quebra de linha por um espaço
    for letra in palavra:  # Para cada 'letra' na 'palavra':
        if letra in 'AEIOU':  # Se a letra estiver no conjunto de vogais 'AEIO':
            print(letra.lower(), end=' ')  # Printar a letra e substituir a quebra de linha por um espaço
    print()  # Printar uma linha em branco
