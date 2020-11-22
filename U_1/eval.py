""" Dieses Skript führt die Funktion 'diffquot' aus.

Es wird die numerische Ableitung der Funktion sin(x) mittels rechtsseitigem
Differenzenquotienten berechnet und mit ihrer analytischen Ableitung, cos(x),
verglichen. Dabei wird insbesondere das Verhalten der Differenz aus beiden
untersucht.
"""

import numpy as np
import matplotlib.pyplot as plt
from diffquot import diffquot

# Aufruf der Ableitungsfunktion und Speichern des Ergebnis in zwei Variablen.
# Wir nutzen hier die Werte für den Beispielaufruf der Funktion diffquot.
fhandle = np.sin  # Definition der input-Funktion
a = -50          # untere Intervallgrenze
b = 50           # obere Intervallgrenze
h = 0.1           # Schrittweite

xwerte, ableitung = diffquot(fhandle, a, b, h)

# Darstellung der Funktion und ihrere Ableitung in einem Plot
fig, ax = plt.subplots()
ax.plot(xwerte, np.sin(xwerte), label='sin(x)')
ax.plot(xwerte, ableitung, label='num. diff.')
ax.set_title('Funktion und ihre Ableitung')
ax.legend(loc='best')
fig.tight_layout()
plt.show()

#%% Gesamtfehler in Abhängigkeit der Schrittweite

anzahl_h = 200
h_min = 0.01
h_max = 3

# äquidistanter Vektor im Intervall [h_min, h_max] der Länge anzahl_h
h = np.linspace(h_min, h_max, anzahl_h)

# Intialisierung des Gesamtfehler-Vektors

fehler = np.full_like(h, None)

for index in range(anzahl_h):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h[index])

    # berechne die analytische Ableitung
    analytisch = np.cos(xwerte)

    fehler[index] = h[index]*np.sum(abs(ableitung-analytisch))


# Darstellung als Linienplot

fig, ax = plt.subplots()
ax.plot(fehler, label='Gesamtfehler')
ax.set_title('Gesamtfehler in Abhängigkeit der Schrittweite')
ax.legend(loc='best')
fig.tight_layout()
plt.show()

#%% lokaler Fehler für feste Schrittweiten

# überschreibe h erneut
h = [1, 2, 2]

fig, ax = plt.subplots()

for index in range(3):

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h[index])

    # berechne die analytische Ableitung
    analytisch = np.cos(xwerte)

    # Darstellung des Betrags der Differenz beider Ableitungen als Linienplot
    ax.plot(xwerte, abs(ableitung-analytisch),
            label='h=%.1f' % h[index])

# Plotbeschriftung
ax.legend(loc='best')
ax.set_xlabel('Koordinate x')
ax.set_ylabel('lokaler Fehler')
ax.set_title('Lokaler Fehler')
fig.tight_layout()
plt.show()
