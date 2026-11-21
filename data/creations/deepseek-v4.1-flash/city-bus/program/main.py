W, H = 64, 32

c = new_canvas(W, H, background=None, name="bus")

PAL = {
    "body":    "#EFF4F8",
    "body_sh": "#D3DEE7",
    "body_dk": "#B4C1CC",
    "roof":    "#C5D1DB",
    "roof_dk": "#9FAAB5",
    "glass":   "#1B2A37",
    "glass2":  "#2C4657",
    "glass3":  "#5F93B4",
    "frame":   "#39454F",
    "dframe":  "#4E5D6B",
    "dglass":  "#22333F",
    "accent":  "#0F8A91",
    "accent2": "#2CC3C9",
    "tyre":    "#15191D",
    "hub":     "#A6B2BD",
    "hub_dk":  "#5E6A76",
    "amber":   "#FFC24B",
    "head":    "#FFF6D2",
    "tail":    "#DB3A31",
    "sign":    "#0A0E12",
    "line":    "#2E3840",
    "well":    "#4A5763",
}
for n, v in PAL.items():
    c.color(v, name=n)

# ---------------- body shell ----------------
c.rect(2, 5, 60, 23, "body")          # x2..61  y5..27

# roof band
c.rect(3, 5, 58, 3, "roof")

# roof equipment (air-con / battery pod)
c.rect(24, 2, 11, 3, "roof_dk")
c.rect(25, 2, 9, 1, "roof")
c.set(27, 4, "line")
c.set(30, 4, "line")

# ---------------- windows ----------------
def win(x, y, w, h):
    c.rect(x, y, w, h, "glass")
    c.rect(x, y, w, 1, "glass2")          # top reflection
    c.rect(x + 1, y + 1, 1, 4, "glass3")  # vertical glint
    c.rect(x + 2, y + 5, 1, 2, "glass2")
    c.rect(x, y + h - 1, w, 1, "glass2")  # sill reflection

wy, wh = 10, 9
win(8, wy, 7, wh)
win(16, wy, 7, wh)
win(34, wy, 7, wh)
win(42, wy, 6, wh)

# windscreen / driver glass at the front (raked top corner)
c.rect(56, 11, 5, 8, "glass")
c.rect(57, 10, 4, 1, "glass2")
c.rect(57, 11, 1, 4, "glass3")
c.rect(58, 15, 1, 2, "glass2")
c.rect(56, 18, 5, 1, "glass2")

# ------------- livery stripe -------------
c.rect(3, 19, 58, 1, "accent2")
c.rect(3, 20, 58, 2, "accent")
c.rect(3, 22, 58, 1, "body_sh")

# ------------- skirt -------------------
c.rect(3, 26, 58, 2, "body_sh")

# ---------------- doors ----------------
def door(x, w=7, y0=10, y1=25):
    c.rect(x, y0, w, y1 - y0 + 1, "dframe")
    c.rect(x + 1, y0 + 1, w - 2, y1 - y0 - 2, "dglass")
    c.rect(x + w // 2, y0 + 1, 1, y1 - y0 - 3, "dframe")
    c.rect(x + 1, y0 + 1, w - 2, 1, "glass2")
    c.rect(x + 1, y1 - 1, w - 2, 1, "body_sh")

door(24)
door(49)

# ---------------- wheels ----------------
def wheel(cx, cy):
    for dy in range(-5, 3):
        for dx in range(-5, 6):
            if dx * dx + dy * dy <= 17:
                x, y = cx + dx, cy + dy
                if 0 <= x < W and y <= 27:
                    c.set(x, y, "well")
    c.circle(cx, cy, 3, "tyre")
    c.circle(cx, cy, 1, "hub_dk")
    c.set(cx, cy, "hub")

wheel(14, 27)
wheel(44, 27)

# ---------------- electronic route display ----------------
c.rect(45, 7, 14, 3, "sign")
for y in (7, 8, 9):
    c.set(48, y, "amber")                                    # "1"
c.set(51, 7, "amber"); c.set(52, 7, "amber"); c.set(53, 7, "amber")
c.set(53, 8, "amber")                                        # "2"
c.set(51, 9, "amber"); c.set(52, 9, "amber"); c.set(53, 9, "amber")
c.set(55, 8, "amber"); c.set(56, 7, "amber"); c.set(56, 9, "amber")
c.set(57, 8, "amber")                                        # destination text

# ---------------- front / rear lights ----------------
c.rect(56, 22, 5, 4, "frame")            # headlight housing
c.rect(57, 23, 3, 2, "head")

c.rect(2, 19, 5, 1, "frame")             # tail light housing
c.rect(2, 24, 5, 1, "frame")
c.rect(3, 20, 2, 4, "tail")

c.rect(56, 26, 5, 1, "body_dk")          # front bumper
c.rect(2, 26, 5, 1, "body_dk")           # rear bumper

# extra body panel detail
c.rect(18, 23, 4, 2, "body_sh")          # charge flap
c.set(20, 23, "body_dk")

# ---------------- silhouette clean-up ----------------
for p in [(2, 5), (3, 5), (2, 6), (60, 5), (61, 5), (61, 6), (2, 27), (61, 27)]:
    c.set(p[0], p[1], None)

c.outline("line")

print(c.stats_text())
print(c.matrix_text())
save("citybus", c)
finish(c)
