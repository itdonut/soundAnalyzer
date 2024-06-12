from enum import Enum


class WindowFunctions(Enum):
    BOHMAN = 'Bohman'
    BARLETT = 'Barlett'
    BLACKMANN = 'Blackmann'
    BARLETT_HANN = 'Barlett-Hann'
    LANCZOS = 'Lanczos'
    HAMMING = 'Hamming'
    HANN = 'Hann'
    TRIANGULAR = 'Triangular'
    GAUSSIAN = 'Gaussian'
    KAISER = 'Kaiser'
