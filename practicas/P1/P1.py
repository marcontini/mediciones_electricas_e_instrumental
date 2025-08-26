# ==========================================================================
#
#                       GUÍA 1: CÁLCULO DE INCERTIDUMBRE
#
# ==========================================================================

import numpy as np
import estadistica as st

# EJERCICIO 1
"""
Se realizan 20 mediciones con un multímetro digital, repetidas en las mismas
condiciones ambientales, obteniéndose una media aritmética de 100,145 V y
una desviación estándar experimental (S) de 1,489V.

El multímetro posee las siguientes especificaciones
    ● Rango: 200V
    ● Dígitos: 3 y ½
    ● Error máximo = ±(0,5% lectura + 3 digitos)

Expresar el resultado de la medición con una probabilidad del 95%
"""

""" 
Como el instrumento es de 3½ Dígitos en el rango de 200V la menor unidad
que muestra por pantalla es 000.1V, por ende, si dice que el 
                   
                     err_max = ±(0,5% lectura + 3 digitos)

nos queda que el error maximo del instrumento para el rango especificad es

                  err_max = ±(0,5% lectura + 3 digitos * 0.1V)

o, sea:
                        err_max = ±(0,5% lectura + 0.3V)
"""


N = 20  # Número de muestras
M = 100.145  # [V] Media aritmética
S = 1.489  # [V] Desvío Estándar Experimental

rango = 200  # [V]
err_max = [0.005, 0.3]  # [V]

# INCERTIDUMBRE TIPO A
u_a = round(S / np.sqrt(N), 3)  # Estimamos el desvío verdadero a partir de N muestras

# INCERTIDUMBRE TIPO B
err_lectura = err_max[0]
err_rango = err_max[1]
semrng_v = round(M * err_lectura + err_rango, 3)
"""
Las especificaciones son un límite uniforme, por lo que se modela con distr.
Rectangular, por ende el k = 3.
"""
k = 3
u_b = round(semrng_v / np.sqrt(k), 3)

# INCERTIDUMBRE COMBINADA
u_c = round(np.sqrt(u_a**2 + u_b**2), 3)

# GRADOS DE LIBERTAD
v_eff = round((u_c**4) / ((u_a**4) / (N - 1)), 0)

"""
Con los grados de libertad puedo buscar en la tabla de T-de-Student el factor k
para corregir la incertidumbre combinada para un 95% de confianza.
"""

print(u_a)
print(u_b)
print(u_c)
print(round(v_eff, 0))
