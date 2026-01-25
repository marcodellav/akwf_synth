from dataclasses import dataclass

import numpy as np
import soundfile as sf

from akwf_synth.wavetable import WaveData


def load_data_from_wav_file(path: str) -> WaveData:
    samples, samplerate = sf.read(path, dtype="float32")

    # If the wav file is stereo, take the first channel
    if samples.ndim > 1:
        samples = samples[:, 0]

    return WaveData(samples=samples)


# wave = load_data_from_wav_file("./data/akwf/AKWF/AKWF_0001/AKWF_0015.wav")

# print(wave.samples)
# print(wave.samples_normalised)
