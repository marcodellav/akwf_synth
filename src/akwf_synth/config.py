from dataclasses import dataclass


@dataclass
class AudioConfig:
    """A class for holding hardware & timing audio parameters"""

    output_device: str = "Built-in Output"
    sample_rate: int = 44100
    channel_count: int = 1
    block_size: int = 512


@dataclass
class SynthConfig:
    """
    Purpose:
        Initial synth behavior.

    Contains:
        - Path to AKWF waveform file
        - Default amplitude
        - Initial frequency (or note)

    Characteristics:
        - Used at startup only
        - Passed into synth/oscillator creation
        - Never touched inside audio callbacks
    """

    path_to_waveform: str = "./"
    default_amplitude: float = 0.5
    initial_frequency: float = 73.5
    base_midi_note: int = 60
    tuning_reference: float = 440.0
    tuning_note: int = 69
