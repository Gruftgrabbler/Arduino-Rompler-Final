"""
This module is an ease to use module to read header files converted from bin2header and wav2header converters
You can use this on its own via the terminal:
    python filereader.py pathToFile
or import this into another python module
"""


def read_file(file, startswith='static const'):
    """
    Reads a C/C++ File containing a single array and returns the C/C++ array as a python list.
    The input file can be formatted as hexadecimal or decimal and the output is always decimal
    :param file: path to given file
    :param startswith: AFTER the line which contains the startswith str the actual array begins
    :return: python list from C/C++ array
    """
    with open(file) as f:
        is_processing = False
        out = []
        for line in f:
            if line.startswith(startswith):
                is_processing = True
            elif line.startswith('};'):
                break
            elif is_processing:
                out.extend(__process(line))

        return out


def __process(line):
    """
    Processes a single line of the array which contains str data and converts it to int
    :param line: line of the given array
    :return: array of int
    """
    line = line.strip()
    items = line.split(',')

    # Cut the last element if its an empty string, for example '\n'
    if not items[-1]:
        items = items[:-1]
    out = []
    # If encoding is hexadecimal
    if items[0].startswith('0x'):
        [out.append(int(item, 16)) for item in items]

    # If encoding is decimal
    elif items[0].startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
        [out.append(int(item)) for item in items]
    return out


if __name__ == '__main__':
    import argparse

    __parser = argparse.ArgumentParser('Reads the given file containing a c array and prints it')
    __parser.add_argument('path',
                          type=str,
                          help='path to the file')
    __parser.add_argument('-startswith',
                          '--s',
                          type=str,
                          help='Start line of the array, for example: "static const int"',
                          default='static const')
    args = __parser.parse_args()

    sample = read_file(args.path, args.s)

    print('Input File: \n {} \n Items: {} \n'.format(sample, len(sample)))
