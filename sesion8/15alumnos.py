examen=0
for i in range(15):
    promedio=float(input("ingrese el promedio de los alumnos "+str(i+1)+": "))
    if promedio>=7 and promedio<12.5:
        examen+=1
print("la cantidad de alumnos que ingresaran al examen sustitutorio son: ",examen)
