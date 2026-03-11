def factorial(numero):
    # Verificar si númro es 0 el factorial es 1 
    # Si número es menor que 0 retornar -1
    #multipicar desde 1 hasta número y acumular el resultado
    acumulador = 1
    for factor in range (1, numero + 1):
        acumulador = acumulador * factor
    return acumulador

resultado = factorial(6)
print (resultado)
