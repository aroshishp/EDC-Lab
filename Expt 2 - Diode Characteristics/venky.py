import numpy as np
import matplotlib.pyplot as plt

# f = 3000
# t = np.arange(0, 0.001, 0.000001)

# Vin = 0.25*np.sin(2*np.pi*f*t)

# x = np.where((Vin > 0), Vin, -Vin)

# plt.subplot(2, 1, 1)
# plt.plot(t, Vin)
# plt.subplot(2, 1, 2)
# plt.plot(t, x)
# plt.show()

# fft_x = np.fft.fft(x)
# x_fft = (2/len(t)) * np.abs(fft_x[:len(t) // 2])

# print(len(x))
# freq = np.fft.fftfreq(len(x), t[1]-t[0])[:len(t)//2]
# print(len(freq))
# plt.plot(freq, x_fft)
# plt.xlabel('Frequency (f)')
# plt.ylabel('Magnitude (in V)')
# plt.xlim(0, 40000)
# plt.grid()
# plt.show()

n = 2
a0 = 4/np.pi
bn = 0

f_t = 0.25 * a0/2 
omega = 2*np.pi*3000
t = np.arange(0, 0.001, 0.0000001)
iters = np.array([1,2,3,4,1000])


for i in iters:
    f_t += 0.25 * (4/(np.pi*(1-(2*i)**2)) * np.cos(2*i*omega*t))
    plt.plot(t, f_t, label = f"N = {i}")

plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Fourier Series of Rectified Output (N = upper limit of sum)')
plt.legend()
plt.grid()
plt.show()