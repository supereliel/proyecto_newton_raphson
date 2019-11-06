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
    i= 0
    xi=0
    from math import e
    while (N> i):
        fund=derivada(f)
        xi=x-(f(x)/fund(x))
        i=i+1
        err=(xi-x)/xi
        x=xi
        if (err<0):
            err=err*-1
        print("Iteración:", i, "Aproximación:", xi, "Error:", err)
        if (err<ER):
            i=N
    return xi
f = lambda x: math.cos(x)- (x)  
if __name__ == "__main__":
    rep="s"
    while (rep=="s"):
        print ("Algoritmo de Newton Raphson para aproximar las raices de una función mediante derivadas.")
        print ("ingrese el valor de la aproximación inicial")
        x= float (input ())
        print ("Ingrese el valor del error para d1etener el algoritmo")
        err=float (input ())
        while (err<0):
            print ("El error no puede ser menor a 0, ingrese un valor correcto.")
            err= float (input ())
        print ("¿Cuántas veces se va a iterar si no ha llegado al error?")
        n= float (input ())
        while (n< 1):
            print ("La cantidad de iteraciones no puede ser menor a 1, ingrese un valor correcto")
            n= input ()
        #print ("el punto medio más cercano a la raiz es: ",biseccion(a, b, err, n,0,0,0,0))
        print ("la aproximación más cercana a la raiz es: ",newton_raphson(f, x, err, n))
        print ("fin del algoritmo, desea repetir las operacones (n/s) ?")
        rep= input ()
        while (rep != "n" and rep != "s"):
            print ("Ingrese un valor correcto (n/s)")
            rep= input()
    print ("Bye.")
    chao=input()
    pass
