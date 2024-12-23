numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

resposta = int(input('Digite um número entre 0 e 20: '))

while resposta < 0 and resposta > 20:
    resposta = int(input('Tente novamnete. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[resposta]}')
