# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def intrect(fhandle, a, b, h):
    """ Numerische Integration einer beliebigen integrierbaren Funktion mittels
    der Rechteckregel.

    Argumente
    ---------
    fhandle : function
        die zu integrierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Teilintervalle

    Output: 3-Tupel
    ---------------
    area : float
        Berechnete Fläche
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    stamm_funk : float
        Berechnete Funktionswerte der Stammfunktion (1-d array)

    Funktionsaufruf
    ---------------
        area, xwerte, stamm_funk = intrect(fhandle, a, b, h)

    Beispiel
    --------
        area, xwerte, stamm_funk = intrect(np.exp, 0, 10, 0.01)
    """

    # Mittelpunkte der Intervalle ermitteln
    # --> Vektor der Intervall-Mittelpunkte durch Verschiebung um h/2
    xwerte_mitte = np.arange(a + h/2, b - h/2, h)
    # Funktionswerte an den Intervallmittelpunkten
    ywerte = fhandle(xwerte_mitte)
    # Aufsummierung von Teilintervallen durch cumsum
    stamm_funk = np.cumsum(ywerte)*h
    # Berechnung der Fläche
    area = stamm_funk[-1]
    # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
    # rechten Rand des Teilintervalls
    # linke Intervallgrenze hinzufügen
    xwerte = np.append(a, xwerte_mitte + h/2)

    return area, xwerte, stamm_funk


if __name__ == '__main__':
    area, xwerte, stamm_funk = intrect(np.exp, 0, 10, 0.01)
    print(stamm_funk)
