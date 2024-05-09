segundos=float(input("ingrese un tiempo en s:"))
horas= segundos//3600
minutos=(segundos % 3600)//60
resto=segundos % 60
print("en horas es :",horas)
print("en minutos es:", minutos)
print("el resto es:", resto)
