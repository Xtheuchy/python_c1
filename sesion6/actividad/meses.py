meses=int(input("ingrese un numero del [1/12]: "))
if (meses==1):
    mes="Enero"
elif(meses==2):
    mes="Febrero"
elif(meses==3):
    mes="Marzo"
elif(meses==4):
    mes="Abril"
elif(meses==5):
    mes="Mayo"
elif(meses==6):
    mes="Junio"
elif(meses==7):
    mes="Julio"
elif(meses==8):
    mes="Agosto"
elif(meses==9):
    mes="Septiembre"
elif(meses==10):
    mes="Octubre"
elif(meses==11):
    mes="Noviembre"
elif(meses==12):
    mes="Diciembre"
else:
    print("no existe ese mes")
    mes="error"
print("Este es el mes de:",mes)