def voto(nascimento):  # Criando a função "voto()" pedindo um parâmetro
    """
    -> Retorna o valor literal indicando se a pessoa possui voto negado, obrigatório ou opcional
    : nascimento: O ano de nascimento da pessoa
    : return: Situação do voto
    __Função feita por Port nos primeiros passos do projeto Orion__
    """
    from datetime import date  # Importando a função "date()" da biblíoteca "datetime" | Importando uma biblíoteca dentro da função, o escopo desta importação é LOCAL, existindo apenas durante o chamado da função.

    idade = date.today().year - nascimento  # Criando a variável "idade" recebendo o valor do ano atual do sistema menos o parâmetro "nascimento"
    if idade < 16:  # Se a idade for menos que dezesseis anos:
        voto = "NÃO VOTA"  # Não vota
    elif 16 <= idade < 18 or idade >= 65:  # Se a idade for dezesseis ou maior, e menor que dezoito:
        voto = "VOTO OPCIONAL"  # Tem o voto opcional
    else:  # Se não:  (Maior que dezoito)
        voto = "VOTO OBRIGATÓRIO"  # O voto é obrigatório

    return idade, voto  # Retornar o valor de "idade" e "voto"

eleitor = voto(int(input("Em que ano você nasceu? ")))  # Criando a variável "eleitor" que vai receber os valores de "idade" e "voto" de dentro da função de acordo com a entrada do usuário. Os valores serão uma tupla.
print(f"Com {eleitor[0]} anos: {eleitor[1]}")
