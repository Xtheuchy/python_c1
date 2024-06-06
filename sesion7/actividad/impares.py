#ejercicio cuatro
continuar="y"
while(continuar=="y"):
    nro=int(input("ingresa un numero: "))
    n=1
    while(n<=nro):
         if n%2==1:
              print(n)
         n+=1
    continuar=input("si desea continuar ingrese (y)")