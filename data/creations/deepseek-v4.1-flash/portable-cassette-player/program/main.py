# 32x32 portable cassette player icon
from pixelbench_api import *  # noqa

c = new_canvas(32, 32, name="player")

# ---------------------------------------------------------------- palette
OUT      = c.color("#151a24", "outline")
BODY     = c.color("#dcdcd4", "body")
BODY_HI  = c.color("#f5f4ee", "body_hi")
BODY_SH  = c.color("#b8b8ae", "body_sh")
FRAME    = c.color("#2a303c", "frame")
GLASS    = c.color("#1e2a3d9c", "glass")     # semi transparent pane
TAPE     = c.color("#7b4b2b", "tape")
TAPE_HI  = c.color("#9a6136", "tape_hi")
CREAM    = c.color("#f2ebd6", "cream")
HUB      = c.color("#3a3026", "hub")
PANEL    = c.color("#333a47", "panel")
PANEL_HI = c.color("#4e5a71", "panel_hi")
KEYSYM   = c.color("#e9e3d0", "keysym")
ACCENT   = c.color("#e8663c", "accent")
METAL    = c.color("#a7b0bd", "metal")
METAL_HI = c.color("#cdd4dd", "metal_hi")
METAL_DK = c.color("#79828f", "metal_dk")
CABLE    = c.color("#242a34", "cable")


# ---------------------------------------------------------------- helpers
def rp(x0, y0, x1, y1, r):
    """Rounded-rect path data, coordinates inclusive of the last pixel."""
    yb = y1 + 1
    return (f"M {x0+r} {y0} H {x1-r} A {r} {r} 0 0 1 {x1} {y0+r} "
            f"V {yb-r} A {r} {r} 0 0 1 {x1-r} {yb} H {x0+r} "
            f"A {r} {r} 0 0 1 {x0} {yb-r} V {y0+r} "
            f"A {r} {r} 0 0 1 {x0+r} {y0} Z")


def rrect(x0, y0, x1, y1, r, colour):
    c.path(rp(x0, y0, x1, y1, r), colour, fill=True)


def glyph(x, y, rows, colour):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == "#":
                c.set(x + i, y + j, colour)


# ---------------------------------------------------------------- headphone cable
c.path("M 0 2 H 4 C 6 2 7 3 7 8", CABLE, fill=False)
c.path("M 0 3 H 5 C 7 3 8 4 8 8", CABLE, fill=False)

# ---------------------------------------------------------------- body
rrect(3, 6, 28, 29, 3, OUT)
rrect(4, 7, 27, 28, 2, BODY)

# bevel / shading of the shell
c.line(4, 9, 4, 26, BODY_HI)
c.line(5, 28, 26, 28, BODY_SH)
c.line(27, 10, 27, 26, BODY_SH)
c.set(5, 8, BODY_HI)
c.set(6, 28, BODY_SH)

# ---------------------------------------------------------------- cassette window
rrect(5, 7, 23, 17, 1, FRAME)
rrect(6, 8, 22, 16, 1, GLASS)

# tape path between the reels
c.line(10, 9, 18, 9, TAPE)
c.line(10, 15, 18, 15, TAPE)

for cx in (10, 18):
    c.circle(cx, 12, 3, TAPE)
    c.circle(cx, 12, 1, CREAM)
    c.set(cx, 12, HUB)
    c.set(cx - 1, 10, TAPE_HI)

# ---------------------------------------------------------------- grooves / bevels
c.line(6, 18, 25, 18, BODY_SH)     # shadow under the door
c.line(6, 20, 25, 20, BODY_HI)     # highlight above the keys

# ---------------------------------------------------------------- control panel
rrect(5, 21, 26, 27, 1, PANEL)
c.line(6, 21, 25, 21, PANEL_HI)

REWIND = ["..#..#",
          ".##.##",
          "######",
          ".##.##",
          "..#..#"]
PLAY   = ["##....",
          "####..",
          "######",
          "####..",
          "##...."]
FF     = ["#..#..",
          "##.##.",
          "######",
          "##.##.",
          "#..#.."]

glyph(6, 22, REWIND, KEYSYM)
glyph(13, 22, PLAY, ACCENT)
glyph(20, 22, FF, KEYSYM)

# ---------------------------------------------------------------- volume thumb wheel
c.line(24, 10, 24, 15, BODY_SH)          # shadow the wheel throws on the shell
c.rect(25, 10, 5, 6, OUT)                # wheel body (capsule)
c.line(26, 9, 28, 9, OUT)
c.line(26, 16, 28, 16, OUT)
c.rect(26, 10, 3, 6, METAL)
for y, col in ((10, METAL_HI), (11, METAL), (12, METAL_DK),
               (13, METAL_HI), (14, METAL), (15, METAL_DK)):
    c.line(26, y, 28, y, col)

# ---------------------------------------------------------------- report / export
print(c.stats_text())
save("player", c)

finish(c)
