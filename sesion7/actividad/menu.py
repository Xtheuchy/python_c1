#ejercicio uno
continuar="si"
while (continuar=="si"):
      
      print("""Elegir una de las siguientes opciones:
      [1] saludar
      [2] sumar numeros
      [3] salir
      """)
      opcion=int(input("ingrese una opcion: "))
      if (opcion==1):
            print("BIENVENIDO AL SISTEMA")
      elif(opcion==2):
            print("ingresa dos numeros a sumar")
            nro1=int(input("ingresa el primer nro: "))
            nro2=int(input("ingresa el segundo nro: "))
            rpta=nro1+nro2
            print("la respuesta de los numeros que sumaste es: ",rpta)
      elif(opcion==3):
            print("hasta la proxima")
            break
      
      continuar=input("desea seguir navegando [si/no]")