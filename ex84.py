pessoas = []  # Criando a lista vazia 'pessoas'
dados = []  # Criando a lista vazia 'dados'
pesados = []  # Criando a lista vazia 'pesados'
leves = []  # Criando a lista vazia 'leves'
maior = menor = 0  # Iniciando as variáveis 'maior' e 'menor'

while True:  # Loop infinito enquanto for True
    dados.append(str(input('Nome: ')).capitalize())  # Adicionando uma string em 'dados[0]'
    dados.append(int(input('Peso: ')))  # Adicionando um inteiro 'dados[1]'
    pessoas.append(dados[:])  # Fazendo uma cópia dos itens de 'dados' para 'pessoas'
    
    if len(pessoas) == 1:  # Se o len de 'pessoas' for igual à um:
        maior = menor = dados[1]  # 'maior' e 'menor' passam a ser 'dados[1]'
    else:  # Se não:
        if dados[1] > maior:  # Se 'dados[1]' for maior que 'maior':
            maior = dados[1]  # 'maior' passa a ser 'dados[1]'
        elif dados[1] < menor:  # Se 'dados[1]' for menor que 'menor':
            menor = dados[1]  # 'menor' passa a ser 'dados[1]'

    dados.clear()  # Limpando a lista 'dados'

    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]  #  Perguntando se o usuário quer continuar, removendo todos os espaçoes antes e depois, jogando para minúsculo e pegando apenas o primeiro indici

    while continuar not in 'sn':  # Enquanto 'continuar' não for 's' ou 'n':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().lower()[0]  # Perguntar novamente

    if continuar == 'n':  # Se 'continuar' for igual a 'n':
        break  # Quebre o loop

for pessoa in pessoas:  # Para cada 'pessoa' em 'pessoas':
    if pessoa[1] == maior:  # Se 'pessoa[1]' for igual à 'maior':
        pesados.append(pessoa[0])  # Adicionar 'pessoa[0]' na lista 'pesados'
    elif pessoa[1] == menor:  # Se não, se 'pessoa[1]' for igual à 'menor':
        leves.append(pessoa[0])  # Adicionar 'pessoa[0]' na lista 'leves'


print(f'Ao todo, você cadastrou {"uma pessoa."if len(pessoas) == 1 else f"{len(pessoas)} pessoas."}')  # Operador ternário para simplicar o 'if/else' dentro de uma f-string
print(f'O maior peso foi de {maior}Kg. Peso de {", ".join(pesados)}.')  # Usando a função join para unir os elementos da lista
print(f'O menor peso foi de {menor}Kg. Peso de {", ".join(leves)}.')  # Usando a função join para unir os elementos da lista
