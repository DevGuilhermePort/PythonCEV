from time import sleep

def contador(inicio, fim, passo):
    if inicio > fim:
        print(f"Contagem de {inicio} até {fim} pulando de {passo} em {passo}")
        for num in range(inicio, fim, passo):
            sleep(0.25)
            print(num, end=' ')
        print("Fim!")
    if fim > inicio:
        

print("-=" * 15)
contador(1, 10, 1)
print("-=" * 15)
contador(10, 0, 2)