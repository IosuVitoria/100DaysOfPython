import math

# 3. Calcula el área de un triángulo.

base = 12.25;
altura = 5;

def areaTriangulo(b, h):
    return (b*h)/2

print(areaTriangulo(base, altura));

# Extra: calcula el area y la circunferencia de un círculo y muestar por consola.

radio = 4

def areaCirculo(r):
    return math.pi * r ** 2

def circunferenciaCirculo(r):
    return 2 * math.pi * r

print("Área del círculo:", areaCirculo(radio))
print("Circunferencia del círculo:", circunferenciaCirculo(radio))