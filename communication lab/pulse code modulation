#PCM (triangle wave)
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import sawtooth
fm = 100
dc_offset = 2

d=2/fm

t=np.arange(0,d,0.0001)
xm= dc_offset+ 1*sawtooth(2*np.pi*fm*t, width=0.5)
fs=30*fm

ts=np.arange(0,d,1/fs)
xs= dc_offset+ 1*sawtooth(2*np.pi*fm*ts, width=0.5)

L=8
qlvl = np.linspace(min(xm), max(xm)+1e-6, L)
xq=np.digitize(xs,qlvl)-1
xq=np.clip(xq,0,L-1)
q=qlvl[xq]


qnoise=xs-q
sigp=((max(xm)-min(xm))**2)/2
noisep=np.mean(qnoise**2)
sqnr=10*np.log10(sigp/noisep)
bps=range(1,9)
sqnrv=[]
sqnrtv=[]

for b in bps:
    L=2**b
    qlvl = np.linspace(min(xm), max(xm)+1e-6, L)
    xq=np.digitize(xs,qlvl)-1
    xq=np.clip(xq,0,L-1)
    q=qlvl[xq]
    qnoise=xs-q
    sigp=((max(xm)-min(xm))**2)/2
    noisep=np.mean(qnoise**2)
    sqnr=10*np.log10(sigp/noisep)
    sqnrv.append(sqnr)
    sqnrt=6.02*b + 1.78
    sqnrtv.append(sqnrt)


plt.figure(figsize=(8, 6))
plt.plot(bps, sqnrv, 'go-',label="Calculated SQNR")
plt.plot(bps,sqnrtv,label="Theoretical SQNR")
plt.title("SQNR vs Bits per Symbol")
plt.xlabel("Bits per Symbol")
plt.ylabel("SQNR (dB)")
plt.legend()
plt.grid(True)
plt.show()
