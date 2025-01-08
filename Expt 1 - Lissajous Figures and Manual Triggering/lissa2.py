import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.25, 10000)
# ctr = 

x = np.sin(2*np.pi*t)
y = np.sin(2*np.pi*t + phi)

phi = np.linspace(0, 2*np.pi, 100000)

x = np.sin(2*np.pi*t)
y = np.sin(2*np.pi*t + phi)


# for phi in np.arange(0, 4*np.pi, np.pi/16):
#     x = np.sin(1500*t)
#     y = np.sin(2500*t + phi)

#     plt.subplot(8, 8, ctr)
#     plt.plot(x, y)
#     ctr += 1

plt.show()