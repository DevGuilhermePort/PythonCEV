def fatorial(numero, show=False):  # Definindo a função contador pedindo um valor obrigatório "numero" e um opcional "show":
    """
    -> Calcula o Fatorial de um número.
    : numero: O número a ser calculado.
    : show: (opcional) Mostrar ou não a conta.
    : return: O valor do fatorial do "numero".
    __Função feita por Port nos primeiros passos do projeto Orion__
    """
    from time import sleep  # Importando a função "sleep()" da biblíoteca "time"

    fatorial = 1  # Iniciando a variável "fatorial" com 1
    for contador in range(numero, 0, -1):  # Para cada "contador" no range de "numero" até zero, de menos um em menos um:
        if show == True:  # Se o parâmetro "show" for True:
            if contador == 1:  # Se o "contador" for igual a um:
                print(contador, end=" = ", flush=True)  # Print o valor do "contador", substitua a quebra de linha do fim por " = ", e atualize o parâmetro "flush" para True
                sleep(0.5)  # Pausa no cógido por 0.5 segundos
            else:  # Se não:
                print(contador, end=" x ", flush=True)  # Print o valor do "contador", substitua a quebra de linha final por " x " e atualize o parâmetro "flush" para True
                sleep(0.5)  # Pausa de 0.5 segundos no código
        fatorial *= contador  # "fatorial" recebe "fatorial" vezes "contador"
    
    return fatorial  # Retorna o valor de "fatorial"

print(fatorial(5, True))
