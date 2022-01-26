from scipy.io import wavfile 
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt 
import numpy as np


## Read the wave file
samplerate, data = wavfile.read('./phase1sample.wav')
initdata = data

## FFT
data = fft(data)

## Calculate length
length = data.shape[0] / samplerate

## Create time 
t = np.linspace(0., length, data.shape[0])

## Filter
LIMIT = 0.25 * (10 ** 9)
for i in range(len(data)):
    if data[i] < LIMIT:
        data[i] = 0
        
## IFFT
data = ifft(data)

## Show the signal in plot
fig, axs = plt.subplots(2)
axs[0].plot(t[1:250], initdata[1:250])
axs[1].plot(t[1:250], data[1:250])

plt.legend("De-noised signal")
plt.xlabel("Time [s]")
plt.ylabel("Value")

plt.show()