import numpy as np
import matplotlib.pyplot as plt
def diffquot(fhandle, a, b, h):

xwerte = np.arange(a, b+h, h)                 #X-Werte von a bis b+h mit h "Abstand"

    ywerte = fhandle(xwerte)                    #Funktionswerte zu den X-Werten
    ableitung = []                              #leeres array für die Ableitungswerte

    for y1, y2 in zip(ywerte[:-1], ywerte[1:]):   #funktionswerte an der stelle i und i+1 also f(xi) und f(xi+h) da xi+1 = xi+h
        value = (y2-y1)/h                       #Ableitungswert berechnet mit f(xi+h)-f(xi)/h
        ableitung.append(value)                 #anhängen an das array

    ableitung = np.array(ableitung)             #umwandlung in np array (np arrays lassen sich besser verrechnen)
    return (xwerte[:-1], ableitung)             #return der x werte und der ableitung


'''Test mit Sinus'''
xval, diff = diffquot(np.sin,-10,10,0.1)
plt.plot(xval, np.sin(xval), xval, diff)
plt.show()
