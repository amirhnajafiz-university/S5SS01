import matplotlib.pyplot as plt
import numpy as np

T0 = 0.1
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


# Time 
time = np.arange(0, T0, TS)

# System m
y1 = [m(x) for x in time]
# System am
y2 = [am(x) for x in time]

fig, s1 = plt.subplots(2)
s1[0].plot(time, y1)
s1[1].plot(time, y2)

plt.show()