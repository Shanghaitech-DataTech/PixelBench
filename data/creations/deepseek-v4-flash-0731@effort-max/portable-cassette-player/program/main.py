from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUTLINE = "#0a0a0f"
BODY = "#23222c"
BODY_LIGHT = "#383742"
BODY_DARK = "#131219"
PANEL = "#2a2935"
SILVER = "#c9ccd6"
SILVER_DARK = "#8a8e9c"
REEL = "#d5d8e1"
HUB = "#17161e"
BTN = "#2d2c37"
BTN_DARK = "#1d1c26"
BTN_TOP = "#3b3a46"
ICON = "#d9dce6"
RED = "#e0503a"
TAPE = "#0e0e14"
LIGHT = "#e9ebf2"
CABLE = "#0e0d13"
CENTER = "#6e7383"

# ---------- body ----------
c.rect(4, 5, 24, 20, OUTLINE)
c.rect(5, 6, 22, 18, BODY)
# round the four corners
c.clear(4, 5, 1, 1)
c.clear(27, 5, 1, 1)
c.clear(4, 24, 1, 1)
c.clear(27, 24, 1, 1)
# top front panel + bottom shade
c.rect(5, 6, 22, 4, PANEL)
c.line(6, 23, 25, 23, BODY_DARK)

# ---------- transparent cassette window ----------
c.clear(9, 8, 14, 7)
c.line(9, 8, 22, 8, BODY_DARK)
c.line(9, 14, 22, 14, BODY_DARK)

# tape band and two reels (visible through the clear window)
c.rect(14, 10, 4, 3, TAPE)
c.circle(11, 11, 2, "#4b4e5e")   # left reel disc
c.circle(11, 11, 1, HUB)
c.set(11, 11, CENTER)
c.circle(20, 11, 2, "#4b4e5e")   # right reel disc
c.circle(20, 11, 1, HUB)
c.set(20, 11, CENTER)
c.set(10, 9, LIGHT)
c.set(21, 9, LIGHT)
c.set(12, 13, SILVER_DARK)
c.set(20, 13, SILVER_DARK)

# ---------- playback buttons (rewind / play / fast-forward / stop) ----------
def btn(x, y):
    c.rect(x, y, 4, 3, BTN)
    c.rect(x, y, 4, 1, BTN_TOP)
    c.rect(x, y + 2, 4, 1, BTN_DARK)

btn(22, 8)
# <<
for x0 in (22, 24):
    c.set(x0, 9, ICON)
    for yy in (8, 9, 10):
        c.set(x0 + 1, yy, ICON)
btn(22, 12)
# >
c.set(23, 13, ICON)
c.set(24, 12, ICON)
c.set(24, 13, ICON)
c.set(24, 14, ICON)
c.set(25, 13, ICON)
btn(22, 16)
# >>
for x0 in (23, 24):
    c.set(x0, 16, ICON)
    c.set(x0, 17, ICON)
    c.set(x0, 18, ICON)
    c.set(x0 + 1, 17, ICON)
btn(22, 20)
c.rect(23, 20, 2, 2, ICON)  # stop square

# ---------- volume dial (left side) ----------
c.circle(4, 15, 3, "#33323e")        # solid cylindrical knob
c.line(2, 13, 2, 17, "#41404d")      # left highlight
c.line(6, 14, 6, 16, "#23222c")      # right shade
c.set(4, 12, RED)                    # red tick
c.set(3, 17, "#454451")               # grip dot

# ---------- small extra details ----------
c.set(26, 21, "#f0453a")            # power LED
for gx in (14, 16, 18, 20):
    c.set(gx, 21, "#3a3945")         # speaker grille dots

# ---------- headphone plug + cable ----------
c.rect(12, 2, 5, 3, CABLE)
c.rect(13, 0, 3, 2, SILVER)
c.rect(13, 1, 3, 1, SILVER_DARK)
c.set(14, 0, LIGHT)
c.line(16, 4, 14, 6, CABLE)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
