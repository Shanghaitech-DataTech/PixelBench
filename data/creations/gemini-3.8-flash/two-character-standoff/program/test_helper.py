import numpy as np
from pixelbench_api import *

def render_ascii_sprite(canvas, x_offset, y_offset, ascii_art, color_map):
    lines = [line for line in ascii_art.strip().split('\n') if line]
    for dy, line in enumerate(lines):
        y = y_offset + dy
        if y < 0 or y >= 128:
            continue
        for dx, char in enumerate(line):
            x = x_offset + dx
            if x < 0 or x >= 128:
                continue
            if char in color_map and color_map[char] is not None:
                canvas.set(x, y, color_map[char])

# Let's verify this helper
c = new_canvas(128, 128)
print("Helper ready")
