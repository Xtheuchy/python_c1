#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas 
print("INGRESE LAS NOTAS DE 0 - 20")
notas=[]
for i in range(5):
    nota=int(input("ingrese la nota "+str(i+1)+":"))
    if 0<nota<20:
        notas.append(nota)
    else:
        print("ESA NOTA ES ERRONEA")
print("Todas las notas del alumno: ",notas)
notaalta=max(notas)
print("Su calificacion mas alta es de: ",notaalta)
notabaja=min(notas)
print("Su menor nota es de: ",notabaja)