import sys
from pixelbench_api import new_canvas, view, save, finish

def parse_sprite(ascii_art, color_map):
    lines = [line.strip() for line in ascii_art.strip().splitlines()]
    h = len(lines)
    w = max(len(line) for line in lines)
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            char = lines[y][x] if x < len(lines[y]) else '.'
            row.append(color_map.get(char, None))
        grid.append(row)
    return grid, w, h

def blit_grid(c, grid, ox, oy):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col is not None:
                c.set(ox + x, oy + y, col)
