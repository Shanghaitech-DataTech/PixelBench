from pixelbench_api import *

c = new_canvas(32, 32, name="usb")

OUT = "#1a1a1a"   # dark outline
MET = "#9aa0a8"   # metal light
MET2 = "#6b7178"  # metal mid
MET3 = "#494f56"  # metal dark
STR = "#c0392b"   # strap red
STR2 = "#8e2418"
GLD = "#e8c15a"   # gold contacts
WHT = "#e8e8e8"
LED = "#40c060"

# keychain strap: loop at top-left
c.line(10, 2, 14, 2, OUT)
c.line(9, 3, 9, 6, OUT)
c.line(15, 3, 15, 6, OUT)
c.rect(10, 3, 5, 4, STR)
c.set(10, 3, STR2); c.set(12, 3, STR2)
c.set(10, 6, STR2); c.set(12, 6, STR2)
# strap attachment to body
c.rect(9, 7, 7, 2, MET3)
c.rect(9, 7, 7, 1, MET2)

# metal body (drive) diagonal-ish vertical body: x 8..23, y 9..24
c.rect(8, 9, 16, 16, MET)
c.rect(8, 9, 16, 1, MET2)
c.rect(8, 24, 16, 1, MET3)
c.line(8, 9, 8, 24, OUT)
c.line(23, 9, 23, 24, OUT)
c.line(8, 9, 23, 9, OUT)
c.line(8, 24, 23, 24, OUT)
# inner shading
c.line(22, 10, 22, 23, MET2)
c.line(9, 10, 9, 23, MET2)
# highlight
c.line(11, 11, 11, 22, WHT)
c.line(12, 11, 12, 22, MET)

# LED
c.rect(20, 12, 2, 2, OUT)
c.set(20, 12, LED); c.set(21, 12, LED); c.set(20, 13, LED); c.set(21, 13, LED)
c.set(20, 12, "#a0ffb0")

# engraved logo / brand line
c.line(14, 14, 19, 14, MET3)
c.line(14, 16, 19, 16, MET3)
c.line(14, 18, 19, 18, MET3)

# USB connector below: x 10..21, y 25..30
c.rect(10, 25, 12, 6, MET)
c.rect(10, 25, 12, 1, MET2)
c.rect(10, 30, 12, 1, MET3)
c.line(10, 25, 10, 30, OUT)
c.line(21, 25, 21, 30, OUT)
c.line(10, 30, 21, 30, OUT)
# gold contacts
for x in (12, 14, 16, 18):
    c.rect(x, 27, 2, 2, GLD)
    c.set(x, 27, "#f5dd8a")

print(c.stats_text())
finish(c)
