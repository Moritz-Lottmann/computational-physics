# -*- coding: utf-8 -*-
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

    # Funktionswerte an den Intervallmittelpunkten

    # Aufsummierung von Teilintervallen durch cumsum

    # Berechnung der Fläche

    # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
    # rechten Rand des Teilintervalls

    # linke Intervallgrenze hinzufügen

    return area, xwerte, stamm_funk
