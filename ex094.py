pessoa = {
    # Criando o dicionário "pessoa" vazio
}
pessoas= list()  # Criando a lista "pessoas" vazia

while True:  # Loop infinito enquanto for True:
    pessoa['nome'] = str(input("Nome: ")).strip().title()  # Criar a chave "nome" no dicionário "pessoa" e adicionar a entrada do usuário a ele
    while True:  # Enquanto for vedadeiro:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]  # Criar a chave literal "sexo" no dicionário "pessoa" e adicionar a entrada do usuário a ele
        if pessoa['sexo'] in 'MF':  # Se o sexo estiver entre "M" ou "F":
            break  # Quebre o loop
        print('ERRO! Por favor, responda apenas M ou F.')
        
    pessoa['idade'] = int(input("Idade: "))  # Criar a chave literal "idade" no dicionário "pessoa" e adicionar a entrada do usuário a ele
    pessoas.append(pessoa.copy())  # Adicionando uma cópia de "pessoa" dentro de "pessoas"
    
    while True:  # Enquanto for verdadeiro:
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]  # Perguntar se o usuário quer continuar
        if continuar in 'sn':  # Se a resposta estiver entre 's' e 'n':
            break  # Quebre o loop
        print("ERRO! Por favor, responda apenas S ou N.")
        
    if continuar == 'n':  # Se continuar for igual a 'n':
        print("-" * 30)
        break  # Quebre o loop
    print("")

print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")

media = sum(p['idade'] for p in pessoas) / len(pessoas)  # Usando um laço com variável de controle para definir uma variável. Usando a função "sum" para somar "p['idade']" para cada "p" em "pessoas", depois dividir tudo isso pelo "len" de "pessoas"
print(f"B) A média de idade é de {media:5.2f} anos.")  # A média formatada em 5 caracteres e com 2 numeros depois do ponto flutuante
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']  # Criando uma lista usando um laço com variável de controle. Me dê o "p['nome']" para cada "p" se o "p['sexo']" for igual a "F"
print(f"C) As mulheres cadastradas foram {" e ".join(mulheres) if len(mulheres) <= 2 else ', '.join(mulheres)}.")  # Usando o operador ternário para deixar o código mais compacto. Use "" e ".join(mulheres)" se o len de "mulheres" for dois, se não, use "", ".join(mulheres)"
print("D) Lista de pessoas que estão acima da média:")
for count in pessoas:  # Para cada "cout" em "pessoas":
    if count['idade'] >= media:  # Se "count['idade']" for maior ou igual à "media":
        for chave, valor in count.items():  # Para cada "chave" e "valor" nos itens de "count":
            print(f"{chave} = {valor}; ", end=" ")
        print()
print("")
print("<<< ENCERRANDO >>>")
