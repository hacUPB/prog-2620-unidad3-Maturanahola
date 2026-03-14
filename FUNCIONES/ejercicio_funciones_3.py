# Función menú: Imprime un menú de opciones y retorna la opción elegida por el usuario

def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. suma. 2. Resta. 3. Multiplicación. 4. división")
        opcion = int(input("selecciones una opción"))
    if opcion< 1 or opcion > 4:
        print("la Opcion no es valida")
        print (input("igrese otra opcion"))
    return opcion

operacion = menu()
print(f"El usuario eligió {operacion}")
