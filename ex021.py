from pygame import * #importando todos os itens de pygame

mixer.init() #Usei isso pra iniciar o uso da biblíoteca do Pygame

mixer.music.load('E:\Python\ExAulas\ex021.mp3') #Carregando a música

inicio = bool(input('Digite algo para iniciar: ')) #Pedindo para inserir a variável para o codigo iniciar
print('\033[1m...TOCANDO...\033[m') #apresentando a informação em negrito

mixer.music.play() #Tocando a música

pause = bool(input('Digite algo para pausar: ')) #dando fim a linha de código