import numpy as np

import main


def test_example():
    n, a, b = main.file_to_array()
    mains = np.array(main.teoplitz(n, a, b))
    nps = np.convolve(a, b)
    assert (mains == nps).all()


def test_dft():
    n, a, b = main.file_to_array()
    mains = np.array(main.dft(a))
    nps = np.fft.fft(a)
    print(mains)
    print(nps)
    np.testing.assert_allclose(mains, nps)


def test_idft():
    n, a, b = main.file_to_array()
    mains = np.array(main.idft(a))
    nps = np.fft.ifft(a)
    print(mains)
    print(nps)
    np.testing.assert_allclose(mains, nps)
