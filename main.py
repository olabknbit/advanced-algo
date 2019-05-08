import numpy as np


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
    i = 1.  # TODO what is i?
    omegaN = np.exp(i * 2. * np.pi / N)
    for k in range(N):
        Xk = 0
        for n, xn in enumerate(x):
            Xk += xn * np.exp(-i * 2 * np.pi * k * n / N)
        X.append(Xk)
    return X


def idft(X):
    x = []
    N = len(X)
    i = 1.  # TODO what is i?
    for n in range(N):
        xn = 0
        for k, Xk in enumerate(X):
            xn += Xk * np.exp(i * 2 * np.pi * k * n / N)
        x.append(1 / N * xn)
    return x


def teoplitz(n, a, b):
    return idft(np.convolve(np.array(dft(a)), np.array(dft(b))))


if __name__ == '__main__':
    print(teoplitz(*file_to_array()))
