# tavern-interior: cozy 64x64 pixel art tavern
c = new_canvas(64, 64, background="#241610", name="tavern")

OUT = "#17100a"

# ---------------- back wall with vertical planks ----------------
c.rect(0, 0, 64, 48, "#3a2417")
for x in range(0, 64, 8):
    c.line(x, 0, x, 47, "#2e1c11")
# faint horizontal wall tone variation
c.rect(0, 28, 64, 6, "#41291a")

# ---------------- ceiling ----------------
c.rect(0, 0, 64, 3, "#1c110a")
c.line(0, 3, 63, 3, "#2a1a0e")

# ---------------- warm lamp glow on the wall (drawn before shelf) ----
for lx in (20, 44):
    c.circle(lx, 9, 7, "#463620")
    c.circle(lx, 9, 4, "#5c4628")

# ---------------- shelves + bottles ----------------
def bottle(x, ytop, body, hi):
    c.set(x + 1, ytop, "#b99a68")          # cork
    c.set(x + 1, ytop + 1, body)           # neck
    c.set(x + 1, ytop + 2, body)
    c.rect(x, ytop + 3, 3, 3, body)        # body
    c.set(x, ytop + 3, hi)                 # highlight

bcols = ["#3f6b35", "#b06a2a", "#3a5a7a", "#8a3a30", "#2c4d26", "#7a6a2a"]
for sy in (16, 26):
    c.rect(6, sy, 52, 2, "#6b4423")        # plank
    c.line(6, sy + 1, 57, sy + 1, "#4a2f1d")
    c.line(6, sy + 2, 57, sy + 2, "#241610")  # shadow under shelf
    c.set(5, sy, OUT); c.set(5, sy + 1, OUT)
    c.set(58, sy, OUT); c.set(58, sy + 1, OUT)
    ytop = sy - 6
    for i, bx in enumerate(range(8, 54, 4)):
        col = bcols[(i + (0 if sy == 16 else 3)) % len(bcols)]
        bottle(bx, ytop, col, "#6a8a55" if col.startswith("#3f") else "#c98a4a")

# ---------------- hanging lamps ----------------
for lx in (20, 44):
    c.line(lx, 3, lx, 4, "#3a2a18")        # chain
    c.line(lx - 1, 5, lx + 1, 5, "#d99a2b")
    c.line(lx - 2, 6, lx + 2, 6, "#d99a2b")
    c.line(lx - 3, 7, lx + 3, 7, "#d99a2b")
    c.line(lx - 3, 8, lx + 3, 8, "#a86f1c")  # rim shade
    c.rect(lx - 1, 9, 3, 2, "#fff3c4")     # bulb
    c.set(lx, 9, "#ffffff")

# ---------------- floor ----------------
c.rect(0, 48, 64, 16, "#2b1a10")
c.line(0, 52, 63, 52, "#1e120a")
c.line(0, 58, 63, 58, "#1e120a")
for x in (12, 34, 54):
    c.line(x, 48, x, 51, "#1e120a")
for x in (22, 44):
    c.line(x, 53, x, 57, "#1e120a")
for x in (8, 30, 52):
    c.line(x, 59, x, 63, "#1e120a")

# ---------------- bar counter ----------------
c.rect(2, 37, 60, 11, "#5f3c1f")           # front panel rows 37-47
for x in range(12, 62, 10):
    c.line(x, 37, x, 46, "#452b16")        # plank seams
c.rect(2, 45, 60, 3, "#3f2814")            # darker base rows 45-47
c.rect(2, 34, 60, 3, "#8a5a2b")            # top surface rows 34-36
c.line(2, 34, 61, 34, "#a8743a")           # lit top edge
c.line(2, 36, 61, 36, "#452b16")           # front edge of top
c.line(1, 34, 1, 47, OUT)                  # dark outline sides
c.line(62, 34, 62, 47, OUT)
c.line(2, 33, 61, 33, OUT)                 # outline above top
c.line(2, 47, 61, 47, OUT)                 # outline at base
# warm light pools on the counter under the lamps
for lx in (20, 44):
    c.rect(lx - 6, 34, 12, 1, "#c08a45")
    for dx in (-5, -2, 2, 5):
        c.set(lx + dx, 35, "#a8743a")

# ---------------- glasses, mug, bottle, candle on the counter -------
def glass(x):
    c.rect(x - 1, 29, 5, 5, OUT)
    c.rect(x, 30, 3, 3, "#b8ccd4")
    c.set(x, 30, "#e8f2f6")
    c.set(x + 1, 31, "#e8f2f6")

glass(10)
glass(30)

# mug with handle
c.rect(39, 29, 6, 5, OUT)
c.rect(40, 30, 3, 3, "#b8ccd4")
c.set(40, 30, "#e8f2f6")
c.set(43, 31, "#8fa8b2"); c.set(43, 32, "#8fa8b2")

# wine bottle on the counter
bottle(52, 28, "#2c4d26", "#4a7a3a")

# candle
c.rect(22, 31, 2, 2, "#e8e0c8")
c.set(22, 30, "#ffd257"); c.set(23, 30, "#ffd257")
c.set(22, 29, "#fff3c4")

# ---------------- barrels (right, stacked) ----------------
def draw_rows(x, y, rows, col):
    for i, (a, b) in enumerate(rows):
        c.line(x + a, y + i, x + b, y + i, col)

def barrel(x, y, rows, bands):
    n = len(rows)
    out_rows = []
    for i in range(-1, n + 1):
        a, b = rows[min(max(i, 0), n - 1)]
        out_rows.append((a - 1, b + 1))
    draw_rows(x, y - 1, out_rows, OUT)
    draw_rows(x, y, rows, "#7a4e26")
    for br in bands:
        a, b = rows[br]
        c.line(x + a, y + br, x + b, y + br, "#3a3a3a")
        c.set(x + a, y + br, "#6a6a6a")
    mid = (rows[0][0] + rows[0][1]) // 2
    for dx in (-2, 2):
        c.line(x + mid + dx, y + 1, x + mid + dx, y + n - 2, "#5a3818")
    a, b = rows[3]
    c.line(x + a + 1, y + 3, x + a + 1, y + n - 4, "#96683a")

big_rows = [(3, 8), (1, 10)] + [(0, 11)] * 8 + [(1, 10), (3, 8)]
small_rows = [(2, 7), (1, 8)] + [(0, 9)] * 6 + [(1, 8), (2, 7)]

barrel(50, 47, big_rows, (2, 9))           # bottom barrel on the floor
barrel(51, 37, small_rows, (2, 7))         # barrel stacked on top
# top surface of the upper barrel catches the lamplight
a, b = small_rows[0]
c.line(51 + a, 37, 51 + b, 37, "#96683a")

# ---------------- bar stools ----------------
def stool(cx):
    c.ellipse(cx, 61, 6, 1, "#1a0f08")     # floor shadow
    c.line(cx - 4, 46, cx - 4, 60, "#33200f")
    c.line(cx + 4, 46, cx + 4, 60, "#33200f")
    c.line(cx - 4, 54, cx + 4, 54, "#33200f")
    c.ellipse(cx, 44, 6, 3, OUT)           # seat outline
    c.ellipse(cx, 44, 5, 2, "#8a5a2b")
    c.line(cx - 3, 43, cx + 3, 43, "#a8743a")

stool(14)
stool(34)

# ---------------- smoky atmosphere ----------------
smoke = "#4a3a28"
smoke_hi = "#5f4a30"
wisps = [
    (4, 12, 8), (26, 5, 10), (50, 13, 7), (12, 22, 6),
    (36, 20, 9), (55, 24, 6), (6, 30, 7), (44, 29, 5),
]
for sx, sy, ln in wisps:
    for i in range(ln):
        if i % 3 != 2:
            c.set(sx + i, sy + (i % 4) - 1, smoke if i % 2 else smoke_hi)
# drifting motes near the lamps
for mx, my in [(16, 6), (24, 11), (40, 7), (48, 12), (30, 15), (10, 17), (56, 8)]:
    c.set(mx, my, smoke_hi)
# haze hugging the ceiling
for x in range(2, 62, 2):
    c.set(x, 4 + (x % 3), smoke)

# ---------------- inspect + deliver ----------------
print(c.stats_text())
save("tavern-interior", c)
finish(c)
