def convert(data):
    """
    :param data: A List of python integers
    :return: A List of python integers converted to twos complement
    """
    out = []
    for datum in data:
        out.append(__twos_complement(datum))
    return out


def __twos_complement(input_value: int, max_value=0x7F) -> int:
    """Calculates a two's complement integer from the given input value's bits."""
    if input_value > max_value:  # if input_value > 0x7F
        return input_value - (max_value + 1)  # return input_value - 0x80
    else:
        return abs(~input_value) + max_value  # return abs(~input_value) + 0x7F
