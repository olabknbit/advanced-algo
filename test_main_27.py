import numpy as np

import main_27 as main

filename = main.example_filename


def test_teoplitz():
    n, a, b = main.file_to_array(filename)
    mains = np.array(main.teoplitz(n, a, b))
    nps = np.convolve(a, b)
    np.testing.assert_array_almost_equal(mains, nps)


def test_dft_slow():
    n, a, b = main.file_to_array(filename)
    mains = np.array(main.dft_slow(a))
    nps = np.fft.fft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_idft_slow():
    n, a, b = main.file_to_array(filename)
    mains = np.array(main.idft_slow(a))
    nps = np.fft.ifft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_fft():
    n, a, b = main.file_to_array(filename)
    mains = np.array(main.fft(a))
    nps = np.fft.fft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_ifft():
    n, a, b = main.file_to_array(filename)
    mains = np.array(main.ifft(a))
    nps = np.fft.ifft(a)
    np.testing.assert_array_almost_equal(mains, nps)
