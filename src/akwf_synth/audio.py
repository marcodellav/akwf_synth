import sys
import sounddevice as sd


class AudioEngine:
    def __init__(self, renderer, audio_config):
        """
        renderer must have a render(frames) method
        audio_config must contain audio settings
        """
        self.renderer = renderer
        self.audio_config = audio_config
        self._stream = None

    def _callback(self, outdata, frames, time, status):
        """
        callback(outdata: numpy.ndarray, frames: int,
                time: CData, status: CallbackFlags) -> None
        """
        if status:
            print(status, file=sys.stderr)
        outdata[:] = self.renderer.render(frames)

    def __enter__(self):
        output_device = self.audio_config.output_device
        samplerate = sd.query_devices(output_device, "output")["default_samplerate"]

        self._stream = sd.OutputStream(
            device=self.audio_config.output_device,
            channels=1,
            callback=self._callback,
            samplerate=samplerate,
        )
        self._stream.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None
