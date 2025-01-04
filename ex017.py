from math import hypot #Importei apenas a função necessária
co = float(input('Informe o valor do cateto oposto: ')) #Fiz o usuário dar o valor da variável
ca = float(input('Informe o valor do cateto adjacente: ')) #Repeti o processo
print(f'A hipotenusa mede {hypot(co, ca):.2f}') #Usei o métedo importado

print(f'''
A hipotenusa mede {((co ** 2) + (ca ** 2)) ** (0.5):.2f}''') #Método para descobrir a hiponusa sem módulos (Tambem poderia importar sqrt)
