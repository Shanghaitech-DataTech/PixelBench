import math
from pixelbench_api import input_canvas, finish, view

out = input_canvas.copy(name='output')

# --- colour remap: day city -> demon night ---
def lerp(c1, c2, t):
    return tuple(int(round(a + (b - a) * t)) for a, b in zip(c1, c2))

DARK   = (16, 6, 18)
PURPLE = (58, 18, 52)
RED    = (110, 24, 38)
PALE   = (156, 96, 96)

def remap(rgba):
    r, g, b, a = rgba
    if a == 0:
        return rgba
    mx, mn = max(r, g, b), min(r, g, b)
    L = mx / 255.0
    sat = 0 if mx == 0 else (mx - mn) / mx
    if r >= b:  # warm (lamps, gold, skin, fire) - keep glowing
        return (r, int(g * 0.92), int(b * 0.85), a)
    if sat < 0.25:  # whites / greys (clouds, concrete)
        t = min(1.0, L)
        return lerp((52, 30, 40), PALE, t) + (a,)
    # cool blues/cyans -> night purple-red ramp
    t = min(1.0, L * 1.15)
    if t < 0.5:
        col = lerp(DARK, PURPLE, t / 0.5)
    else:
        col = lerp(PURPLE, RED, (t - 0.5) / 0.5)
    return col + (a,)

w, h = out.to_rgba()[0], out.to_rgba()[1]
data = out.to_rgba()[2]
idx = 0
for y in range(h):
    for x in range(w):
        v = data[idx]
        rr, gg, bb, aa = (v >> 24) & 255, (v >> 16) & 255, (v >> 8) & 255, v & 255
        nr, ng, nb, na = remap((rr, gg, bb, aa))
        if (nr, ng, nb, na) != (rr, gg, bb, aa):
            out.set(x, y, (nr, ng, nb, na))
        idx += 1

# --- blood moon ---
MOON_X, MOON_Y, R = 62, 34, 24
core    = (196, 30, 40)
shade   = (140, 18, 30)
deep    = (96, 10, 22)
rim     = (232, 84, 72)
glow1   = (120, 26, 40)
glow2   = (70, 16, 34)

for gy in range(MOON_Y - R - 6, MOON_Y + R + 7):
    for gx in range(MOON_X - R - 6, MOON_X + R + 7):
        d = math.hypot(gx - MOON_X, gy - MOON_Y)
        if d <= R:
            t = ((gx - MOON_X) + (gy - MOON_Y)) / (2.0 * R)
            col = lerp(core, deep, max(0.0, min(1.0, (t + 0.6) / 1.4)))
            out.set(gx, gy, col)
        elif d <= R + 2:
            out.set(gx, gy, rim if d <= R + 1 else glow1)
        elif d <= R + 4:
            out.set(gx, gy, glow1)
        elif d <= R + 6:
            out.set(gx, gy, glow2)

# craters / scars on the moon
for cx, cy, cr in [(54, 26, 4), (70, 40, 5), (60, 46, 3), (72, 24, 3), (50, 40, 2)]:
    out.circle(cx, cy, cr, shade)
out.circle(70, 40, 2, deep)
out.circle(54, 26, 2, deep)

# --- demon castle spires ---
tower = (24, 8, 20)
dark  = (12, 4, 12)
win   = (255, 60, 50)
win2  = (180, 30, 30)

def spire(x, base_y, top_y, half_w):
    for y in range(top_y, base_y):
        t = (y - top_y) / max(1, base_y - top_y)
        hw = max(1, int(round(half_w * (0.35 + 0.65 * t))))
        for xx in range(x - hw, x + hw + 1):
            out.set(xx, y, tower if xx > x - hw else dark)
    for i, y in enumerate(range(top_y - 10, top_y)):
        hw = max(0, half_w - i // 2 - 1)
        for xx in range(x - hw, x + hw + 1):
            out.set(xx, y, tower)
    out.set(x, top_y - 11, win)

spire(18, 128, 70, 7)
spire(238, 128, 62, 8)
spire(210, 128, 88, 5)

for sx, sy in [(18, 80), (18, 96), (18, 112), (238, 74), (238, 92), (238, 110), (210, 100), (210, 116)]:
    out.set(sx, sy, win)
    out.set(sx, sy + 1, win2)

# bats / embers in the sky
for bx, by in [(120, 20), (150, 34), (100, 44), (170, 16)]:
    out.set(bx, by, dark)
    out.set(bx - 1, by - 1, dark)
    out.set(bx + 1, by - 1, dark)

print(out.stats_text())
print(out.matrix_text(region=(50, 25, 75, 45)))
finish(out)
