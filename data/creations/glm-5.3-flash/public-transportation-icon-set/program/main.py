# Public transportation icon set - 64x64, consistent 2x2 grid
# Tiles: 30x30 rounded squares, 2px gutters, 1px outer margin.
# Icons: 24x24 design box centred in each tile, shared 1px line weight,
#        shared palette, shared optical baseline (ink centred on y~12).

W = H = 64

BG     = "#C9D3DF"   # canvas background - cool grey blue
TILE   = "#FFFFFF"   # icon tile fill
BORDER = "#22303F"   # dark navy - frames and all line work
GLASS  = "#A9D6F5"   # window glass
ACCENT = "#2E7CC4"   # livery blue stripe
YELLOW = "#F5B841"   # lights
GRAY   = "#8A97A6"   # wheel hubs

c = new_canvas(W, H, background=BG, name="public-transport-icons")

TILES = [(1, 1), (33, 1), (1, 33), (33, 33)]


def draw_tile(cx, cy):
    """30x30 rounded tile frame, identical for all four icons."""
    c.rect(cx, cy, 30, 30, BORDER)
    c.rect(cx + 1, cy + 1, 28, 28, TILE)
    for ax, ay in ((0, 0), (1, 0), (0, 1)):
        for px, py in ((ax, ay), (29 - ax, ay), (ax, 29 - ay), (29 - ax, 29 - ay)):
            c.set(cx + px, cy + py, BG)   # rounded corner reveals the page


def wheel5(cx, cy):
    """5px octagonal wheel with a hub dot (bus)."""
    c.rect(cx - 1, cy - 2, 3, 5, BORDER)
    c.rect(cx - 2, cy - 1, 5, 3, BORDER)
    c.set(cx, cy, GRAY)


def wheel9(cx, cy):
    """9px closed ring (bicycle)."""
    c.circle(cx, cy, 4, BORDER, fill=False)
    c.set(cx, cy - 3, BORDER)   # close the engine's top-centre gap
    c.set(cx, cy + 3, BORDER)   # close the engine's bottom-centre gap


# ---------------------------------------------------------------- bus (side)
def draw_bus(ox, oy):
    c.rect(ox + 2, oy + 5, 20, 12, BORDER)    # body block   x2..21  y5..16
    c.rect(ox + 3, oy + 6, 18, 10, TILE)      # body fill    x3..20  y6..15
    c.rect(ox + 4, oy + 8, 4, 4, GLASS)       # window 1
    c.rect(ox + 9, oy + 8, 4, 4, GLASS)       # window 2
    c.rect(ox + 15, oy + 8, 5, 4, GLASS)      # door bay x15..19
    c.rect(ox + 17, oy + 8, 1, 4, BORDER)     # door split -> 2 + 2 leaves
    c.rect(ox + 3, oy + 12, 18, 1, ACCENT)    # livery stripe
    c.rect(ox + 4, oy + 13, 2, 2, YELLOW)     # rear light
    c.rect(ox + 18, oy + 13, 2, 2, YELLOW)    # front light
    wheel5(ox + 6, oy + 17)
    wheel5(ox + 17, oy + 17)


# ------------------------------------------------------------- subway (front)
def draw_subway(ox, oy):
    c.rect(ox + 8, oy + 4, 8, 1, BORDER)      # roof cap     x8..15  y4
    c.rect(ox + 6, oy + 5, 12, 2, BORDER)     # shoulders    x6..17  y5..6
    c.rect(ox + 5, oy + 7, 14, 10, BORDER)    # body         x5..18  y7..16
    c.rect(ox + 7, oy + 5, 10, 1, TILE)       # inner shoulder
    c.rect(ox + 6, oy + 7, 12, 9, TILE)       # inner body   x6..17  y7..15
    c.rect(ox + 7, oy + 6, 10, 6, GLASS)      # windshield   x7..16  y6..11
    c.rect(ox + 9, oy + 7, 6, 1, TILE)        # destination sign
    c.rect(ox + 6, oy + 12, 12, 1, ACCENT)    # livery stripe
    c.rect(ox + 7, oy + 13, 2, 2, YELLOW)     # left light
    c.rect(ox + 15, oy + 13, 2, 2, YELLOW)    # right light
    c.rect(ox + 7, oy + 16, 3, 3, BORDER)     # bogie wheel L
    c.rect(ox + 14, oy + 16, 3, 3, BORDER)    # bogie wheel R
    c.rect(ox + 3, oy + 19, 18, 2, BORDER)    # track


# ------------------------------------------------------------------ bicycle
def draw_bike(ox, oy):
    wheel9(ox + 5, oy + 15)                            # rear wheel
    wheel9(ox + 18, oy + 15)                           # front wheel
    c.line(ox + 5, oy + 15, ox + 11, oy + 15, BORDER)  # chainstay
    c.line(ox + 8, oy + 7, ox + 5, oy + 15, BORDER)    # seat stay
    c.line(ox + 11, oy + 15, ox + 8, oy + 7, BORDER)   # seat tube
    c.line(ox + 8, oy + 7, ox + 16, oy + 7, BORDER)    # top tube
    c.line(ox + 16, oy + 7, ox + 11, oy + 15, BORDER)  # down tube
    c.line(ox + 16, oy + 7, ox + 18, oy + 15, BORDER)  # fork
    c.rect(ox + 10, oy + 14, 3, 3, BORDER)             # chainring
    c.rect(ox + 6, oy + 5, 5, 1, BORDER)               # saddle
    c.line(ox + 8, oy + 6, ox + 8, oy + 7, BORDER)     # seat post
    c.line(ox + 14, oy + 5, ox + 18, oy + 5, BORDER)   # handlebar
    c.line(ox + 16, oy + 5, ox + 16, oy + 7, BORDER)   # stem


# --------------------------------------------------------------- pedestrian
def draw_person(ox, oy):
    c.rect(ox + 12, oy + 2, 3, 5, BORDER)              # head (octagon)
    c.rect(ox + 11, oy + 3, 5, 3, BORDER)
    c.line(ox + 13, oy + 7, ox + 12, oy + 14, BORDER)  # torso
    c.line(ox + 13, oy + 8, ox + 17, oy + 12, BORDER)  # front arm
    c.line(ox + 13, oy + 8, ox + 9, oy + 12, BORDER)   # back arm
    c.line(ox + 12, oy + 14, ox + 16, oy + 21, BORDER)  # front leg
    c.line(ox + 16, oy + 21, ox + 18, oy + 21, BORDER)  # front foot
    c.line(ox + 12, oy + 14, ox + 8, oy + 21, BORDER)   # back leg
    c.line(ox + 6, oy + 21, ox + 8, oy + 21, BORDER)    # back foot


for (cx, cy), icon in zip(TILES, (draw_bus, draw_subway, draw_bike, draw_person)):
    draw_tile(cx, cy)
    icon(cx + 3, cy + 3)

print(c.stats_text())
save("public-transport-icons", c)

INSPECT = 1
if INSPECT:
    def ranges(cols):
        out, start, prev = [], None, None
        for x in sorted(cols):
            if start is None:
                start = prev = x
            elif x == prev + 1:
                prev = x
            else:
                out.append(f"{start}-{prev}" if prev > start else f"{start}")
                start = prev = x
        if start is not None:
            out.append(f"{start}-{prev}" if prev > start else f"{start}")
        return ",".join(out)

    for i, (x0, y0) in enumerate(TILES):
        print("=== tile", i, "===")
        for y in range(y0, y0 + 30):
            cols = [x for x in range(x0, x0 + 30) if c.get(x, y) not in (1, 3)]
            if cols:
                print(f"y{y - y0:2d}: {ranges(cols)}")

finish(c)
