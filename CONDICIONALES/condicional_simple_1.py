''''''

''''''
# La moneda es en pesos colombianos

compra = int(input("ingrese el valor de la compra"))
domicilio = 0
if compra < 100000:
    domicilio = 9000
total = compra + domicilio
print (f"El valor a pagar es {total}")

# Otra forma
# compra = int(input("Ingrese el valor de la compra"))
# total = compra + 9000
#if compra > 100000:
#   total = compra