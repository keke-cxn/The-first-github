from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
from thinkdsp import SquareSignal
import thinkdsp
import thinkplot
from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
from IPython.display import Audio
from thinkdsp import read_wave


class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

class SquareSignal(Sinusoid):
    """Represents a sawtooth signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = self.amp*np.sign(unbias(frac))
        return ys


# 2-2
# triangle =thinkdsp.TriangleSignal(200).make_wave(duration=0.05, framerate=40000)
# triangle.plot()
# plt.show()
# triangle.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# sawtooth = SawtoothSignal(200).make_wave(duration=0.05, framerate=40000)
# sawtooth.plot()
# plt.show()
# sawtooth.make_audio()
# sawtooth.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# Square=SquareSignal(200).make_wave(duration=0.05, framerate=40000)
# Square.plot()
# plt.show()
# Square.make_audio()
# Square.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# sawtooth.make_spectrum().plot(color='blue')
# Square.make_spectrum().plot(color='red')
# triangle.make_spectrum().plot(color='black')
# decorate(xlabel='Frequency (Hz)')
# plt.show()




# 2-3
# square = SquareSignal(1100).make_wave(duration=0.005, framerate=10000)
# square.plot()
# plt.show()
# square.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# 2-4
# triangle = thinkdsp.TriangleSignal().make_wave(duration=0.01)
# triangle.plot()
# decorate(xlabel='Time (s)')
# plt.show()

# spectrum = triangle.make_spectrum()
# spectrum.hs[0]
# print(spectrum.hs[0])

# spectrum.hs[0] = 100
# triangle.plot(color='gray')
# spectrum.make_wave().plot()
# decorate(xlabel='Time (s)')
# plt.show()

2-5
def filter_spectrum(spectrum):
    """Divides the spectrum through by the fs.
    
    spectrum: Spectrum object
    """
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = thinkdsp.TriangleSignal(freq=440).make_wave(duration=0.5)
wave.make_audio()
wave.plot()
plt.show()
spectrum = wave.make_spectrum()
spectrum.plot()
plt.show()

spectrum.plot(high=10000, color='red')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000, color='blue')
decorate(xlabel='Frequency (Hz)')
plt.show()


filtered = spectrum.make_wave()
filtered.make_audio()
filtered.plot()
plt.show()