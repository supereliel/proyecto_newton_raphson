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

    i = 0
    lastAprox = x
    currentAprox = 0.0

    getCurrentAprox = lambda: lastAprox - (f(lastAprox)/derivada(f)(lastAprox))
    getRelativeError = lambda: abs((currentAprox - lastAprox)/currentAprox)

    while(i <= N):
        i += 1
        currentAprox = getCurrentAprox()
        error = getRelativeError()
        lastAprox = currentAprox

        print("Iteración:", i, "Aproximación:", currentAprox, "Error:", error)

        if(error < ER):
            print("El error relativo aproximado de:", ER, "para la funcion:", 0, "es de:", error)
            return currentAprox
    else:
        print("Se ha alcanzado el litmite de iteraciones.")
        return currentAprox


if __name__ == "__main__":

    f = lambda x: math.sin(x) - math.exp(-x)
    print("La aproximacion para la raiz de la funcion:", 0, "es de:", newton_raphson(f, 3.5, 0.035, 10))
    pass
