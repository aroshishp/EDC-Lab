# import numpy as np
# import matplotlib.pyplot as plt

# def x(t):
#     return np.sin(500 * t)

# fs = 10000
# T = 1.0
# f = 10

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 60000  # Sampling rate (samples per second)
T = 0.008  # Duration in seconds
f = 1000  # Frequency of the sine wave in Hz

# Generate the time vector
t = np.linspace(0, T, int(Fs * T), endpoint=True)

# Generate the sine wave
x = np.where(np.sin(2 * np.pi * f * t) < 0, -np.sin(2 * np.pi * f * t), 0)
# x = np.sin(2 * np.pi * f * t)

# Compute the FFT
X = np.fft.fft(x)

# Compute the frequency vector
frequencies = np.fft.fftfreq(len(X), 1/Fs)

# plt.plot(t, x)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.grid()
plt.title("Input Wave y(t) = sin(2000πt)")
plt.xlabel("Time (t)")
plt.ylabel("y(t)")


plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], np.abs(X)[:len(X)//2])
# plt.xlim(0, 30000)
plt.grid()
plt.title('Fourier Transform of y(t)')
plt.xlabel('Frequency (f)')
plt.ylabel('$|Y(f)|$')

plt.tight_layout()
plt.show()