from thinkdsp import SinSignal
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import Chirp
from thinkdsp import ExpoChirp
from thinkdsp import SinSignal
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from thinkdsp import normalize, unbias
from thinkdsp import read_wave

# 3-1
# 设置一个sin信号泄露，周期是30.25这样可以产生泄露，因为期间不是周期的整数倍就会有泄露
signal = SinSignal(freq=440)
duration = signal.period * 30.25
wave = signal.make_wave(duration)
wave.plot()
plt.show() # sin的波形

spectrum = wave.make_spectrum()
spectrum.plot(high=880)
decorate(xlabel='Frequency (Hz)')
plt.show() #sin的频谱

# 用不同的窗口看看他们对泄露的影响，分别用了bartlett,blackman,hamming,hanning窗口进行对比
for window_func in [np.bartlett, np.blackman, np.hamming, np.hanning]:
    wave = signal.make_wave(duration)
    wave.ys *= window_func(len(wave.ys))

    spectrum = wave.make_spectrum()
    spectrum.plot(high=880, label=window_func.__name__)

decorate(xlabel='Frequency (Hz)')
plt.show()

# 3-2
PI2 = 2 * np.pi
# 锯齿调频
# 名为SawtoothChirp的类
class SawtoothChirp(Chirp):
    """Represents a sawtooth signal with varying frequency."""
    # 重写 evaluate
    def evaluate(self, ts):
        """Helper function that evaluates the signal.

        ts: float array of times
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys
    
# 设置信号为锯齿波调制
signal = SawtoothChirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=4000)
wave.apodize()
wave.make_audio()
# 信号的频谱
sp = wave.make_spectrogram(256)
sp.plot()
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()


# 3-3
# 设置信号为锯齿波调制 从2500-3000Hz
signal = SawtoothChirp(start=2500, end=3000)
# 时长为1s 帧率为20kHz
wave = signal.make_wave(duration=1, framerate=20000)
wave.make_audio()
# 他的频谱如下
wave.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

# 3-4
# 打开"滑奏" glissando 听声音 查看频谱
wave = read_wave(r'C:\Users\Administrator\Desktop\wangyigang-shiyan\ThinkDSP-master\code\72475__rockwehrmann__glissup02.wav')
wave.make_audio()
# 他的频谱如下
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()


# 3-5
# 写名为TromboneGliss的类(以扩展Chirp) 写evaluate函数
# evaluate用于创建一个模拟长号滑奏的波形
class TromboneGliss(Chirp):
    """Represents a trombone-like signal with varying frequency."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys
# 设置低音和高音
low = 262
high = 349
# 调用TromboneGliss类创建一个模拟长号滑奏的信号
# 从音调高到低播放
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()
# 音调从低到高播放
signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
# 音调先从高到低再从低到高播放
wave = wave1 | wave2
wave.make_audio()
# 音调先从高到低再从低到高播放大的频谱
sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
decorate(xlabel='Time (s)', ylabel='Frequency (aHz)')
plt.show()


# 3-6
# 打开元音发音的音频
wave = read_wave(r'C:\Users\Administrator\Desktop\wangyigang-shiyan\ThinkDSP-master\code\87778__marcgascon7__vocals.wav')
wave.make_audio()
# 他的频谱如下
wave.make_spectrogram(1024).plot(high=1000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()
# 取得范围为0-1000
high = 1000
# 截取元音a的片段,画出他们的频谱
segment = wave.segment(start=1, duration=0.25)
segment.make_spectrum().plot(high=high)
plt.show()
# 截取元音e的片段,画出他们的频谱
segment = wave.segment(start=2.2, duration=0.25)
segment.make_spectrum().plot(high=high)
decorate(xlabel='Frequency (Hz)')
plt.show()
# 截取元音i的片段,画出他们的频谱
segment = wave.segment(start=3.5, duration=0.25)
segment.make_spectrum().plot(high=high)
decorate(xlabel='Frequency (Hz)')
plt.show()
# 截取元音o的片段,画出他们的频谱
segment = wave.segment(start=5.1, duration=0.25)
segment.make_spectrum().plot(high=high)
decorate(xlabel='Frequency (Hz)')
plt.show()
# 截取元音u的片段,画出他们的频谱
segment = wave.segment(start=6.5, duration=0.25)
segment.make_spectrum().plot(high=high)
decorate(xlabel='Frequency (Hz)')
plt.show()