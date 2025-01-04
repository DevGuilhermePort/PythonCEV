from time import sleep  # Importando a função "sleep" da biblíoteca "random"

def maior(*numeros):  # Definindo a função "maior" fazendo ela receber um empacotamento chamado "numeros"
    maior = menor = 0  # iniciando tanto "maior" quanto "menor" com zero
    print("-=" * 20)
    print("Analisando os valores passados...")
    sleep(1)  # Dando uma pausa de 1 segundo no código
    for posicao, numero in enumerate(numeros):  # Para cada "posicao" e "numero" em "numeros" numerado:
        if posicao == 0:  # Se "posicao" for zero:
            maior = menor = numero  # "maior" e "menor" recebem "numero"
            print(numero, end=", ", flush=True)  # Printando numero, trocando o final e atualizando o fluxo para True, para que a saída seja imediata
            sleep(0.5)  # Dando uma pausa de 0.5 segundos no código
        elif posicao == len(numeros) - 1:  # Se não, se "posicao" for o len de "numeros" menos um:
            print(f"{numero}.", end=' ', flush=True)  # Printa "numero" e um ponto final, substitui a quebra de linha e atualiza o fluxo para True, para a saída ser imediata
            sleep(0.5)  # Pausa o código por 0.5 segundos
            if numero > maior:  # Se "numero" for maior que "maior":
                maior = numero  # "maior" passa a ser "numero"
            if numero < menor:  # Se "numero" for menor que "menor":
                menor = numero  # "menor" passa a ser "numero"
        else:  # Se não:
            print(numero, end=", ", flush=True)  # Printa o "numero", substitui a quebra de linha final e muda o fluxo para True, para o print ter uma saída imediata
            sleep(0.5)  # Dá uma pausa de 0.5 segundos no código de novo
            if numero > maior:  # Se "numero" for maior que "maior":
                maior = numero  # "maior" passa a ser "numero"
            if numero < menor:  # Se "numero" for menor que "menor":
                menor = numero  # "menor" passa a ser "numero"

    print(f"Foram informados {len(numeros)} valores ao todo")  # Pritando o len de "numeros"
    print(f"O maior valor informado foi {maior}")  # Printando o "maior"


# Código principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()