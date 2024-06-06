#ejercicio nro ocho
nro = int(input("Ingrese un número: "))
i = 2
primo = True
while i < nro:
    if nro % i == 0:
        primo = False
        break
    i += 1
    print(primo)
if primo:
    print(nro,"es primo.")
else:
    print(nro,"no es primo.")
