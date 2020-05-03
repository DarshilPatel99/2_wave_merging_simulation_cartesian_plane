import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-2,0,50)
x2 = np.linspace(0,2,50)
y1 = np.sqrt(1-(x1+1)**2)+2
y2 = np.sqrt(1-(x2-1)**2)+2
y3 = -(4*np.arcsin(x1+1))/np.pi
y4 = (4*np.arcsin(x2-1))/np.pi
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x1,y3)
plt.plot(x2,y4)
plt.axis([-5, 5, -3, 4])
plt.legend()
plt.show()

