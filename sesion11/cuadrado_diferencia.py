def calcular_cuadrado():
    valor=int(input("Ingrese un numero: "))
    cuadrado=valor*valor
    print("el cuadrado de",valor,"es: ",cuadrado)
    print("**************************************")
def calcular_diferencia():
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    diferencia=valor1-valor2
    print("La diferencia de los valores es: ",diferencia)
#programa principal
calcular_cuadrado()
calcular_diferencia()