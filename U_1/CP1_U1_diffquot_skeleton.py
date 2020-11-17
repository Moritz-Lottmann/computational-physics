def diffquot(fhandle, a, b, h):
    """ Berechne den rechtseitigen Differenzenquotienten.

    Argumente
    ---------
    fhandle : function
        die zu differenzierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Differentiation

    Output: 2-Tupel
    ------
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    ableitung : float
        Ergebnisvektor mit der numerischen Ableitung (1-d array)

    Funktionsaufruf
    ---------------
        xwerte, ableitung = diffquot(fhandle, a, b, h)

    Beispiel
    --------
        xwerte, ableitung = diffquot(np.sin, -10, 10, 0.1)
    """

    import numpy as np

    # Bestimmung des Definitionsbereichs der Funktion

    # Evaluierung der Funktion 'fhandle'


    # Berechung der numerischen Ableitung mittels des rechtsseitigen
    # Differenzenquotienten

    return (xwerte[:-1], ableitung)
