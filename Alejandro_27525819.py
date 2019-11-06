#!/usr/bin/env python3
"""
Proyecto Algoritmo de Newton-Raphson.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def f(x):
    return math.exp(x)-3*x**2

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
    rela=ER+1
    xi=x
    xiI=0
    ni=1 
    h=derivada(f)
    while(ER<rela) and (ni<N):
        xiI=xi-(f(xi)/h(xi))
        rela=abs(xiI-xi)/xiI
        print("Iteración:", ni,"Xi", xi,"Aproximación:", xiI, "Error:", rela)
        xi=xiI
        ni=ni+1
    return xiI


if __name__ == "__main__":
    # Pruebe aquí su función.
    print (newton_raphson(f,0.5,0.02,10))
 
