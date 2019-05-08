import numpy as np

import main


def test_example():
    n, a, b = main.file_to_array()
    assert (main.teoplitz(n, a, b) == np.convolve(a, b)).all()
