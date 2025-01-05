# Funções em Python: Conceitos Fundamentais

# Uma função em Python é definida usando a palavra-chave 'def'. 
# A definição de função inclui o nome da função e, opcionalmente, uma lista de parâmetros entre parênteses.

# Exemplo de sintaxe básica:
# def nome_da_funcao(param1, param2=valor_padrao):
#     """Docstring explicando o propósito da função."""
#     corpo_da_funcao
#     return valor_ou_expressao_opcional

# 1. Funções com múltiplos parâmetros:
# Você pode definir funções que aceitam múltiplos parâmetros, inclusive com valores padrão.
# Exemplo:
def saudacao(nome, saudacao="Olá"):
    """Saúda o usuário com um nome e uma saudação personalizados."""
    return f"{saudacao}, {nome}!"

# 2. Funções Lambda (Anônimas):
# Funções lambda são úteis para expressões simples.
# Exemplo:
dobro = lambda x: x * 2

# 3. Funções de Ordem Superior:
# Funções que recebem outras funções como argumento ou retornam funções.
# Exemplo:
def aplicar(funcao, valor):
    """Aplica uma função ao valor fornecido."""
    return funcao(valor)

# 4. Escopo de Variáveis: Global vs Local
# Variáveis definidas dentro de uma função são locais, enquanto as definidas fora são globais.
# Para modificar uma variável global dentro de uma função, use a palavra-chave 'global'.
numero_global = 10

def modificar_global():
    """Modifica a variável global."""
    global numero_global
    numero_global += 5

# 5. Usando 'return':
# 'return' termina a execução de uma função e retorna um valor opcional.
def quadrado(numero):
    """Retorna o quadrado do número fornecido."""
    return numero * numero

# 6. Documentação (Docstrings):
# Use docstrings para documentar suas funções. Descreva o que a função faz, os parâmetros e o valor retornado.
def exemplo_funcao(parametro):
    """
    Explica o que a função faz.
    
    :param parametro: Descreva o parâmetro.
    :return: Descreva o valor retornado.
    """
    pass  # Código da função

# 7. Decoradores:
# Decoradores são usados para modificar ou estender o comportamento de funções ou métodos.
# Exemplo de decorador simples:
def decorador_exemplo(func):
    def wrapper():
        print("Algo antes da função")
        func()
        print("Algo depois da função")
    return wrapper

@decorador_exemplo
def funcao_simples():
    print("Função sendo chamada")

# 8. Módulos e Importação:
# Funções podem ser organizadas em módulos (arquivos .py) e importadas em outros scripts.
# Exemplo de importação:
# from modulo import nome_da_funcao

# 9. Diferença entre 'return' e 'print':
# 'print' exibe o resultado no console, enquanto 'return' envia o resultado de volta para o chamador da função.

# Exemplo de uso de 'return':
def adicionar(a, b):
    """Retorna a soma de a e b."""
    return a + b

# Exemplo de uso de 'print':
print("Essa é uma mensagem para o console")


