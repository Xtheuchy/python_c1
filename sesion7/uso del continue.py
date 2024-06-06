c=0
while c<=5:
    c+=1
    if c==3 or c==4:
        print("continuamos con la siguiente interaccion",c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la interaccion y c vale",c)