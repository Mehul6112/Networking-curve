import numpy as np
import matplotlib.pyplot as plt

# code for input graph below

sample_rate = 1e6

t = np.arange(1024*1000)/sample_rate 
f = 50e3
x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))

#code for output graph below

fft_size = 1024
num_rows = int(np.floor(len(x)/fft_size))
spectrogram = np.zeros((num_rows, fft_size))

for i in range(num_rows):
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
spectrogram = spectrogram[:,fft_size//2:] # get rid of negative freqs because we simulated a real signal

plt.imshow(spectrogram, aspect='auto', extent = [0, sample_rate/2/1e6, 0, len(x)/sample_rate])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()