from time import sleep

def maior(*numeros):
    maior = menor = 0
    print("-=" * 20)
    print("Analisando os valores passados...")
    sleep(1)
    for posicao, numero in enumerate(numeros):
        if posicao == 0:
            maior = menor = numero
            print(numero, end=", ", flush=True)
            sleep(0.3)
        elif posicao == len(numeros) - 1:
            print(f"{numero}.", end=' ', flush=True)
            sleep(0.3)
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        else:
            print(numero, end=", ", flush=True)
            sleep(0.3)
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

    print(f"Foram informados {len(numeros)} valores ao todo")
    print(f"O maior valor informado foi {maior}")


# Código principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()