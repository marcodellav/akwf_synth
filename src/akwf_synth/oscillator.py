import numpy as np


class SineOscillator:
    """
    a phase-accumulator sine oscillator implementation
    """

    def __init__(self, frequency, amplitude, sampling_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.sampling_rate = sampling_rate
        self.phase = 0

    def render(self, frames):
        phase_increment = self.frequency / self.sampling_rate
        buffer = np.empty((frames, 1), dtype=np.float32)

        for sample in range(0, frames):
            # convert phase to amplitude
            sine_value_at_sample = self.amplitude * np.sin(2 * np.pi * self.phase)
            # advance phase
            self.phase += phase_increment
            # wrap phase
            if self.phase >= 1:
                self.phase -= 1
            # write into buffer
            buffer[sample] = sine_value_at_sample
        return buffer


class WavetableOscillator:
    """
    a phase-accumulator single-cycle waveform oscillator implementation
    """

    def __init__(self, waveform, frequency, amplitude, sampling_rate):
        self.waveform = waveform
        self.frequency = frequency
        self.amplitude = amplitude
        self.sampling_rate = sampling_rate
        self.phase = 0

    def render(self, frames):
        phase_increment = self.frequency / self.sampling_rate
        buffer = np.empty((frames, 1), dtype=np.float32)
        for sample in range(0, frames):
            index = int(self.phase * self.waveform.length)
            if index >= self.waveform.length:
                index = self.waveform.length -1
            # convert phase to amplitude
            sample_value_at_index = (
                self.amplitude * self.waveform.samples_normalised[index]
            )
            # advance phase
            self.phase += phase_increment
            # wrap phase
            if self.phase >= 1:
                self.phase -= 1
            # write into buffer
            buffer[sample] = sample_value_at_index
        return buffer
