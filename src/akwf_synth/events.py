from dataclasses import dataclass


@dataclass
class NoteEvent:
    midi_note: int


@dataclass
class NoteOn(NoteEvent):
    midi_velocity: int


@dataclass
class NoteOff(NoteEvent):
    pass
