from pixelbench_api import *

def render_bitmap(c, x0, y0, bitmap, color_map, outline_col=None, shadow_col=None, shadow_offset=(1, 2)):
    # bitmap is a list of strings, each character maps to a color in color_map
    h = len(bitmap)
    w = max(len(row) for row in bitmap)
    
    # 1. Shadow if requested
    if shadow_col:
        sx, sy = shadow_offset
        for y, row in enumerate(bitmap):
            for x, ch in enumerate(row):
                if ch != ' ':
                    # Draw shadow footprint with padding
                    c.rect(x0 + x + sx - 1, y0 + y + sy - 1, 3, 3, shadow_col)
                    
    # 2. Outline if requested
    if outline_col:
        for y, row in enumerate(bitmap):
            for x, ch in enumerate(row):
                if ch != ' ':
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            if c.get(x0 + x + dx, y0 + y + dy) != shadow_col: # or just draw
                                c.set(x0 + x + dx, y0 + y + dy, outline_col)

    # 3. Main letter pixels
    for y, row in enumerate(bitmap):
        for x, ch in enumerate(row):
            if ch != ' ' and ch in color_map:
                c.set(x0 + x, y0 + y, color_map[ch])

print("Helper defined")
