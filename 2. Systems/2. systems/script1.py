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
h2 = 3 * unit_impulse(len(t), 5) - unit_impulse(len(t))

x3 = convolution(x, h1)
x4 = convolution(x, h2)

f, plot_array = plt.subplots(3,2, constrained_layout=True)

f.delaxes(plot_array[0][1])

plot_array[0][0].stem(t, x)
plot_array[0][0].title.set_text('x[t]   = e^2t (-u(t - 2) + u(t + 3))')

plot_array[1][0].stem(t, h1)
plot_array[1][0].title.set_text('h1[t]  = u(n + 10) - u(n)')

plot_array[1][1].stem(t, x3)
plot_array[1][1].title.set_text('y1[t]  = x[t] * h1[t]')

plot_array[2][0].stem(t, h2)
plot_array[2][0].title.set_text('h2[t]  = 3d[t - 5] - d[t]')

plot_array[2][1].stem(t, x4)
plot_array[2][1].title.set_text('y2[t]  = x[t] * h1[t]')

plt.show()
