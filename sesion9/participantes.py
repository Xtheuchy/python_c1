#practica dos
cantidad=int(input("ingrese la cantidad de participantes: "))
participante=[]
for nombre in range(cantidad):
    participante.append(input("ingrese su nombre: "))
print("-----------")
for i in participante:
    print(i, end=" ")