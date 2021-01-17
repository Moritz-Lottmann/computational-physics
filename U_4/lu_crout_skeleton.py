# -*- coding: utf-8 -*-

import numpy as np


def elimination(L, U, b):
    if(False):
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

    n = b.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)

    # Vorwärtselimination
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))

    # Rückwärtselimination
    for i in range(n-1, -1, -1):
        x[i] = 1 / U[i, i] * (y[i] - sum(U[i, j] * x[j] for j in range(1+i, n)))

    return x


def myLU(A):
    if(False):
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

    n = A.shape[0]
    L = np.identity(n)
    U = np.copy(A)


    for j in range(n):

        for i in range(j+1, n):

            L[i, j] = U[i, j] / U[j, j]
            U[i, j] = 0

            for k in range(j+1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]


    return L, U

if __name__ == "__main__":
    A = np.array([[1,2,3],
                  [4,5,6],
                  [9,8,7]])
    C = np.array([[1,1,0],
                  [4,0,2],
                  [0,2,1]])
    B = np.ones_like(A)
    b = np.array([1, 3, 3])
    L, U = myLU(C)
    x = elimination(L, U, b)
    print(x)
    print(C.dot(x))
