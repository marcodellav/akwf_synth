from akwf_synth.audio import AudioEngine
from akwf_synth.config import AudioConfig
from akwf_synth.oscillator import WavetableOscillator
from akwf_synth.synth import MonoSynth
from loaders.wav_loader import load_data_from_wav_file
from akwf_synth.input.keyboard import KeyboardController

"""
main.py

"""


def main():
    wave = load_data_from_wav_file("./data/akwf/AKWF/AKWF_0002/AKWF_0130.wav")
    audio_config = AudioConfig()
    # synth_config = SynthConfig()
    synth = MonoSynth()
    renderer = WavetableOscillator(
        waveform=wave, frequency=110, amplitude=1, sampling_rate=44100
    )
    engine = AudioEngine(renderer, audio_config)
    kc = KeyboardController(synth.handle_note_event)
    with engine, kc:
        input("Press Enter to quit...\n")


if __name__ == "__main__":
    main()
