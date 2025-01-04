algo = input('Digite algo: ')
print(f'O \033[1;32mtipo primitivo\033[m desse valor é: \033[1;32m{type(algo)}\033[m.')
if algo.isspace() == True:
    print(f'Só tem \033[1;32mespaços\033[m? \033[1;32m{algo.isspace()}\033[m.')
else:
    print(f'Só tem \033[1;32mespaços\033[m? \033[1;31m{algo.isspace()}\033[m.')
if algo.isnumeric() == True:
    print(f'É um \033[1;32mnúmero\033[m? \033[1;32m{algo.isnumeric()}\033[m.')
else:
    print(f'É um \033[1;32mnúmero\033[m? \033[1;31m{algo.isalnum()}\033[m.')
if algo.isalpha() == True:
    print(f'É \033[1;32malfabético\033[m? \033[1;32m{algo.isalpha()}\033[m.')
else:
    print(f'É \033[1;32malfabético\033[m? \033[1;31m{algo.isalpha()}\033[m.')
if algo.isalnum() == True:
    print(f'É \033[1;32malfanumérico\033[m? \033[1;32m{algo.isalnum()}\033[m.')
else:
    print(f'É \033[1;32malfanumérico\033[m? \033[1;31m{algo.isalnum()}\033[m.')
if algo.isupper() == True:
    print(f'Está em \033[1;32mmaiúsculas\033[m? \033[1;32m{algo.isupper()}\033[m.')
else:
    print(f'Está em \033[1;32mmaiúsculas\033[m? \033[1;31m{algo.isupper()}\033[m.')
if algo.islower() == True:
    print(f'Está em \033[1;32mminúsculas\033[m? \033[1;32m{algo.islower()}\033[m.')
else:
    print(f'Está em \033[1;32mminúsculas\033[m? \033[1;31m{algo.islower()}\033[m.')
if algo.istitle() == True:
    print(f'Está \033[1;32mcapitalizada\033[m? \033[1;32m{algo.istitle()}\033[m.')
else:
    print(f'Está \033[1;32mcapitalizada\033[m? \033[1;31m{algo.istitle()}\033[m.')
if len(algo.split()) == 1:
    print(f'Possui \033[1;32m{len(algo.split())}\033[m palavra.')
else:
    print(f'Possui \033[1;32m{len(algo.split())}\033[m palavas.')
if len(algo) == 1:
    print(f'Possui \033[1;32m{len(algo)}\033[m letra.')
else:
    print(f'Possui \033[1;32m{len(algo)}\033[m letras.')
