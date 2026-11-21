from pixelbench_api import new_canvas, finish

# Palette
DARK        = "#241706"  # thick dark outline / engraving
GOLD_DARK   = "#8a5f14"
GOLD_MID    = "#c8912a"
GOLD_LIGHT  = "#eec35e"
GOLD_BRIGHT = "#fbe08a"
BLUE_DARK    = "#0f3157"
BLUE_MID     = "#1b57a0"
BLUE_LIGHT  = "#4f96e0"
BLUE_BRIGHT = "#9fd0f8"
WHITE       = "#f6fbff"

c = new_canvas(32, 32)
cx, cy = 15, 15

# --- base: thick dark outline disc -------------------------------------
c.circle(cx, cy, 14, DARK)
# --- golden body (radial gradient bands) ------------------------------
c.circle(cx, cy, 12, GOLD_DARK)
c.circle(cx, cy, 10, GOLD_MID)
c.circle(cx, cy, 9, GOLD_LIGHT, fill=False)   # engraved light groove
c.circle(cx, cy, 8, DARK, fill=False)         # inner dark ring

# --- cardinal arrows on the rim ---------------------------------------
c.poly([(15, 1), (13, 5), (17, 5)], GOLD_BRIGHT)   # N (highlighted)
c.poly([(15, 29), (13, 25), (17, 25)], GOLD_LIGHT)  # S
c.poly([(29, 15), (25, 13), (25, 17)], GOLD_LIGHT)  # E
c.poly([(1, 15), (5, 13), (5, 17)], GOLD_LIGHT)     # W

# --- small diagonal tick engravings on the bright band -----------------
for (tx, ty) in [(8, 8), (22, 8), (8, 22), (22, 22)]:
    c.rect(tx, ty, 2, 2, DARK)

# --- blue crystal center (faceted diamond) ----------------------------
# 4-facet gem, light from top-left:
# top half  -> BLUE_BRIGHT (left) / BLUE_LIGHT (right)
# bottom    -> BLUE_MID (left)    / BLUE_DARK  (right)
HALF = 7
for y in range(cy - HALF, cy + HALF + 1):
    span = HALF - abs(y - cy)
    for x in range(cx - span, cx + span + 1):
        if y < cy:
            col = BLUE_BRIGHT if x <= cx else BLUE_LIGHT
        else:
            col = BLUE_MID if x <= cx else BLUE_DARK
        c.set(x, y, col)
# glint / sparkle on the lit top facet
for (sx, sy) in [(15, 10), (14, 11), (15, 11), (16, 11), (15, 12)]:
    c.set(sx, sy, WHITE)

print(c.stats_text())
print(c.matrix_text())

finish(c)
