continuar="si"
clientes=[]
while continuar=="si":
    print("""elegir una opcion del menu
          [1] mostrar lista
          [2] agregar elementos
          [3] editar elementos
          [4] eliminar un elemento
          [5] salir del sistema 
          """)
    opcion=int(input("ingrese opcion elegida"))
    if opcion==1:
        print(clientes)
    elif opcion==2:
        agregar=input("ingrese un nombre: ")
        clientes.append(agregar)
    elif opcion==3:
        nombreantiguo=input("ingrese el nombre anteriormente: ")
        if nombreantiguo in clientes:
            nombreactual=input("ingrese el nombre actual: ")
            for i in range(len(clientes)):
                if clientes[i]==nombreantiguo:
                    clientes[i]=nombreactual
        else:
            print("este cliente no existe")
    elif opcion==4:
        nombrecliente=input("ingrese el nombre a eliminar: ")
        if nombrecliente in clientes:
            for i in range(len(clientes)):
                if clientes[i]==nombrecliente:
                    del clientes[i]
                    break
    elif opcion==5:
        print("Finalizando sistema")
        break