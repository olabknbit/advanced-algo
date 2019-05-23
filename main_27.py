#!/usr/bin/env python

from teoplitz_27 import teoplitz

example_filename = 'example.txt'
another_example_filename = 'another_example.txt'


def file_to_array(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = [float(x) for x in lines[1].split(' ')]
        b = [float(x) for x in lines[2].split(' ')]
    return n, a, b


def write_results_to_file(original_filename, results):
    results_filename = original_filename.split('.txt')[0] + ".wyj.txt"
    line = ' '.join([str(int(el)) for el in results])
    with open(results_filename, 'w') as f:
        f.writelines([line])


if __name__ == '__main__':
    results = teoplitz(*file_to_array(example_filename))
    print(results)
    write_results_to_file(example_filename, results)
