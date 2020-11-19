import numpy as np
import matplotlib.pyplot as plt
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

    xwerte = np.arange(a,b+h,h)                 #X-Werte von a bis b+h mit h "Abstand"
    ywerte = fhandle(xwerte)                    #Funktionswerte zu den X-Werten
    ableitung = []                              #leeres array für die Ableitungswerte
    for y1,y2 in zip(ywerte[:-1],ywerte[1:]):   #funktionswerte an der stelle i und i+1 also f(xi) und f(xi+h) da xi+1 = xi+h
        value = (y2-y1)/h                       #Ableitungswert berechnet mit f(xi+h)-f(xi)/h
        ableitung.append(value)                 #anhängen an das array

    ableitung = np.array(ableitung)             #umwandlung in np array (np arrays lassen sich besser verrechnen)
    return (xwerte[:-1], ableitung)             #return der x werte und der ableitung

'''Test mit Sinus'''
xval, diff = diffquot(np.sin,-10,10,0.1)
plt.plot(xval, np.sin(xval), xval, diff)
plt.show()
