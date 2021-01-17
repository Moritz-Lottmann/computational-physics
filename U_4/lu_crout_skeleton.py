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
    y = np.array([b[i] - sum(L[i, j] * y[j] for j in range(0, i-1)) for i in range(0,n)])

    # Rückwärtselimination
    x = np.array([1 / U[i, i] * (y[i] - sum(U[i, j] * x[j] for j in range(1+i, n))) for i in range(0,n)])

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
    U = A


    for j in range(0, n):

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

    L, U = myLU(A)
    print(L)
    print()
    print(U)
    print()
    print(np.dot(L,U))
