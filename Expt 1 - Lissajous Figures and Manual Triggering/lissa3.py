import numpy as np
import matplotlib.pyplot as plt

w = 500
t = np.linspace(0, 10, 1000000)

# x = 10*np.sin(4*w*t)
# y = 10*np.sin(5*w*t)

# plt.figure(figsize=(5, 5))
# plt.plot(x, y)
# plt.show()
ctr = 1

for w1 in np.arange(1, 6, 1):
    for w2 in np.arange(w1, 6, 1):
        for phi in np.arange(0, np.pi/1.9, np.pi/8):
            if w1 == 1:
                x = np.sin(w1*w*t)
                y = np.sin(w2*w*t + phi)
                
                plt.subplot(10, 5, ctr)
                plt.plot(x, y)
                ctr += 1
            elif w2 % w1 != 0:
                x = np.sin(w1*w*t)
                y = np.sin(w2*w*t + phi)
                
                plt.subplot(10, 5, ctr)
                plt.plot(x, y)

                ctr += 1

plt.show()