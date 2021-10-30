import matplotlib.pyplot as plt
import numpy as np 

UNIT_IMPULSE = np.zeros( (13,))
UNIT_IMPULSE[6] = 1.0

# System
def system(n): 
    return np.heaviside([n - 3], 1)[0] - np.heaviside([-1 * n + 3], 1)[0] + 2 * UNIT_IMPULSE[n]


# Initialize 
start = -6
end = 6


# Signal
x1 = [n for n in range(start, end+1)]

y1 = [system(n) for n in x1]

plt.stem(x1, y1)

plt.show()
