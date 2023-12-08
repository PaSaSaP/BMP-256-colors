#!/usr/bin/env python3
import os
import sys
from header_parser import BmpHeader


def main():
    if len(sys.argv) < 3:
        print("usage: {} <input file> <output file>".format(sys.argv[0]))
        sys.exit(1)
    hdr = BmpHeader()
    hdr.parse(sys.argv[1])
    print(hdr)
    if hdr.bit_count != 16:
        print("it is not bmp565...")
        sys.exit(1)
    with open(sys.argv[1], "rb") as input_file:
        with open(sys.argv[2], "wb") as output_file:
            header_data = input_file.read(hdr.offset)
            output_file.write(header_data)
            input_file.seek(0, os.SEEK_END)
            file_size = input_file.tell()
            input_file.seek(hdr.offset, os.SEEK_SET)
            while input_file.tell() < file_size:
                d = input_file.read(2)
                d = d[1:2] + d[0:1]
                output_file.write(d)


if __name__ == '__main__':
    main()

