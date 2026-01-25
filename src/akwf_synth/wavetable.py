from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class WaveData:
    samples: np.ndarray

    @property
    def length(self) -> int:
        return self.samples.shape[0]

    @property
    def samples_normalised(self) -> np.ndarray:
        peak_abs = np.max(np.abs(self.samples))

        if peak_abs == 0 or peak_abs == 1:
            return self.samples
        else:
            coefficient = 1 / peak_abs
            normalised = self.samples * coefficient
            return normalised
