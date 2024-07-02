def nrosprimos():
    nro=int(input("Ingrese un nro: "))
    for i in range(2,nro):
        if nro%i==0:
            print(nro,"NO PRIMO")
            return False
    print("Es primo")
    return True
#programa principal
nrosprimos()