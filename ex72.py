numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if escolha >= 0 and escolha <= 20:
        break
    escolha = int(input('Tente novamente. Digite umnúmero entre 0 e 20: '))
print(f'Você digitou o número {numeros[escolha]}')
