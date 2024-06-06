#ingrese 15 nros y sumar numeros mayores a 100
suma=0
for i in range(15):
    nro=int(input("ingrese el nro "+str(i+1)+": "))
    if nro>100:
        suma+=nro
#imprimir la suma
print("la suma de los mayores a 100 es", suma)
