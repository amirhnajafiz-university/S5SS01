from scipy.io import wavfile 
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt 
import numpy as np


rate1 = [2,2,2,2,2,0.1,0.1,0.1,0.1,0.1]  # less than 1200
rate2 = [0.1,0.1,0.1,0.1,0.1,0.1,2,2,2,2]  # more than 2000


## Amplify function
def amplify(sig, freqbands):
    for i in range(len(sig)):
        data = sig[i]
        index = -1
        if data > 20 and data < 50:          # Band 1
            index = 0
        elif data >= 50 and data < 100:      # Band 2
            index = 1
        elif data >= 100 and data < 200:     # Band 3
            index = 2
        elif data >= 200 and data < 500:     # Band 4
            index = 3
        elif data >= 500 and data < 1000:    # Band 5
            index = 4
        elif data >= 1000 and data < 2000:   # Band 6
            index = 5
        elif data >= 2000 and data < 4000:   # Band 7
            index = 6
        elif data >= 4000 and data < 8000:   # Band 8
            index = 7
        elif data >= 8000 and data < 12000:  # Band 9
            index = 8
        elif data >= 12000 and data < 20000: # Band 10
            index = 9
        
        if index != -1:
            sig[i] = data * freqbands[index]
    return sig


## Read the wave file
samplerate, data = wavfile.read('./phase2sample.wav')

## FFT
data = fft(data)

## Filter
LIMIT = 500
for i in range(len(data)):
    if data[i] < LIMIT:
        data[i] = 0

data = amplify(data, rate2)

## IFFT
data = ifft(data)

## Calculate length
length = data.shape[0] / samplerate

## Create time 
t = np.linspace(0., length, data.shape[0])

## Store into the file
# wavfile.write("output1.wav", samplerate, data.astype(np.int16))

## Show the signal in plot
fig, axs = plt.subplots()
axs.plot(t[1:250], data[1:250])

plt.legend("Signal")
plt.xlabel("Frequence")
plt.ylabel("Value")

plt.show()