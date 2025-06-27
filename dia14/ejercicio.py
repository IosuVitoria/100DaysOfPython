# Números del 1 al 100 divisibles por 3 y 5.

def divisiblesEntre3y5():
    for i in range(100):
        if i%3 == 0 and i%5 == 0:
            print(i);

divisiblesEntre3y5()