import math

c = new_canvas(32, 32, name="output")

# palette
BL = c.color("#e8c893", "bamboo_light")
BM = c.color("#c89457", "bamboo_mid")
BD = c.color("#9c6b36", "bamboo_dark")
BE = c.color("#6b4522", "bamboo_edge")
IN = c.color("#43280f", "inside")
DW = c.color("#f8f0e2", "dough")
DS = c.color("#dcc6a8", "dough_shade")
DL = c.color("#b29573", "dough_line")
FI = c.color("#d87a5a", "filling")
ST = c.color("#e6f0f4", "steam")

# ---------------- tilted lid (behind), hinged on the back-right rim -------
LCX, LCY, LRX, LRY, SLOPE = 19, 8, 9, 4.0, 0.33
for x in range(LCX - LRX, LCX + LRX + 1):
    t = (x - LCX) / LRX
    h = LRY * math.sqrt(max(0.0, 1.0 - t * t))
    yc = LCY - SLOPE * (x - LCX)
    ytop, ybot = int(round(yc - h)), int(round(yc + h))
    face = BM if (x - LCX) % 3 == 0 else BL
    for y in range(ytop, ybot + 1):
        c.set(x, y, face)
    c.set(x, ytop, BD)
    c.set(x, ybot, BD)
    if t < 0.3:                      # rim thickness under the lower arc
        c.set(x, ybot + 1, BE)
# knob
c.set(LCX, LCY - 1, BD)
c.set(LCX + 1, LCY - 1, BD)
c.set(LCX, LCY, BE)
c.set(LCX + 1, LCY, BE)

# ---------------- back rim + dark interior --------------------------------
c.ellipse(16, 17, 12, 3, BM)
c.ellipse(16, 17, 12, 3, BD, fill=False)
c.ellipse(16, 18, 11, 2, IN)
c.line(5, 17, 27, 17, IN)

# ---------------- three dumplings -----------------------------------------
def dumpling(cx, cy):
    c.ellipse(cx, cy, 3, 3, DW)
    c.ellipse(cx, cy, 3, 3, DL, fill=False)
    c.line(cx + 2, cy - 1, cx + 2, cy + 2, DS)
    c.set(cx + 3, cy, DS)
    c.set(cx, cy - 4, DL)
    c.set(cx - 1, cy - 3, DL)
    c.set(cx + 1, cy - 3, DL)
    c.set(cx, cy - 3, DW)
    c.set(cx, cy - 2, FI)
    c.set(cx - 1, cy - 1, DL)
    c.set(cx + 1, cy - 1, DL)

dumpling(7, 18)
dumpling(16, 18)
dumpling(25, 18)

# ---------------- front rim + basket body ---------------------------------
c.ellipse(16, 23, 12, 3, BL)
c.ellipse(16, 23, 12, 3, BD, fill=False)
c.poly([(4, 23), (28, 23), (26, 30), (6, 30)], BM)
c.poly([(4, 23), (28, 23), (26, 30), (6, 30)], BD, fill=False)

for y in (27, 29):
    c.line(6, y, 26, y, BD)
for y in (26, 28):
    for x in range(6, 27, 3):
        c.set(x, y, BD)
c.line(7, 30, 25, 30, BE)
c.line(25, 25, 24, 29, BD)
c.line(6, 25, 7, 29, BL)
# corner posts
c.line(5, 24, 6, 30, BE)
c.line(27, 24, 26, 30, BE)

# ---------------- steam, from the open left side --------------------------
c.path("M6 14 q -3 -3 0 -5 q 3 -2 0 -4", ST, fill=False)
c.path("M11 11 q -2 -2 0 -3 q 2 -2 0 -3", ST, fill=False)
c.set(3, 8, ST)
c.set(8, 3, ST)

view(c)
print(c.stats_text())
finish(c)
