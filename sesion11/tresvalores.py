def menor_valor():
    valor1=int(input("Ingrese su primer valor: "))
    valor2=int(input("Ingrese su segundo valor: "))
    valor3=int(input("Ingrese su tercer valor: "))
    print("El menor valor de los tres es: ")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)
    print("********************************")
#Programa principal
menor_valor()
menor_valor()
        