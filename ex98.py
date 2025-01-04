from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= 1
    if passo == 0:
        passo = 1

    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} pulando de {passo} em {passo}.")
    sleep(2)
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(contador, end=" ", flush=True)
            sleep(0.25)
            contador += passo
        print("Fim!")
    else:
        contador = inicio
        while contador >= fim:
            print(contador, end=" ", flush=True)
            sleep(0.25)
            contador -= passo
        print("Fim!")


# Código principal
contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem.")
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))
