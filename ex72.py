numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')  # Criação da tupla com os números de 0 á 20 por extenso

resposta = int(input('Digite um número entre 0 e 20: '))  # Resposta do usuário

while resposta < 0 and resposta > 20:  # Se a resposta for menor que 0 ou maior que 20:
    resposta = int(input('Tente novamnete. Digite um número entre 0 e 20: '))  # Respota inválida, perguntar de novo

print(f'Você digitou o número {numeros[resposta]}')  # Mostrando a saída da resposta do usuário
