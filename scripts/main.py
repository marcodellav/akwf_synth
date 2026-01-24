from akwf_synth.audio import AudioEngine
from akwf_synth.config import AudioConfig, SynthConfig
from akwf_synth.oscillator import ConstantRenderer, SineOscillatorRenderer

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
    audio_config = AudioConfig()
    # synth_config = SynthConfig()
    renderer = SineOscillatorRenderer(
        frequency=1000, amplitude=0.5, sampling_rate=44100
    )
    engine = AudioEngine(renderer, audio_config)

    with engine:
        input("Press Enter to quit...")


if __name__ == "__main__":
    main()
