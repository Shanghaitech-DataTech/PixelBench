from pixelbench_api import *

W = H = 256
WU = 0
# ---------- palette ----------
OUTLINE = (18, 12, 6)
BARK    = (94, 62, 28)
BARK_D  = (60, 40, 16)
BARK_DD = (40, 27, 12)
BARK_L  = (126, 92, 48)
BARK_HL = (160, 124, 78)
ROOT    = (54, 38, 18)
ROOT_D  = (34, 24, 12)
MOSS    = (58, 110, 44)
MOSS_L  = (88, 156, 62)
MOSS_D  = (38, 74, 28)
FOL     = (50, 94, 34)
FOL_D   = (32, 60, 22)
FOL_DD  = (22, 42, 16)
FOL_L   = (76, 128, 50)
FOL_HL  = (104, 160, 68)
EYE = (110, 255, 82)
EYE_L = (190, 255, 148)
EYE_C = (235, 255, 210)
SKY  = (26, 44, 38)
SKY_D = (18, 32, 28)
SKY_M = (34, 58, 50)
TREE_D   = (16, 22, 18)
TREE_MID = (24, 34, 28)
TREE_M   = (30, 44, 36)
RAY  = (255, 236, 160)
RAY_A = 120
RAY2 = (255, 250, 210)
GROUND    = (42, 36, 22)
GROUND_D  = (32, 27, 17)
GROUND_L  = (62, 56, 34)
GRASS    = (66, 88, 40)
GRASS_L  = (92, 118, 58)
GRASS_D  = (40, 54, 26)
ROCK     = (52, 48, 34)
FLOWER   = (200, 120, 90)

def mixc(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

# ---------- background ----------
bg = new_canvas(W, H, name="bg")
bg.rect(0, 0, W, H, SKY_D)
# sky gradient bands
for i in range(14):
    y0 = 0 + i * (H//14)
    col = mixc(SKY_D, SKY_M, i/13)
    bg.rect(0, y0, W, H//14, col)
# distant forest canopy at top
bg.rect(0, 0, W, 26, TREE_D)
for xx in range(0, W, 34):
    bg.ellipse(xx+10, 18, 34, 34, TREE_D)
for xx in range(17, W, 40):
    bg.ellipse(xx+8, 26, 40, 40, TREE_MID)
# background trees framing the clearing
for (tx, tr) in [(18, 26), (236, 26), (4, 34), (250, 32)]:
    bg.ellipse(tx, 40, tr, 60, TREE_D)
# distant trunks silhouettes near edges
for tx in (30, 224):
    bg.rect(tx-4, 40, 9, 200, TREE_D)
# a few mid trees
for tx in (66, 190):
    bg.rect(tx-3, 70, 7, 140, TREE_M)
    bg.ellipse(tx, 60, 22, 40, TREE_M)
# dark ground silhouette under clearing horizon
bg.poly([(0,198),(30,192),(70,196),(110,190),(150,196),(200,190),(256,196),(256,256),(0,256)], TREE_D)

# ---------- god rays ----------
rays = new_canvas(W, H, name="rays")
def ray_beam(p1, p2, p3, p4, col, a):
    rays.poly([p1, p2, p3, p4], col + (a,))
ray_beam((40,-10),(118,76),(146,62),(70,-10), RAY, 70)
ray_beam((96,-10),(168,92),(204,88),(140,-10), RAY, 90)
ray_beam((150,-10),(218,110),(252,104),(200,-10), RAY, 60)
ray_beam((190,-10),(252,84),(272,78),(224,-10), RAY, 50)
ray_beam((150,-10),(196,90),(214,88),(176,-10), RAY2, 60)

# ---------- ground ----------
g = new_canvas(W, H, name="ground")
g.poly([(0,194),(40,188),(84,194),(128,186),(170,194),(212,190),(256,196),(256,256),(0,256)], GROUND_D)
g.poly([(0,190),(44,184),(86,190),(128,182),(172,188),(214,186),(256,192),(256,256),(0,256)], GROUND)
# grass patches
for (cx, cy, r) in [(40,196,16),(92,204,20),(150,206,18),(52,222,24),(130,240,30),(200,224,22),(238,210,18),(16,226,26),(110,210,12)]:
    g.ellipse(cx, cy, r, r, GRASS_D)
for (cx, cy, r) in [(96,212,16),(58,232,20),(150,238,20),(205,214,14),(248,220,16)]:
    g.ellipse(cx, cy, r, r, GRASS)
g.poly([(0,222),(36,216),(70,222),(110,214),(150,222),(198,216),(256,224),(256,256),(0,256)], GROUND_D)
for (cx, cy, r) in [(70,246,26),(172,244,26),(18,252,30),(240,250,24),(120,256,30)]:
    g.ellipse(cx, cy, r, r, GROUND)
# highlights + small grass tufts
for (x, y) in [(86,206),(128,198),(202,204),(52,214)]:
    g.line(x, y, x+3, y-3, GRASS_L)
for (x, y) in [(150,210),(238,206),(64,232),(178,224)]:
    g.line(x, y, x-3, y-3, GRASS_L)
# few rocks and flowers
for (rx, ry, r) in [(36,236,5),(210,240,6),(160,252,4)]:
    g.ellipse(rx, ry, r, r, ROCK)
for (fx, fy) in [(46,224),(92,236),(186,228),(226,236)]:
    g.rect(fx, fy-2, 2, 2, FLOWER)
    g.rect(fx-2, fy, 2, 2, FLOWER)
    g.rect(fx, fy, 2, 2, FLOWER)
    g.rect(fx+2, fy, 2, 2, FLOWER)

# ---------- treant ----------
t = new_canvas(W, H, name="treant")

def thick(c, pts, col, wd):
    c.poly(pts, col)
    # outline the branch
    c.poly(pts, OUTLINE, fill=False)
    # wiggle texture
    for i in range(len(pts)-1):
        x0, y0 = pts[i]; x1, y1 = pts[i+1]
        c.line(x0, y0, x1, y1, col)

# --- canopy crown (head) ---
def leaf_lump(cx, cy, rx, ry, col):
    c.ellipse(cx, cy, rx, ry, col)
# big dark base crown
t.ellipse(128, 56, 30, 36, FOL_DD)
# outer silhouette outline (dark)
t.ellipse(128, 56, 33, 39, OUTLINE, fill=False)
# main foliage lumps
for (cx, cy, rx, ry, col) in [
    (112, 46, 20, 18, FOL_D),
    (146, 48, 22, 18, FOL_D),
    (128, 36, 20, 16, FOL_D),
    (100, 60, 18, 16, FOL_D),
    (158, 62, 18, 16, FOL_D),
    (126, 66, 22, 18, FOL_D),
    (112, 52, 16, 12, FOL),
    (146, 54, 16, 13, FOL),
    (128, 42, 14, 11, FOL),
    (104, 66, 12, 10, FOL),
    (156, 68, 13, 11, FOL),
    (122, 62, 10, 9, FOL_L),
    (140, 58, 11, 10, FOL_L),
    (132, 44, 9, 8, FOL_HL),
    (118, 50, 8, 7, FOL_HL),
    (150, 62, 9, 8, FOL_HL),
]:
    t.ellipse(cx, cy, rx, ry, col)
# outline key lumps
for (cx, cy, rx, ry) in [(128,56,33,39),(100,60,18,16),(158,62,18,16),(128,36,20,16)]:
    t.ellipse(cx, cy, rx, ry, OUTLINE, fill=False)
# small crown twigs
for (sx, sy, ex, ey) in [(96,40,84,32),(160,42,174,30),(90,56,78,52),(166,60,180,56),(128,20,124,12),(130,22,136,14)]:
    t.line(sx, sy, ex, ey, BARK_D)
    t.line(sx+1, sy, ex+1, ey, OUTLINE)
    t.line(sx-1, sy, ex-1, ey, OUTLINE)

# --- neck branch mass connecting crown to trunk ---
thick(t, [(118,72),(116,84),(112,92)], BARK, 10)
thick(t, [(138,72),(142,82),(150,90)], BARK, 10)
t.line(114, 84, 142, 82, BARK)

# --- trunk (body) ---
trunk_pts = [(112,88),(144,88),(150,106),(148,150),(156,176),(156,206),(102,206),(104,176),(110,150),(108,106)]
t.poly(trunk_pts, BARK)
t.poly(trunk_pts, OUTLINE, fill=False)
# bark shadow sides
t.poly([(142,90),(146,106),(144,150),(116,150),(140,150),(148,176),(150,206),(156,206),(156,176),(148,150),(150,106),(144,88)], BARK_D)
# dark center verticals
for pts, col in [
    ([(120,92),(118,120),(120,146),(118,176),(120,206)], BARK_DD),
    ([(134,90),(136,118),(134,146),(136,176),(134,206)], BARK_DD),
]:
    t.line(pts[0][0], pts[0][1], pts[1][0], pts[1][1], col)
    t.line(pts[1][0], pts[1][1], pts[2][0], pts[2][1], col)
    t.line(pts[2][0], pts[2][1], pts[3][0], pts[3][1], col)
    t.line(pts[3][0], pts[3][1], pts[4][0], pts[4][1], col)
# bark lightning streaks
for pts in [(122,92,126,146),(136,90,140,122),(140,180,138,150),(126,146,126,176)]:
    t.line(pts[0], pts[1], pts[2], pts[3], BARK_L)
# muscle shoulder bulges
t.ellipse(112, 100, 10, 16, BARK_D, fill=False)
t.ellipse(144, 100, 10, 16, BARK_D, fill=False)
# horizontal gnarled grooves
for y in (112, 138, 160, 182):
    t.line(110, y, 146, y-2, BARK_DD)
# knots
for (kx, ky) in [(118,172),(136,166),(110,118),(146,124)]:
    t.circle(kx, ky, 3, BARK_DD)
    t.circle(kx, ky, 2, BARK_D, fill=False)

# --- arms ---
def arm(points, wd):
    thick(t, points, BARK, wd)
    # claws
    sx, sy = points[-1]
    for (ex, ey) in [(sx-4, sy-26),(sx+4, sy-28),(sx+14, sy-18),(sx-16, sy-14),(sx+18, sy+2),(sx-20, sy-2)]:
        t.line(sx, sy, ex, ey, BARK_D)
        t.line(sx, sy+1, ex, ey+1, OUTLINE)
    # elbow branchlets
    mx, my = points[len(points)//2]
    for (ex, ey) in [(mx-2, my-18),(mx-2, my+16),(mx+2, my-16)]:
        t.line(mx, my, ex, ey, BARK_D)
arm([(112,102),(94,96),(78,100),(64,108)], 8)
arm([(146,102),(164,98),(180,104),(196,114)], 8)

# --- root legs rising ---
t.poly([(102,200),(96,172),(88,196),(84,214)], ROOT)
t.poly([(96,196),(92,180),(82,206),(80,220)], ROOT, fill=False)
t.poly([(154,200),(162,174),(172,198),(176,214)], ROOT)
t.poly([(160,196),(166,182),(176,206),(180,220)], ROOT, fill=False)
for pts in [(100,206,92,176,84,206),(158,208,166,178,174,208)]:
    pass
t.line(92,176, 84,206, ROOT_D)
t.line(166,178, 174,206, ROOT_D)

# --- moss patches on trunk ---
for (mx, my, rx, ry) in [(114,96,8,6),(132,92,7,5),(110,116,8,5),(140,134,9,6),(120,150,10,6),(112,178,8,5),(146,182,9,5)]:
    t.ellipse(mx, my, rx, ry, MOSS_D)
for (mx, my, rx, ry) in [(118,99,6,4),(136,95,5,3),(112,119,6,3),(138,137,7,4),(122,153,8,4),(114,180,6,3),(144,184,7,3)]:
    t.ellipse(mx, my, rx, ry, MOSS)
for (mx, my, rx, ry) in [(120,100,4,2),(139,96,3,2),(114,120,4,2),(136,138,4,2),(124,154,5,2),(116,181,4,2)]:
    t.ellipse(mx, my, rx, ry, MOSS_L)

# --- hanging vines ---
def vine(x, top, length, col):
    pts = [(x,top)]
    y = top
    d = 1
    for _ in range(length//6):
        x += d
        y += 6
        d = -d
        pts.append((x, y))
    t.poly(pts, col)
    x, y = pts[-1]
    t.line(x, y, x+3, y+4, col)
for (x, top, length) in [(108,92,30),(120,68,46),(136,60,52),(150,88,36),(96,78,26),(160,70,34),(128,52,40),(142,80,28)]:
    vine(x, top, length, MOSS_D)
    vine(x+2, top+6, length-10, MOSS)

# --- face ---
# brow ridges
t.poly([(114,116),(120,111),(126,116)], BARK_DD)
t.poly([(130,116),(136,111),(142,116)], BARK_DD)
# eye sockets
t.ellipse(121, 128, 7, 8, BARK_DD)
t.ellipse(137, 128, 7, 8, BARK_DD)
t.ellipse(121, 128, 9, 9, OUTLINE, fill=False)
t.ellipse(137, 128, 9, 9, OUTLINE, fill=False)
# glowing eyes
t.ellipse(121, 128, 5, 6, EYE)
t.ellipse(137, 128, 5, 6, EYE)
t.ellipse(121, 128, 3, 4, EYE_L)
t.ellipse(137, 128, 3, 4, EYE_L)
t.circle(121, 128, 1, EYE_C)
t.circle(137, 128, 1, EYE_C)
# eye glow spill onto bark
for (gx, gy, r, col) in [(121,128,11,EYE),(137,128,11,EYE),(129,122,4,EYE)]:
    pass
t.circle(121, 128, 12, EYE + (70,))
t.circle(137, 128, 12, EYE + (70,))

# mouth gash
t.poly([(120,148),(128,144),(136,148),(140,154),(136,159),(128,156),(120,152)], OUTLINE)
t.poly([(122,149),(128,147),(134,149),(136,154),(132,156),(126,154)], BARK_DD)

# --- rim light (god ray side, left) ---
for (x, y0, y1) in [(106,92,180)]:
    pass
t.poly([(106,92),(112,90),(110,150),(106,176)], BARK_HL)
t.poly([(104,92),(105,94),(104,176)], BARK_L)
# light on crown top
t.ellipse(124, 36, 16, 10, FOL_HL, fill=False)

# ---------- foregound shrubs in front of roots ----------
g2 = new_canvas(W, H, name="fg")
for (cx, cy, r) in [(96,214,12),(160,216,12)]:
    g2.ellipse(cx, cy, r, r, FOL_D)
    g2.circle(cx-4, cy-2, 5, FOL)
g2.poly([(90,214),(96,206),(102,214)], FOL)
g2.poly([(154,216),(160,208),(166,216)], FOL)
g2.poly([(90,214),(94,210),(102,214)], FOL_D)
g2.poly([(154,216),(158,210),(166,216)], FOL_D)

# ---------- composite ----------
result = flatten([bg, rays, g, t, g2], name="final")

result.stats_text() if 'result' in dir() else None
save("ancient-treant-boss", result)
print(result.stats_text())
finish(result)
