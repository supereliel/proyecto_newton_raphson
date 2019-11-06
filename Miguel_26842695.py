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

def newrp_recursivo(f,x,ER,N,ERac,i,xi):
    #Algoritmo recursivo que realiza el procedimiento de Newton Rapshon

    der=derivada(f) #Se calcula la derivada de la funcion

    if ER>ERac or i>N: #Condicion de parada del algoritmo
        return xi
    else:
        xi=xi-f(x)/der(x)# Se calcula la xi actual
        if i==0:
            #Esta linea esta para evitar mostrar el primer error relativo que seria 0.1
            print("Iteracion: ",i," Aproximacion ",xi," Error: No posee")
        else:
            ERac=math.fabs((xi-x)/xi) #Se calcula el error relativo actual
            print("Iteracion: ",i, "Aproximacion",xi," Error: ",ERac)
        x=xi
        """Se continua ejecutando el algoritmo hasta su condicion de parada"""
        return newrp_recursivo(f,x,ER,N,ERac,i+1,xi) 

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

    """ Se envia como parametro 5to parametro 0.1 que corresponde
    al error realitvo actual para hacer funcionar el algoritmo,
    el 6to parametro coresponde a i que se iniciliza en 0, el
    ultimo parametro es el xi que en la primera iteracion posee el
    mismo valor que x"""
    return newrp_recursivo(f,x,ER,N,0.1,0,x) 


if __name__ == "__main__":
    # Pruebe aquí su función.

    f= lambda x: math.exp(x)-3*x**2
    yx=lambda x: math.sin(x)-math.exp(-x)

    print("Xi Final: ",newton_raphson(f,0.5,0.02,5))
    
