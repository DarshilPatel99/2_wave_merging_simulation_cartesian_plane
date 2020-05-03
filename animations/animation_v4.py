import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

piby2 = np.pi/2
A = 1
B = 1
a = 1
b = 0
c = 1
d = piby2

fig, ax = plt.subplots()
position = 15
ax.set_xlim((0, 20))
ax.set_ylim((-3, 8))
t = np.linspace(0,16*np.pi,800)
linex, = ax.plot([], [])
liney, = ax.plot([], [])
line_final, = ax.plot([], [])
point, = ax.plot([], [],'--',marker = 'o')

linex.set_data([], [])
liney.set_data([], [])
line_final.set_data([], [])
point.set_data([], [])


def animate(i):
    global A
    global B
    global a
    global b
    global c
    global d

    temp = t[i:i+400]
    x = t[0:400]
    X_graph = 6 + A*np.sin(a*(temp+b))
    Y_graph = 3 + B*np.sin(c*(temp+d))
    final_graph = X_graph + Y_graph-9
    linex.set_data(x, X_graph)
    liney.set_data(x, Y_graph)
    line_final.set_data(x,final_graph)
    point.set_data([x[position],x[position],x[position]],[X_graph[position],Y_graph[position],final_graph[position]])

anim = animation.FuncAnimation(fig, animate,frames=400, interval=3)

plt.show()