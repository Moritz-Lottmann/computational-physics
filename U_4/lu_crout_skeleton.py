# -*- coding: utf-8 -*-

import numpy as np


def elimination(L, U, b):
    '''Löst ein Gleichungssystem A*x=b durch Vorwärts- und Rückwärtselimination
    für die LU-Zerlegung von A=L*U.

    Beispiel
    --------
    x = elimination(L, U, b)

    Eingabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix

    b : float (vector)
        Inhomogenitätsvektor des Gleichungssystems

    Ausgabe
    -------
    x : float (vector)
        Lösungsvektor
    '''


    # Vorwärtselimination

    # Rückwärtselimination
    
    return x


def myLU(A):
    '''LU-Zerlegung einer Matrix A=L*U mittels Crout-Algorithmus.

    Beispiel
    --------
    L, U = myLU(A)

    Eingabe
    -------
    A : float (2d array)
        Die zu zerlegende Matrix

    Ausgabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix
    '''


    return L, U
