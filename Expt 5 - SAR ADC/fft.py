import numpy as np
import matplotlib.pyplot as plt

sequence = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 
                     8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 13, 
                     13, 14, 14, 16, 16, 17, 17, 17, 17, 18, 18, 19, 19, 20, 20, 
                     21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 
                     25, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 30, 30, 
                     0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 
                    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 
                    13, 13, 14, 14, 15, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 
                    20, 20, 20, 20, 21, 21, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 
                    24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 0, 0, 
                    0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 
                    7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 12, 12, 13, 
                    13, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 19, 19, 
                    20, 20, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 
                    24, 25, 25, 26, 26, 27, 27, 27, 27, 28, 28, 29, 29, 29, 29, 
                    0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 
                    7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 11, 12, 
                    12, 13, 13, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 19, 19, 
                    19, 19, 20, 20, 21, 21, 21, 21, 22, 22, 23, 23, 23, 23, 24, 
                    24, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 29, 29])

# Concatenate the original and new sequence
# combined_sequence = np.concatenate((sequence, new_sequence))

next_seq = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 
                     8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 13, 
                     13, 14, 14, 16, 16, 17, 17, 17, 17, 18, 18, 19, 19, 20, 20, 
                     21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 
                     25, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 30, 30, 
                     0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 
                    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 
                    13, 13, 14, 14, 15, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 
                    20, 20, 20, 20, 21, 21, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 
                    24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 0, 0, 
                    0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 
                    7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 12, 12, 13, 
                    13, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 19, 19, 
                    20, 20, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 
                    24, 25, 25, 26, 26, 27, 27, 27, 27, 28, 28, 29, 29, 29, 29, 
                    0, 0, 0, 0, 1, 1])

# print(len(next_seq))
# exit()

# Perform FFT on the combined sequence
# combined_fft_values = np.fft.fft(sequence)
# combined_fft_magnitude = np.abs(combined_fft_values)
# combined_fft_frequency = np.fft.fftfreq(len(sequence))
combined_fft_values = np.fft.fft(next_seq)
combined_fft_magnitude = np.abs(combined_fft_values)
combined_fft_frequency = np.fft.fftfreq(len(next_seq))

# print(len(combined_sequence))
# Find frequencies where the magnitude is greater than 100
high_magnitude_frequencies = combined_fft_frequency[combined_fft_magnitude > 100]
high_magnitude_values = combined_fft_magnitude[combined_fft_magnitude > 100]

# Display the frequencies and their corresponding magnitudes
for freq, mag in zip(high_magnitude_frequencies, high_magnitude_values):
    print(f"Frequency (mHz): {freq*1000},  Magnitude: {mag}")

# print(len(combined_sequence))
# plt.figure(figsize=(14, 6))

# plt.subplot(1, 2, 1)
plt.plot(np.arange(0, 96, 96/256), next_seq, color="blue")
plt.axhline(y=16, color='r', linestyle='--', label='y = 16')
plt.xlabel("Time (s)")
plt.ylabel("Output in Decimal")
plt.title("ADC Output (Sawtooth Input)")
plt.legend()
plt.grid()
plt.show()

# Display the concatenated sequence's FFT
# plt.subplot(1, 2, 2)
# plt.figure(figsize=(12, 6))
# plt.stem(combined_fft_frequency, combined_fft_magnitude, basefmt=" ", markerfmt="ro")
# plt.xlim(-0.005, 0.5)
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.title("FFT of the Combined Sequence")
# plt.show()
