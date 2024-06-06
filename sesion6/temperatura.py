temperatura=int(input("ingrese la temperatura de su hogar: "))
if(temperatura<=-10):
   print("exceso de frio")
elif(temperatura>-10 and temperatura<10):
    print("mucho frio")
elif(temperatura>=10 and temperatura<15):
    print("poco frio")
elif(temperatura>=15 and temperatura<25):
    print("temperatura normal")
elif(temperatura>=25 and temperatura<30):
    print("poco calor")
elif(temperatura>=30 and temperatura<40):
    print("mucho calor")
elif(temperatura>=40):
    print("exceso de calor")
