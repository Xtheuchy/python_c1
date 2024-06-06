nota1=int(input("ingrese la primera nota: "))
nota2=int(input("ingrese la segunda nota: "))
nota3=int(input("ingrese la tercera nota: "))
#procedimiento
promedio= (nota1+nota2+nota3)/3
#final
if promedio>=13:
    resultado="aprobado"
else: 
    resultado="desaprobado" 
#validar si el promedio esta entre 0-20
if not(promedio>=0 and promedio<=20):
    print("promedio no valido")
else:
    print("promedio valido")
    print("su condicion es: ",resultado)
