from pixelbench_api import *

W = H = 32
c = new_canvas(W, H, background=None, name="forest-slime")

OUTL  = "#1e3313"
MIDG  = "#4a7a2e"
LIGHTG= "#6ba83f"
HILITE= "#8fce5e"
MOSS  = "#527a30"
EYE   = "#f2ff8a"
EYEHI = "#ffffff"
EYEC  = "#8fc43a"
MUDRK = "#7a1e1e"
MUSHI = "#e85a3a"
MUSPOT= "#f2c894"
MUSWH = "#ffffff"
MOUTH = "#10200a"
SHINE = "#b8e58a"
BLUSH = "#a3c46a"

# Build sprite within bounds. Slime blob centered ~ y 12-29.
c.circle(16, 21, 10, OUTL, fill=True)   # outline
c.circle(16, 20, 9, MIDG, fill=True)    # body

# lighten upper half
c.path("M 11 15 Q 11 11 16 11 Q 21 11 21 15 Q 21 18 18 19 Q 16 20 14 19 Q 11 18 11 15 Z",
       LIGHTG, fill=True)

# top highlight
c.ellipse(13, 12, 3, 1, HILITE, fill=True)
c.ellipse(14, 12, 1, 1, SHINE, fill=True)

# bottom flatten
c.path("M 8 27 Q 8 29 11 29 L 21 29 Q 24 29 24 27 L 24 26 L 8 26 Z", MIDG, fill=True)

# moss spots
c.circle(9, 21, 1, MOSS, fill=True)
c.circle(24, 20, 1, MOSS, fill=True)
c.circle(15, 25, 1, MOSS, fill=True)
c.circle(21, 26, 1, MOSS, fill=True)
c.circle(11, 16, 1, MOSS, fill=True)
c.circle(22, 15, 1, MOSS, fill=True)
c.set(12, 28, MOSS)
c.set(20, 28, MOSS)
c.set(17, 26, MOSS)

# --- Eyes (glowing) ---
c.circle(11, 15, 3, EYE, fill=True)
c.circle(11, 15, 2, EYEC, fill=True)
c.set(11, 15, OUTL)
c.set(10, 13, EYEHI)
c.circle(21, 15, 3, EYE, fill=True)
c.circle(21, 15, 2, EYEC, fill=True)
c.set(21, 15, OUTL)
c.set(20, 13, EYEHI)

# --- Smile ---
c.path("M 13 18 Q 16 21 19 18 Q 19 20 16 22 Q 13 20 13 18 Z", MOUTH, fill=True)

# --- blush ---
c.set(8, 18, BLUSH)
c.set(9, 17, BLUSH)
c.set(23, 17, BLUSH)
c.set(24, 18, BLUSH)

# --- Antlers (far sides, upward) ---
c.line(11, 10, 9, 5, OUTL)
c.line(10, 7, 7, 4, OUTL)
c.line(10, 7, 12, 4, OUTL)
c.line(9, 5, 8, 3, OUTL)
c.line(21, 10, 23, 5, OUTL)
c.line(22, 7, 25, 4, OUTL)
c.line(22, 7, 20, 4, OUTL)
c.line(23, 5, 24, 3, OUTL)

# --- Small red mushroom on the top of the head ---
c.rect(15, 7, 2, 4, MUSPOT, fill=True)
c.rect(15, 10, 2, 2, MUSWH, fill=True)  # gill ring
c.path("M 9 9 Q 10 4 16 4 Q 22 4 23 9 Q 22 7 16 7 Q 10 7 9 9 Z",
       MUSHI, fill=True)
c.path("M 9 9 Q 10 4 16 4 Q 22 4 23 9", MUDRK, fill=True)
c.path("M 12 6 Q 14 5 16 5 Q 17 5 15 6 Z", MUSWH, fill=True)
c.circle(12, 6, 1, MUSWH, fill=True)
c.circle(19, 6, 1, MUSWH, fill=True)
c.set(20, 7, MUSWH)

save("forest-slime", c)
finish(c)
