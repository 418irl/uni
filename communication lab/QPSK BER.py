#QPSK Generation and BER plot

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import standard_normal
from scipy.special import erfc
N = 100000
L = 4
Fc = 10
Fs = L * Fc
ak = np.random.randint(0, 2, N)
odd = ak[0::2]
even = ak[1::2]
nrz1 = 2 * odd - 1
upsampleddata1 = np.repeat(nrz1, L)
nrz2 = 2 * even - 1
upsampleddata2 = np.repeat(nrz2, L)
t = np.arange(len(upsampleddata1)) /Fs
BPSK1 = upsampleddata1 * np.cos(2 * np.pi * Fc * t)
BPSK2 = upsampleddata2 * np.sin(2 * np.pi * Fc * t)
QPSK = BPSK1 - BPSK2
ebn0db = np.arange(-20, 11, 2)
BER = np.zeros(len(ebn0db))
theoretical_BER = np.zeros(len(ebn0db))
for i in range(len(ebn0db)):
 ebn0 = 10**(ebn0db[i] / 10)
 noise_amp = 1 / np.sqrt(ebn0)
 noise = noise_amp * standard_normal(len(QPSK))
 noisy_BPSK1 = BPSK1 + noise
 noisy_BPSK2 = BPSK2 + noise
 received_i = noisy_BPSK1 * np.cos(2 * np.pi * Fc * t)
 received_q = noisy_BPSK2 * np.sin(2 * np.pi * Fc * t)
 demodulated_i = np.convolve(received_i, np.ones(L))
 demodulated_q = np.convolve(received_q, np.ones(L))
 demodulated_i = demodulated_i[L - 1::L]
 demodulated_q = demodulated_q[L - 1::L]
 detected_i = demodulated_i > 0
 detected_q = demodulated_q > 0
 BER[i] = (np.sum(odd != detected_i) + np.sum(even != detected_q)) / N
 theoretical_BER[i] = 0.5 * erfc(np.sqrt(ebn0))
plt.title("Error Performance of QPSK")
plt.xlabel("SNR ($E_b/N_0$) in dB")
plt.ylabel("Bit Error Rate (BER)")
plt.semilogy(ebn0db, BER, 'o-', label="Simulated BER")
plt.semilogy(ebn0db, theoretical_BER, 'r--', label="Theoretical BER")
plt.ylim(10**-4, 1)
plt.legend()
plt.grid(True, which='both')
plt.show()
