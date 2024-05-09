#evaluar si un alumno aaprueba 
#datos de entrada
nota1=int(input("ingrese la nota 1: "))
nota2=int(input("ingrese la nota 2: "))
nota3=int(input("ingrese la nota 3: "))
#procesar
promedio=(nota1+nota2+nota3)/3
#decision
if promedio>=13:
    print("aprobo")
else:
   print("desaprobado") 
