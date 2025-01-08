import numpy as np
import matplotlib.pyplot as plt

w = 2 * np.pi * 1000

# def y(t):
#     k = 20
#     sum = 0
#     for n in np.arange(2, k, 2):
#         sum += np.cos(n * w * t) / (n**2 - 1)
#     sum *= 2

#     return sum/np.pi - 1/np.pi

def y(k, t):
    sum = 0
    for n in np.arange(2, k, 2):
        sum += np.cos(n * w * t) / (n**2 - 1)
    sum *= 2/np.pi

    return 1/np.pi - np.sin(w*t)/2 - sum

t = np.linspace(0, 0.002, 100000)

for k in np.arange(1, 9, 2):
    Y = y(k, t)
    plt.plot(t, Y, label = f"N = {k}")

Y = y(100, t)
plt.plot(t, Y, label='N = 100')

plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Fourier Series of Rectified Output (N = upper limit of sum)')
plt.legend()
# plt.show()

plt.clf()


def y1(k, t):
    sum = 0
    for n in np.arange(1, k):
        sum += np.cos(2*n*w*t)/(4*n**2 - 1)
    
    return 0.25*(1/np.pi + np.sin(w*t)/2 - 2*sum/np.pi)

for k in np.arange(1, 4):
    Y = y1(k, t)
    plt.plot(t, Y, label = f"N = {k}")

Y = y1(100, t)
plt.plot(t, Y, label='N = 100')

plt.grid()
plt.ylabel('Magnitude (in V)')
plt.xlabel('t')
plt.title('Fourier Series of Rectified Output (N = upper limit of sum)')
plt.legend()
plt.show()
# def y1(t):
#     return np.sin(2 * np.pi * 1000 * t)

# t = np.linspace(0, 0.008, 400)
# Y1 = y1(t)

# Y1_fft = np.fft.fft(Y1)
# freq = np.fft.fftfreq(len(Y1), 1/400)

# # plt.plot(t, y1(t))
# plt.plot(freq, np.abs(Y1_fft))
# plt.show()