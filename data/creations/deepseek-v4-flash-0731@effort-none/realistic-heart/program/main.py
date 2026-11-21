from pixelbench_api import *

c = new_canvas(64, 64, name="heart")

# Color palette - realistic shading
C_BLACK_EDGE = c.color((30, 4, 8))       # very dark outline
C_DEEP       = c.color((45, 6, 12))      # deep shadow
C_DARK       = c.color((60, 8, 14))      # dark red shadow
C_MID_DARK   = c.color((90, 12, 22))     # mid-dark
C_RED        = c.color((140, 22, 36))    # base red
C_BRIGHT     = c.color((185, 35, 50))    # bright red
C_LIGHT      = c.color((220, 60, 72))    # lighter red
C_HIGHLIGHT  = c.color((245, 100, 105))  # highlight
C_GLOSS      = c.color((255, 150, 140))  # glossy
C_WHITE      = c.color((255, 220, 215))  # specular
C_VEIN_D     = c.color((80, 12, 20))     # dark vein
C_VEIN       = c.color((120, 22, 32))    # mid vein
C_AORTA_D    = c.color((70, 10, 18))     # aorta dark
C_AORTA      = c.color((140, 26, 36))    # aorta

CX, CY, S = 32, 40, 19.0

def in_heart(x, y):
    hx = (x - CX) / S
    hy = (y - CY) / S
    val = (hx*hx + hy*hy - 1.0)**3 - hx*hx * (hy**3)
    return val <= 0

# ---------------------------------------------------------------
# 1. Base shape + realistic shading
# ---------------------------------------------------------------
for y in range(64):
    for x in range(64):
        if in_heart(x, y):
            dx = (x - CX) / S
            dy = (y - CY) / S
            dist = (dx*dx + dy*dy) ** 0.5
            # light from top-left: brightness falls with distance from (upper-left)
            # Boost brightness toward the upper-left lobe, darken toward bottom-right
            offset = (dx + dy)  # light-facing component (-diagonal)
            val = dist - 0.22 * offset

            # main body red
            col = C_RED
            if val < 0.30:
                col = C_GLOSS
            elif val < 0.50:
                col = C_HIGHLIGHT
            elif val < 0.72:
                col = C_LIGHT
            elif val < 0.95:
                col = C_BRIGHT
            elif val < 1.20:
                col = C_RED
            elif val < 1.45:
                col = C_MID_DARK
            elif val < 1.70:
                col = C_DARK
            else:
                col = C_DEEP
            c.set(x, y, col)

# ---------------------------------------------------------------
# 2. Dark outline
# ---------------------------------------------------------------
for y in range(64):
    for x in range(64):
        if in_heart(x, y):
            edge = False
            for nx in (x-1, x+1):
                if nx < 0 or nx > 63 or not in_heart(nx, y):
                    edge = True
            for ny in (y-1, y+1):
                if ny < 0 or ny > 63 or not in_heart(x, ny):
                    edge = True
            if edge:
                c.set(x, y, C_BLACK_EDGE)

# ---------------------------------------------------------------
# 3. Specular gloss on the upper-left lobe
# ---------------------------------------------------------------
for y in range(20, 34):
    for x in range(14, 30):
        if in_heart(x, y):
            ddx = x - 22
            ddy = y - 28
            d = (ddx*ddx + ddy*ddy)**0.5
            if d < 4.0:
                c.set(x, y, C_WHITE)
            elif d < 6.5:
                c.set(x, y, C_GLOSS)
            elif d < 9.5:
                c.set(x, y, C_HIGHLIGHT)

# A secondary softer highlight on the right lobe
for y in range(22, 34):
    for x in range(34, 48):
        if in_heart(x, y):
            ddx = x - 43
            ddy = y - 28
            d = (ddx*ddx + ddy*ddy)**0.5
            if d < 4.0:
                c.set(x, y, C_HIGHLIGHT)
            elif d < 6.5:
                c.set(x, y, C_LIGHT)

# ---------------------------------------------------------------
# 4. Veins / surface detail
# ---------------------------------------------------------------
vein_paths = [
    [(28,24),(30,29),(31,34),(30,40),(28,46)],
    [(33,25),(35,30),(36,36),(35,43)],
    [(37,26),(40,32),(42,39),(42,47),(40,54)],
    [(26,27),(26,34),(24,40),(22,46)],
    [(44,28),(46,34),(46,41),(44,48)],
    [(31,38),(32,43),(31,49),(29,55)],
    [(34,30),(37,32),(40,34)],
]
for pts in vein_paths:
    for i in range(len(pts)-1):
        c.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], C_VEIN_D)

# ---------------------------------------------------------------
# 5. Aorta and vessels at the top
# ---------------------------------------------------------------
# The cleft top of heart is around x=29..34, y=18..20
for x in range(28, 37):
    for y in range(8, 13):
        c.set(x, y, C_AORTA)
# descending into heart
for x in range(29, 36):
    for y in range(13, 19):
        if in_heart(x, y):
            c.set(x, y, C_AORTA_D)
# aorta highlight stripe
for y in range(8, 14):
    for x in range(31, 34):
        c.set(x, y, C_VEIN)
c.line(32, 8, 32, 14, C_LIGHT)

# aortic arch branches left and right
for x in range(23, 29):
    c.set(x, 9, C_AORTA)
    c.set(x, 10, C_AORTA)
for x in range(36, 41):
    c.set(x, 9, C_AORTA)
    c.set(x, 10, C_AORTA)
# darken the underside of the arch
for x in range(24, 29):
    c.set(x, 11, C_AORTA_D)
for x in range(36, 40):
    c.set(x, 11, C_AORTA_D)
# branch tubes going up
c.rect(23, 4, 3, 5, C_AORTA)
c.rect(38, 4, 3, 5, C_AORTA)
c.set(24, 3, C_AORTA_D); c.set(38, 3, C_AORTA_D)
# small top spurs
c.set(22, 5, C_AORTA_D)
c.set(40, 5, C_AORTA_D)

# ---------------------------------------------------------------
# 6. Bottom / tip : deepen the point (gradient, not flat)
# ---------------------------------------------------------------
for y in range(52, 64):
    for x in range(64):
        if in_heart(x, y):
            depth = (y - 52) / 11.0
            col = C_DEEP if depth > 0.75 else (C_DARK if depth > 0.45 else C_MID_DARK)
            c.set(x, y, col)
# soft reflected light along the bottom inside edge
for y in range(52, 60):
    for x in range(64):
        if in_heart(x, y):
            edge = False
            for ny in (y+1, y-1):
                if ny > 63 or not in_heart(x, ny):
                    edge = True
            if edge:
                c.set(x, y, C_MID_DARK)

# ---------------------------------------------------------------
# 7. Cleft crease between lobes (the two bumps at the top)
# ---------------------------------------------------------------
c.set(30, 19, C_DARK); c.set(34, 19, C_DARK)
c.set(30, 20, C_DEEP); c.set(34, 20, C_DEEP)
c.set(30, 21, C_DEEP); c.set(34, 21, C_DEEP)

# ---------------------------------------------------------------
# 8. Small dark shading patches near lobe edges
# ---------------------------------------------------------------
for d in [(25,44),(39,47),(26,50),(44,52)]:
    c.circle(d[0], d[1], 1, C_DARK)

# A couple of subtle mid-level glow streaks on left lobe
c.line(20, 26, 24, 30, C_LIGHT)
c.line(22, 30, 20, 35, C_LIGHT)

print(c.stats_text())
finish(c)
