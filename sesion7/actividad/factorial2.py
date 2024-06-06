#ejecicio nro siete
while True:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")
    elif numero == 0:
        print("FIN")
        break
    else:
        factorial = 1
        i = 1
        while i <= numero:
            factorial *= i
            i += 1
        print("El factorial de", numero, "es", factorial)
