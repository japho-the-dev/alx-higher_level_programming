#!/usr/bin/python3
for decimal_num in range(0, 99):
    hex_representation = '0x{:x}'.format(decimal_num)
    print('{} = {}'.format(decimal_num, hex_representation))