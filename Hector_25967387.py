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

def err(x,prev):

    return math.fabs((x-prev)/x)

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
    prev=0
    error= ER+1
    dev= derivada(f)

    for i in range(N):
        if(error>ER):
            dev=derivada(f)
            prev=x
            x=x-f(x)/dev(x)
            e=err(x,prev)
            print("Iteración:", i, "Aproximación:", x, "Error:", error)
    return x


if __name__ == "__main__":
    f= lambda x : math.e**x-2*x**3
    b= lambda x : math.cos(x) + math.exp(-x)
    newton_raphson(f,0.4,0.01,10)
  