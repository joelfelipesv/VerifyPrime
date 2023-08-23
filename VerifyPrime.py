def verifyPrime(n):
    if n <= 1: # Si el número ingresado es menor a 1, automáticamente arroja el resultado "no es un número primo".
        return False
    elif n <= 3: # Si el número ingresado es 2 o 3, automáticamente arroja el resultado "es un número primo".
        return True
    elif n % 2 == 0 or n % 3 == 0: # Si el número es divisible por 2 o 3 automáticamente arroja el resultado "no es un número primo".
        return False
    i = 5 # Se considera 5 como el primer primo de la lista.
    while i * i <= n: # Se comprueba que el cuadrado del número primo actual sea menor o igual al número ingresado.
        if n % i == 0 or n % (i + 2) == 0: # Si el módulo del número ingreasdo con respecto al primo actual (o al siguiente) es cero, automáticamente arroja el resultado "no es un número primo".
            return False
        i += 6 # Se suma 6 al primo actual avanzando dos posiciones en la lista de números primos.

    return True # Si ninguna de las condiciones anteriores se cumple, entonces el número es primo.

n = int(input("Ingrese el número que desea verificar: ")) # El usuario debe ingresar un número entero.

if verifyPrime(n):
    print(n, "es un número primo.")
else:
    print(n, "no es un número primo.")
