**Variables**

Una variable es un nombre simbólico que hace referencia a un valor almacenado en la memoria. *A diferencia de otros lenguajes de programación, Python es dinámicamente tipado, lo que significa que no necesitas declarar explícitamente el tipo de una variable.* Python infiere (deduce) el tipo de dato basándose en el valor que le asignes.

1. **Nomenclatura de Variable**.

- *Caracteres permitidos*: Pueden contener letras (mayúsculas y minúsculas), números y guiones bajos (_).
- *No pueden empezar con un número*: Deben comenzar con una letra o un guion bajo.
- *Sensible a mayúsculas y minúsculas*: miVariable es diferente de mivariable.
- *Evitar palabras reservadas*: No puedes usar palabras clave de Python (como if, for, while, def, class, etc.) como nombres de variables.
- *Convención de estilo (PEP 8)*: Se recomienda usar snake_case (todo en minúsculas y palabras separadas por guiones bajos) para nombres de variables y funciones (ej: nombre_de_usuario, edad_del_cliente).

-- EJEMLOS DE VARIABLES MAL NOMBRADAS --

# 1nombre = "Bob"  # No puede empezar con número
# for = "Ciclo"    # 'for' es una palabra reservada
# mi-variable = 5  # El guion medio no está permitido

2. **Asignación de Valores**

El operador de asignación en Python es el signo igual (=).

**x = 10**         # Asigna el valor 10 a la variable x
**nombre = "Iosu"** # Asigna la cadena "Juan" a la variable nombre
**pi = 3.14159**   # Asigna el valor flotante 3.14159 a pi
**es_activo** = True # Asigna el valor booleano True a es_activo

*Asignación Múltiple*: Puedes asignar múltiples variables en una sola línea.


3. **Tipos de Datos Comunes**

Python tiene varios tipos de datos incorporados. Los más comunes son:

*Números:*
A) *int (Enteros)*: Números sin decimales (ej: 5, -100, 0).
B) *float (Flotantes)*: Números con decimales (ej: 3.14, -0.5, 2.0).
C) *complex (Complejos)*: Números con parte real e imaginaria (ej: 1 + 2j).

*str (Cadenas de Texto)*: Secuencias de caracteres encerradas entre comillas simples (') o dobles (").
*bool (Booleanos)*: Representan valores de verdad, True o False.

*Colecciones*:
A) *list (Listas)*: Colección ordenada y mutable de ítems (ej: [1, 2, 'a', True]).
B) *tuple (Tuplas)*: Colección ordenada e inmutable de ítems (ej: (10, 20, 30)).
C) *dict (Diccionarios)*: Colección desordenada de pares clave-valor (mutable) (ej: {'nombre': 'Ana', 'edad': 25}).
D) *set (Conjuntos)*: Colección desordenada de ítems únicos (ej: {1, 2, 3}).

4. **Mutabilidad e Inmutabilidad**

Un concepto importante es si un tipo de dato es mutable (su valor puede ser cambiado después de la creación) o inmutable (su valor no puede ser cambiado una vez creado).

A) *Inmutables*: Números (int, float, complex), Cadenas (str), Tuplas (tuple), Booleanos (bool).
B) *Mutables*: Listas (list), Diccionarios (dict), Conjuntos (set).

**Operadores en Python**

Los operadores son símbolos especiales que realizan operaciones sobre uno o más operandos (variables o valores).

1. *Operadores Aritméticos*
Realizan cálculos matemáticos.

**Operador**	*Descripción*	        *Ejemplo*	*Resultado*
    +	            Suma	              5 + 3	        8
    -	            Resta	              10 - 4	    6
    *	            Multiplicación	       6 * 2	    12
    /	            División (flotante)	  10 / 3	  3.333...
    //	            División entera     	10 // 3 	3
    %	            Módulo (resto)	      10 % 3	    1
    **	            Exponenciación	      2 ** 3	    8


2. **Operadores de Asignación**

*Se utilizan para asignar valores a variables*. Pueden combinar una operación aritmética con la asignación.

*Operador*	    *Equivalente a* 	*Ejemplo*
    =	        Asignación simple	 x = 10
    +=	            x = x + y	     x += 5
    -=	            x = x - y      	 x -= 2
    *=	            x = x * y	     x *= 3
    /=	            x = x / y	     x /= 2
    //=	            x = x // y	     x //= 3
    %=	            x = x % y	     x %= 4
    **=         	x = x ** y	     x **= 2


3. **Operadores de Comparación (Relacionales)**

Se utilizan para comparar dos valores y siempre devuelven un valor booleano (True o False).

**Operador**	**Descripción** 	**Ejemplo** 	**Resultado**
    ==	            Igual a	            5 == 5	        True
    !=	        Diferente de	        10 != 5	        True
    >	            Mayor que	        7 > 3	        True
    <	            Menor que	        2 < 8	        True
    >=	        Mayor o igual que	    5 >= 5	        True
    <=	        Menor o igual que	    4 <= 2	        False


4. **Operadores Lógicos**

*Se utilizan para combinar expresiones condicionales.*

*Operador*	       *Descripción*	                   *Ejemplo*	   *Resultado*
    and	    True si ambas expresiones son True	   (True and False)	      False
    or	    True si al menos una expresión es True	(True or False)	      True
    not	    Invierte el valor booleano	                not True          False

