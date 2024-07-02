lista1=[]
lista2=[]
lista3=[]
for i in range(10):
    nro=int(input("ingrese un numero entero: "))
    if i<5:
        lista1.append(nro)
    if 5<=i<10:
        lista2.append(nro)
for i in range(5):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)
print(lista3)
