lista=[]
continuar="si"
while continuar=="si":
    agregar_nro=int(input("ingrese el numero: "))
    if agregar_nro>0:
        lista.append(agregar_nro)
    else:
        print(lista)
        break
