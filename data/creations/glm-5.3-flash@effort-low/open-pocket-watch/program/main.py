from pixelbench_api import *

c = new_canvas(64, 64, background=(12, 10, 8), name="watch")

# palette
GOLD      = c.color((212, 168, 60), "gold")
GOLD_HI   = c.color((255, 224, 130), "gold_hi")
GOLD_DK   = c.color((130, 92, 28), "gold_dk")
BRASS     = c.color((180, 140, 70), "brass")
SILVER    = c.color((200, 205, 215), "silver")
SILVER_DK = c.color((120, 128, 140), "silver_dk")
DIAL      = c.color((240, 234, 218), "dial")
INK       = c.color((35, 30, 25), "ink")
RED       = c.color((170, 40, 35), "red")
SHADOW    = c.color((50, 38, 20), "shadow")
BG        = c.color((12, 10, 8), "bg")

# background gradient-ish (dark vignette)
for y in range(64):
    for x in range(64):
        d = ((x-32)**2 + (y-32)**2) ** 0.5
        if d > 30:
            c.set(x, y, BG)

# ---- watch case (open, lid swung left) ----
# main case: circle centred right at (38,32) r=17
cx, cy, r = 38, 32, 17
c.circle(cx, cy, r, GOLD)
c.circle(cx, cy, r-1, GOLD_DK)
c.circle(cx, cy, r-2, DIAL)  # dial face

# crown + bow on right side
c.rect(cx+r-1, cy-3, 5, 6, GOLD)
c.rect(cx+r+2, cy-2, 2, 4, GOLD_DK)
# bow (ring above crown)
c.circle(cx+r+3, cy-5, 3, GOLD, fill=False)

# ---- open lid on the left (tilted disc, seen edge-on-ish) ----
# lid as ellipse at (12,32), rx=6, ry=17
c.ellipse(11, 32, 6, 17, GOLD)
c.ellipse(11, 32, 4, 15, GOLD_HI)
c.ellipse(11, 32, 2, 12, GOLD_DK)
# hinge connecting lid to case
c.line(16, 24, 22, 22, GOLD_DK)
c.line(16, 40, 22, 42, GOLD_DK)

# ---- dial ----
# tick marks
import math
for i in range(12):
    a = i * math.pi / 6
    x1 = cx + (r-4) * math.sin(a)
    y1 = cy - (r-4) * math.cos(a)
    x2 = cx + (r-7) * math.sin(a)
    y2 = cy - (r-7) * math.cos(a)
    c.line(round(x1), round(y1), round(x2), round(y2), INK)
# small subdial (seconds) at lower left of dial
c.circle(cx-6, cy+6, 3, SILVER_DK, fill=False)
c.line(cx-6, cy+6, cx-6, cy+4, RED)

# hands
c.line(cx, cy, cx, cy-11, INK)      # minute
c.line(cx, cy, cx+7, cy+3, INK)     # hour
c.set(cx, cy, RED)
c.set(cx+1, cy, RED)

# ---- gear train visible through cutaway (bottom-right of case) ----
# big gear overlapping dial lower right
gx, gy = 46, 40
c.circle(gx, gy, 6, BRASS)
c.circle(gx, gy, 4, GOLD_DK)
c.set(gx, gy, INK)
# gear teeth
for i in range(10):
    a = i * math.pi / 5
    c.set(round(gx + 7*math.sin(a)), round(gy + 7*math.cos(a)), BRASS)
# spokes
c.line(gx-3, gy, gx+3, gy, GOLD_DK)
c.line(gx, gy-3, gx, gy+3, GOLD_DK)

# medium gear meshing above-left
mx, my = 37, 46
c.circle(mx, my, 4, SILVER)
c.circle(mx, my, 2, SILVER_DK)
c.set(mx, my, INK)
for i in range(8):
    a = i * math.pi / 4
    c.set(round(mx + 5*math.sin(a)), round(my + 5*math.cos(a)), SILVER)

# small gear
sx, sy = 29, 50
c.circle(sx, sy, 3, GOLD_DK)
c.set(sx, sy, GOLD_HI)
for i in range(6):
    a = i * math.pi / 3
    c.set(round(sx + 4*math.sin(a)), round(sy + 4*math.cos(a)), GOLD_DK)

# ---- watch chain from bow, curving down-right ----
chain = [(58, 27), (60, 31), (61, 36), (61, 41), (60, 46), (58, 51), (55, 56), (51, 60), (46, 62)]
for i in range(len(chain)-1):
    x0, y0 = chain[i]
    x1, y1 = chain[i+1]
    c.line(x0, y0, x1, y1, GOLD)
    # links: alternate highlight
    if i % 2 == 0:
        c.set(x0, y0, GOLD_HI)

# ---- highlights / reflections ----
# specular arc on case upper-left
c.line(cx-10, cy-11, cx-4, cy-14, GOLD_HI)
c.line(cx-4, cy-14, cx+3, cy-15, GOLD_HI)
c.set(cx+8, cy-14, GOLD_HI)
# shine on lid
c.line(9, 20, 8, 30, (255, 240, 180))
# dial reflection sweep
c.line(cx-8, cy-6, cx-2, cy-9, SILVER)

print(c.stats_text())
save("open_pocket_watch", c)
finish(c)
