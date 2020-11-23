# -*- coding: utf-8 -*-
""" Dieses Skript führt die Funktion 'intrect' aus.

Die numerische Integration nach der Rechteckregel wird an den Funktionen
f(x) = x, f(x) = x^2 und f(x) = exp(x) durchgeführt. Anhand der berechneten
Stammfunktionen und Flächeninhalte wird das Konvergenzverhalten zum jeweiligen
analytischen Ergebnis verglichen.
"""


# Berechnung der exakten Flächeninhalte

# %% Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle

# logarithmisch äquidistanter Vektor der Schrittweiten

# Initialisierung der arrays


# Definition der Funktionen (vgl. MatLab function handles)


# Schleife über alle h zur Berechnung von Integral und dessen Fehler

for counter in range(h.size):
    # f(x) = x
    # f(x) = x^2
    # f(x) = exp(x)


# logarithmischer Plot Fehler vs. Schrittweite h
# Darstellung als Linienplot


# Plotbeschriftung


# %% Abhaengigkeit der Integrationskonstante vom linken Intervallrand
# am Bsp. der Stammfunktion F von x^2

# rechte Intervallgrenze fest

# linke Intervallgrenze mit verschiedenen Werten



for loop in range(a.size):

    # Auswertung des numerischen Integrals

    # Darstellung als Linienplot

# Plotbeschriftung für alle Graphen im selben Plot
