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
    xi=x
    contador=0
    error=1000
    b=False
    while (b==False):
    	ximas1=xi-(f(xi)/derivada(f)(xi))
    	if contador>0:
    		error=abs((ximas1-xi)/ximas1)
    		xi=ximas1
    	else:
    		xi=ximas1
    	if contador==0:
    		print("Iteración:", contador, "Aproximación:", xi)
    	else:
    		print("Iteración:", contador, "Aproximación:", xi, "Error:", error)
    	contador=contador+1	
    	if error<ER:
    		b=True
    	if contador>N:
    		b=True
    return xi


if __name__ == "__main__":
    # Pruebe aquí su función.
    f=lambda x:(math.e)**x-3*(x**2)
    newton_raphson(f,0.5,0.02,100)
