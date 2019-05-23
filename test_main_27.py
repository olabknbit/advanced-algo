import numpy as np

import main_27 as main


def test_example():
    n, a, b = main.file_to_array()
    mains = np.array(main.teoplitz(n, a, b))
    nps = np.convolve(a, b)
    np.testing.assert_array_almost_equal(mains, nps)


def test_dft():
    n, a, b = main.file_to_array()
    mains = np.array(main.dft(a))
    nps = np.fft.fft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_idft():
    n, a, b = main.file_to_array()
    mains = np.array(main.idft(a))
    nps = np.fft.ifft(a)
    np.testing.assert_array_almost_equal(mains, nps)
