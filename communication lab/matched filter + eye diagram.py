#Matched Filter
import numpy as np
import matplotlib.pyplot as plt


N=100
L=8
num_taps=101
num_trace=100
beta=0.7
span=2*L

t=np.arange(num_taps)-(num_taps-1)//2
bits=np.random.randint(0,2,N)
x=np.repeat(2*bits-1,L)

h=np.sinc(t/L)*np.cos(np.pi*beta*t/L)/(1-(2*beta*t/L)**2)
h=h/np.sum(h)

x_shaped=np.convolve(x, h)

noise=0.1*np.random.normal(0,2,len(x_shaped))
x_noisy=x_shaped + noise

x_filtered=np.convolve(x_noisy,h)
decision_points=np.arange(N)*L+num_taps//2
samples=x_noisy[decision_points.astype(int)]
op=(samples>0).astype(int)

#Eye Diagram
plt.figure(figsize=(8,6))
for i in range(num_trace):
    start=i*L
    end=start+span
    if end<len(x_shaped):
        plt.plot(np.linspace(0 , span, span) ,x_shaped[start:end], 'b', alpha=0.3)
