import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
position = 15
ax.set_xlim((0, 20))
ax.set_ylim((-3, 3))
t = np.linspace(0,16*np.pi,800)

line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], marker = 'o')
line.set_data([], [])
point.set_data([], [])


def animate(i):
    temp = t[i:i + 400]
    x = t[0:400]
    y = np.sin(temp)
    line.set_data(x, y)
    point.set_data(x[position],y[position])

anim = animation.FuncAnimation(fig, animate,frames=400, interval=5)

plt.show()