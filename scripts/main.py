from PIL import Image, ImageDraw
from math import log, log2
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from datetime import datetime


MAX_ITER = 50

WIDTH = 2**5
HEIGHT = int(3 * WIDTH / 4)

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


def filename_generator(size: int=18, chars: str=ascii_lowercase + ascii_uppercase + digits) -> str:
    return ''.join(choice(chars) for _ in range(size))

def mandelbrot(z: complex) -> int:
    c = z
    for n in range(MAX_ITER):
        if abs(z) > 2:
            return n + 1 - log(log2(abs(z)))
        z = z * z + c
    return MAX_ITER

def generate_image() -> None:
    start_date = datetime.now()

    image = Image.new('HSV', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    for x in range(WIDTH):
        print(f'[{datetime.now().isoformat()}] Image drawing: {round(x / WIDTH * 100, 2)} %')

        for y in range(HEIGHT):
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            m = mandelbrot(c)

            r = int(255 * m / MAX_ITER)
            g = 255
            b = 255 if m < MAX_ITER else 0

            draw.point([x, y], (r, g, b))

    image.convert('RGB').save(f'img/{WIDTH}x{HEIGHT}_{MAX_ITER}_{filename_generator()}.png')
    image.show()

    print()
    print(f'Start date: {start_date.isoformat()}')
    print(f'End date: {datetime.now().isoformat()}')
    print(f'Program took: {datetime.now() - start_date} to run')


if __name__ == "__main__":
    generate_image()
