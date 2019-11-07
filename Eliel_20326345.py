#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proyecto Algoritmo de Newton-Raphson.
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
    error_aprox  = ER+1000000
    aprox_actual = x
    i = 1
    while i <= N:
        if error_aprox > ER:
            fp = derivada(f)(aprox_actual)
            if fp == 0:
                print("El método no se puede aplicar, el resultado de la derivada es 0.")
                return 0
            aprox_sig    = aprox_actual - (f(aprox_actual)/fp)
            error_aprox  = math.fabs((aprox_sig-aprox_actual)/aprox_sig)
            aprox_actual = aprox_sig
            print("Iteración:", i,"Aproximación:", aprox_actual,"Error:", error_aprox)
        i += 1
    return aprox_actual

if __name__ == "__main__":
    ITERACIONES = 4
    ER          = 0.02

    f = lambda x: math.exp(-x)-math.log(x)
    g = lambda x: math.atan(x)+x-1
    y = lambda x: math.pow(x,2)-26

    newton_raphson(f, 1, ER, ITERACIONES)
    #newton_raphson(g, 0, ER, ITERACIONES)
    #newton_raphson(y, 5, ER, ITERACIONES)