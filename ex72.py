numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',  # Questões de estética recomendam no máximo 80 linhas
           'dez', 'onze', 'doze', 'treze', 'quatorze',  # Por comando
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')  # Criando a tupla com os números escritos por extenso
escolha = int(input('Digite um número entre 0 e 20: '))  # Perguntando o número para o jogador
while True:  # Enquanto for verdadeiro:
    if escolha >= 0 and escolha <= 20:  # Se a escolha for maior ou igual a zero e menor ou igual a 20:
        break  # Quebre o loop
    escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))  # Perguntando de novo
print(f'Você digitou o número {numeros[escolha]}')  # Escrevendo a respota por extenso
