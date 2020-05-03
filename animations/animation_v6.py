import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider

piby2 = np.pi/2
A = 1
B = 1
a = 1
b = 0
c = 1
d = piby2
count = 0
position = 15

fig, ax = plt.subplots(figsize=(18, 12))
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim((0, 24))
ax.set_ylim((-3, 21))
t = np.linspace(0,16*np.pi,800)
linex, = ax.plot([], [], label = 'X=Asin(ax+b)')
liney, = ax.plot([], [], label = 'Y=Bsin(cx+d)')
line_final, = ax.plot([], [], label = 'X+Y')
point, = ax.plot([], [],'--',marker = 'o')

xamp = plt.axes([0.20, 0.2, 0.25, 0.02])
yamp = plt.axes([0.55, 0.2, 0.25, 0.02])
xfreq = plt.axes([0.20, 0.15, 0.25, 0.02])
yfreq = plt.axes([0.55, 0.15, 0.25, 0.02])
xphase = plt.axes([0.20, 0.1, 0.25, 0.02])
yphase = plt.axes([0.55, 0.1, 0.25, 0.02])
point_position = plt.axes([0.20, 0.05, 0.25, 0.02])

linex.set_data([], [])
liney.set_data([], [])
line_final.set_data([], [])
point.set_data([], [])

sxamp = Slider(xamp, 'A', 0, 2, valinit=A)
syamp = Slider(yamp, 'B', 0, 2, valinit=B)
sxfreq = Slider(xfreq, 'a', 0, 4, valinit=a)
syfreq = Slider(yfreq, 'c', 0, 4, valinit=c)
sxphase = Slider(xphase, 'b', 0, 7, valinit=b)
syphase = Slider(yphase, 'd', 0, 7, valinit=d)
spoint_position = Slider(point_position, 'point', 0, 300, valinit=position)

def animate(i):
    global A
    global B
    global a
    global b
    global c
    global d
    global position
    global count
    temp = np.linspace(count, 24+count, 500)
    x = temp - count
    X_graph = 13 + A*np.sin(a*temp+b)
    Y_graph = 7 + B*np.sin(c*temp+d)
    final_graph = X_graph + Y_graph-19
    linex.set_data(x, X_graph)
    liney.set_data(x, Y_graph)
    line_final.set_data(x,final_graph)
    point.set_data([x[position],x[position],x[position]],[X_graph[position],Y_graph[position],final_graph[position]])
    count += 0.1

anim = animation.FuncAnimation(fig, animate,frames=400, interval=3)

def update(val):
    global anim
    global A
    global B
    global a
    global b
    global c
    global d
    global position
    A = sxamp.val
    B = syamp.val
    a = sxfreq.val
    c = syfreq.val
    b = sxphase.val
    d = syphase.val
    position = int(spoint_position.val)
    fig.canvas.draw_idle()

sxamp.on_changed(update)
syamp.on_changed(update)
sxfreq.on_changed(update)
syfreq.on_changed(update)
sxphase.on_changed(update)
syphase.on_changed(update)
spoint_position.on_changed(update)

ax.legend(fontsize=12)
plt.show()