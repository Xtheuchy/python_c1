añoactual=int(input("ingrese es año en el que estas: "))
añodiferente=int(input("escribe un año: "))
#resolucion 
if(añoactual>añodiferente):
    pasado=añoactual-añodiferente
    print("han pasado",pasado,"años")
elif(añoactual<añodiferente):
    falta=añodiferente-añoactual
    print("faltan",falta,"años")
