# Imprimir los numeros desde el 100 hasta el 50, pero unicamente los impares
numero = 100
while numero > 50:
    residuo = numero % 2
    if residuo == 1:
        print (numero)
    numero -= 1
