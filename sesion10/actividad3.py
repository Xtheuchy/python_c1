Meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
continuar="si"
DIAS=28
DIAS2=30
DIAS3=31
while continuar=="si":
    nro=int(input("ingrese un numero del 1-12: "))
    if nro==2:
        print("Es el mes de",Meses[nro-1])
        print("Tiene ",DIAS,"días")
    elif nro==4 or nro==6 or nro==9 or nro==11:
        print("Es el mes de",Meses[nro-1])
        print("Tiene ",DIAS2,"días")
    elif nro==1 or nro==3 or nro==5 or nro==8 or nro==10 or nro==12:
        print("Es el mes de",Meses[nro-1])
        print("Tiene ",DIAS3,"días")
    else:
        print("ERROR ESE MES NO EXISTE")