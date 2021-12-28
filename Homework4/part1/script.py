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