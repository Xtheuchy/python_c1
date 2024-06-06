marca_auto=input("ingrese la marca de su auto: ")
nrodelunas=int(input("ingrese la cantidad de lunas a comprar: "))
#calculamos el prcio inicial
if(marca_auto=="Toyota" and nrodelunas>2):
    costoluna=150
    descuento=0.20*(costoluna*nrodelunas)
    preciototal=(costoluna*nrodelunas)-descuento
elif(marca_auto=="Nissan" and nrodelunas>3):
    costoluna=200
    descuento=0.25*(costoluna*nrodelunas)
    preciototal=(costoluna*nrodelunas)-descuento
elif(marca_auto=="Hyundai"):
    costoluna=100
    descuento=0.10*(costoluna*nrodelunas)
    preciototal=(costoluna*nrodelunas)-descuento
print("este es el precio por cada luna:",costoluna)
print("este es el precio con descuento: ",preciototal)
