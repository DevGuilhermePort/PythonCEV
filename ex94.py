pessoa = {

}
pessoas= list()

while True:
    pessoa['nome'] = str(input("Nome: ")).strip().title()
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().lower()[0]
        if pessoa in 'mf':
            break
        print('ERRO! Por favor, responda apenas M ou F.')
        
    pessoa['idade'] = int(input("Idade: "))
    pessoas.append(pessoa.copy())
    
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
        if continuar in 'sn':
            break
        print("ERRO! Por favor, responda apenas S ou N.")
        
    if continuar == 'n':
        print("-" * 30)
        break
    print("")

print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")

media = sum(p['idade'] for p in pessoas) / len(pessoas)

print(f"B) A média de idade é de {media} anos.")

mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'f']

print(f"As mulheres cadastradas foram {', '.join(mulheres)}.")
print("D) Lista de pessoas que estão acima da média:")
for count in pessoas:
    if count['idade'] >= media:
        for chave, valor in count.items():
            print(f"{chave} = valor; ", end=" ")
        print()
