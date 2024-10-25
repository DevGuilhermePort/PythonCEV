tabuada = int(input('Digite um valor: '))
print(f'Tabuada do {tabuada}.')
print(f'{'-=' * 6}')
for fator in range(1, 11):
    print(f'{tabuada} x {fator:2} = {tabuada * fator}')
print(f'{'-=' * 6}')
