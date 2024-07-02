#practica final
lista_edades=[]
mayores=0
menores=0
suma_edades=0
for i in range(7):
    i=int(input("ingrese las edades "+str(i+1)+": "))
    lista_edades.append(i)
for M in lista_edades:
    if M>=18:
        mayores+=1
    elif M<18 and M>0:
        menores+=1
print("esta es la cantidad de menores: ",menores)
print("esta es la cantidad de mayores: ",mayores)
#suma de las edades
for S in lista_edades:
    suma_edades+=S
#promedio
promedio=suma_edades/7
print("El promedio de las edades es: ",promedio)