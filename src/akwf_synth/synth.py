from akwf_synth.input.keyboard import NoteOff, NoteOn
from akwf_synth.oscillator import WavetableOscillator
from loaders.wav_loader import load_data_from_wav_file


def midi_note_to_frequency(midi_note):
    """
    MIDI note 60 corresponds to C4 (Middle C).
    """
    A4_FREQUENCY = 440.0
    A4_MIDI_NOTE = 69

    return A4_FREQUENCY * 2 ** ((midi_note - A4_MIDI_NOTE) / 12)


class Voice:
    def __init__(self):
        self.is_active = False
        self.wave = load_data_from_wav_file("./data/akwf/AKWF/AKWF_0002/AKWF_0139.wav")
        self.frequency = 440

        self.oscillator = WavetableOscillator(
            self.wave, self.frequency, 1, sampling_rate=44100
        )

    def start(self, note):
        self.is_active = True
        self.oscillator.frequency = midi_note_to_frequency(note)
        self.oscillator.amplitude = 1
        # print (self.oscillator.frequency)

    def stop(self):
        self.is_active = False

    def render(self, frames):
        return self.oscillator.render(frames)


class MonoSynth:
    def __init__(self):
        self.voice = Voice()
        self.current_note = None

    def handle_note_event(self, event):
        if isinstance(event, NoteOn):
            self.current_note = event.midi_note
            self.voice.start(event.midi_note)

        elif isinstance(event, NoteOff):
            if event.midi_note == self.current_note:
                self.voice.stop()
                self.current_note = None

    def render(self, frames):
        return self.voice.render(frames)
