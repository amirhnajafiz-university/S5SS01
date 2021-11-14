import matplotlib.pyplot as plt
import numpy as np 


def convolution(a, b, mode='full'):
    return np.convolve(a, b, mode=mode)

# Systems
def system1(t, f0):  # First continues signal
    return np.cos( (np.pi * f0 * t) / 2 ) ** 2

def system2(n, f0):  # Second distributed signal
    return np.cos( 2 * np.pi * f0 * n )


# Initialize 
start = -10
end = 10 
step = 0.001

# Signals
t = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
x1 = [1, 2, 3, 4, 3, 2, 1, 0, -1]
x2 = [1, 3, 5, 0, 2]

f, plt_array = plt.subplots(3) 

f.suptitle('Signals convolution')

plt_array[0].stem(t[2:-2], x1) 
plt_array[1].stem(t[4:-4], x2)

x3 = convolution(x1, x2)

plt_array[2].stem(t, x3)

plt.show()
