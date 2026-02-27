#Datos iniciales
cuenta = 85
propina_porcentaje = 0.15
persona = 4

#calcualr el total de la propina
propina = cuenta * propina_porcentaje

#Calcular el total a pagar
total = cuenta + propina

#Calcular cuanto debe paga cada persona
pago_por_persona = total/persona
print ("propina total:"),round(propina,2)
print ("total a pagar:"), round (total,2)
print ("Cada persona debe pagar:"),round (pago_por_persona,2)
