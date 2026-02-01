from pynput import keyboard

from akwf_synth.events import NoteOff, NoteOn


class KeyboardController:
    """
    A tiny KeyboardController that:
    listens for key down / up
    translates keys → frequency
    calls oscillator.set_frequency(...)
    """

    def __init__(self, event_callback):
        self.event_callback = event_callback

    base_note = 60
    _key_to_semitone = {
        "a": 0,
        "w": 1,
        "s": 2,
        "e": 3,
        "d": 4,
        "f": 5,
        "t": 6,
        "g": 7,
        "y": 8,
        "h": 9,
        "u": 10,
        "j": 11,
        "k": 12,
        "o": 13,
        "l": 14,
        "p": 15,
        ";": 16,
        "'": 17,
    }

    def _map_key_to_semitone(self, key):
        if key not in self._key_to_semitone:
            return None

        semitone = self._key_to_semitone[key]
        return semitone

    def on_press(self, key):
        if not hasattr(key, "char"):
            return  # ignore special keys cleanly

        semitone = self._map_key_to_semitone(key.char)
        if semitone is not None:
            midi_note = self.base_note + semitone
            print(midi_note)
            self.event_callback(NoteOn(midi_note, 100))
        else:
            return

    def on_release(self, key):
        if not hasattr(key, "char"):
            return  # ignore special keys cleanly

        semitone = self._map_key_to_semitone(key.char)
        if semitone is not None:
            midi_note = self.base_note + semitone
            self.event_callback(NoteOff(midi_note))
        else:
            return

    def __enter__(self):
        """
        start the keyboard listener thread.
        """
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None


# keyboard_test = KeyboardController("A")
# print(keyboard_test._map_key_to_semitone())
