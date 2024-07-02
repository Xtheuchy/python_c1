#practica tres 
notas=[]
suma=0
for i in range(5):
    i=int(input("ingrese las notas: "))
    notas.append(i)
    suma+=i
print("la suma de sus notas es: ",suma)
print("las notas fueron: ")
for nota in notas:
    print(nota)
promedio=suma/5
print("el promedio es: ",promedio)