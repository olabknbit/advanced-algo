#!/usr/bin/env python
import numpy as np

imag = 1j


def file_to_array():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = [float(x) for x in lines[1].split(' ')]
        b = [float(x) for x in lines[2].split(' ')]
    return n, a, b


def fft(x):
    X = []
    N = len(x)

    rreusables = [[np.exp(-imag * 2. * np.pi * k * m / (N / 2.)) for m in range(int(N / 2))] for k in range(N)]
    factor = np.exp(-imag * 2. * np.pi * np.arange(N) / N)
    for k in range(N):
        x_even = x[::2]
        x_odd = x[1::2]
        even = sum(x_even * rreusables[k])
        odd = sum(x_odd * rreusables[k])

        odd *= factor[k]
        X.append(even + odd)
    return X


def dft_slow(x):
    X = []
    N = len(x)
    for k in range(N):
        Xk = 0.
        for n, xn in enumerate(x):
            Xk += xn * np.exp(-imag * 2. * np.pi * k * n / N)
        X.append(Xk)
    return X


def idft(X):
    x = []
    N = len(X)
    for n in range(N):
        xn = 0.
        for k, Xk in enumerate(X):
            xn += Xk * np.exp(imag * 2. * np.pi * k * n / N)
        x.append(1. / N * xn)
    return x


def teoplitz(n, a, b):
    padding = [0] * (n - 1)
    a = np.append(a, padding)
    b = np.append(padding, b)
    b = np.append(b, [0.] * (len(a) - len(b)))

    dft_a = np.array(fft(a))
    dft_b = np.array(fft(b))

    prod = dft_a * dft_b

    idft_c = np.real(idft(prod))

    return np.append(idft_c[n - 1:], idft_c[:n - 1])


if __name__ == '__main__':
    print(teoplitz(*file_to_array()))
