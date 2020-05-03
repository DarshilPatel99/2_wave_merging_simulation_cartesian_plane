import numpy as np
import matplotlib.pyplot as plt

#here is no any animation

fig, ax = plt.subplots()

ax.set_xlim(( 0, 20))
ax.set_ylim((-2, 2))

x = np.linspace(0, 8*np.pi, 400)
y = np.sin(x)

ax.plot(x, y)

plt.show()