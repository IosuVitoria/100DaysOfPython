from datetime import datetime

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    edad = anio_actual - anio_nacimiento
    return edad

print("Edad de alguien nacido en 1990:", calcular_edad(1985))  
print("Edad de alguien nacido en 2005:", calcular_edad(2005)) 