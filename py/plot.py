import matplotlib.pyplot as plt


def plot(data):
    plt.plot(data)
    plt.show()


if __name__ == '__main__':
    import filereader
    import argparse

    parser = argparse.ArgumentParser('Plots the given file')
    parser.add_argument('path',
                        metavar='path',
                        type=str,
                        help='path to the file')
    parser.add_argument('-startswith',
                        '--s',
                        metavar='startswith',
                        type=str,
                        help='Start line of the array, for example: "static const int"',
                        default='static const')

    args = parser.parse_args()
    sample = filereader.read_file(args.path, startswith=args.s)

    plot(sample)
