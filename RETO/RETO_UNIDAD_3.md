## ENTRADAS,SALIDAS, CONSTANTES Y CONTROLES

![TABALA_DE_VARIABLES](/images/TABLA_DE_VARIABLES.png)

## PSEUDOCÓDIGO
    consumo_base = 10
    headwind = 0.25
    tailwind = -0.125
    viento_nulo = 0

**FUNCIÓN OBLIGATORIA (IA)**
    FUNCION calcular_consumo_tramo(tramo, tipo_viento): 

        SI tipo_viento == 1 
            valor = 1 + headwind
        SINO SI tipo_viento == 2 
            valor = 1 + tailwind
        SINO
            valor = 1 + viento_nulo
        FIN SI
        RETORNAR tramo* consumo_base * valor
    FIN FUNCION

**INICIO DEL SISTEMA**

    LEER combustible_actual # Empieza con la carga inicial
    LEER reserva_legal # Reserva de combustible que debe tener o lleva en el avión

**BUCLE**

    PARA punto_control DESDE 1 HASTA 6 HACER   
        MOSTRAR "Punto de Control actual: ", punto_control
        LEER tramo ("distancia en kilometros")
        LEER tipo_viento (1: Headwind, 2: Tailwind, 3: Nulo)

        #Cálculo del gasto usando la función

        gasto_tramo = calcular_consumo_tramo(tramo, tipo_viento)

**DECISIÓN**
        SI (combsutible_actual - gasto_tramo) < reserva_legal ENTONCES:

            MOSTRAR "ALERTA: Combustible insuficiente."

        SINO:
            combustible_aactual >= combustible_actual - gasto_tramo
            consumo_combustible = combustible_actual
            MOSTRAR "Tramo exitoso. Cantidad de combustible en el tanque: ", control_combustible
        FIN SI
    FIN PARA

FIN ALGORITMO