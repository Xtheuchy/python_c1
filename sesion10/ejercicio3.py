lista1=[]   
for i in range(5):
    cadena=input("ingrese un nombre: ")
    lista1.append(cadena)
    lista2=lista1[:]
lista2.reverse()
print(lista2)