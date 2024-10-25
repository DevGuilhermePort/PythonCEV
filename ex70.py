total = tot_mil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).title().strip()
    preco = float(input('Preço: '))
    contador += 1
    total += preco
    if preco >= 1000:
        tot_mil += 1
    if contador == 1 or preco < menor:  # Quando eu possuo dois blocos iguais eu posso simplificar
        menor = preco
        barato = produto
   # else:
   #     if preco < menor:
   #         menor = preco
   #         barato = produto
    continuar = ' '
    while continuar not in 'SN':  # Se continuar não estiver em 'S' ou 'N':
        continuar = str(input('Quer cotinuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':  # Se continuar for igual a 'N':
        break  # Quebre o loop
print(f'O total da compra foi {total:.2f}')
print(f'Temos {tot_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
