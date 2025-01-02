num = [12, 7, 2024]  # Criei a lista
print(num)  # Mostrei na tela
num[1] = 6  # Mudei o valor 7 (no indicie 1) para 6
num.append(7)  # Adicionei 7 no fim da lista
print(num)  # Mostrei na tela
num.sort()  # Ordenei a lista
print(num)  # Mostrei na tela de novo
num.sort(reverse= True)  # Ordenando a lista de trás pra frente
print(num)  # Mostrei na tela mais uma vez
print(f'Essa lista tem {len(num)} elementos!')  # Formantando a saída de dados
num.insert(0, 25)  # Inserindo 25 na posição 0
print(num)  # Mostrei na tela novamente
num.pop()  # Removi o último item (6(Passou a ser o último depois que ordenei a lista de trás pra frente ))
print(num)  # Mostrei novamente na tela
del num[0]  # Deletei o item do indicie 0 (25)
print(num)  # Mostrei na tela outra vez
num.append(2024)  # Adicionei 2024 no fim da lista
num.remove(2024)  # Removi o primeiro 2024 que aparece na lista
print(num)  # Mostrei na tela mais uma vez
if 5 in num:  # Se 5 estiver na lista:
    num.remove(5)  # Remove o cinco
else:  # Se não:
    print('Cinco não está na linha!')
for data in num:  # Mostrar data em num
    if data == num[-1]:  # Se data for igual ao último item de num:
        print(data, end='\n')  # Mudei o fim para uma quebra de linha
    else:  # Se não:
        print(data, end='.')  # Mudei o fim para um ponto final
