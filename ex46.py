from time import sleep  # Importando a função desejada
print('\033[1mOs fogos de ano novo ja irão ESTOURAR\033[m!!!')
sleep(2)  # Dando pausa de 2 seg
for contagem in range(10, 0, -1):  # Laço contagem no intervalo 10 até zero de -1 em -1:
    sleep(1)  # Pausa de 1 seg
    print(f'FOGOS EM {contagem}!!!')
sleep(1.25)  # Pausa de 1.25 seg
print('KAH BOOM TATATATA')