def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    : numero: O número a ser calculado.
    : show: (opcional) Mostrar ou não a conta.
    __Função feita por Port nos primeiros passos do projeto Orion__
    """
    from time import sleep

    fatorial = 1
    for contador in range(numero, 0, -1):
        if show == True:
            if contador == 1:
                print(contador, end=" = ", flush=True)
                sleep(0.5)
            else:
                print(contador, end=" x ", flush=True)
                sleep(0.5)
        fatorial *= contador
    return fatorial

print(fatorial(5, True))