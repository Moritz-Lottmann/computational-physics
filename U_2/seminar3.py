# -*- coding: utf-8 -*-
from intrect import *
""" Dieses Skript führt die Funktion 'intrect' aus.

Die numerische Integration nach der Rechteckregel wird an den Funktionen
f(x) = x, f(x) = x^2 und f(x) = exp(x) durchgeführt. Anhand der berechneten
Stammfunktionen und Flächeninhalte wird das Konvergenzverhalten zum jeweiligen
analytischen Ergebnis verglichen.
"""


# Berechnung der exakten Flächeninhalte
exakt_x = 50
exakt_x2 = 1000 / 3
exakt_ex = np.exp(10) - 1

# %% Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle
# logarithmisch äquidistanter Vektor der Schrittweiten
li_h = np.logspace(-4, -1, 400)

# Initialisierung der arrays
li_x = []
li_x2 = []
li_ex = []

# Definition der Funktionen (vgl. MatLab function handles)
f_x = lambda x : x
f_x2 = lambda x : x**2
f_ex = lambda x : np.exp(x)


# Schleife über alle h zur Berechnung von Integral und dessen Fehler
for h in li_h:
    # f(x) = x
    li_x.append(abs(intrect(f_x, 0, 10, h)[0] - exakt_x))
    # f(x) = x^2
    li_x2.append(abs(intrect(f_x2, 0, 10, h)[0] - exakt_x2))
    # f(x) = exp(x)
    li_ex.append(abs(intrect(f_ex, 0, 10, h)[0] - exakt_ex))

# logarithmischer Plot Fehler vs. Schrittweite h
# Darstellung als Linienplot
fig, ax = plt.subplots(1, 3)
ax[0].plot(li_h, li_x)
ax[1].plot(li_h, li_x2)
ax[2].plot(li_h, li_ex)
plt.setp(ax, xscale = 'log', yscale = 'log')

# Plotbeschriftung
ax[0].set_ylabel('Fehler')
plt.setp(ax, xlabel = 'h')
ax[0].set_title('Funktion : f(x) = x')
ax[1].set_title('Funktion : f(x) = $\ x^2$')
ax[2].set_title('Funktion : f(x) = $\ e^x$')
plt.show()

# rechte Intervallgrenze fest
b = 10
# linke Intervallgrenze mit verschiedenen Werten
li_a = np.arange(0,10,1)
li_Stammfunk = []

for a in li_a:
    # Auswertung des numerischen Integrals
    li_Stammfunk.append(intrect(f_x2, a, b, 0.00001)[1:3])
    # Darstellung als Linienplot

fig, ax2 = plt.subplots()
for F in li_Stammfunk:
    ax2.plot(F[0][:-1], F[1], label = "a = " + str(int(F[0][0])))

# Plotbeschriftung für alle Graphen im selben Plot
ax2.set_ylabel("F(x)")
ax2.set_xlabel("x")
ax2.set_title("Funktion: $\ f(x) = x^2$")
ax2.legend()
plt.show()
