def factorial():
    continuar="si"
    nros=0
    while continuar=="si":
        nro=int(input("ingrese su nro: "))
        factorial=1
        for i  in range(1,nro+1):
            factorial*=i
        print("el factorial de",nro,"es: ",factorial)
        nros+=1
        continuar=input("desea continuar? [si/no]: ")
    print("El total de nros calculados son: ",nros)
#programa principal
factorial()