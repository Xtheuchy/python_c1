def contar_digito(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    ocurrencias = numero_str.count(digito_str)
    return ocurrencias
numero = int(input("ingrese los numeros"))
digito = int(input("ingrese el nro que desea ver"))
resultado = contar_digito(numero, digito)
print(f'El dígito {digito} aparece {resultado} veces en el número {numero}.')