from scipy.io import wavfile 
import matplotlib.pyplot as plt 
import numpy as np


## Read the wave file
samplerate, data = wavfile.read('./phase1sample.wav')

## Calculate length
length = data.shape[0] / samplerate

# Create time 
t = np.linspace(0., length, data.shape[0])

## Show the signal in plot
fig, axs = plt.subplots()
axs.plot(t[1:250], data[1:250])

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Wave Data")

plt.show()