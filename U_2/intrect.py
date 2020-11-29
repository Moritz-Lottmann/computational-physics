import numpy as np
import matplotlib.pyplot as plt
def intrect(fhandle, a, b, h):
    # Mittelpunkte der Intervalle ermitteln
    # --> Vektor der Intervall-Mittelpunkte durch Verschiebung um h/2
    xwerte_mitte = np.arange(a + h/2, b - h/2.00001, h)
    #2.00001 da sonst der letzte Wert nicht mitgenommen wird
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

#Test
if __name__ == '__main__':
    f_x2 = np.sin
    area, xwerte, stamm_funk = intrect(f_x2 , 0, 10, 0.0001)
    plt.plot(xwerte[:-1], stamm_funk, xwerte[:-1], f_x2(xwerte[:-1]))
    plt.show()
