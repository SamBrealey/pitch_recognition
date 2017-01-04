import pylab
from scipy.io import wavfile
import matplotlib.pyplot as plt

# sampFreq, snd = wavfile.read('440_sine.wav')

# snd = snd / (2.**15)
# # converts our sound array to floating point values ranging from -1 to 1

# s1 = snd[:, 0]
# # work with one channel



def plot_tone(channel, frequency):
    timeArray = pylab.arange(0, len(channel), 1)
    timeArray = (timeArray / float(frequency)) * 1000
    plt.plot(timeArray, channel, color='k')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (ms)')
    plt.show()


def get_unique_part_of_fourier_transform(channel):
    transform = pylab.fft(channel)
    no_of_unique_points = int(pylab.ceil((len(channel)+1)/2.0))
    return transform[0:no_of_unique_points]


def get_power_spectrum(transform, channel_length):
    p = abs(transform)
    p = p / float(channel_length)
    # scale by the number of points so that
    # the magnitude does not depend on the length
    # of the signal or on its sampling frequency
    p = p**2  # square it to get the power

    # Since we dropped half the FFT, we multiply mx by 2 to keep the same energy.
    # The DC component and Nyquist component, if it exists, are unique and should not be multiplied by 2.
    if channel_length % 2 > 0:  # we've got odd number of points fft
        p[1:len(p)] = p[1:len(p)] * 2
    else:
        p[1:len(p)-1] = p[1:len(p) - 1] * 2  # we've got even number of points fft

    return p


def plot_power_spectrum(power, channel_length, frequency):
    freqArray = pylab.arange(0, len(power), 1.0) * (frequency / channel_length)
    plt.plot(freqArray/1000, 10*pylab.log10(power), color='k')
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')
    plt.show()
