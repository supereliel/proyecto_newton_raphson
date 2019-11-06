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
    #Autor: Estefano Ramos C.I: V-267778542
    #Fecha: 05/11/2019
    #Versión: 1.0.1

    df = derivada(f)        #Se obtine la derivada de la funcion.
    xi = x                  #Se crea la variable que almacenara la aproximación de la raiz y se le asigna la aproximación inicial como el primer valor a iterar.
    x_1= 0                  #Se crea la variable auxiliar para almacenar la aproximación actual.
    ea=ER+1                 #Se crea la variable que almacena el error acumulado, se inicializa con el valor minimo del error relativo + 1 para que no falle el programa.
    i=0                     #se crea un contador para saber en que iteracion estamos

    print("Aproximación inicial:", xi)                                  #Mensaje inicial.

    while ( i<=N and ea>ER):                                            #Inicio de un loop mientras el contador sea menor al numero maximo de iteraciones y el error aprozimado no sea el optimo.

        i= i + 1                                                        #Incrementa el contador.
        
        x_1= xi-(f(xi)/df(xi))                                          #Se calcula la siguiente aproximación.

        ea=abs((x_1-xi)/x_1)                                            #Se calcula el nuevo error.

        xi = x_1                                                        #A la aproximación actual se le asigna la siguiente.

        print("Iteración:", i, "Aproximación:", xi, "Error:", ea)      #Estado de las variables por iteracion.
                  
    return xi                                                           #Valor de salida.


if __name__ == "__main__":
    # Pruebe aquí su función.

    k = lambda x: math.atan(x)+x-1


    newton_raphson(k,0,0.01,10)

    pass
