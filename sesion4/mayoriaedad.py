#pedir un nombre y su edad, mostrar si la persona 
#es mayor o menor de edad 
nombre=input("ingresa tu nombre: ")
edad=int(input("ingresa tu edad: "))
#decision
print("nombre:", nombre)
if edad>=18:
    print("mayor de edad")
else:
    print("menor de edad")
