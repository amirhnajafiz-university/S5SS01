import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz


T0 = 0.1
FC = 250

FS = 1000
TS = 0.0001
M = 1024 * 1024

ORDER = 6
CUT_OFF = 100

# Signal 
def input_signal(t):
    if t >= 0 and t <= T0:
        return np.sinc(100 * t)
    else:
        return 0

# Fourier transform with frequence bandwidth
def f_transform(x, fs, m):
    sig = np.fft.fft(x, m)
    shift_fft = np.abs(np.fft.fftshift(sig))
    frequence = np.linspace(-fs / 2, fs / 2, m)
    return (frequence, shift_fft)

# Carrier
def c(t):
    return np.cos(2 * np.pi * FC * t)

# DSB-AM signal
def modulate(t):
    return input_signal(t) * c(t)

# Demodulation
def demodulate(t):
    return modulate(t) * c(t)

# Low pass filter
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Time 
time = np.linspace(0, T0, FS)

# System of input signal
y1 = [input_signal(x) for x in time]
# FT
freq_1, res_1 = f_transform(y1, FS, M)

# System of modulated signal
y2 = [modulate(x) for x in time]
# FT
freq_2, res_2 = f_transform(y2, FS, M)

# System of demodulated signal
y3 = [demodulate(x) for x in time]
# FT
freq_3, res_3 = f_transform(y3, FS, M)

# Lowpass filter
y4 = butter_lowpass_filter(CUT_OFF, FS, ORDER)
# FT
freq_4, res_4 = f_transform(y4, FS, M)

fig, s1 = plt.subplots(8)
s1[0].plot(time, y1)
s1[1].plot(time, y2)
s1[2].plot(freq_1, res_1)
s1[3].plot(freq_2, res_2)
s1[4].plot(time, y3)
s1[5].plot(freq_3, res_3)
s1[6].plot(time, y4)
s1[7].plot(freq_4, res_4)

plt.show()