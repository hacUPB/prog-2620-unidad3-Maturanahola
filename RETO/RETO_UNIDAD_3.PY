# Nombres: Juan Esteban Maturana

consumo_base = 10
headwind = 0.25 # 25% suponiendo que son vientos fuertes (Información sale de IA)
tailwind = -0.125 # -12.5 promedio (ya que va a favor de la dirección del avión reduce su consumo)
viento_nulo = 0


def calcular_consumo_tramo (tramo, tipo_viento):
 if tipo_viento == 1:
  valor = headwind + 1
 elif tipo_viento == 2:
  valor = tailwind + 1
 else:
    Valor = viento_nulo + 1  
 return tramo * consumo_base * valor

combustible_actual = float(input("Ingrese la cantidad de combustible con la que va despegar: "))
reserva_legal = float(input("ingrese la cantidad de combustible que lleva en reserva leagl: "))

for punto_control in range(1,5):
  print(f"Punto de control actual {punto_control}")
  tramo = int(input("Ingrese la distancia en km"))
  print("condición de viento (1: Headwind, 2: Tailwind, 3: Nulo)")
  tipo_viento = int(input("seleccione la condición del viento"))

  gasto_tramo = calcular_consumo_tramo (tramo, tipo_viento)

  if (combustible_actual - gasto_tramo) < reserva_legal:
    print("⚠️COMBUSTIBLE IN SUFICIENTE⚠️")
    print (f"El tramo requiere {gasto_tramo}kg de combustible")
    break
  else:
    combustible_actual = combustible_actual - gasto_tramo
    control_combustible = combustible_actual
    print("tramo completado")
    print(f"Combustible restante {control_combustible}Kg")
  






 


