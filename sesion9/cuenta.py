#practica cinco
saldo=2000
continuar="si"
Lista_Retiro=[]
Lista_Deposito=[]
while continuar=="si":
    opcion=input("¿Que desea realizar:[Retiro o Deposito]?")
    if opcion=="retiro":
        cantidad=int(input("ingrese la cantidad a retirar: "))
        Lista_Retiro.append(cantidad)
        saldo-=cantidad
        print("se retiro la cantidad de: ",cantidad)
        print("Su saldo actual es: ",saldo)
        print("detalles del retiro: ",Lista_Retiro)
    elif opcion=="deposito":
        cantidad=int(input("ingrese la cantidad a depositar: "))
        Lista_Deposito.append(cantidad)
        saldo+=cantidad
        print("se deposito la cantidad de: ",cantidad)
        print("Su saldo actual es: ",saldo)
        print("detalles del deposito: ",Lista_Deposito)
    continuar=input("¿desea continuar? [si/no]")