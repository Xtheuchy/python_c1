#ejercicio nro nueve
limite = int(input("Ingrese el límite superior: "))

if limite < 0:
    print("No hay números primos hasta el límite proporcionado.")
else:
    print("Números primos hasta el límite proporcionado:")
    numero = 1
    while numero <= limite:
        primo = True
        divisor = 2
        while divisor <= numero / 2:
            if numero % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            print(numero)
        numero += 1
