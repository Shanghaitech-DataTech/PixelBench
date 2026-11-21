from pixelbench_api import *

c = input_canvas
output = c.copy(name='output')

# Potion palette.
purple_dark   = output.color('#3f1f6e', name='potion_dark')
purple_mid    = output.color('#6f3fa8', name='potion_mid')
purple_light  = output.color('#a97cd9', name='potion_light')
purple_light2 = output.color('#bd97e8', name='potion_light2')
purple_light3 = output.color('#d0b4f2', name='potion_light3')
bubble_rim    = output.color('#3a1d63', name='bubble_rim')
bubble_fill   = output.color('#e6d7fc', name='bubble_fill')
bubble_shine  = output.color('#ffffff')

# Recolour the original blue water shades to purple potion shades.
blue_map = {5: purple_dark, 6: purple_mid, 7: purple_light, 8: purple_light2, 10: purple_light3}
water = set(blue_map.keys())

for y in range(64):
    for x in range(64):
        i = c.get(x, y)
        if i in blue_map:
            output.set(x, y, blue_map[i])

# Bubble candidates inside the liquid (cx, cy, radius).
candidates = [
    (18, 29, 1), (25, 28, 2), (34, 31, 1), (42, 29, 1), (46, 32, 1),
    (12, 34, 1), (30, 35, 2), (38, 36, 1), (22, 33, 1),
    (14, 40, 1), (46, 40, 1), (24, 45, 2), (34, 44, 1), (42, 46, 1),
    (16, 48, 1), (30, 47, 2), (38, 49, 1), (12, 50, 1), (44, 51, 2),
    (22, 52, 1), (33, 54, 2), (18, 56, 1), (40, 56, 1), (27, 58, 1),
    (36, 59, 1),
]

def fits(cx, cy, r):
    r2 = r * r
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy > r2:
                continue
            x = cx + dx
            y = cy + dy
            if x < 0 or y < 0 or x > 63 or y > 63:
                return False
            if c.get(x, y) not in water:
                return False
    return True

chosen = []
for cx, cy, r in candidates:
    if not fits(cx, cy, r):
        continue
    # Keep bubbles from crowding each other.
    ok = True
    for ox, oy, orr in chosen:
        if (cx - ox) ** 2 + (cy - oy) ** 2 < (r + orr + 1) ** 2:
            ok = False
            break
    if ok:
        chosen.append((cx, cy, r))

# Draw the bubbles.
for cx, cy, r in chosen:
    output.circle(cx, cy, r, bubble_fill, fill=True)
    output.circle(cx, cy, r, bubble_rim, fill=False)
    if r <= 1:
        output.set(cx, cy, bubble_shine)
    else:
        output.set(cx - 1, cy - 1, bubble_shine)
        output.set(cx, cy - 1, bubble_shine)

finish(output)
