edad_usuario = 14
saldo_billetera = 70.0
tiene_suscripcion_premium = True
juego = 60.0
#Calculo del precio final con descuento si tiene suscribción
precio_final = juego * (0.10 if tiene_suscripcion_premium else 100/100)
#Requisitos de compra exitosa
if (edad_usuario >= 17) and (saldo_billetera >= precio_final):
    print("compra exitosa")
else :
    print("compra no exitosa")







