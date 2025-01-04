from math import sqrt
n = int(input('Digite um número: '))
print(f'O \033[1;32mdobro\033[m de \033[1;36m{n}\033[m vale \033[1;32m{n * 2}\033[m.')
print(f'O \033[1;32mtriplo\033[m de \033[1;36m{n}\033[m vale \033[1;32m{n * 3}\033[m.')
print(f'A \033[1;32mraiz quadrada\033[m de \033[1;36m{n}\033[m é igual a \033[1;32m{sqrt(n):.2f}\033[m')