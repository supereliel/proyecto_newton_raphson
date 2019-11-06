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

def error (x,ant):
    return math.fabs((x-ant)/x)

def newton_raphson(f, x, ER, N):
    """
    Implementa el Algoritmo de Newton-Raphson y retorna la aproximación de la
    raiz.

    Parámetros:
    f: función de variable real f(x).
    x: aproximación inicial.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    i=1
    ant=0
    e=ER+1 
    for i in range (N):
        if (e>ER):
            ant=x
            d=derivada(f)
            x=x- f(x)/d(x)
            e=error(x,ant)
            print("Iteración:", i, "Aproximación:", x, "Error:", e)    
    return x
       

if __name__ == "__main__":
     f = lambda x: math.e**x-3*x**2
     g= lambda x: math.cos(x)+math.e**-x
     newton_raphson(f,0.5,0.02,10)
    # Pruebe aquí su función
