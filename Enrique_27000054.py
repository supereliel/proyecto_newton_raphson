#!/usr/bin/env python3
"""
Proyecto Algoritmo de Newton-Raphson.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

from math import *

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

def newton_raphson(f,x,ER,N):
    df=derivada(f, h=0.02)
    xi= x
    error= 1e3
    n=1
    while (error>ER) and (n<N):
        xi= xi-f(xi)/df(xi)
        error = abs (f(xi))
        print ("Iteracion :", (n)," Aproximacion: ", (xi), " Error: ", (error))
        n= n+1 
    print ("Solucion aproximada ", (xi))
    return xi

##def newton_raphson(f, x, ER, N):
##    """
##    Implementa el Algoritmo de Newton-Raphson y retorna la aproximación de la
 ##   raiz.

##    Parámetros:
##    f: función de variable real f(x).
##    x: aproximación inicial.
##    ER: cota mínima del error relativo.
##    N: número máximo de iteraciones.
##    """

##    print("Iteración:", i, "Aproximación:", xi, "Error:", err)

##   return xi


if __name__ == "__main__":
    # Pruebe aquí su función.
    f= lambda x: x**2-10;
    newton_raphson(f,3,1e-3,5)
    pass
