from simplex import *
from himmelblau import himmelblau
from matplotlib import pyplot as plt

fhandle = himmelblau
N_max   = 1e10
p       = 1e-15

'''Erstes Minimum:'''
x_start = [0,0]
data = simplex(fhandle, x_start, N_max, p)
print("Erstes Minimum bei: ", data[0], ", mit Funktionswert: ", data[1], ", nach " , data[2], " iterationen")
print()

'''Zweites Minimum:'''
x_start = [-5,5]
data = simplex(fhandle, x_start, N_max, p)
print("Zweites Minimum bei: ", data[0], ", mit Funktionswert: ", data[1], ", nach " , data[2], " iterationen")
print()

'''Drittes Minimum:'''
x_start = [-5,-5]
data = simplex(fhandle, x_start, N_max, p)
print("Drittes Minimum bei: ", data[0], ", mit Funktionswert: ", data[1], ", nach " , data[2], " iterationen")
print()

'''Viertes Minimum:'''
x_start = [5,-5]
data = simplex(fhandle, x_start, N_max, p)
print("Viertes Minimum bei: ", data[0], ", mit Funktionswert: ", data[1], ", nach " , data[2], " iterationen")
print()

'''Evaluation von f(xmin) in Abhängigkeit von N_max:'''
li_f = []
x_start = [-1,-1]
for i in range(200):
    data = simplex(fhandle, x_start, i, 0)
    li_f.append(data[1])
'''das wäre sicher auch effizienter möglich gewesen, z.B. durch abspeicherung der Funktionswerte
in ein Array im simplex Program. Ist aber bei dieser doch recht einfachen Funktion kein Problem für
meinen und ich hoffe auch ihren PC.'''
plt.plot(li_f)
plt.yscale('log')
plt.xlabel('N(Anzahl der maximalen Iterationen)')
plt.ylabel('f(x_min)')
plt.show()

'''Plotten des Flächeninhalts'''
data = simplex(fhandle, x_start, 200, 0, return_area = True)
plt.plot(data[3])
plt.xlabel('N(Anzahl der maximalen Iterationen)')
plt.ylabel('Flächeninhalt')
plt.show()


'''Interessante Visualisierung:'''
x_start = [3, 2]
simplex(fhandle, x_start, N_max, p, visualize_walk = True, visualize_path = True, print_statements = False)
#setzt man print_statements = True, so kann man sehen dass sich mirror und contract immer abwechseln,
#ich habe es zunächst ausgelassen da die Konsole sonst ziemlich zugemüllt wird
