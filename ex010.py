print(f'\033[1;30;44m{'=' * 25}\033[m')
print(f'\033[1;30;44m{'Conversor De Moedas':^25}\033[m') #Formatei quantas casas eu queria colorir para o conversor de moedas
print(f'\033[1;30;44m{'=' * 25}\033[m') #Nos espaços em branco também
din = float(input('Quanto dinheiro você tem na carteira? R$')) # Atribuí o valor que o usuário informar para a variável din
print(f'Com R${din:.2f} você pode comprar US${(din / 5.43):.2f}.') #Formatei o valor atribuído à variavel e seu valor dividido dentro das chaves
print(f'Com R${din:.2f} você pode comprar {din / 6.8:.2f}€. ') #Formatei o valor dividido na cotação do euro
print(f'Com R${din:.2f} covÊ pode comprar {din * 26.23}JP¥.')
