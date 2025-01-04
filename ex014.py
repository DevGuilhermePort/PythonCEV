cel = float(input('Qual a temperatura °C: ')) #O usuário informa a temperatura
fah = (1.8 * cel) + 32 #Converto pra °F usando a fórmula simplificada
print(f'A temperatura de °C {cel} corresponde a {fah}°F') #Printo as informações
cel -= 273.15 #Reatribúo o valor de cel pra usa-lo como kelvin
print(f'E {cel:2f}°K') #printo o valor reatribuído
