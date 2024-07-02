productos=[]
continuar="Si"
while continuar=="Si":
    print("""¿QUE DESEA REALIZAR?
          [1] Agregar productos
          [2] Editar productos
          [3] Listar productos y la cantidad
          [4] eliminar productos
          [5] mostrar de manera ordenada los productos
          [6] eliminar todos los productos
          [7] Salir del programa
          """)
    opcion=int(input("Ingrese su opcion: "))
    if opcion==1:
        print("¿Cuantos productos desea agregar?")
        cantidad=int(input("Ingrese la cantidad de productos a agregar: "))
        for i in range(cantidad):
            añadir_pro=input("Que productos desea agregar?: ")
            productos.append(añadir_pro)
    elif opcion==2:
        Nombrepro_antiguo=input("ingrese el nombre del producto que desea editar: ")
        if Nombrepro_antiguo in productos:
            Nombrepro_actual=input("ingrese el nombre del producto actual: ")
            for  i in range(len(productos)):
                if productos[i]==Nombrepro_antiguo:
                    productos[i]=Nombrepro_actual
    elif opcion==3:
        print("Tenemos los siguientes productos: ",productos)
        nroproductos=0
        for i in productos:
           nroproductos+=1
        print("tenemos la siguiente cantidad de productos: ",nroproductos)
    elif opcion==4:
         nombreproduc=input("ingrese el nombre a eliminar: ")
         if nombreproduc in productos:
            for i in range(len(productos)):
                if productos[i]==nombreproduc:
                    del productos[i]
                    break
    elif opcion==5:
        productos.sort()
        print(productos)
    elif opcion==6:
        productos.clear()
        print(productos)
    elif opcion==7:
        print("HASTA LA PROXIMA")
        break