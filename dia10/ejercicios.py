# 10. Conversión de temperatura (Celsius a Fahrenheit).

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    c = float(input("Introduce la temperatura en Celsius: "))
    f = celsius_a_fahrenheit(c)
    print(f"{c}°C son {f}°F")