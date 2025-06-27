# 13. Factorial de un número.

def factorial(a):
    resultado = 1
    for i in range(a):
        resultado *= i

    print(resultado)

factorial(8)
factorial(9)