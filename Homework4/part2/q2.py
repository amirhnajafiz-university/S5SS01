# Using python matplot lib and numpy to generate our plots
import matplotlib.pyplot as plt
import numpy as np
# Using scipy for creating filters and convolutions
from scipy.signal import butter, lfilter, freqz, hilbert


# const
T0 = 0.1
TS = 0.0001

FC = 250
FS = 1000

M = 1024 * 1024
CO = 100


# Input Signal of the system which is the sinc function
def input_signal(t):
    if t >= 0 and t <= T0:
        return np.sinc(100 * t)
    else:
        return 0

# Carrier signal which is con(2pi250t)
def carrier(t):
    return np.cos(2 * np.pi * FC * t)

def sin_func(t):
	return np.sin(2 * np.pi * FC * t)


# Continous time fourier transform
def FFT(x, m):
    return np.abs( np.fft.fftshift( np.fft.fft(x, m) ) )

# DSB-AM signal
def modulate_signal(t):
    return input_signal(t) * carrier(t)

# Demodulation signal
def demodulate_signal(t):
    return modulate_signal(t) * carrier(t)


# Hilbert signal 
def signal_hilbert(t):
	return hilbert( [input_signal(x) for x in t] )

# LSSB - AM
def modulete_low(t):
	sig = signal_hilbert(t)
	return [ ( modulate_signal(t[i]) + sin_func(t[i]) * sig[i] ) for i in range( len(t) )]


# Low pass filter 
# Link: https://www.delftstack.com/howto/python/low-pass-filter-python/
def lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    # Time 
    time = np.linspace(0, T0, FS)
    frequence = np.linspace(-FS / 2, FS / 2, M)

    # input signal
    y1 = [input_signal(x) for x in time]
    fy1 = FFT(y1, M)

    # hilbert
    y2 = signal_hilbert(time)
    fy2 = FFT(y2, M)

    # lssb-modulated 
    y3 = modulete_low(time)
    fy3 = FFT(y3, M)

    # Phase
    phase1 = np.angle(y1)
    phase3 = np.angle(y3)

    # demodulated 
    y4 = [demodulate_signal(x) for x in time]
    fy4 = FFT(y4, M)

    figoure, my_plot = plt.subplots(10)

    my_plot[0].plot(time, y1)
    my_plot[1].plot(frequence, fy1)
    my_plot[2].plot(time, y2)
    my_plot[3].plot(frequence, fy2)
    my_plot[4].plot(time, y3)
    my_plot[5].plot(frequence, fy3)
    my_plot[6].plot(time, phase1)
    my_plot[7].plot(time, phase3)
    my_plot[8].plot(time, y4)
    my_plot[9].plot(frequence, fy4)

    plt.show()