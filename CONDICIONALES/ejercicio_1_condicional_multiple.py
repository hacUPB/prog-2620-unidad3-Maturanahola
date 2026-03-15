# CLASIFICAR A LAS PERSONAS SEGÚN LA EDAD
edad = int (input("ingrese la edad"))
if edad >= 0 and edad <= 124:
    if  edad < 6:
        etapa = "infancia"
    elif edad < 12:
        etapa = "Niñes"
    elif edad < 20:
        etapa = "Adolecencia"
    elif edad < 25:
        etapa = "juventud"
    elif edad < 60:
        etapa = "Adultez" 
    else:
        etapa = "ancianidad/vejez"
    print(f"A sus {edad} años, Udted esta en la etapa de {etapa} ")

else:
    print("La edad no es valida")