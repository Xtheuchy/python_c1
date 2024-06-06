nombre=input("ingrese su nombre: ")
especialidad=input("ingrese su especialidad:")
atencion="si"
if (especialidad=="obstetricia"):
    montoapagar=50
elif(especialidad=="pediatria"):
    montoapagar=60
elif(especialidad=="gastroenterologia"):
    montoapagar=100
elif(especialidad=="neumologia"):
    montoapagar=80
else:
    atencion="no"
    print("esta especialidad no atendemos")
#resultado
if atencion=="si":
    print("el monto a pagar en:",especialidad,"es",montoapagar)
