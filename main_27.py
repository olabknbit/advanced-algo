#!/usr/bin/env python

import sys

from teoplitz_27 import teoplitz

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


def choose_filename():
    import Tkinter
    import tkFileDialog

    root = Tkinter.Tk()
    root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    return root.filename


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('No input file given')
    input_file = sys.argv[1]

    results = teoplitz(*file_to_array(input_file))
    print(results)
    write_results_to_file(input_file, results)
