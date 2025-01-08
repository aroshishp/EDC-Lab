# import numpy as np
# import matplotlib.pyplot as plt

# Fs = 60000 
# T = 0.008
# f = 1000  

# t = np.linspace(0, T, int(Fs * T), endpoint=True)

# x = np.sin(2 * np.pi * f * t)
# X = np.fft.fft(x)
# frequencies = np.fft.fftfreq(len(X), 1/Fs)[:len(t)//2]

# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(t, x)
# plt.grid()
# plt.title("Input Wave y(t) = sin(2000πt)")
# plt.xlabel("Time (t)")
# plt.ylabel("y(t)")


# plt.subplot(2, 1, 2)
# plt.plot(frequencies[:len(frequencies)//2], np.abs(X)[:len(X)//2])
# plt.grid()
# plt.title('Fourier Transform of y(t)')
# plt.xlabel('Frequency (f)')
# plt.ylabel('$|Y(f)|$')

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000000  # Sampling rate
T = 0.002  # Duration
f = 3000  # Frequency of the sine wave

# Generate the time vector
t = np.linspace(0, T, int(Fs * T), endpoint=True)

# Generate the sine wave as per your original code
# x = np.where(0.25*np.sin(2 * np.pi * f * t) < 0, 0, 0.25*np.sin(2 * np.pi * f * t))
x = np.abs(0.25*np.sin(2 * np.pi * f * t))

# Compute the FFT of the original sine wave
X = np.fft.fft(x)

# Normalize the FFT output
X_normalized = X / len(t)

# Compute the frequency vector
frequencies = np.fft.fftfreq(len(X), 1/Fs)

# Keep only the positive frequencies
frequencies = frequencies[:len(t)//2]
X_normalized = X_normalized[:len(t)//2]

# Multiply by 2 to account for the symmetric nature of the FFT (except for DC component)
X_normalized[1:] = 2 * X_normalized[1:]

# Plot the time-domain signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.grid()
plt.title("Input Wave y(t) = 0.25sin(6000πt)")
plt.xlabel("Time (t)")
plt.ylabel("f(t)")

# Plot the magnitude of the FFT, which corresponds to the Fourier series coefficients
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(X_normalized))
plt.grid()
plt.title('Fourier Transform Plot')
plt.xlabel('Frequency (f)')
plt.xlim(0, 50000)
plt.ylabel('Magnitude (in V)')

plt.tight_layout()
plt.show()
