#!/usr/bin/env python
# coding: utf-8

import math


def twos_complement(input_value: int) -> int:
    """Calculates a two's complement integer from the given input value's bits."""
    if input_value > 0x7FFF:
        return input_value - 0x8000
    else:
        return abs(~input_value) + 0x7FFF


table = []
table_len = 128
max_int = 0xFFFF
for i in range(table_len):
    print('{:04x}'.format(int((math.sin(2 * math.pi * i / table_len) + 1) / 2 * max_int)), end=' => ')
    table.append(
        twos_complement(int((math.sin(2 * math.pi * i / table_len) + 1) / 2 * max_int))
    )
    print('{:04x}'.format(twos_complement(int((math.sin(2 * math.pi * i / table_len) + 1) / 2 * max_int))))

for n in table:
    print('  0x{:04x},'.format(int(n)))
