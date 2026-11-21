import math
from pixelbench_api import new_canvas, finish

c = new_canvas(128, 128, name="motorcycle")

black    = c.color((13,13,15),   "black")
tire     = c.color((19,19,22),   "tire")
dark     = c.color((46,48,54),   "dark")
mid      = c.color((74,77,84),   "mid")
silver   = c.color((180,185,194),"silver")
silver_d = c.color((133,138,148),"silver_d")
hub      = c.color((108,112,120),"hub")
white    = c.color((238,240,244),"white")
rim      = c.color((60,62,68),   "rim")
red      = c.color((208,28,30),  "red")
darkred  = c.color((128,20,24),  "darkred")
tailc    = c.color((240,60,56),  "tail")
wind     = c.color((24,26,34),   "wind")

def lw(x0, y0, x1, y1, col, w):
    dx = x1 - x0; dy = y1 - y0
    L = math.hypot(dx, dy)
    if L == 0:
        return
    px = -dy / L; py = dx / L
    for k in range(-(w // 2), w // 2 + 1):
        c.line(round(x0 + px * k), round(y0 + py * k),
               round(x1 + px * k), round(y1 + py * k), col)

def wheel(cx, cy):
    c.circle(cx, cy, 23, tire)
    c.circle(cx, cy, 19, silver_d)          # brake disc ring
    c.circle(cx, cy, 16, rim)               # dark rim
    c.line(cx - 12, cy - 21, cx + 12, cy - 20, rim)   # tire sheen
    c.line(cx - 8, cy - 22, cx + 8, cy - 21, silver_d)
    for a in range(0, 360, 60):
        x0 = cx + math.cos(math.radians(a)) * 9
        y0 = cy + math.sin(math.radians(a)) * 9
        x1 = cx + math.cos(math.radians(a)) * 15.5
        y1 = cy + math.sin(math.radians(a)) * 15.5
        c.line(round(x0), round(y0), round(x1), round(y1), white)
    c.circle(cx, cy, 8, hub)
    c.circle(cx, cy, 3, silver)
    c.circle(cx, cy, 15, silver, fill=False)

# --- wheels ---
wheel(28, 96)
wheel(102, 96)

# --- swingarm (silver tubular) ---
lw(58, 84, 30, 95, silver, 3)

# --- frame down tube ---
lw(86, 62, 60, 84, silver_d, 3)

# --- engine: round silver gray cover ---
c.circle(58, 84, 12, silver)
c.circle(58, 84, 7, silver_d, fill=False)
c.circle(58, 84, 5, silver_d)
c.circle(58, 85, 2, dark)
c.circle(58, 84, 10, red, fill=False)       # red accent ring

# --- brake calipers (red) ---
c.rect(9, 88, 7, 6, darkred)
c.rect(83, 88, 7, 6, darkred)

# --- exhaust ---
lw(66, 78, 56, 88, silver_d, 3)
lw(56, 88, 44, 94, silver_d, 3)
c.rect(30, 90, 14, 12, dark)
c.rect(26, 92, 5, 9, silver_d)

# --- body: wide dark gray fairing, upswept tail ---
c.poly([(100,50),(96,58),(86,64),(72,69),(58,72),(44,71),
        (38,67),(30,62),(20,56),(14,48),(9,42),(16,39),
        (26,42),(38,44),(48,45),(60,44),(76,40),(90,37)], dark)

# tank highlight
lw(86, 38, 58, 43, mid, 2)

# seat (black)
c.poly([(40,46),(58,44),(62,40),(54,38),(40,42)], black)

# red accent stripe on fairing
c.poly([(97,53),(88,57),(60,64),(48,62),(56,57),(90,52)], red)

# red tail light
c.rect(6, 40, 8, 7, tailc)
c.rect(7, 42, 5, 3, darkred)

# small black tilted windscreen
c.poly([(84,29),(93,28),(99,42),(92,43)], wind)

# front fender (silver), hugging the wheel
c.poly([(86,75),(108,73),(112,76),(106,79),(86,82)], silver)
c.poly([(90,77),(106,76),(104,78),(90,79)], silver_d)

# headlight lens
c.ellipse(98, 49, 2, 4, mid)

# --- front fork (silver) in front of everything ---
lw(86, 58, 102, 96, silver, 5)
lw(87, 60, 101, 95, black, 1)
lw(84, 56, 88, 60, silver, 3)

print(c.stats_text())
print("---- body/windscreen region ----")
print(c.matrix_text(region=(0, 25, 110, 70)))
print("---- wheels region ----")
print(c.matrix_text(region=(0, 70, 127, 120)))

finish(c)
