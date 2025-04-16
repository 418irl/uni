# BPSK Generation and BER plot

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import standard_normal
from scipy.special import erfc

N = 100000
L = 8
Fc = 10
Fs = L * Fc
ak = np.random.randint(0, 2, N)
data = np.repeat(ak, L)
nrz = 2 * ak - 1
upsampleddata = np.repeat(nrz, L)
t = np.arange(0, len(ak) * L)
bpsk = upsampleddata * np.cos(2 * np.pi * Fc * t / Fs)
ebn0db = np.arange(-20, 11, 2)
BER = np.zeros(len(ebn0db))
theoretical_BER = np.zeros(len(ebn0db))
for i in range(len(ebn0db)):
 ebn0 = 10 ** (ebn0db[i] / 10)
 noiseamp = 1 / np.sqrt(ebn0 / 2)
 channel = bpsk + noiseamp * standard_normal(len(bpsk))
 received = channel * np.cos(2 * np.pi * Fc * t / Fs)
 demodulated = np.convolve(received, np.ones(L))
 demodulated = demodulated[L - 1:-1:L]
 detected = (demodulated > 0)
 BER[i] = np.sum(ak != detected) / N
 theoretical_BER[i] = 0.5 * erfc(np.sqrt(ebn0))

plt.title("Error performance of BPSK")
plt.xlabel("SNR ($E_b/N_0$) in dB")
plt.ylabel("Bit Error Rate (BER)")
plt.semilogy(ebn0db, BER, 'o-', label="Simulated BER")
plt.semilogy(ebn0db, theoretical_BER, 'r--', label="Theoretical BER")
plt.ylim(10 ** -4)
plt.legend()
plt.grid(True, which='both')
plt.show()
