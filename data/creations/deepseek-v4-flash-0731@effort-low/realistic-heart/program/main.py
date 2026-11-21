from pixelbench_api import *

W = H = 64
c = new_canvas(W, H)

RIM      = "#3a0101"
VDARK    = "#550303"
DEEP     = "#a01010"
MID      = "#c41f1f"
LIGHT    = "#e03a32"
LIGHTER  = "#ef5a48"
PINK     = "#f6886f"
SOFT     = "#fcb29a"
GLOSS    = "#ffe0cc"
CREASE   = "#5e0606"

CX, CY = 32, 34
pts = [
 (0,23),(-8,15),(-19,8),(-20,-4),
 (-21,-12),(-15,-19),(-8,-19),
 (-3,-19),(-1,-16),(0,-12),
 (1,-16),(3,-19),(8,-19),
 (15,-19),(21,-12),(20,-4),
 (19,8),(8,15),(0,23),
]

def heart_path(s, dx=0, dy=0):
    P = [(round(CX+ox*s+dx), round(CY+oy*s+dy)) for ox,oy in pts]
    d = "M %d %d" % P[0]
    for i in range(1, 19, 3):
        d += " C %d %d, %d %d, %d %d" % (P[i][0],P[i][1],P[i+1][0],P[i+1][1],P[i+2][0],P[i+2][1])
    d += " Z"
    return d

# ---- outer rim ----
c.path(heart_path(1.10, 1, 0), RIM)
c.path(heart_path(1.01), VDARK)

# ---- vessels behind top (aorta / pulmonary) ----
c.path("M 29 17 C 27 10, 22 7, 19 4 L 27 4 C 29 8, 33 9, 34 17 Z", VDARK)
c.path("M 35 17 C 36 10, 40 6, 42 4 L 35 4 C 33 8, 31 10, 31 17 Z", VDARK)
c.path("M 26 14 C 24 9, 21 7, 19 6 L 23 6 C 25 8, 28 10, 29 14 Z", DEEP)
c.path("M 38 14 C 39 9, 41 7, 42 6 L 39 6 C 37 8, 35 10, 34 14 Z", DEEP)

# ---- base heart ----
c.path(heart_path(1.0), DEEP)

# ---- ventricular shadow: darken bottom (apex) ----
c.path(heart_path(0.88, 1, 3), MID)
c.path(heart_path(0.74, 1, 4), DEEP)
c.path(heart_path(0.60, 0, 5), CREASE)

# ---- coronary sulcus groove band ----
c.path("M 14 30 C 24 36, 41 36, 52 28 L 52 31 C 40 39, 25 39, 14 33 Z", CREASE)
c.path("M 16 31 C 25 36, 40 36, 50 30 L 50 32 C 39 38, 26 38, 16 33 Z", RIM)

# ---- gradient sheen above sulcus (upper atria) ----
c.path(heart_path(0.66, -2, -1), MID)
c.path(heart_path(0.46, -3, -2), LIGHT)
c.path(heart_path(0.30, -4, -3), PINK)

# ---- highlights on the top bulbs ----
c.ellipse(20, 23, 7, 6, SOFT)
c.ellipse(44, 24, 6, 5, SOFT)
c.ellipse(20, 22, 4, 3, GLOSS)
c.ellipse(44, 23, 3, 2, GLOSS)
# specular spot left-top
c.ellipse(18, 20, 2, 2, GLOSS)

# vein lines on left ventricle (subtle darker streaks)
c.line(26, 38, 22, 46, CREASE)
c.line(30, 40, 28, 49, CREASE)
c.line(37, 41, 40, 49, CREASE)

print(c.stats_text())
print(c.matrix_text(region=(12,6,54,56)))
view(c, scale=4, margin=0)
save("heart", c)
finish(c)
