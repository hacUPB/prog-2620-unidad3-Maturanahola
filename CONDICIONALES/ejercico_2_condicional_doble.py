# Variables
articulo1 = int (input("Ingrese el valor del articulo"))
articulo2 = int (input("Ingrese el valor del articulo"))
articulo3 = int (input("ingrese el valor del articulo"))
menor = 0.50

if articulo1 < articulo2 and articulo1 < articulo3:
    print ("El esticulo 1 es el menor y tiene descuento")
    valor_descuento = articulo1 * menor
    total = valor_descuento + articulo2 + articulo3
    print (f"el total es {total}")

elif articulo2 < articulo1 and articulo2 < articulo3:
    print ("El articulo 2 es el menor y tiene descuento")
    valor_descuento = articulo2 * menor
    total = valor_descuento + articulo1 + articulo3
    print (f"el total es {total}")

else:
    print("El articulo 3 es el menor y tiene descuento")
    valor_descuento = articulo3 * menor
    total = valor_descuento + articulo1 + articulo3
    print (f"el total es {total}")





