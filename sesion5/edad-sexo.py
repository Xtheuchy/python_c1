edad=int(input("ingrese su edad: "))
sexo=input("ingrese su genero varon/mujer: ")
#procedimiento
if  sexo=="varon":
    if edad>=65:
        print("puede jubilarse")
    else:
            print("no puede jubilarse")
elif sexo=="mujer":
 if edad>55:
        print("se puede jubilar")
 else:
     print("no puede jubilarse")



