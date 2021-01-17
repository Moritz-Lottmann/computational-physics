import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class DownhillSimplex():        #Klasse die einen Simplex erstellt

    '''
    fhandle: übergebene Funktion
    x_start: Startpunkt
    dimension: Dimension der Funktion
    (hätte man sicher auch irgendwie aus der fhandle bestimmen können, ist hier aber
    auch nicht weiter wichtig für diese Aufgabe)
    '''
    def __init__(self, fhandle, x_start, dimension = 2):
        '''
        im allgeimenen habe ich meine Funktionen weitestgehend so ausgelegt, dass
        diese auch n-Dimensional funktionieren, mit Ausnahme der Berechnung der Fläche
        des Simplex. Für die Aufgabe wird jedoch nur ein 2-Dimensionales Problem gefordert
        weshalb dimension standardmäßig 2 ist
        '''
        self.dimension = dimension
        self.fhandle = fhandle

        self.alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
        self.beta_   = 0.5  # empfohlener Faktor für die Kontraktion
        self.gamma_  = 2.0  # empfohlener Faktor für die Expansion
        self.lambda_ = 0.1  # empfohlene Größe des Startsimplex

        self.x_array = np.empty([dimension+1,dimension])    #leres Array für die Punktkoordinaten
        self.x_array[0] = np.array(x_start)                 #der erste Punkt ist der übergebene

        lambda_array = self.lambda_ * np.identity(dimension)#Matrix zur "verschiebung" der weiteren Punkte
        for d in range(dimension):                          #Erstellen der weiteren punkte um lamda verschoben
            self.x_array[d+1] = self.x_array[0] + lambda_array[d]

        self.y_array = self.fhandle(self.x_array)           #array der Funktionswerte

        self.x_sort = self.x_array[np.argsort(self.y_array)] #"bester" Wert bei 0
        self.y_sort = self.y_array[np.argsort(self.y_array)] #"bester" Wert bei 0

    def print_points(self):         #printet alle Punkte
        for point in self.x_array:
            print(point)

    def print_y(self):              #printet die Funktionswerte der Punkte
        print(self.y_array)

    def update_sort(self):          #berechnet die sortierten arrays neu
        self.x_sort = self.x_array[np.argsort(self.y_array)] #"bester" Wert bei 0
        self.y_sort = self.y_array[np.argsort(self.y_array)] #"bester" Wert bei 0

    def mirror(self):               #spiegelung des Simplex
        x_s = 1 / (len(self.x_array)-1) * np.sum(self.x_sort[:-1], axis = 0)
        x_r = x_s - self.alpha_ * (self.x_sort[-1] -x_s)
        y_r = self.fhandle(x_r)
        return x_s, x_r, y_r

    def expand(self, x_s, x_r):     #vergrößern des Simplex
        x_e = x_s + self.gamma_ * (x_r - x_s)
        y_e = self.fhandle(x_e)
        return x_e, y_e

    def contract(self, x_s, x_max): #verkleinern des Simplex
        x_c = x_s + self.beta_ * (x_max - x_s)
        y_c = self.fhandle(x_c)
        return x_c, y_c

    def compress(self):             #zusammenziehen des Simplex
        x_min = self.x_sort[0]
        for i in range(len(self.x_array)):
            self.x_array[i] = (self.x_array[i] + x_min) / 2
        self.update_sort()

    def replace_max(self, x_new, y_new):    #erneuert die Punkte und Funktionswerte im Simplex Objekt
        self.x_array[np.argmax(self.y_array)] = x_new
        self.y_array[np.argmax(self.y_array)] = y_new
        self.update_sort()

    def deviation(self):            #gibt die Standardabweichung zurück
        return np.std(self.y_array)

    def area(self):            #gibt die Fläche zurück, funktioniert so nur bei n=2
        return np.abs(np.cross(self.x_array[0], self.x_array[1]) / 2)

    def centeroid(self):            #gibt den Mittelpunkt der Punkte wieder
       length = self.x_array.shape[0]
       sum_x = np.sum(self.x_array[:, 0])
       sum_y = np.sum(self.x_array[:, 1])
       return sum_x/length, sum_y/length


'''
fhandle: übergebene Funktion
x_start: Startpunkt des simplex
N_max: maximale Anzahl an Iterationen
p: Standartabweichung und Fläche bei der der Simplex das Minimum gefunden hat
visualize_walk, visualize_path, print_statements: Boolean Variablen zur Visualisierung
des Simplex. Weitere Erläuterungen in der PDF
'''
def simplex(fhandle, x_start, N_max, p, visualize_walk = False, visualize_path = False, print_statements = False, return_area = False):
    l_centeroid = []    #liste der Mittelpunkte
    l_area = []         #liste der Flächeninhalte
    l_points = []       #liste aller Punkt-Koordinaten
    iteration_no = 0    #anzahl der Iterationen
    pltr = [[x_start[0], x_start[0]], [x_start[1], x_start[1]]]#plot range für die Visualisierung
    ts = DownhillSimplex(fhandle, x_start)  #Simplex Objekt
    '''
    im Folgenden wird das Downhill Simplex Verfahren nach dem in der bereitgestellten
    PDF beschriebenen Algorhitmus ausgefürt. Ich werde diesen hier nicht weiter
    kommentieren da relativ klar vorgegeben war was zu tun ist.
    Jedoch habe ich einige Funktionen beigefügt die die visualisierung ermöglichen,
    welche ich etwas erläutern werde.
    '''
    for i in range(int(N_max)):
        xs, xr, yr = ts.mirror()
        if(yr < ts.y_sort[0]):
            xe, ye = ts.expand(xs, xr)
            if(ye < yr):
                ts.replace_max(xe, ye)
                if(print_statements):print('replaced expand')
            else:
                ts.replace_max(xr, yr)
                if(print_statements):print('replaced mirror')
        elif(yr < ts.y_sort[int(ts.dimension / 2)]):
            ts.replace_max(xr, yr)
            if(print_statements):print('replaced mirror')
        elif(yr < ts.y_sort[-1]):
            ts.replace_max(xr, yr)
            if(print_statements):print('replaced mirror')
        else:
            xc, yc = ts.contract(xs, ts.x_sort[-1])
            if(yc < ts.y_sort[-1]):
                ts.replace_max(xc, yc)
                if(print_statements):print('replaced contract')
            else:
                ts.compress()
                if(print_statements):print('compressed')

        if(print_statements):
            ts.print_points()
            print()

        '''
        falls visualize_path oder visualize_walk True sind werden die Punkte bzw
        Mittelpunkte in ein Array gespeichert.
        '''
        if(visualize_path or visualize_walk):
            l_centeroid.append(ts.centeroid())

        if(visualize_walk):
            l_points.append(np.copy(ts.x_array))

            '''Die folgenden if-Abfragen  prüfen ob ein neuer Punkt auserhalb der biserugen Plot range liegt,
            um diese entsprechend anzupassen'''
            pltr[0] = [np.amin(ts.x_array[:, 0]) if np.amin(ts.x_array[:, 0]) < pltr[0][0] else pltr[0][0],
                       np.amax(ts.x_array[:, 0]) if np.amax(ts.x_array[:, 0]) > pltr[0][1] else pltr[0][1]]
            pltr[1] = [np.amin(ts.x_array[:, 1]) if np.amin(ts.x_array[:, 1]) < pltr[1][0] else pltr[1][0],
                       np.amax(ts.x_array[:, 1]) if np.amax(ts.x_array[:, 1]) > pltr[1][1] else pltr[1][1]]

        if(return_area):
            l_area.append(ts.area())

        if(ts.deviation() < p and ts.area() < p):
            iteration_no = i
            if(print_statements):print('Done at iteration ', i)
            break

    '''einfaches Plotten aller Mittelpunkte was den "Weg" des Simplex zeigt'''
    if(visualize_path and not(visualize_walk)):
        l_centeroid = np.array(l_centeroid)
        plt.plot(l_centeroid[:,0], l_centeroid[:,1])
        plt.show()

    '''
    hier habe ich einen relativ simplen interaktieven Plot mit schieberegler erstellt, was etweder nur die einzelnen
    Punkte zu dem in dem Schieberegler gegebenen Zeitpunkt anzeigt, oder alternativ auch den
    Mittlepunkt zusätzlich plottet
    '''
    if(visualize_walk):
        l_centeroid = np.array(l_centeroid)

        fig, ax = plt.subplots()

        #die ersten beiden linien
        l1, = plt.plot(l_points[0][:,0], l_points[0][:,1], 'm', marker = "x")
        #die dritte linie
        l2, = plt.plot([l_points[0][0,0], l_points[0][-1,0]], [l_points[0][0,1], l_points[0][-1,1]], 'm',  marker = "x")
        #falls diese option angegeben ist plotten der Mittelpunkte
        if(visualize_path): l3, = plt.plot(l_centeroid[:,0], l_centeroid[:,1], 'c')
        #plotten des Mittelpunktes
        p1, = plt.plot(l_centeroid[0,0], l_centeroid[0,1], marker = "x")

        plt.xlim(pltr[0][0], pltr[0][1])
        plt.ylim(pltr[1][0], pltr[1][1])

        ax_slider = plt.axes([0.25, .03, 0.50, 0.02])   #größe des Silders

        slider = Slider(ax_slider, 't', 0, iteration_no, valinit=0, valfmt="%i")

        def update(val):
            t = slider.val

            l1.set_xdata(l_points[int(t)][:,0])
            l1.set_ydata(l_points[int(t)][:,1])

            l2.set_xdata([l_points[int(t)][0,0], l_points[int(t)][-1,0]])
            l2.set_ydata([l_points[int(t)][0,1], l_points[int(t)][-1,1]])

            p1.set_xdata(l_centeroid[int(t),0])
            p1.set_ydata(l_centeroid[int(t),1])
            fig.canvas.draw_idle()

        slider.on_changed(update)

        plt.show()

    #die Funktion gibt wie gefordert die Punkte, den Funktionswert und die Anzahl der Iterationen zurück
    #dabei wird jeweils der "beste" Wert zurück gegeben
    if(return_area):
        return ts.x_sort[0,:], ts.y_sort[0], iteration_no, l_area
    else:
        return ts.x_sort[0,:], ts.y_sort[0], iteration_no

if(__name__ == '__main__'):
    from himmelblau import himmelblau
    fhandle = himmelblau
    N_max   = 1e10
    p       = 1e-15
    x_start = [100, 10]
    simplex(fhandle, x_start, N_max, p, visualize_walk = True, visualize_path = True, print_statements = False)
