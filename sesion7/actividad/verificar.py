#ejercicio tres
continuar="s"
while(continuar=="s"):
    nro=int(input("ingrese su numero: "))
    if nro%2==0:
        print("Su numero ingresado es Par")
    else:
        print("El numero que a ingresado es impar")
        
    continuar=input("desea continua [s/n]")