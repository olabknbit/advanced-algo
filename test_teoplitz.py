import numpy as np

import teoplitz


def test_teoplitz():
    a = [7, 3, 2, 5, 1, 1, 1]
    b = [2, 5, 9, 4]
    mains = np.array(teoplitz.teoplitz(a, b))
    nps = np.convolve(a, b, mode='valid')
    print(mains)
    print(nps)
    np.testing.assert_array_almost_equal(mains, nps)


def test_dft_slow():
    a = [7, 3, 2, 5, 1, 1, 1]
    mains = np.array(teoplitz.dft_slow(a))
    nps = np.fft.fft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_idft_slow():
    a = [7, 3, 2, 5, 1, 1, 1]
    mains = np.array(teoplitz.idft_slow(a))
    nps = np.fft.ifft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_fft():
    a = [7, 3, 2, 5, 1, 1, 1]
    mains = np.array(teoplitz.fft(a))
    nps = np.fft.fft(a)
    np.testing.assert_array_almost_equal(mains, nps)


def test_ifft():
    a = [7, 3, 2, 5, 1, 1, 1]
    mains = np.array(teoplitz.ifft(a))
    nps = np.fft.ifft(a)
    np.testing.assert_array_almost_equal(mains, nps)


if __name__ == '__main__':
    test_teoplitz()
