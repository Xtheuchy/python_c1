menor_50=0
entre100y50=0
entre100y200=0
sobre200=0
for i in range(10):
    monto_venta=int(input("ingrese el monto de venta "+str(i+1)+": "))
    if monto_venta<50:
       menor_50+=1
    elif monto_venta>=50 and monto_venta<100:
        entre100y50+=1
    elif monto_venta>=100 and monto_venta<200:
        entre100y200+=1
    elif monto_venta>=200:
        sobre200+=1
print("menor a 50: ",menor_50)
print("entre 50 y 100: ",entre100y50)
print("entre 100 y 200: ",entre100y200)
print("sobre 200: ",sobre200)




    