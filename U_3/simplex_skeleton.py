import numpy as np
from himmelblau import himmelblau
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider


class DownhillSimplex():

    def __init__(self, fhandle, x_start, dimension = 2):
        self.dimension = dimension

        self.alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
        self.beta_   = 0.5  # empfohlener Faktor für die Kontraktion
        self.gamma_  = 2.0  # empfohlener Faktor für die Expansion
        self.lambda_ = 0.1  # empfohlene Größe des Startsimplex

        self.x_array = np.empty([dimension+1,dimension])
        self.x_array[0] = np.array(x_start)

        lambda_array = self.lambda_ * np.identity(dimension)
        for d in range(dimension):
            self.x_array[d+1] = self.x_array[0] + lambda_array[d]

        self.y_array = fhandle(self.x_array)

        self.x_sort = self.x_array[np.argsort(self.y_array)] #"bester" Wert bei 0
        self.y_sort = self.y_array[np.argsort(self.y_array)] #"bester" Wert bei 0

    def print_points(self):
        for point in self.x_array:
            print(point)

    def print_y(self):
        print(self.y_array)

    def update_sort(self):
        self.x_sort = self.x_array[np.argsort(self.y_array)] #"bester" Wert bei 0
        self.y_sort = self.y_array[np.argsort(self.y_array)] #"bester" Wert bei 0

    def mirror(self):
        x_s = 1 / (len(self.x_array)-1) * np.sum(self.x_sort[:-1], axis = 0)
        x_r = x_s - self.alpha_ * (self.x_sort[-1] -x_s)
        y_r = fhandle(x_r)
        return x_s, x_r, y_r

    def expand(self, x_s, x_r):
        x_e = x_s + self.gamma_ * (x_r - x_s)
        y_e = fhandle(x_e)
        return x_e, y_e

    def contract(self, x_s, x_max):
        x_c = x_s + self.beta_ * (x_max - x_s)
        y_c = fhandle(x_c)
        return x_c, y_c

    def compress(self):
        x_min = self.x_sort[0]
        for i in range(len(self.x_array)):
            self.x_array[i] = (self.x_array[i] + x_min) / 2
        self.update_sort()

    def replace_max(self, x_new, y_new):
        self.x_array[np.argmax(self.y_array)] = x_new
        self.y_array[np.argmax(self.y_array)] = y_new
        self.update_sort()

    def deviation(self):
        return np.std(self.y_array)

    def centeroid(self):
       length = self.x_array.shape[0]
       sum_x = np.sum(self.x_array[:, 0])
       sum_y = np.sum(self.x_array[:, 1])
       return sum_x/length, sum_y/length


def simplex(fhandle, x_start, N_max, p, visualize_walk = False, visualize_path = False, print_statements = False):
    l_centeroid = []
    l_points = []
    iteration_no = 0
    pltr = [[x_start[0], x_start[0]], [x_start[1], x_start[1]]]
    ts = DownhillSimplex(fhandle, x_start)
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

        if(visualize_path or visualize_walk):
            l_centeroid.append(ts.centeroid())

        if(visualize_walk):
            l_points.append(np.copy(ts.x_array))

            pltr[0] = [np.amin(ts.x_array[:, 0]) if np.amin(ts.x_array[:, 0]) < pltr[0][0] else pltr[0][0],
                       np.amax(ts.x_array[:, 0]) if np.amax(ts.x_array[:, 0]) > pltr[0][1] else pltr[0][1]]
            pltr[1] = [np.amin(ts.x_array[:, 1]) if np.amin(ts.x_array[:, 1]) < pltr[1][0] else pltr[1][0],
                       np.amax(ts.x_array[:, 1]) if np.amax(ts.x_array[:, 1]) > pltr[1][1] else pltr[1][1]]

        if(ts.deviation() < p):
            iteration_no = i
            if(print_statements):print('Done at iteration ', i)
            break

    if(visualize_path and not(visualize_walk)):
        l_centeroid = np.array(l_centeroid)
        plt.plot(l_centeroid[:,0], l_centeroid[:,1])
        plt.show()

    if(visualize_walk):
        l_centeroid = np.array(l_centeroid)

        fig, ax = plt.subplots()

        l1, = plt.plot(l_points[0][:,0], l_points[0][:,1], 'm', marker = "x")
        l2, = plt.plot([l_points[0][0,0], l_points[0][-1,0]], [l_points[0][0,1], l_points[0][-1,1]], 'm',  marker = "x")
        if(visualize_path): l3, = plt.plot(l_centeroid[:,0], l_centeroid[:,1], 'c')
        p1, = plt.plot(l_centeroid[0,0], l_centeroid[0,1], marker = "x")

        plt.xlim(pltr[0][0], pltr[0][1])
        plt.ylim(pltr[1][0], pltr[1][1])

        ax_slider = plt.axes([0.25, .03, 0.50, 0.02])

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

    return ts.x_sort[0,:], ts.y_sort[0], iteration_no

fhandle = himmelblau
x_start = [3, 2]
N_max   = 1e10
p       = 1e-15
simplex(fhandle, x_start, N_max, p, visualize_walk = True, visualize_path = True, print_statements = True)
