def validacion_correo():
    correo=input("Ingrese su correo: ")
    if "@" in correo:
        print("ESTE CORREO ES VALIDO.")
    else:
        print("EL CORREO INGRESADO ES INCORRECTO")
validacion_correo()