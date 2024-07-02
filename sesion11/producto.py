def carga_producto():
    valor1=int(input("ingrese su primer valor: "))
    valor2=int(input("ingrese su segundo valor: "))
    producto=valor1*valor2
    print("El producto es: ",producto)
def separacion():
    print("*************************************")

#programa principal 
for i  in range(5):
    carga_producto()
    separacion()