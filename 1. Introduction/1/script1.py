import matplotlib.pyplot as plt
import numpy as np 


# Systems
def system1(t, f0):  # First continues signal
    return np.cos( (np.pi * f0 * t) / 2 ) ** 2

def system2(n, f0):  # Second distributed signal
    return np.cos( 2 * np.pi * f0 * n )


# Initialize 
start = 0
end = 10 
step = 0.01

variable = [0, 0.125, 0.25, 0.375, 0.5 ,5]

# Signals
x1 = np.linspace(start, end, int(end - start / step))

x2 = []
for i in range(start, end+1):
    x2.append(i)


f, plt_array = plt.subplots(len(variable) * 2) 

f.suptitle('Signals')

i = 0
for f0 in variable:
    y = [system1(t, f0) for t in x1]
    plt_array[i].plot(x1,y)
    plt_array[i].set_title(f'System 1 : f0 = {f0}')
    i += 1

for f0 in variable:
    y = [system2(n, f0) for n in x2]
    plt_array[i].stem(x2, y)
    plt_array[i].set_title(f'System 2 : f0 = {f0}')
    i += 1

plt.show()
