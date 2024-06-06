america_norte=0
america_central=0
america_sur=0
for i in range(0,10):
    pais=input("ingrese un pais "+str(i+1)+": ") 
    if pais=="USA" or pais=="Canada":
        america_norte+=1
    elif pais=="Mexico" or pais=="El Salvador" or pais=="Cuba" or pais=="Panama":
        america_central+=1
    elif pais=="Peru" or pais=="Chile" or pais=="Colombia" or pais=="Brasil" or pais=="Argentina":
        america_sur+=1
print("En america del norte son: ",america_norte)
print("En america central son: ",america_central)
print("En america del sur son: ",america_sur)