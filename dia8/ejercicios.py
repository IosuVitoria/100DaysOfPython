# 8. Calcula el área y perímetro de un círculo.

import math

def caracteristicasCirculo(radio):
    perimetro = 2 * math.pi * radio
    area = math.pow(radio, 2) * math.pi
    return [perimetro, area]

radioProblema = 5

datosCirculo = caracteristicasCirculo(radioProblema)

print("El área del círculo problema es: " + str(datosCirculo[1]));
print("El perímetro del círculo problema es: " + str(datosCirculo[0]));

