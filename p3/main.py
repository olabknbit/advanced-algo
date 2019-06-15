#!/usr/bin/env python
import numpy as np

imag = 1j

example_filename = 'example.txt'
another_example_filename = 'another_example.txt'


def file_to_array():
    with open(example_filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = [float(x) for x in lines[1].split(sep=' ')]
        b = [float(x) for x in lines[2].split(sep=' ')]
    return n, a, b


def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        Xk = 0.
        for n, xn in enumerate(x):
            Xk += xn * np.exp(-imag * 2 * np.pi * k * n / N)
        X.append(Xk)
    return X


def idft(X):
    x = []
    N = len(X)
    for n in range(N):
        xn = 0
        for k, Xk in enumerate(X):
            xn += Xk * np.exp(imag * 2 * np.pi * k * n / N)
        x.append(1 / N * xn)
    return x


def teoplitz(n, a, b):
    padding = [0] * (n - 1)
    a = np.append(a, padding)
    b = np.append(padding, b)
    b = np.append(b, [0.] * (len(a) - len(b)))

    dft_a = np.array(dft(a))
    dft_b = np.array(dft(b))
    prod = dft_a * dft_b

    idft_c = np.real(idft(prod))

    return np.append(idft_c[n - 1:], idft_c[:n - 1])


if __name__ == '__main__':
    print(teoplitz(*file_to_array()))
