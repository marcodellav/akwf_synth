from akwf_synth.input.keyboard import NoteOff, NoteOn


def midi_note_to_frequency(midi_note):
    """
    MIDI note 60 corresponds to C4 (Middle C).
    """
    A4_FREQUENCY = 440.0
    A4_MIDI_NOTE = 69

    return A4_FREQUENCY * 2 ** ((midi_note - A4_MIDI_NOTE) / 12), 2


class Voice:
    def __init__(self):
        self.is_active = False

    def start(self, note):
        self.is_active = True

    def stop(self):
        self.is_active = False

    def render(self, frames):
        pass


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
