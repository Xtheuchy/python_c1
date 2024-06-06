tipo=input("ingrese el tipo de habitacion")
nrodedias=int(input("ingrese el nro de dias"))
if tipo=="A":
    costopordia=75
elif tipo=="B":
    costopordia=65
elif tipo=="C":
    costopordia=55
elif tipo=="D":
    costopordia=40
else:
    print("habitacion invalida")
    costopordia=0
#costo adicional por jacuzi
if(tipo=="A" or tipo=="B"):
    rpta=input("Tiene jacuzi: [si/no] ")
    if rpta.flower()=="si":
        costopordia+=5
#descuento
if 1<=nrodedias<=3:
    descuento=0.02*costopordia*nrodedias
elif 4<=nrodedias<=7:
    descuento=0.10*costopordia*nrodedias
elif nrodedias>=8:
    descuento=0.25*costopordia*nrodedias
#resultado
total=costopordia*nrodedias-descuento
print("el precio final es: ",total)