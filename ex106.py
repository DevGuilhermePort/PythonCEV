from time import sleep  # Importando a função sleep() da biblíoteca time.

def mensagem(msg, fonte=0, cor=30):  # Criando a função mensagem recebendo um parâmetro obrigatório e dois opcionais.
    """
    -> Escreve um "título" de cabeçário centralizado com cor personalizada.
    : param msg: A mensagem que vai ser escrita.
    : param fonte: (Opcional) a fonte que vai ser ficar o cabeçário.
    : param cor: (Opcional) a cor da mensagem toda.
    __Função feita por Port nos primeiros passos do projeto Orion.__
    """
    tamanho = len(msg)  # Tamanho recebendo o len de mensagem.
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")  # Printando o tamanho do cabeçário com a cor e a fonte personalizada.
    print(f"\033[{cor}m  {msg}  \033[m")  # Printando a mensagem com a cor escolhida.
    print(f"\033[{fonte};{cor}m{"-" * (tamanho + 4)}\033[m")  # Printando o tamanho do cabeçário com a cor e a fonte personalizada.


def ajuda(comando):  # Definindo a função ajuda() recebendo o parâmetro comando.
    """
    -> Mostra a ajuda interativa do python sobre a biblíoteca ou função pedida.
    : param comando: O comando que você precisa entender.
    __Função feita por Port nos primeiros passos do projeto Orion.__
    """
    mensagem(f"Acessando o manual do comando '{comando}'", cor=32)  # Chamando a função mensagem() dentro da função ajuda().
    sleep(2)  # dando uma pausa de dois segundos.
    help(comando)  # Mostrando a ajuda interativa do comando digitado.

while True:  # Loop infinito:
    mensagem("SISTEMA DE AJUDA PyHELP", 1, 32)  # Chamando a função mensagem().
    resposta = str(input("Função ou biblíoteca: ")).strip().lower()  # Resposta recebendo a entrada do usuário (a função/biblíoteca que ele deseja ver).
    if resposta == "fim":  # Se a resposta do usuário for "fim":
            break  # Quebra o loop.
    else:  # Se não for "fim":
        ajuda(resposta)  # Chamando a função ajuda() passando a entrada do usuário como parâmetro.
    sleep(1)  # Pausando o código por um segundo.
    print('')  # Linha em branco
mensagem("Adeus!", cor=31)  # Adeus em vermelho
