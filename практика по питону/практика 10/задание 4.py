import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def WaveCalculation(frequency, amplitude, t):
    return amplitude * np.sin(2 * np.pi * frequency * t)


def WaveSumCalculation(frequency1, amplitude1, frequency2, amplitude2, t):
    wave1 = WaveCalculation(frequency1, amplitude1, t)
    wave2 = WaveCalculation(frequency2, amplitude2, t)
    return wave1, wave2, wave1 + wave2


def update(val):

    freq1 = freq_slider1.val
    amp1 = amp_slider1.val
    freq2 = freq_slider2.val
    amp2 = amp_slider2.val


    t = np.linspace(0, 1, 1000)
    wave1, wave2, sum_wave = WaveSumCalculation(freq1, amp1, freq2, amp2, t)


    ax_wave1.clear()
    ax_wave1.plot(t, wave1, label='Волна 1')
    ax_wave1.set_title('Волна 1')
    ax_wave1.set_xlabel('Время')
    ax_wave1.set_ylabel('Амплитуда')
    ax_wave1.legend()

    ax_wave2.clear()
    ax_wave2.plot(t, wave2, label='Волна 2')
    ax_wave2.set_title('Волна 2')
    ax_wave2.set_xlabel('Время')
    ax_wave2.set_ylabel('Амплитуда')
    ax_wave2.legend()

    ax_sum_wave.clear()
    ax_sum_wave.plot(t, sum_wave, label='Сумма волн')
    ax_sum_wave.set_title('Сложение двух волн')
    ax_sum_wave.set_xlabel('Время')
    ax_sum_wave.set_ylabel('Амплитуда')
    ax_sum_wave.legend()

    plt.draw()


fig, (ax_freq1, ax_amp1, ax_freq2, ax_amp2, ax_wave1, ax_wave2, ax_sum_wave) = plt.subplots(7, 1, figsize=(8, 14))


freq_slider1 = Slider(ax_freq1, 'Частота 1', 1, 10, valinit=1)
amp_slider1 = Slider(ax_amp1, 'Амплитуда 1', 0, 1, valinit=0.5)
freq_slider2 = Slider(ax_freq2, 'Частота 2', 1, 10, valinit=1)
amp_slider2 = Slider(ax_amp2, 'Амплитуда 2', 0, 1, valinit=0.5)


freq_slider1.on_changed(update)
amp_slider1.on_changed(update)
freq_slider2.on_changed(update)
amp_slider2.on_changed(update)


update(None)

plt.tight_layout()
plt.show()