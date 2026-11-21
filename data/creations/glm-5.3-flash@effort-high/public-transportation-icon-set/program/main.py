# Public transportation icon set - 64x64, 2x2 grid
# bus (TL), subway (TR), bicycle (BL), pedestrian (BR)

BG     = "#D8E1EA"   # light blue-grey sheet background
WHITE  = "#FFFFFF"   # tile face
DARK   = "#2B3A4A"   # line weight / ink
ACCENT = "#E8A33D"   # glass + lights

c = new_canvas(64, 64, background=BG, name="transport_icons")


def tile(ox, oy):
    """Consistent framing: 28x28 rounded tile inside each 32x32 cell."""
    c.rect(ox + 2, oy + 2, 28, 28, DARK, fill=False)   # 1px border
    c.rect(ox + 3, oy + 3, 26, 26, WHITE, fill=True)   # face
    for px, py in [(ox + 2, oy + 2), (ox + 29, oy + 2),
                   (ox + 2, oy + 29), (ox + 29, oy + 29)]:
        c.set(px, py, BG)                              # round the corners


def tline(x0, y0, x1, y1, col=DARK):
    """2px line weight: the stroke plus one row below."""
    c.line(x0, y0, x1, y1, col)
    c.line(x0, y0 + 1, x1, y1 + 1, col)


# ---------------- bus (top-left) ----------------
def bus(ox, oy):
    x, y = ox, oy
    c.rect(x + 7, y + 9, 18, 12, DARK, fill=True)      # body
    c.rect(x + 9, y + 11, 14, 8, WHITE, fill=True)     # face
    c.rect(x + 10, y + 12, 5, 4, ACCENT, fill=True)    # front window
    c.rect(x + 17, y + 12, 5, 4, ACCENT, fill=True)    # rear window
    c.set(x + 22, y + 17, ACCENT)                      # headlight
    c.circle(x + 11, y + 22, 2, DARK, fill=True)       # wheels
    c.circle(x + 21, y + 22, 2, DARK, fill=True)


# ---------------- subway (top-right) ----------------
def subway(ox, oy):
    x, y = ox, oy
    c.rect(x + 9, y + 6, 14, 16, DARK, fill=True)      # car body
    c.rect(x + 11, y + 8, 10, 12, WHITE, fill=True)    # face
    c.rect(x + 12, y + 9, 8, 5, ACCENT, fill=True)     # windshield
    c.set(x + 12, y + 17, ACCENT)                      # headlights
    c.set(x + 19, y + 17, ACCENT)
    c.rect(x + 11, y + 22, 3, 2, DARK, fill=True)      # bogies
    c.rect(x + 18, y + 22, 3, 2, DARK, fill=True)
    c.rect(x + 8, y + 25, 16, 2, DARK, fill=True)      # track


# ---------------- bicycle (bottom-left) ----------------
def bicycle(ox, oy):
    x, y = ox, oy
    for cx in (10, 22):                                # wheels: 1px rings
        c.circle(x + cx, y + 20, 5, DARK, fill=False)
    c.line(x + 10, y + 20, x + 13, y + 12, DARK)             # chain stay
    c.line(x + 13, y + 12, x + 16, y + 20, DARK)             # seat tube
    c.line(x + 16, y + 20, x + 10, y + 20, DARK)             # bottom bracket
    c.line(x + 13, y + 12, x + 20, y + 13, DARK)             # top tube
    c.line(x + 20, y + 13, x + 22, y + 20, DARK)             # fork
    c.line(x + 20, y + 13, x + 16, y + 20, DARK)             # down tube
    c.line(x + 11, y + 10, x + 15, y + 10, DARK)             # saddle
    c.line(x + 20, y + 13, x + 21, y + 10, DARK)             # stem
    c.line(x + 19, y + 9, x + 23, y + 9, DARK)               # handlebar


# ---------------- pedestrian (bottom-right) ----------------
def pedestrian(ox, oy):
    x, y = ox, oy
    c.circle(x + 16, y + 8, 2, DARK, fill=True)        # head
    c.line(x + 16, y + 11, x + 15, y + 17, DARK)             # torso
    c.line(x + 16, y + 12, x + 12, y + 15, DARK)             # back arm
    c.line(x + 16, y + 12, x + 20, y + 14, DARK)             # front arm
    c.line(x + 15, y + 17, x + 12, y + 23, DARK)             # back leg
    c.line(x + 15, y + 17, x + 19, y + 22, DARK)             # front leg
    c.set(x + 11, y + 24, DARK); c.set(x + 12, y + 24, DARK)   # feet
    c.set(x + 19, y + 23, DARK); c.set(x + 20, y + 23, DARK)


cells = [(0, 0, bus), (32, 0, subway), (0, 32, bicycle), (32, 32, pedestrian)]
for ox, oy, icon in cells:
    tile(ox, oy)
    icon(ox, oy)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

save("transport_icons", c, indexed=True)
finish(c)
