import matplotlib.pyplot as plt
import numpy as np 


def convolution(a, b):  # Convolving two signals
    a = np.concatenate([ np.zeros( len(b) / 2 - 1 ), a,  np.zeros( len(b) / 2 )])
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
x1 = [1, 2, 3, 2, 1, 2, 3]
x1 = np.concatenate([np.zeros(len(t) / 2 - len(x1) / 2 - 1), x1, np.zeros(len(t) / 2 - len (x1) / 2)])

x2 = [2, 4, -2]
x2 = np.concatenate([np.zeros(len(t) / 2 - len(x2) / 2 - 1), x2, np.zeros(len(t) / 2 - len (x2) / 2)])

x3 = convolution(x1, x2)

f, plot_array = plt.subplots(3)

plot_array[0].stem(t, x1)
plot_array[1].stem(t, x2)
plot_array[2].stem(t, x3)

plt.show()
