"""
This python module takes a python list and reduces its size by a given ratio
"""


# TODO something with the process is not correct the sample is a little bit distorted when written back to wavefile
# TODO Refactor: Alle Module in eigene Dateien und nur eine main Datei soll mit argparse ausgestattet sein


def reduce(sample, ratio):
    out = []
    sample_sum = 0.0

    for i in range(len(sample)):
        sample_sum += sample[i]
        if i % ratio == 0:
            out.append(int(sample_sum / ratio))
            sample_sum = 0
    return out


def write_header(file: str, declaration: str, data, style=None):
    """
    Writes a python list to a C/C++ header file
    :param file: Filename
    :param declaration: Declaration of array, for example:
        const uint8_t sample_data
        or:
        __code const uint8_t sample_data
    :param data:
    :param style: Will decide how if the array elements are fully embraced or not
        for style == 'SDCC' it will {number} embrace every element. Otherwise it does nothing
    :return: True if file was written successfully
    """
    with open(file, mode='w') as f:
        f.write('#ifndef SAMPLE_H\n'
                '#define SAMPLE_H\n')
        f.write('const int SAMPLE_LEN = {};\n'.format(len(data)))
        f.write(declaration)
        f.write('= {\n')
        if type == 'SDCC':
            pass
        else:
            f.write(data)
        f.write('\n};\n'
                '#endif\n')


if __name__ == '__main__':
    import filereader
    import argparse
    import twos_complement
    import plot
    import soundfile as sf
    import numpy as np

    def parse_write_header():
        pass

    __parser = argparse.ArgumentParser()
    __parser.add_argument('path',
                          type=str,
                          help='Path to the file')

    __parser.add_argument('ratio',
                          type=int,
                          help='Ratio of samplerate reduction')

    __parser.add_argument('-s',
                          '--startswith',
                          type=str,
                          help='Start line of the array, for example: "static const"',
                          default='static const')

    __parser.add_argument('-p',
                          '--print_sample',
                          action='store_true',
                          help='Print to Data to Terminal')

    __parser.add_argument('-t',
                          '--twos_complement',
                          help='Convert the samples to unsigned twos complement format.'
                               ' This is important for any king of I2S DAC',
                          action='store_true')

    __parser.add_argument('-plt',
                          '--plot',
                          help='Plot the reduced samples via matplotlib',
                          action='store_true')
    __parser.add_argument('-w',
                          '--write_sample',
                          help='If specified: Name of the wav file where the data is written back'
                               'Note: You must specify the samplerate!')
    __parser.add_argument('-sr',
                          '--samplerate',
                          type=int,
                          help='Samplerate for writ back wavfile')
    __parser.add_argument('-c',
                          '--cut',
                          help='Cut the last element of the array. Sometimes its necessary because Audacity will write'
                               'one sample too much.',
                          action='store_true')

    args = __parser.parse_args()

    sample = filereader.read_file(args.path, startswith=args.startswith)
    sample = reduce(sample, args.ratio)

    # (Optional) Cut the last sample
    if args.cut:
        sample = sample[:-1]

    # (Optional) Convert the samples into twos complement format
    if args.twos_complement:
        sample = twos_complement.convert(sample)

    # (Optional) Print Data to Terminal
    if args.print_sample:
        print('Reduced Sample: \n {} \n Sample Len: {} \n'.format(sample, len(sample)))

    # (Optional) Write the samples to wavfile
    samplerate = None
    if args.samplerate:
        samplerate = int(args.samplerate)
    if args.write_sample:
        sample_np = np.array(sample, dtype='int16')
        sample_np = sample_np << 8
        if not samplerate:
            raise Exception('Specify samplerate if you want write the samples back to wavfile!\n')
        sf.write(args.write_sample, sample_np, samplerate)

    # (Optional) Plot the samples
    if args.plot:
        plot.plot(sample)
