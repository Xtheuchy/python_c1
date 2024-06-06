area=input("en que area trabajas: ")
nrohijos=int(input("cuantos hijos tienes"))
#calcular sueldo basico
if(area=="ventas"):
    sueldo=750
elif(area=="MKT"):
    sueldo=900
elif(area=="almacen"):
    sueldo=1000
else:
    sueldo=1200
#calcular el monto adicinal
if(nrohijos==0):
    montoadicional=0
elif(1<=nrohijos<=3):
    montoadicional=0.15*sueldo
elif(nrohijos<=4):
    montoadicional=0.20*sueldo
#sueldo neto
sueldoneto=sueldo+montoadicional
print("tu sueldo es: ",sueldo)
print("el monto adicional es: ",montoadicional)
print("tu sueldo final es: ",sueldoneto)