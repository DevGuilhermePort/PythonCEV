n = str(input('Qual seu nome? ')).strip().capitalize().split()
print(f'é um prazer te conhecer \033[35m{n[0]}\033[m')
if n[0] == 'Melissa':
    print('MOMEUUU!!!\033[1;31mEu te amo muito\033[0;31m, momeu!!!')
elif n[0] == 'Kauan':
    print(f'\033[36mNedeff rabudo\033[m!')
else:
    print('Acho que não te conheco.')