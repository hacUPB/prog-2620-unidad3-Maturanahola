# Datos de entrada
promedio = float (input("ingrese su promedio"))
nivel_socioeconomico = int (input("ingrese su nivelsocioeconomico"))
#evaluación de cumplimiento de la beca
beca = promedio >= 9.0 or promedio >8.0 and nivel_socioeconomico == 1
#resultado
mensaje = "Obtuviste la beca." if beca else "no obtienes la beca." 
print(mensaje)
