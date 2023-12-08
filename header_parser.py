#!/usr/bin/env python3

import sys


class BmpHeader:
    def __init__(self):
        self.file_size = 0
        self.reserved1 = 0
        self.reserved2 = 0
        self.offset = 0

        self.img_header_size = 0
        self.width = 0
        self.height = 0
        self.planes = 0
        self.bit_count = 0
        self.compression = 0
        self.image_size = 0
        self.xpix_per_meter = 0
        self.ypix_per_meter = 0
        self.color_map = 0
        self.num_of_significant_colors = 0

    def parse(self, filename):
        with open(filename, 'rb') as f:
            bm = f.read(2)
            if bm != b'BM':
                raise Exception(F"Invalid BMP file: {filename} starts with {bm}")
            self.file_size = int.from_bytes(f.read(4), 'little')
            self.reserved1 = int.from_bytes(f.read(2), 'little')
            self.reserved2 = int.from_bytes(f.read(2), 'little')
            self.offset = int.from_bytes(f.read(4), 'little')

            self.img_header_size = int.from_bytes(f.read(4), 'little')
            self.width = int.from_bytes(f.read(4), 'little')
            self.height = int.from_bytes(f.read(4), 'little')
            self.planes = int.from_bytes(f.read(2), 'little')
            self.bit_count = int.from_bytes(f.read(2), 'little')
            self.compression = int.from_bytes(f.read(4), 'little')
            self.image_size = int.from_bytes(f.read(4), 'little')
            self.xpix_per_meter = int.from_bytes(f.read(4), 'little')
            self.ypix_per_meter = int.from_bytes(f.read(4), 'little')
            self.color_map = int.from_bytes(f.read(4), 'little')
            self.num_of_significant_colors = int.from_bytes(f.read(4), 'little')

    def get_bytes(self):
        b = b'BM'
        b += self.file_size.to_bytes(4, 'little')
        b += self.reserved1.to_bytes(2, 'little')
        b += self.reserved2.to_bytes(2, 'little')
        b += self.offset.to_bytes(4, 'little')
        b += self.img_header_size.to_bytes(4, 'little')
        b += self.width.to_bytes(4, 'little')
        b += self.height.to_bytes(4, 'little')
        b += self.planes.to_bytes(2, 'little')
        b += self.bit_count.to_bytes(2, 'little')
        b += self.compression.to_bytes(4, 'little')
        b += self.image_size.to_bytes(4, 'little')
        b += self.xpix_per_meter.to_bytes(4, 'little')
        b += self.ypix_per_meter.to_bytes(4, 'little')
        b += self.color_map.to_bytes(4, 'little')
        b += self.num_of_significant_colors.to_bytes(4, 'little')
        return b

    def __repr__(self):
        return str(self.__dict__)


def main():
    for filename in sys.argv[1:]:
        hdr = BmpHeader()
        hdr.parse(filename)
        print(hdr)


if __name__ == '__main__':
    main()
