# 9. Determina si un número es positivo, negativo o cero.

def mayorOmenor(numero):
    if(numero > 0):
        print("Numero mayor que 0.")
    elif(numero < 0):
        print("Numero menor que 0.")
    else:
        print("El numero es 0.")

a = 5
b = -5
c = 0

mayorOmenor(5);
mayorOmenor(-5);
mayorOmenor(0);