from pixelbench_api import *
from collections import Counter

c = input_canvas.copy(name="probe")
pal = c.palette()
rgba = {e['index']: e['rgba'] for e in pal}
W, H = 250, 147

def cls(i):
    r, g, b, a = rgba[i]
    L = 0.299*r + 0.587*g + 0.114*b
    mx, mn = max(r, g, b), min(r, g, b)
    if L < 55:
        return 'F' if b < r - 6 else 'm'   # forest / dark mountain
    if mx - mn < 35 and L > 180:
        return 'O'                          # moon
    if r - b > 45:
        return 'A'                          # warm accent (snow/cloud)
    if L >= 100:
        return '.'                          # sky
    return 'M'                              # mountain

# class map per column segments
import sys
grid = [[cls(c.get(x, y)) for x in range(W)] for y in range(H)]

# downsampled overview: every 2 cols, every 2 rows -> char majority
print("overview (2x2 blocks, cols 0-249 rows 0-146):")
for y0 in range(0, H, 3):
    line = ""
    for x0 in range(0, W, 2):
        cnt = Counter()
        for dy in range(3):
            for dx in range(2):
                if y0+dy < H and x0+dx < W:
                    cnt[grid[y0+dy][x0+dx]] += 1
        line += cnt.most_common(1)[0][0]
    print("%3d %s" % (y0, line))
