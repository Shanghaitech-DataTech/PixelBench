out = input_canvas.copy(name='output')

# --- 1. Recolor the water into purple potion tones -------------------
# original water palette indices (from legend):
#  5 = #2f7598 dark blue   6 = #74b8cf   7 = #77b7ce
#  8 = #76b7d1            9 = #31121d dark band  10 = #7bb5cb
DEEP  = out.color('#6a2fa3')   # deep violet  (was dark blue)
LAV   = out.color('#a86ce8')   # bright lavender (was light blue)
LAV2  = out.color('#9a58d6')   # slightly deeper lavender
DARKP = out.color('#2a0b45')   # near-black purple (was #31121d)

mapping = {5: DEEP, 6: LAV, 7: LAV2, 8: LAV, 9: DARKP, 10: LAV2}
WATER = set(mapping.keys())

for y in range(64):
    for x in range(64):
        idx = out.get(x, y)
        if idx in mapping:
            out.set(x, y, mapping[idx])
WATER = {5, 6, 7, 8, 9, 10}   # original water indices, captured before recolor

# --- 2. Bubbles inside the potion (only painted over potion) ---------
WATER = {DEEP, LAV, LAV2, DARKP}   # potion indices after the recolor
BUB1 = out.color('#d9b0ff')
BUB2 = out.color('#f2dcff')

def bubble(cx, cy, r, col):
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r:
                x, y = cx + dx, cy + dy
                if 0 <= x < 64 and 0 <= y < 64 and out.get(x, y) in WATER:
                    out.set(x, y, col)

for cx, cy, r, col in [
    (14, 34, 2, BUB1), (30, 32, 1, BUB2), (41, 37, 2, BUB1),
    (22, 44, 2, BUB2), (36, 49, 1, BUB1), (12, 51, 1, BUB2),
    (28, 55, 2, BUB1), (44, 53, 1, BUB2), (19, 39, 1, BUB1),
    (33, 41, 1, BUB2), (25, 29, 1, BUB1), (47, 45, 1, BUB1),
    (9, 43, 1, BUB2), (20, 57, 1, BUB1),
]:
    bubble(cx, cy, r, col)

# --- 3. Bubbles escaping above the tilted mouth ----------------------
out.circle(26, 8, 2, LAV, fill=False)
out.circle(33, 5, 1, LAV2, fill=False)
out.circle(22, 4, 1, LAV, fill=False)
out.circle(37, 9, 1, LAV2, fill=False)
out.set(29, 2, BUB1)
out.set(18, 7, BUB2)
out.set(40, 3, BUB2)

# --- 4. Tiny sparkles around the bottle ------------------------------
def sparkle(cx, cy, col):
    out.set(cx, cy, col)
    out.set(cx - 1, cy, col); out.set(cx + 1, cy, col)
    out.set(cx, cy - 1, col); out.set(cx, cy + 1, col)

sparkle(8, 14, BUB2)
sparkle(46, 20, BUB1)
sparkle(58, 30, BUB2)
sparkle(57, 44, BUB1)

# --- 5. Bubbles rising in the neck (over the deep violet) ------------
for cx, cy, r, col in [(35, 24, 1, BUB2), (32, 20, 1, BUB1), (36, 16, 1, BUB2)]:
    bubble(cx, cy, r, col)

for cx, cy, r, col in [(24, 22, 1, BUB2), (21, 19, 1, BUB1), (27, 17, 1, BUB2)]:
    bubble(cx, cy, r, col)

print(out.stats_text())

finish(out)
