import matplotlib.pyplot as plt
import numpy as np 

def convolution(a, b, mode='same'):
    return np.convolve(a, b, mode=mode)

# Initialize 
start = -10
end = 10 
step = 0.001

# Signals
t = [x for x in range(start, end)]

x1 = np.zeros(len(t))
x1[len(x1) / 2 - 2: len(x1) / 2 + 3] = [1, 2, 3, 2, 1]

x2 = np.zeros(len(t))
x2[len(x2) / 2 - 1: len(x2) / 2 + 2] = [2, 4, -2]

x3 = convolution(x1, x2)

f, plot_array = plt.subplots(3)

plot_array[0].stem(t, x1)
plot_array[1].stem(t, x2)
plot_array[2].stem(t, x3)

plt.show()
