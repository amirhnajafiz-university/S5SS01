from this import d
from scipy.io import wavfile 
from scipy.fft import fft
import matplotlib.pyplot as plt 
import numpy as np


## Read the wave file
samplerate, data = wavfile.read('./phase1sample.wav')

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

## Show the signal in plot
fig, axs = plt.subplots()
axs.plot(t, data)

plt.legend("Fourier transform")
plt.xlabel("Frequency")
plt.ylabel("Value")

plt.show()