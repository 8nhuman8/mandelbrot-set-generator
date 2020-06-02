from PIL import Image, ImageDraw

from math import log, log2
from datetime import datetime

from utils import generate_filename, get_runtime


ITERS = 50

WIDTH = 2**10
HEIGHT = int(3 * WIDTH / 4)

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


def mandelbrot(z: complex) -> int:
    c = z
    for n in range(ITERS):
        if abs(z) > 2:
            return n + 1 - log(log2(abs(z)))
        z = z * z + c
    return ITERS


if __name__ == "__main__":
    start_date = datetime.now()

    image = Image.new('HSV', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    for x in range(WIDTH):
        print(f'[{datetime.now().time()}]', 'Image drawing:', f'{round(x / WIDTH * 100, 5)} %', sep='\t')
        for y in range(HEIGHT):
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            m = mandelbrot(c)

            r = int(255 * m / ITERS)
            g = 255
            b = 255 if m < ITERS else 0

            draw.point([x, y], (r, g, b))

    image.convert('RGB').save(f'img/{WIDTH}x{HEIGHT}_{ITERS}_{generate_filename()}.png')
    image.show()

    get_runtime(start_date)
