import matplotlib.pyplot as plt
import numpy as np


def unit_impulse(size, part=0):
    x = np.zeros(size)
    x[ (int)(size / 2) + part ] = 1
    return x 


def convolution(a, b):  # Convolving two signals
    a = np.concatenate([ np.zeros( (int)(len(b) / 2) - 1 ), a,  np.zeros( (int)(len(b) / 2) )])
    b = b[::-1]

    step = len(b)
    c = np.zeros(len(a) - step + 1)

    for i in range(len(c)):
        c[i] = np.sum(a[i:i+step] * b)
    
    return c

# Initialize 

# CT
start = -15
end = 15 
t_step = 0.1

# DT
d_step = 1

# Signals
t = np.arange(start, end, t_step)

# DT signals
x = ( (1/4) ** (2*t)) *  np.heaviside(t + 3, 1)
h1 = np.abs(t) * (np.heaviside(t - 2, 1) - np.heaviside(t, 1))
h2 = np.heaviside(t + 5, 1)

x3 = convolution(x, h1)
x4 = convolution(x, h2)

f, plot_array = plt.subplots(5)

plot_array[0].plot(t, x, label="x(t)")
plot_array[1].plot(t, h1, label="h(t)")
plot_array[2].plot(t, x3, label="x(t) * h(t)")
plot_array[3].plot(t, h2)
plot_array[4].plot(t, x4)

plt.show()
