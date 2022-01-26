import matplotlib.pyplot as plt
import numpy as np 


# System
def system(t): 
    x = 0.0
    for n in range(-20, 21):
        x += np.e ** (-1 * ( np.abs( 2 * t + n ) ))
    return x


# Initialize 
start = -6
end = 6
step = 0.01


# Signal
x1 = np.linspace(start, end, int(end - start / step))

y1 = [system(t) for t in x1]

plt.plot(x1, y1)

plt.show()
