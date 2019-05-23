import numpy as np


def fft(x):
    N = len(x)
    x = np.asarray(x)

    if N % 2 > 0:
        return dft_slow(x)
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd, X_even + factor[N / 2:] * X_odd])


def dft_slow(x):
    X = []
    N = len(x)
    for k in range(N):
        Xk = 0.
        for n, xn in enumerate(x):
            Xk += xn * np.exp(-1j * 2. * np.pi * k * n / N)
        X.append(Xk)
    return X


def ifft(x):
    N = len(x)
    x = np.asarray(x)

    if N % 2 > 0:
        return idft_slow(x)
    else:
        X_even = ifft(x[::2])
        X_odd = ifft(x[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)

        return 1. / 2 * np.concatenate([X_even + factor[:N / 2] * X_odd, X_even + factor[N / 2:] * X_odd])


def idft_slow(X):
    x = []
    N = len(X)
    for n in range(N):
        xn = 0.
        for k, Xk in enumerate(X):
            xn += Xk * np.exp(1j * 2. * np.pi * k * n / N)
        x.append(1. / N * xn)
    return x


def teoplitz(a, b):
    n = len(b)
    padding = [0] * (n - 1)
    a = np.append(a, padding)
    b = np.append(padding, b)
    b = np.append(b, [0.] * (len(a) - len(b)))

    dft_a = np.array(fft(a))
    dft_b = np.array(fft(b))

    prod = dft_a * dft_b

    idft_c = np.real(ifft(prod))

    return np.append(idft_c[n - 1:], idft_c[:n - 1])


def teoplitz_slow(a, b):
    n = len(b)
    padding = [0] * (n - 1)
    a = np.append(a, padding)
    b = np.append(padding, b)
    b = np.append(b, [0.] * (len(a) - len(b)))

    dft_a = np.array(dft_slow(a))
    dft_b = np.array(dft_slow(b))

    prod = dft_a * dft_b

    idft_c = np.real(idft_slow(prod))

    return np.append(idft_c[n - 1:], idft_c[:n - 1])
