#solicitar dos número al ususuario e imprimir los valores pares que hay entre dichos números
n1 = int(input("ingrese el primer número"))
n2 = int(input("Ingrese el segundo número"))

#Identificar el número mayor y el número menor
if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

while mayor >= menor:
    residuo = mayor % 2
    if mayor % 2 ==0:
        print (mayor)
    mayor -= 1
    