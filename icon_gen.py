#! /usr/bin/env python3

import argparse
from PIL import Image

ICON_SIZE = 16, 16
COLOR_BYTES = 3


def main(args):
    with Image.open(args.input) as im:
        data = []
        im = im.resize(ICON_SIZE)
        im.convert("RGB")
        for x in range(ICON_SIZE[0]):
            for y in range(ICON_SIZE[1]):
                real_y = 15 - y if x % 2 else y
                data.extend(im.getpixel((x, real_y))[0:COLOR_BYTES])
        byte_data = bytearray(data)
        print(byte_data)
        if args.save_thumb:
            im.save(args.input + ".thumb.png", "png")
        if args.out_file:
            with open(args.out_file, "w") as out:
                out.write("icon = ")
                out.write(repr(byte_data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate 16x16 icon from image in iconically format"
    )
    parser.add_argument("input")
    parser.add_argument("--out_file")
    parser.add_argument("--save_thumb", action="store_true")
    args = parser.parse_args()

    main(args)
