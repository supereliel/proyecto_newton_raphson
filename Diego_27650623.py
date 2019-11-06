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
    i=0; xi=0; err= ER+1
    while (err>ER) & (i<N):
        f_prima=derivada(f)
        xi= x-(f(x)/f_prima(x))
        if (i==0):
            print("Iteración:", i+1, "Aproximación:", xi, "Error: ------------------------") 
        else:
            err=abs((xi-x)/xi)
            print("Iteración:", i+1, "Aproximación:", xi, "Error:", err)
        x=xi
        i=i+1
    return xi


if __name__ == "__main__":
    # Pruebe aquí su función. (se utilizaron los ejemplos dados en clase)
    f1= lambda x: math.exp(x)-3*x**2
    f2= lambda x: math.sin(x)-math.exp(-x)   
    print("Ejemplo 1:")   
    newton_raphson(f1, 0.5, 0.02, 40)
    print()
    print("Ejemplo 2:")
    newton_raphson(f2,3.5,0.02,40) 
    pass
