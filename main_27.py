#!/usr/bin/env python


example_filename = 'example.txt'
another_example_filename = 'another_example.txt'


def file_to_array(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        a = [float(x) for x in lines[1].split(' ')]
        b = [float(x) for x in lines[2].split(' ')]
    return a, b


def write_results_to_file(original_filename, results):
    results_filename = original_filename.split('.txt')[0] + ".wyj.txt"
    line = ' '.join([str(int(el)) for el in results])
    with open(results_filename, 'w') as f:
        f.writelines([line])


def get_filename():
    import sys

    if len(sys.argv) < 2:
        raise Exception('No input file given')
    return sys.argv[1]


if __name__ == '__main__':
    from teoplitz_27 import teoplitz

    input_file = get_filename()
    results = teoplitz(*file_to_array(input_file))
    print(results)
    write_results_to_file(input_file, results)
