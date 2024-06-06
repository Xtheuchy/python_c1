costo_compra=int(input("ingrese lo que gasto en su compra: "))
if costo_compra>1000:
    descuento=costo_compra*0.20
    preciofinal=costo_compra-descuento
    print("el precio con el descuento es de: ",preciofinal,"soles")
else:
    print("no tiene descuento")