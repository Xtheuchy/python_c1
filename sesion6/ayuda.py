# Solicitar el tipo de habitación y el número de días
tipo = input("Ingrese el tipo de habitacion (A, B, C, D): ")
nrodedias = int(input("Ingrese el numero de dias: "))

# Definir el costo por día según el tipo de habitación
if tipo == "A":
    costopordia = 75
elif tipo == "B":
    costopordia = 65
elif tipo == "C":
    costopordia = 55
elif tipo == "D":
    costopordia = 40
else:
    print("Tipo de habitacion no válido")
    costopordia = 0  # Defecto a 0 en caso de entrada inválida

# Verificar si la habitación tipo A o B tiene jacuzzi
if tipo == "A" or tipo == "B":
    rpta = input("Tiene jacuzzi: [si/no] ")
    if rpta.lower() == "si":
        costopordia += 5

# Calcular el descuento basado en el número de días
if nrodedias > 0:
    if 1 <= nrodedias <= 3:
        descuento = 0.02 * costopordia * nrodedias
    elif 4 <= nrodedias <= 7:
        descuento = 0.10 * costopordia * nrodedias
    elif nrodedias >= 8:
        descuento = 0.25 * costopordia * nrodedias
    else:
        descuento = 0  # Sin descuento para número de días inválido
else:
    descuento = 0
    print("Número de días no válido")

# Calcular el precio total final
total = costopordia * nrodedias - descuento

# Mostrar el precio final
if costopordia > 0 and nrodedias > 0:
    print("El precio final es: ", total)
else:
    print("No se pudo calcular el precio final debido a entradas no válidas.")
