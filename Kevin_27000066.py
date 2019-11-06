#!/usr/bin/env python3
"""
Proyecto Algoritmo de Newton-Raphson.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def derivada(f, h = 0.02):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _

i = 0    
err = 0
xi = 0
d = None

def newton_raphson(f, x, ER, N):
    global i
    global err
    global xi
    global d
    ap = 0

    if(i == 0):
        err = ER +1
        xi = x
        d = derivada(f)

    if(i <= N and err > ER):
        ap = xi - (f(xi) / d(xi))
        err = abs((ap - xi) / ap)
        xi = ap
        i += 1
        print("Iteración:", i, "Aproximación:", xi, "Error:", err)
        return newton_raphson(f,x, ER, N) 
    else:
        return xi

if __name__ == "__main__":
    # Pruebe aquí su función.
    fc = lambda x: math.exp(x) - ( 3 * pow(x,2))
    print("Aproximacion: ", newton_raphson(fc,0.5,0.02,10))
    pass
