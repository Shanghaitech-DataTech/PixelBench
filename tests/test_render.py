import io

import numpy as np
from PIL import Image

from pixelbench.core.canvas import PixelCanvas
from pixelbench.core.render import load_png_as_canvas, render_pil, render_png_bytes


def test_render_pil_sizes():
    c = PixelCanvas(8, 8)
    c.register_color("red", "#e0455a")
    c.paint_circle(4, 4, 3, "red")
    img = render_pil(c, scale=8)
    assert img.size == (64, 64)
    assert img.mode == "RGBA"
    # center pixel is red
    assert img.getpixel((32, 32))[:3] == (224, 69, 90)
    # corner is transparent
    assert img.getpixel((0, 0))[3] == 0
    grid = render_pil(c, scale=4, grid=True)
    assert grid.size == (32, 32)


def test_render_png_bytes():
    c = PixelCanvas(4, 4)
    c.register_color("blue", "#3f5fd9")
    c.paint_rect(0, 0, 4, 4, "blue")
    png = render_png_bytes(c, scale=8)
    img = Image.open(io.BytesIO(png))
    assert img.size == (32, 32)


def test_checker_background():
    c = PixelCanvas(4, 4)
    img = render_pil(c, scale=4, checker=True)
    assert img.getpixel((0, 0)) == (255, 255, 255, 255) or img.getpixel((0, 0)) == (220, 220, 220, 255)


def test_load_png_as_canvas_small_palette():
    c = PixelCanvas(8, 8)
    c.register_color("red", "#e0455a")
    c.register_color("white", "#ffffff")
    c.paint_rect(0, 0, 8, 8, "white")
    c.paint_rect(2, 2, 4, 4, "red")
    png = c.render_png_bytes(scale=1)
    c2 = load_png_as_canvas(png, max_colors=4)
    assert c2.width == 8 and c2.height == 8
    assert c2.matrix[0, 0] != c2.transparent_id
    assert c2.matrix[3, 3] != c2.matrix[0, 0]


def test_load_png_merges_colors():
    # gradient -> many colors -> merge down to 8
    img = Image.new("RGBA", (16, 16))
    px = img.load()
    for y in range(16):
        for x in range(16):
            px[x, y] = (x * 16, y * 16, 128, 255)
    c = load_png_as_canvas(img, max_colors=8)
    used = len({int(v) for v in np.unique(c.matrix) if int(v) != c.transparent_id})
    assert used <= 8


def test_load_png_resizes():
    img = Image.new("RGBA", (32, 32), (255, 0, 0, 255))
    c = load_png_as_canvas(img, width=8, height=8)
    assert c.width == 8 and c.height == 8
