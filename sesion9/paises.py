#practica cuatro
paises=[]
for i in range(5):
    paises.append(input("ingrese los paises "+str(i+1)+": "))
paises.sort()
print("los paises son: ")
for P in paises:
    print(P)