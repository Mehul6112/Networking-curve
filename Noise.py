import numpy as np
import matplotlib.pyplot as plt

N = 1024 # number of samples to simulate, choose any number you want
x = np.random.randn(N)
plt.plot(x, '.-')
plt.show()

X1 = np.fft.fftshift(np.fft.fft(x))
X2 = X[N//2:] # only look at positive frequencies.  remember // is just an integer divide
plt.plot(np.real(x1), (x2), '.-')
plt.show()

#Complex Noising

n0 = np.random.randn() + 1j * np.random.randn()
power = np.var(x)
n1 = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # AWGN with unity power
n2 = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2)

plt.plot(np.real(n1),'.-')
plt.plot(np.imag(n2),'.-')
plt.legend(['real','imag'])
plt.show()
