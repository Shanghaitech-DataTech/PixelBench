# Green pear, 32x32, <=7 colors
c = new_canvas(32, 32, background=None, name="pear")

DARK   = c.color("#1e4d1e", "outline_dark")
MID    = c.color("#7ab648", "pear_mid")
LIGHT  = c.color("#b8d977", "pear_light")
SHADE  = c.color("#4e8a2a", "pear_shade")
STEM   = c.color("#6b4a2b", "stem_brown")
LEAF   = c.color("#3e8a2a", "leaf_green")
SPEC   = c.color("#eaf5d0", "specular")

# Body width table: row -> width (centered on x=16); narrow top, round bottom
widths = {
    8: 4, 9: 6,
    10: 6, 11: 8,
    12: 8, 13: 10,
    14: 10, 15: 12,
    16: 12, 17: 14,
    18: 14, 19: 16,
    20: 16, 21: 18,
    22: 18, 23: 18,
    24: 16, 25: 14,
    26: 10, 27: 6,
    28: 4,
}

# --- Dark silhouette first (body outline + stem + leaf outline) ---
for y, w in widths.items():
    c.rect(16 - w // 2 - 1, y, w + 2, 1, DARK)
# cap the silhouette top and bottom
c.rect(13, 7, 6, 1, DARK)
c.rect(13, 29, 6, 1, DARK)

# stem block outline (dark) with brown core drawn later
c.rect(14, 2, 4, 5, DARK)      # x14-17, y2-6
c.set(15, 1, DARK)
c.set(16, 1, DARK)

# leaf outline (dark) around a small leaf to the right
c.ellipse(21, 5, 4, 2, DARK)
# --- Body fill ---
for y, w in widths.items():
    c.rect(16 - w // 2, y, w, 1, MID)

# --- Shading: dark right side, light left side ---
for y, w in widths.items():
    L = 16 - w // 2
    R = L + w - 1
    if w >= 6:
        c.set(R, y, SHADE)
    if w >= 8:
        c.set(R - 1, y, SHADE)
    if w >= 6:
        c.set(L, y, LIGHT)
    if w >= 10:
        c.set(L + 1, y, LIGHT)
    if w >= 14:
        c.set(L + 2, y, LIGHT)
# darker belly at the very bottom
for x in range(13, 20):
    c.set(x, 27, SHADE)
c.set(14, 26, SHADE)
c.set(18, 26, SHADE)

# --- Specular glint, upper-left bulge ---
c.set(13, 13, SPEC)
c.set(14, 13, SPEC)
c.set(13, 14, SPEC)

# --- Stem core (brown) ---
c.rect(15, 3, 2, 3, STEM)      # x15-16, y3-5
c.set(15, 2, STEM)

# --- Leaf (green) over its dark outline ---
c.ellipse(21, 5, 3, 1, LEAF)
c.set(20, 4, LEAF)
c.set(20, 6, LEAF)
c.set(18, 6, LEAF)             # little stalk joining leaf to stem

print(c.stats_text())
print(c.matrix_text())

finish(c)

