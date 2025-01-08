import numpy as np
import matplotlib.pyplot as plt

w1 = np.array([500, 500, 500, 500, 500, 2000, 2000, 2000, 2000, 500, 500, 1500])
w2 = np.array([500, 500, 500, 1000, 1000, 1500, 1500, 2500, 2500, 500, 500, 2500])
A1 = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20])
A2 = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 10])
phi = np.array([0, 0.25, 0.5, 0, 0.5, 0, 0.125, 0, 0.125, 0.5, 0, 0])

t = np.linspace(0, 1, 10000)

for i in np.arange(12):
    x = A1[i] *np.sin(w1[i]*t) 
    y = A2[i] *np.sin(w2[i]*t + phi[i] * np.pi)

    plt.figure(figsize=(8, 8*A2[i]/A1[i]))
    plt.plot(x, y)
    plt.grid()
    plt.xlabel(f'{A1[i]}sin({w1[i]}t)')
    phi_label = f' + {phi[i]}\u03C0' if phi[i] != 0 else ''
    plt.ylabel(f'{A2[i]}sin({w2[i]}t{phi_label})')
    plt.savefig(f'image{i+1}.png')
    plt.clf()


