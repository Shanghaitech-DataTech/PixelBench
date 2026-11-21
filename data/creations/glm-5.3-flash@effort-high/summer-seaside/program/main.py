import math, random

c = new_canvas(128, 128, name="seaside")

# ---------- gradient helpers ----------
SKY_STOPS  = [(0,(47,124,206)),(26,(105,170,228)),(51,(188,224,246))]
SEA_STOPS  = [(52,(20,64,142)),(60,(26,96,168)),(70,(36,140,182)),(80,(56,180,190)),(86,(88,206,196))]
SAND_STOPS = [(87,(240,210,146)),(105,(231,196,126)),(127,(210,172,102))]

def grad_col(stops, y):
    if y <= stops[0][0]:
        return stops[0][1]
    for i in range(len(stops)-1):
        (y0,c0),(y1,c1) = stops[i], stops[i+1]
        if y <= y1:
            t = (y-y0)/float(y1-y0)
            return tuple(int(round(c0[k]+(c1[k]-c0[k])*t)) for k in range(3))
    return stops[-1][1]

def vgrad(stops, y0, y1, step):
    y = y0
    while y <= y1:
        y2 = min(y+step-1, y1)
        c.rect(0, y, 128, y2-y+1, grad_col(stops, y))
        y = y2+1

# ---------- sky / sea / sand ----------
vgrad(SKY_STOPS, 0, 51, 4)
vgrad(SEA_STOPS, 52, 86, 3)
vgrad(SAND_STOPS, 87, 127, 4)

# ---------- sun ----------
c.circle(100, 16, 10, "#FFE9A8")
c.circle(100, 16, 7, "#FFD84D")
c.circle(100, 16, 4, "#FFF7DC")

# ---------- clouds ----------
def cloud(cx, cy, col, shade):
    c.ellipse(cx-8, cy+2, 6, 4, col)
    c.ellipse(cx, cy-1, 8, 5, col)
    c.ellipse(cx+9, cy+2, 6, 4, col)
    c.ellipse(cx, cy+4, 12, 3, col)
    c.ellipse(cx, cy+5, 11, 2, shade)

cloud(24, 16, "#FFFFFF", "#D8EAF6")
cloud(66, 30, "#FFFFFF", "#D8EAF6")
c.ellipse(74, 44, 5, 3, "#E6F3FB")
c.ellipse(80, 43, 4, 3, "#E6F3FB")
c.ellipse(77, 45, 7, 2, "#E6F3FB")

# ---------- gulls ----------
c.path("M12 36 Q16 31 19 35 Q22 31 26 36", "#3C4A58", fill=False)
c.path("M42 24 Q46 19 49 23 Q52 19 56 24", "#3C4A58", fill=False)

# ---------- foam lines rolling in the sea ----------
FOAM  = "#FFFFFF"
FOAM2 = "#D9F4EE"
for x in range(128):
    y = 72 + int(round(2*math.sin(x/7.0)))
    c.set(x, y, FOAM2); c.set(x, y+1, FOAM)
for x in range(128):
    y = 79 + int(round(2*math.sin(x/6.0 + 2.0)))
    c.set(x, y, FOAM2); c.set(x, y+1, FOAM)

# ---------- sand speckles ----------
random.seed(7)
for i in range(70):
    x = random.randint(0, 127)
    y = random.randint(92, 127)
    c.set(x, y, "#C9A25F" if i % 2 else "#F4E0AC")

# ---------- wet sand at the waterline ----------
WET = "#CFA763"
for x in range(128):
    d = 2 + int(round(1.5*math.sin(x/5.0 + 1.0)))
    c.rect(x, 87, 1, d, WET)

# ---------- shore foam ----------
for x in range(128):
    base = 84 + int(round(2*math.sin(x/5.0 + 1.0)))
    c.set(x, base, FOAM)
    c.set(x, base+1, FOAM)
    c.set(x, base+2, FOAM2)

# ---------- beach umbrella ----------
# shadow on sand
c.ellipse(36, 109, 13, 3, "#DDB671")
# pole
c.rect(31, 30, 2, 77, "#7A4A22")
c.rect(31, 30, 1, 77, "#96683A")
c.circle(32, 29, 1, "#5C3618")
# canopy: half disc with red/white wedges
cx, cy, r = 32, 52, 19
RED, WHITE, RIM = "#E23B2E", "#FAF8F4", "#A02015"
for y in range(cy - r, cy + 1):
    for x in range(cx - r, cx + r + 1):
        dx, dy = x - cx, y - cy
        if dx*dx + dy*dy <= r*r:
            ang = math.degrees(math.atan2(dx, -dy))
            idx = int((ang + 90) // 22.5)
            c.set(x, y, RED if idx % 2 == 0 else WHITE)
# rim outline on the arc and the bottom edge
for y in range(cy - r, cy + 1):
    for x in range(cx - r, cx + r + 1):
        dx, dy = x - cx, y - cy
        d2 = dx*dx + dy*dy
        if d2 <= r*r and d2 >= (r-1.6)*(r-1.6):
            c.set(x, y, RIM)
for x in range(cx - r, cx + r + 1):
    dx = x - cx
    if dx*dx <= r*r:
        c.set(x, cy, RIM)

# ---------- striped towel ----------
tx, ty, tw = 56, 98, 26
stripes = [("#FF7A5C",3),("#FFF6EA",3),("#3FBFB0",3),("#FF7A5C",3),("#FFF6EA",3),("#3FBFB0",1)]
y = ty
for col, h in stripes:
    c.rect(tx, y, tw, h, col)
    y += h
c.rect(tx-1, ty, 1, 16, "#E5D5BF")
c.rect(tx+tw, ty, 1, 16, "#E5D5BF")

# ---------- flip-flops ----------
c.ellipse(94, 108, 3, 5, "#FF9E3D")
c.line(92, 106, 94, 109, "#FFF6EA")
c.line(96, 106, 94, 109, "#FFF6EA")
c.ellipse(105, 106, 3, 5, "#FF9E3D")
c.line(103, 104, 105, 107, "#FFF6EA")
c.line(107, 104, 105, 107, "#FFF6EA")

# ---------- sailboat far out ----------
c.poly([(97,46),(97,56),(103,56)], "#FFFFFF")
c.poly([(95,47),(95,56),(90,56)], "#F0F0EC")
c.line(96, 46, 96, 57, "#4A3626")
c.poly([(90,57),(101,57),(99,60),(92,60)], "#6B4226")

print(c.stats_text())
print("---- sailboat / gulls ----")
print(c.matrix_text(region=(8, 18, 110, 62)))
finish(c)
