from enum import Enum


class FilterType(Enum):
    LOWPASS = 'low-pass'
    HIGHPASS = 'high-pass'
    BANDPASS = 'band-pass'
