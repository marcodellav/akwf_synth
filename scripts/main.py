from akwf_synth.audio import AudioEngine
from akwf_synth.config import AudioConfig
from akwf_synth.input.keyboard import KeyboardController
from akwf_synth.synth import MonoSynth

"""
main.py

"""


def main():
    audio_config = AudioConfig()
    synth = MonoSynth()
    engine = AudioEngine(synth, audio_config)
    kc = KeyboardController(synth.handle_note_event)
    with engine, kc:
        input("Press Enter to quit...\n")


if __name__ == "__main__":
    main()
