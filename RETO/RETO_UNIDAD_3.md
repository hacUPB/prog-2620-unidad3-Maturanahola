## ENTRADAS,SALIDAS, CONSTANTES Y CONTROLES
|---          |---                |---         |---               |
|        ---  |---                |---         |---               |
|**INPUTS**   |**OUTPUTS**        |**COSNTANTES**|**V.CONTROL**   |
|PUNTO_CONTROL|CONTROL_COMBUSTIBLE|CONSUMO_BASE|COMBUSTIBLE_ACTUAL|
|TRAMO        |      ------       |HEADWIND    |                  |
|TIPO_VIENTO  |        -------    |TAILWIND    |                  |
|---          |---                |RESERVA_LEGAL|              ---|
|---          |---                |viento_nulo  |---               |

## PSEUDOCÓDIGO
**1) Configuración de constantes y variables**

    consumo_base = 10
    headwind = 0.25 # 25%
    tailwind = -0.125 #12.5
    viento_nulo = 0
    viento = 0
    Leer: combustible_inicial (combustible antes de despegar)
    leer: reserva_legal (lo que hay en reserva)

**2) BUCLE**

(Para cada punto de control)

    for **i** in **range** (1,3)

        Leer: tramo (distancia en kilomentros)
        leer: viento (ingrese 1. para headwind, 2.para tailwind, 3.nulo)

    if viento == 1:
        valor = headwind + 1 #aumenta el consumo

    elif viento == 2:
        valor = tailwind + 1 #reduce el consumo

    else:
        valor = 1 (No sufre cambios)

**3) Calcular el gasto por tramo**

gasto_tramo = tramo * consumo_base * valor

**4) desición**

**if** (combustible_actual - gasto_tramo) < reserva_legal:

    mostar: "Alerta"
    mostrar: 

else: 

    combustible_actual = combustible_actual - gasto_tramo (actualiza el combustible actual a lo que queda segín lo que se ha gastado en el tramo)

    control_combustible = combustible_actual
    






