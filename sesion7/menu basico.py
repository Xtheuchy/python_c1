continuar="si"
while(continuar=="si"):
    print("""Elegir una de las siguientes opciones:
          [1] saludar
          [2] recibir un numero
          [3] salir
          """)
    opcion=int(input("ingrese su opcion: "))
    if (opcion==1):
        print("hola bienvenido al sistema")
    elif(opcion==2):
        nro=int(input("ingrese un numero"))
        print("el doble del numero es: ",2*nro)
    elif(opcion==3):
        print("vuelve pronto...")
        break
    
    continuar=input("desea continuar? [si/no]") 