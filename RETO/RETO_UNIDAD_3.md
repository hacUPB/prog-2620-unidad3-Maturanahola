## ENTRADAS,SALIDAS, CONSTANTES Y CONTROLES

![TABALA_DE_VARIABLES](/images/TABLA_DE_VARIABLES.png)

## PSEUDOCÓDIGO
    CONSUMO_BASE = 10
    HEADWIND = 0.25
    TAILWIND = -0.125
    viento_nulo = 0

**FUNCIÓN OBLIGATORIA (IA)**
    FUNCION calcular_consumo_tramo(TRAMO, TIPO_VIENTO): 

        SI TIPO_VIENTO == 1 
            valor = 1 + HEADWIND
        SINO SI TIPO_VIENTO == 2 
            valor = 1 + TAILWIND
        SINO
            valor = 1 + viento_nulo
        FIN SI
        RETORNAR TRAMO * CONSUMO_BASE * valor
    FIN FUNCION

**INICIO DEL SISTEMA**

    LEER COMBUSTIBLE_ACTUAL # Empieza con la carga inicial
    LEER RESERVA_LEGAL # Reserva de combustible que debe tener o lleva en el avión

**BUCLE**

    PARA PUNTO_CONTROL DESDE 1 HASTA 6 HACER   
        MOSTRAR "Punto de Control actual: ", PUNTO_CONTROL
        LEER TRAMO ("distancia en kilometros")
        LEER TIPO_VIENTO (1: Headwind, 2: Tailwind, 3: Nulo)

        #Cálculo del gasto usando la función
        GASTO_TRAMO = calcular_consumo_tramo(TRAMO, TIPO_VIENTO)

**DECISIÓN**
        SI (COMBUSTIBLE_ACTUAL - GASTO_TRAMO) < RESERVA_LEGAL ENTONCES:

            MOSTRAR "ALERTA: Combustible insuficiente."

        SINO:
            COMBUSTIBLE_ACTUAL >= COMBUSTIBLE_ACTUAL - GASTO_TRAMO
            CONTROL_COMBUSTIBLE = COMBUSTIBLE_ACTUAL
            MOSTRAR "Tramo exitoso. Cantidad de combustible en el tanque: ", CONTROL_COMBUSTIBLE
        FIN SI
    FIN PARA

FIN ALGORITMO

