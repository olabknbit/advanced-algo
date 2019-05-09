import numpy as np

imag = 1j


def file_to_array():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = [int(x) for x in lines[1].split(sep=' ')]
        b = [int(x) for x in lines[2].split(sep=' ')]
    return n, a, b


def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        Xk = 0
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
    from numpy.fft import ifft, fft
    b += [0] * (len(a) - len(b))
    return ifft((fft(a) * fft(b)))


if __name__ == '__main__':
    print(teoplitz(*file_to_array()))
