def area(largura, comprimento):  # Definindo a função "area()" pedindo dois parâmetros:
    area_terreno = largura * comprimento  # "area_terreno" tem o valor do parâmetro "largura" vezes o parâmetro "comprimento"
    print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area_terreno:.1f}m²")  # Printando a saída dos dados


# Código principal
print(" Controle de terrenos")
print("-" * 20)
area(float(input("Lárgura (m): ")), float(input("Comprimento (m): ")))  # Chamando a função "area" recebendo duas entradas do usuário como parâmetro