import numpy as np


class ConstantRenderer:
    def __init__(self, value):
        self.value = value

    def render(self, frames):
        return np.full((frames, 1), self.value, dtype=np.float32)


class SineOscillatorRenderer:
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


class SingleCycleWaveFormOscillatorRenderer:
    """
    a phase-accumulator single-cycle waveform oscillator implementation
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
