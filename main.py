#!/usr/bin/env python3
# http://www.dragonwins.com/domains/getteched/bmp/bmpfileformat.htm


class Bmp:
    def __init__(self, fname):
        self.fname = fname
        self.data = []

    def prepare_data(self):
        self.data = [
            [i for i in range(256)] for _ in range(128)
        ]

    def get_wh(self):
        return len(self.data[0]), len(self.data)

    def get_palette(self):
        palette = [(i + (i << 8) + (i << 16)) for i in range(256)]
        palette[1] = 0xFF0000  # Manual override
        palette[2] = 0x00FF00
        palette[3] = 0x0000FF
        return b''.join(i.to_bytes(3, 'little') + b'\x00' for i in palette)

    def get_header(self):
        width, height = self.get_wh()
        palette = self.get_palette()
        header = b'BM'
        header += (14 + width * height + 40).to_bytes(4, 'little')
        header += b'\x00\x00\x00\x00'  # reserved1, reserved2
        # Tells where the actual image data is located within the file
        header += (len(palette) + 14 + 40).to_bytes(4, 'little')
        assert len(header) == 14
        image_header = b''
        image_header += (40).to_bytes(4, 'little')  # Header Size - Must be at least 40
        image_header += width.to_bytes(4, 'little')  # Image width in pixels
        image_header += height.to_bytes(4, 'little')  # Image height in pixels
        image_header += (1).to_bytes(2, 'little')  # Must be 1
        image_header += (8).to_bytes(2, 'little')  # Bits per pixel - 1, 4, 8, 16, 24, or 32
        image_header += (0).to_bytes(4, 'little')  # Compression type (0 = uncompressed)
        image_header += (0).to_bytes(4, 'little')  # Image Size - may be zero for uncompressed images
        image_header += (2834).to_bytes(4, 'little')  # Preferred resolution in pixels per meter
        image_header += (2834).to_bytes(4, 'little')  # Preferred resolution in pixels per meter
        image_header += (0).to_bytes(4, 'little')  # Number Color Map entries that are actually used
        image_header += (0).to_bytes(4, 'little')  # Number of significant colors
        assert len(image_header) == 40
        # below size (offset) is 1078
        return header + image_header + palette

    def draw(self):
        self.prepare_data()
        header = self.get_header()
        with open(self.fname, "wb") as f:
            f.write(header)
            for line in self.data:
                b = bytes(line)
                f.write(b)


def main():
    bmp = Bmp('out.bmp')
    bmp.draw()


if __name__ == '__main__':
    main()
