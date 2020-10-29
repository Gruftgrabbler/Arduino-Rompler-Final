# TODO Write a python sketch which uses the AudioSampleSample data and converts it for the project
# TODO Export the modified samples data back to a wav to check it for correctness


def read_sample(path: str, startswith: str, base: str):
    # TODO Outsource this code into an additional python module
    """
    This function reads a AudioSample.cpp File converted with wav2sketch into a python list
    :param path: path to the .cpp file containing the samples data
    :param startswith: the startswith string after which the actual samples data begin's
    :param base: hex or dec
    :return: samples data as python list
    """
    isProcessing = False
    sample = []

    def process(line):
        line = line.strip()
        items = line.split(',')
        if not items[-1]:
            items = items[:-1]
        if base == 'dec':
            [sample.append(item) for item in items]
        elif base == 'hex':
            [sample.append(int(item, 16)) for item in items]
        else:
            raise Exception("Please use base = 'hex' or base = 'dec")

    with open(path) as file:
        for line in file:
            if isProcessing & line.startswith('}'):
                break  # Reading is done
            if isProcessing:
                process(line)
            elif line.startswith(startswith):
                isProcessing = True

    # return list(map(int, samples))  # Return the samples data and convert it to a list of integer
    return sample


class Process:

    @staticmethod
    def process(sample, input_sample_rate, output_sample_rate, input_bit_rate, output_bit_rate):
        """
        :param sample: in form of a python list
        :param input_sample_rate: of the signal, for example 44100kHz
        :param output_sample_rate: of the signal
        :param input_bit_rate: For example 32 Bit unsigned
        :param output_bit_rate: For example 8 Bit unsigned
        :return:
        """
        output = []

        # Reduce Sample Bits
        # mask = 0xFF
        for i in range(len(sample)):
            shift = input_bit_rate - output_bit_rate
            sample[i] = sample[i] >> shift  # Use only the highest output_bit_rate Bits of the samples
            # samples[i] = samples[i] & mask  # Use only the highest 8 Bits of the samples

        # Reduce samples rate // TODO This cuts off samples of the ratio is not a factor of the samples len
        ratio = int(input_sample_rate / float(output_sample_rate))
        sample_sum = 0
        for i in range(len(sample)):
            sample_sum += sample[i]
            if (i + 1) % ratio == 0:
                output.append(sample_sum / ratio)
                sample_sum = 0

        # Bit rate reduction
        for i in range(len(output)):
            output[i] = int((round(output[i] * 2 ** output_bit_rate) / (2 ** output_bit_rate)))

        return output


if __name__ == '__main__':
    import pandas  # Write list to csv
    import soundfile as sf

    # Audio Sample
    PATH = '../../samples/Converters/wav2sketch/AudioSampleSample.cpp'
    STARTS_WITH = 'const unsigned int AudioSample'
    BASE = 'hex'

    # Sine Test
    # PATH = '../samples/wav2sketch/AudioSampleSineData.cpp'
    # STARTS_WITH = 'const uint8_ AudioSampleSineData'
    # BASE = 'dec'

    INPUT_SAMPLERATE = 44100
    OUTPUT_SAMPLERATE = 44100

    INPUT_BITRATE = 32
    OUTPUT_BIT_RATE = 8

    sample_data = read_sample(PATH, STARTS_WITH, BASE)
    # print('Imported samples data: \n {} \n Sample Len: {} \n'.format(sample_data, len(sample_data)))

    sample_data = Process.process(sample_data, INPUT_SAMPLERATE, OUTPUT_SAMPLERATE, INPUT_BITRATE, OUTPUT_BIT_RATE)

    print('Processed sampel data: \n {} \n Sample Len: {} \n'.format(sample_data, len(sample_data)))
