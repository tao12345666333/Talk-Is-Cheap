#!/usr/bin/env python
# coding=utf-8
import sys

from PIL import Image, ImageDraw, ImageFont


def main():
    # This function is to write text on the picture.

    pic_path = sys.argv[1]
    try:
        pic = Image.open(pic_path)
    except:
        return

    x, y = pic.size
    pic_draw = ImageDraw.Draw(pic)
    font_size = int(min(x, y) * 0.1)

    try:
        font = ImageFont.truetype(font='Hack-Bold.ttf', size=font_size)
    except:
        return

    pic_draw.text(
        [x * 0.9, y * 0.1 - font_size], '1', fill=(255, 0, 0), font=font)

    del pic_draw
    pic.save('finally.jpg')


if __name__ == '__main__':
    main()
