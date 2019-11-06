#!/usr/bin/env python3
"""
Proyecto Algoritmo de Newton-Raphson.
Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math
f = lambda x: math.exp(x)-3*x**2 
x=0.5
ER=0.02
N=10
def derivada(f,h=0.02):
    """
    Retorna la función derivada de f dado un h.
    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x+h)-f(x))/h

    return _
def recursivo(f, rel, xi, I, x):
    df=derivada(f) 
    if (rel>ER)&(I<N):
        xi=x-(f(x)/df(x))
        rel=abs((xi-x)/xi)
        if I==1:
            print("Iteración:", I, "Aproximación:", xi)
        else:
            print("Iteración:", I, "Aproximación:", xi, "Error:", rel)
        return recursivo(f, rel, xi, I+1, xi)
    else:
        return xi
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
    rel=ER+1
    xi=0
    I=1
    recursivo(f, rel, xi, I, x)
    return xi


if __name__ == "__main__":
    # Pruebe aquí su función.
    
    newton_raphson(f,x,ER,N)
    pass



