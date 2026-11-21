from pixelbench_api import new_canvas, finish

c = new_canvas(64, 32, name="citybus")

OUT = "#24334a"
BODY = "#b4c6d8"
ROOF = "#8fa4ba"
SKIRT = "#92a7bb"
WIN = "#a8d4e8"
GLASS = "#7fb4d0"
DGLASS = "#8fc0d8"
TEAL = "#2fbfa8"
DISP = "#14181e"
DISPON = "#7dffb0"
DOOR = "#c9d6e4"
BUMP = "#666d78"
HEAD = "#ffd94f"
TAIL = "#e63946"
WHEEL = "#26292e"
HUB = "#9aa4ad"

# ---- main body -----------------------------------------------------
c.rect(1, 5, 62, 21, OUT, fill=False)   # overall outline  x1..62 y5..25
c.rect(2, 6, 60, 2, ROOF)              # roof band         x2..61 y6..7
c.rect(2, 8, 60, 17, BODY)             # body panel        x2..61 y8..24
c.rect(2, 24, 60, 1, SKIRT)            # skirt             x2..61 y24

# ---- row of windows ------------------------------------------------
c.rect(13, 9, 34, 6, WIN)              # window band x13..46 y9..14
c.rect(12, 8, 36, 8, OUT, fill=False)  # window frame x12..47 y8..15
for x in (19, 26, 33, 40):
    c.rect(x, 9, 1, 6, OUT)            # pillars

# ---- windshield (front is the right side) ---------------------------
c.rect(51, 8, 10, 7, OUT, fill=False)  # frame x51..60 y8..14
c.rect(52, 9, 8, 5, GLASS)             # glass x52..59 y9..13

# ---- electronic route display on the roof ---------------------------
c.rect(45, 3, 15, 5, OUT, fill=False)  # display housing x45..59 y3..7
c.rect(46, 4, 13, 3, DISP)             # dark screen x46..58 y4..6
for x in (47, 51, 55):
    c.rect(x, 5, 1, 1, DISPON)         # glowing route dots

# ---- exhaust pipe (rear / left) --------------------------------------
c.rect(3, 26, 2, 1, OUT)              # pipe x3..4 y26

# ---- roof AC unit -----------------------------------------------------
c.rect(5, 1, 8, 4, OUT, fill=False)   # unit housing x5..12 y1..4
c.rect(6, 2, 6, 2, ROOF)              # unit body x6..11 y2..3

# ---- accent stripe --------------------------------------------------
c.rect(2, 20, 60, 2, TEAL)             # stripe x2..61 y20..21

# ---- doors (front door right, rear door left) ------------------------
for dx in (5, 50):
    c.rect(dx, 16, 8, 8, DOOR)         # door panel x..x+7 y16..23
    c.rect(dx + 1, 16, 5, 4, DGLASS)   # small door window
    c.rect(dx + 4, 16, 1, 8, OUT)      # split seam
    c.rect(dx - 1, 15, 10, 10, OUT, fill=False)  # door frame

# ---- bumpers ---------------------------------------------------------
c.rect(1, 21, 2, 3, BUMP)
c.rect(61, 21, 2, 3, BUMP)

# ---- lights -----------------------------------------------------------
c.rect(2, 15, 2, 2, TAIL)              # tail light x2..3 y15..16
c.rect(58, 16, 3, 4, OUT, fill=False)  # headlight housing x58..60 y16..19
c.rect(59, 17, 2, 2, HEAD)             # headlight glow x59..60 y17..18
c.rect(61, 7, 2, 2, OUT)               # side mirror
c.rect(61, 9, 1, 1, OUT)               # mirror arm

# ---- wheels ------------------------------------------------------------
for wx in (20, 45):
    c.circle(wx, 26, 3, WHEEL)          # tire xwx-3..wx+3 y23..29
    c.circle(wx, 26, 2, OUT, fill=False)  # rim ring
    c.circle(wx, 26, 1, HUB)            # hub

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 31)))

finish(c)
