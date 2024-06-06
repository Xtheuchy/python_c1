GO="S"
while GO=="S":
    nro=int(input("ingrese un nro: "))
    for i in range (1,nro+1):
        if i%2==1:
         print(i)
    GO=input("desea continuar? [S=si N=no]:",)