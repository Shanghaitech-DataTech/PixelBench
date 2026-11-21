import random
random.seed(7)

out = input_canvas.copy(name='output')

# register purple palette
dark_p = out.color('#5b2a86', name='potion_dark')
mid_p  = out.color('#8b4bb8', name='potion_mid')
light_p= out.color('#b07de0', name='potion_light')
hi_p   = out.color('#d9b3ff', name='potion_highlight')
# map existing water colours to purples
mapping = {
    5: dark_p,   # e dark blue
    6: mid_p,    # f light blue
    7: mid_p,    # g
    8: mid_p,    # h
    10: mid_p,   # j
    9: dark_p,   # i dark spot
}
w, h = 64, 64
for y in range(h):
    for x in range(w):
        idx = out.get(x, y)
        if idx in mapping:
            out.set(x, y, mapping[idx])

# find water pixels (now purple) to place bubbles inside
purple = {dark_p, mid_p}
pts = [(x, y) for y in range(h) for x in range(w) if out.get(x, y) in purple]

def bubble(cx, cy, r, body, rim):
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            d2 = dx * dx + dy * dy
            if d2 <= r * r:
                col = rim if d2 > (r - 1) ** 2 else body
                out.set(cx + dx, cy + dy, col)
    # tiny highlight
    out.set(cx - r + 1, cy - r + 1, hi_p)

# bubbles: a few big ones near the bottom, small ones rising
big = [(14, 52, 3), (30, 55, 4), (44, 50, 3), (22, 44, 2), (38, 42, 2),
       (10, 42, 2), (48, 40, 2), (28, 34, 2), (16, 30, 1), (40, 30, 1),
       (24, 27, 1), (34, 26, 1), (50, 34, 1), (8, 34, 1)]
for cx, cy, r in big:
    body = light_p if r >= 2 else hi_p
    bubble(cx, cy, r, body, mid_p if r >= 3 else light_p)

print(out.stats_text())
finish(out)
