dados = []  # Criando a lista dados
principal = []  # E a lista principal
maior = menor = 0  # Iniciando as variáveis 'maior' e 'menor'

while True:  # Loop while infinito
    dados.append(str(input('Nome: ').strip().capitalize()))  # Adicionando na lista uma string do teclado do usuária
    dados.append(float(input('Peso: ')))  # Adicionando um float na lista
    
    if len(principal) == 0:  # Se a lista principal não possui nenhum item dentro:
        maior = menor = dados[1]  # maior e menor passa a ser 'dados[1]'
    else:  # Se  não
        if dados[1] > maior:  # Se dados[1] for maior que 'maior':
            maior = dados[1]  # Maior passa a ser dados[1]
        elif dados[1] < menor:  # Se não, se dados[1] for menor que  'menor':
            menor = dados[1]  # Menor passa a ser dados[1]
            
    principal.append(dados[:])  # Adicionando a lista 'dados' na lista 'principal' 
    dados.clear()  # Limpando a lista 'dados'

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Pedindo uma entrada do usuário, tirando todos os espaços adjacentes, passando para maiúsculo e pegando apenas a primeira letra
    while continuar not in 'SN':  # Se 'continuar' não for 'S' ou 'N':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]  # Repetir a pergunta até que a resposta seja válida
    if continuar == 'N':  # Se a resposta do usuário for 'N':
        break  # Quebre o loop

pesados = []  # Criando a lista 'pesados'
leves = []  # E 'leves'
for pos, pessoa in enumerate(principal):  # Cada 'pos' e 'pessoa' na lista 'principal'
    if pessoa[1] == maior:  # Se pessoa[1] for igual a 'maior':
        pesados.append(pessoa[0])  # Adiciona pessoa[0] na lista 'pesados'
    elif pessoa[1] == menor:  # Se pessoa[1] for igual a 'menor':
        leves.append(pessoa[0])  # Adiciona pessoa[0] na lista 'leves'

print(f'Ao todo você registrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de {pesados}.')
print(F'O menor peso foi de {menor:.2f}Kg. Peso de {leves}')
