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


def optimized_dft(x):
    X = []
    N = len(x)
    for k in range(N):
        even = 0.
        reusables = []
        for m in range(int(N / 2)):
            reusables.append(np.exp(-imag * 2. * np.pi * k * m / (N / 2.)))
            even += x[2 * m] * reusables[m]
        odd = 0.
        for m in range(int(N / 2)):
            odd += x[2 * m + 1] * reusables[m]
        odd *= np.exp(-imag * 2 * np.pi * k / N)
        X.append(even + odd)
    return X


def dft(x):
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

    dft_a = np.array(optimized_dft(a))
    dft_b = np.array(optimized_dft(b))

    prod = dft_a * dft_b

    idft_c = np.real(idft(prod))

    return np.append(idft_c[n - 1:], idft_c[:n - 1])


if __name__ == '__main__':
    print(teoplitz(*file_to_array()))
