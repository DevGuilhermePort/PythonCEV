def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area_terreno:.1f}m²")


# Código principal
print(" Controle de terrenos")
print("-" * 20)
area(float(input("Lárgura (m): ")), float(input("Comprimento (m): ")))