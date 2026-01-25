from akwf_synth.audio import AudioEngine
from akwf_synth.config import AudioConfig, SynthConfig
from akwf_synth.oscillator import WavetableOscillator
from akwf_synth.wavetable import WaveData
from loaders.wav_loader import load_data_from_wav_file

"""
main.py
 ├─ create AudioConfig
 ├─ create SynthConfig
 │
 ├─ load waveform (using SynthConfig)
 ├─ create Oscillator (using SynthConfig + waveform)
 └─ create AudioEngine (using AudioConfig + oscillator)
"""


def main():
    wave = load_data_from_wav_file("./data/akwf/AKWF/AKWF_0002/AKWF_0130.wav")
    audio_config = AudioConfig()
    # synth_config = SynthConfig()
    renderer = WavetableOscillator(
        waveform=wave, frequency=110, amplitude=1, sampling_rate=44100
    )
    engine = AudioEngine(renderer, audio_config)

    with engine:
        input("Press Enter to quit...")


if __name__ == "__main__":
    main()
