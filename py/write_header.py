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
        if style == 'SDCC':
            for i in range(len(data)):
                # f.write('{{}}, '.format(data[i]))
                s = '{' + str(data[i]) + '}, '
                f.write(s)

        else:
            f.write(','.join(str(item) for item in data))
        f.write('\n};\n'
                '#endif\n')


if __name__ == '__main__':
    # Test module
    import filereader

    sample = filereader.read_file('../include/sineData.h', startswith='const uint8_t sample_data')
    write_header('write_header_gcc.h', declaration='const uint8_t sample_data[]', data=sample)

    write_header('write_header_sdcc.h', declaration='__code const uint8_t sample_data[]', data=sample, style='SDCC')
