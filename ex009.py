n = int(input('Digite um número para ver sua tabuada: '))
print(f'''\033[1m{'-=' * 10}\033[m
\033[1;36m{n}\033[m x  \033[1;32m1\033[m = \033[1;35m{n}\033[m
\033[1;36m{n}\033[m x  \033[1;32m2\033[m = \033[1;35m{n * 2:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m3\033[m = \033[1;35m{n * 3:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m4\033[m = \033[1;35m{n * 4:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m5\033[m = \033[1;35m{n * 5:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m6\033[m = \033[1;35m{n * 6:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m7\033[m = \033[1;35m{n * 7:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m8\033[m = \033[1;35m{n * 8:}\033[m
\033[1;36m{n}\033[m x  \033[1;32m9\033[m = \033[1;35m{n * 9:}\033[m
\033[1;36m{n}\033[m x \033[1;32m10\033[m = \033[1;35m{n * 10}\033[m
\033[1m{'-=' * 10}\033[m''')
