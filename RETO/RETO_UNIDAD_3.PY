# Nombres: Juan Esteban Maturana y Daniel Mano Tabares

capacidad_inicial = float (input("ingrese el combustible con el que despega la aeronave"))
consumo_base = 10 # Kg/Km (Promedio que sale de un aproximado de un consumo de entre 8 a 12 Kg/Km que dio la IA)
headwind = 0.25 # suponiendo que hay un viento en contra fuerte según la IA
tailwind =  - 0.125 # Suponiendo que hay vientos fuertes (promedio que sale de un aproximado de un aumento de entre 10 a 15 porciento según la IA)
reserva_legal = float(input("Ingrese cuanto combustible lleva en reserva legal"))
viento = float(input("Ingrese la velocidad del viento en nudos"))