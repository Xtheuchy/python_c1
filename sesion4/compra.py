#docenas,descuento,monto a pagar, numero de obsequio
#precio de la compra
nrodedocenas=int(input("ingrese la cantidad de docenas al comprar: "))
preciodocena=float(input("ingrese precio de las docenas: "))
#proceso
montocompra=nrodedocenas*preciodocena
if (nrodedocenas>3):
    montodescuento=0.15*montocompra
else:
        montodescuento=0.10*montocompra
#calcular monto a pagar
montopagar=montocompra-montodescuento
#calcular nro de obsequio 
nroobsequio=nrodedocenas-3
#resultados
print("monto de compra: ", montocompra)
print("monto del descuento: ",montodescuento)
print("monto a pagar:", montopagar)
print("nro de obsequios: ", nroobsequio)