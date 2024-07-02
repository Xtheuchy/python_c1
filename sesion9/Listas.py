#listas
cursos=["ingles","matematica","informatica"]
#imprimir lista
print(cursos)
#imprimir un elemento
print(cursos[1])
#modificar un elemento
cursos[2]="contabilidad"
print(cursos)
#elemntos de manera separada
for elemento in cursos:
    print(elemento)
#recorrer elementos con range
for i in range(3):
    print(cursos[i]) 
#agregar elemntos en la lista .append
cursos.append("arte")
print(cursos)
#ordenar los elementos de lista .sort() a-z
cursos.sort()
print(cursos)