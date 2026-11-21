from pixelbench_api import *

c = input_canvas.copy(name='output')
c.clear()

def sky_color(y):
    if y < 10:  return '#0c0411'
    if y < 20:  return '#150a1c'
    if y < 30:  return '#1f0d23'
    if y < 40:  return '#2a1026'
    if y < 50:  return '#341328'
    if y < 58:  return '#3d1424'
    if y < 66:  return '#45151f'
    return '#491420'

for y in range(128):
    col = sky_color(y)
    for x in range(256):
        c.set(x, y, col)

MOONX, MOONY, MOONR = 120, 28, 18
GLOWO = c.color('#3d1030', name='glow_outer')
GLOWI = c.color('#5b1730', name='glow_inner')
MOOND = c.color('#6e0e1c', name='moon_dark')
MOONM = c.color('#9c1426', name='moon_mid')
MOONB = c.color('#cf2a34', name='moon_bright')
CRAT  = c.color('#420812', name='crater')
CLOUD1= c.color('#260a18', name='cloud1')
CLOUD2= c.color('#330e1e', name='cloud2')
CAST = c.color('#0c030d', name='castle')
CAST2= c.color('#150614', name='castle_back')
CAST3= c.color('#1d0917', name='castle_front')
WIN  = c.color('#ff3b22', name='window')
WIN2 = c.color('#ffac3e', name='window2')
GRND = c.color('#060207', name='ground')
STAR = c.color('#ffb8a8', name='star')

# --- blood moon ---
c.circle(MOONX, MOONY, MOONR + 8, GLOWO)
c.circle(MOONX, MOONY, MOONR + 4, GLOWI)
c.circle(MOONX, MOONY, MOONR, MOOND)
# shading: bright upper-right
c.circle(MOONX + 1, MOONY - 1, MOONR - 3, MOONM)
c.circle(MOONX + 2, MOONY - 2, MOONR - 7, MOONB)
# craters
for (dx, dy, r) in [(-2, 3, 3), (3, 4, 2), (-5, 0, 2), (2, -1, 2), (0, 6, 2), (-6, 5, 2), (5, 2, 3), (-3, -3, 2), (6, -4, 1)]:
    c.circle(MOONX + dx, MOONY + dy, r, CRAT)

# --- stars (avoid moon area x 92..148, y 4..52) ---
stars = [(12,8),(30,16),(52,6),(74,12),(86,24),(150,10),(168,20),(190,8),(220,14),(244,6),(14,26),(40,34),(80,36),(178,30),(208,26),(236,34),(60,22),(250,20),(24,44),(196,40),(234,44),(10,52),(90,52),(150,50),(70,58)]
for (sx, sy) in stars:
    c.set(sx, sy, STAR)

# --- clouds across the moon ---
for (cy, col, x0, x1, step, rr) in [(22, CLOUD1, 74, 176, 12, 3), (44, CLOUD2, 88, 168, 10, 3), (50, CLOUD1, 40, 210, 14, 4)]:
    i = 0
    for x in range(x0, x1, step):
        c.ellipse(x, cy + (i % 3 - 1), rr + (i % 2), rr, col)
        i += 1

# --- distant mountain silhouettes behind castle ---
for (x0, x1, pk, col) in [(0, 60, 86, CAST2), (56, 118, 80, CAST2), (110, 170, 74, CAST2), (162, 226, 82, CAST2), (218, 254, 78, CAST2)]:
    c.poly([(x0, 122), ((x0 + x1) // 2, pk), (x1, 122)], CAST2)

# --- castle ---
# back wall with crenellations
c.rect(8, 100, 240, 21, CAST2)
for x in range(8, 248, 8):
    c.rect(x, 96, 5, 5, CAST2)

# main keep (center): wide pyramid
c.poly([(92, 80), (128, 46), (164, 80)], CAST)
c.rect(92, 80, 72, 42, CAST)
# tall central spire above the keep
c.rect(124, 34, 8, 12, CAST)
c.poly([(128, 18), (121, 34), (135, 34)], CAST)
c.circle(128, 16, 1, WIN)   # glowing orb on the spire
for x in range(92, 164, 7):
    c.rect(x, 74, 5, 7, CAST)   # keep crenellation under roof
# side towers
for (bx, bw, py) in [(46, 40, 56), (170, 40, 56)]:
    c.poly([(bx - 2, 82), (bx + bw // 2, py), (bx + bw + 2, 82)], CAST)
    c.rect(bx, 82, bw, 40, CAST)
# outer towers
for (bx, bw, py) in [(14, 30, 68), (212, 30, 68)]:
    c.poly([(bx - 2, 92), (bx + bw // 2, py), (bx + bw + 2, 92)], CAST)
    c.rect(bx, 92, bw, 30, CAST)

# front wall between towers with crenellations
c.rect(10, 106, 236, 16, CAST3)
for x in range(10, 246, 8):
    c.rect(x, 102, 5, 5, CAST3)

# --- gates & windows (red glow) ---
# keep great window
c.rect(122, 82, 12, 40, WIN)
c.rect(124, 78, 8, 5, WIN)
c.rect(124, 122, 8, 1, WIN)
# keep side windows
c.rect(100, 88, 6, 14, WIN)
c.rect(150, 88, 6, 14, WIN)
c.rect(106, 108, 4, 10, WIN2)
c.rect(146, 108, 4, 10, WIN2)
# tower windows
c.rect(60, 92, 6, 16, WIN)
c.rect(190, 92, 6, 16, WIN)
c.rect(22, 100, 4, 10, WIN2)
c.rect(230, 100, 4, 10, WIN2)
# keep gate
c.rect(120, 116, 16, 6, WIN)
c.rect(122, 112, 12, 5, WIN)
c.rect(126, 110, 4, 3, WIN)

# window bars in great window
for bx in (126, 130):
    for by in range(84, 120, 6):
        c.set(bx, by, CAST)
        c.set(bx + 1, by, CAST)

# pennants on spires
c.poly([(128, 40), (133, 45), (128, 50)], WIN)
c.poly([(66, 52), (71, 57), (66, 62)], WIN)
c.poly([(190, 52), (195, 57), (190, 62)], WIN)
c.poly([(29, 64), (33, 68), (29, 73)], WIN2)
c.poly([(227, 64), (231, 68), (227, 73)], WIN2)

# ground + rocks
c.rect(0, 120, 256, 8, GRND)
# blood-red glow reflected on the ground under the moon
c.ellipse(120, 121, 42, 4, c.color('#3d0a12', name='ground_glow'))
for x in range(2, 244, 9):
    c.poly([(x, 123), (x + 4, 115), (x + 9, 123)], CAST3)
    c.poly([(x + 4, 123), (x + 7, 118), (x + 11, 123)], CAST)

# --- lightning bolt in the moody sky (upper left) ---
LIGHT = c.color('#fdeff0', name='lightning')
def polyline(pts, col):
    for i in range(len(pts) - 1):
        c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col)

polyline([(38, 4), (30, 22), (38, 26), (28, 48)], LIGHT)
polyline([(36, 12), (52, 26), (42, 30), (60, 46)], LIGHT)
# a faint wider glow beside it
polyline([(39, 6), (29, 26), (39, 31), (30, 48)], c.color('#7a3a48', name='light_glow'))

# --- bats ---
def stamp_bat(x, y, col):
    pat = [
        "X.....X",
        "XX...XX",
        "XXXXXXX",
        ".XX.XX.",
        "..XXX..",
    ]
    for dy, row in enumerate(pat):
        for dx, ch in enumerate(row):
            if ch == 'X':
                c.set(x + dx - 3, y + dy, col)

for (bx, by) in [(104, 24), (162, 22), (88, 44), (178, 38), (60, 50), (196, 14), (132, 52), (228, 54)]:
    stamp_bat(bx, by, CAST)

# --- inspection regions ---
import json
def region_chars(x0, y0, x1, y1, w=256):
    # map each color to a char by palette index
    pal = c.palette()
    idx = {}
    for p in pal:
        idx[p['index']] = p['index']
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    def ch(i):
        return charset[i % len(charset)]
    lines = []
    for yy in range(y0, y1 + 1):
        lines.append("".join(ch(c.get(xx, yy)) for xx in range(x0, x1 + 1)))
    return "\n".join(lines)

print(c.stats_text())
print("palette size:", len(c.palette()))

# Save a preview for reference (not submitted)
save("demon_castle", c)

finish(c)
