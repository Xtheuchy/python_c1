cero=0
positivo=0
negativo=0
for i in range(20):
    nro=int(input("ingrese un numero"+str(i+1)+": "))
    if nro>0:
        positivo+=nro
    elif nro<0:
        negativo+=nro
    elif nro==0:
        cero+=1
print("la cantidad de ceros que ahi son: ",cero)
print("la suma de los numeros positivos son: ",positivo)
print("La suma de los numeros negativos son: ",negativo)


