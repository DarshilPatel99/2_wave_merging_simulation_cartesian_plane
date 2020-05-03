import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


piby2 = np.pi/2
A = 1
a = 1
b = 0
count = 0
fig,ax = plt.subplots()

ax.set_xlim(0,10)
ax.set_ylim(-3,3)
axamp = plt.axes([0.25, .02, 0.50, 0.02])
axfreq = plt.axes([0.25, .05, 0.50, 0.02])
x_graph, = ax.plot([],[])

# Slider
samp = Slider(axamp, 'A', 0, 2, valinit=A)
sfreq = Slider(axfreq, 'a', 0.01, 10, valinit=a)

def fun(i):
    global A
    global a
    global b
    global count
    temp = np.linspace(count, 10+count, 1000)
    y = A*np.sin(a*temp+b)
    x = temp - count
    x_graph.set_data(x, y)
    count += 0.1

animation = FuncAnimation(fig,func=fun,frames = 100,interval=5)

def update(val):
    global animation
    global A
    global a
    A = samp.val
    a = sfreq.val
    fig.canvas.draw_idle()

samp.on_changed(update)
sfreq.on_changed(update)
plt.show()
