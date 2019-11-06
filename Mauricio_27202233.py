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

def errorRelativo(xi, x):
    return abs((xi - x) / xi)

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
    dxdf = derivada(f)
    error, iteracion, xi= 1,0,0
    while (not error < ER and iteracion <= N):
        try:
            xi = x - (f(x)/dxdf(x))
            error = errorRelativo(xi,x)
            print("Iteración:", iteracion, "Aproximación:", xi, "Error:", error)
            iteracion += 1
            x = xi
        except ZeroDivisionError:
            print ("Ha ocurrido un error.") 
    return xi


if __name__ == "__main__":
    f = lambda x : math.e**x-3*x**2
    g = lambda x : math.sin(x)-math.e**-x
    print (newton_raphson(f,0.5,0.02,10))
