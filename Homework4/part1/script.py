import matplotlib.pyplot as plt
import numpy as np

T0 = 0.4
FC = 250
TS = 0.0001

# Signal 
def m(t):
    if t >= 0 and t <= T0:
        return np.sinc(100 * t)
    else:
        return 0

# Carrier
def c(t):
    return np.cos(2 * np.pi * FC * t)

# DSB-AM signal
def am(t):
    return ( 1 + m(t) ) * c(t)

def lowpassfilter(t):
    temp = []
    for x in t:
        if x >= -100 and t < 100:
            temp.append(x)
        else:
            temp.append(0)
    return temp

# Demodulation
def demodule(t):
    temp = [c(x) for x in t]
    temp = np.fft.fft(temp)
    temp = lowpassfilter(temp)
    temp = np.fft.ifft(temp)
    return temp


# Time 
time = np.arange(0, T0, TS)

# System m
y1 = [m(x) for x in time]
# FT
y1 = np.fft.fft(y1)
# System am
y2 = [am(x) for x in time]
# FT
y2 = np.fft.fft(y2)

fig, s1 = plt.subplots(3)
s1[0].plot(time, y1)
s1[1].plot(time, y2)
s1[2].plot(time, demodule(y2))

plt.show()