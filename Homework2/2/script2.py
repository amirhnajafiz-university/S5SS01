import matplotlib.pyplot as plt
import numpy as np

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
start = -10
end = 10 
t_step = 0.1

# DT
d_step = 1

# Signals
t = np.arange(start, end, d_step)

# DT signals
x = np.exp(2 * t) * ( np.heaviside(t + 3, 1) - np.heaviside(t - 2, 1) )
h1 = np.heaviside(t + 10, 1) - np.heaviside(t, 1)

x3 = convolution(x, h1)

f, plot_array = plt.subplots(3)

plot_array[0].stem(t, x, label="x(t)")
plot_array[1].stem(t, h1, label="h(t)")
plot_array[2].stem(t, x3, label="x(t) * h(t)")

plt.show()
