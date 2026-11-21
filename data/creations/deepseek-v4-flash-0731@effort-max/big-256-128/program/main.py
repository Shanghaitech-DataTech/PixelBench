from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')
W, H = 256, 128

def recolor(y0, y1, mapping):
    for y in range(y0, y1):
        for x in range(W):
            idx = out.get(x, y)
            if idx in mapping:
                out.set(x, y, mapping[idx])

# ---------- SKY -> blood-red twilight (rows 0..41) ----------
SKY = {1:(28,5,18), 2:(52,9,22), 3:(88,16,28), 4:(132,24,38), 5:(176,44,52),
       6:(34,7,14), 7:(110,24,38), 8:(150,36,48), 9:(196,84,74),
       10:(244,110,94), 12:(255,205,185), 11:(238,100,86), 18:(40,12,16),
       19:(230,120,90), 22:(150,36,50), 25:(90,26,34), 21:(70,18,30)}
recolor(0, 42, SKY)

# ---------- SEA -> blood sea (rows 36..83) ----------
SEA = {37:(150,44,58), 38:(118,30,46), 44:(92,20,34), 45:(66,14,26),
       46:(44,8,18), 47:(30,5,12), 4:(168,60,66), 5:(190,80,78),
       12:(255,150,120), 10:(240,110,90), 11:(200,60,58), 6:(24,4,10),
       49:(58,12,24), 48:(70,16,28), 50:(84,18,32), 51:(120,40,52),
       54:(20,6,10), 55:(16,5,8), 53:(14,6,12), 56:(130,40,50)}
recolor(36, 84, SEA)

# shore line + castle ground base
out.rect(0, 78, W, 6, (24,8,16))
out.rect(0, 84, W, H-84, (16,7,14))

# ---------- DEMON KING'S CASTLE ----------
WALL   = (22,10,20)
WALL2  = (34,14,26)
ROOF   = (56,16,38)
GLOW   = (255,150,70)
GLOW2  = (200,80,50)
DARK   = (10,4,10)

# backdrop curtain wall + crenellations
out.rect(0, 96, W, 32, WALL)
for x in range(0, W, 8):
    out.rect(x, 92, 4, 4, WALL)
out.rect(0, 104, W, 24, WALL2)

def tower(x, w, top, roof_tip, wy=1, win1=2, win2=1, ty=88):
    out.rect(x, top, w, 104 - top + 23, WALL)
    out.poly([(x, top), (x + w//2, roof_tip), (x + w, top)], ROOF)
    out.rect(x + w//2 - 1, roof_tip, 2, 6, ROOF)
    out.rect(x + 3, top + wy, 3, 5, GLOW)
    out.rect(x + w - 6, top + wy + 2, 3, 4, GLOW2)
    out.rect(x + w//2 - 1, top + 2, 3, 4, GLOW2)

# flanking towers (left -> right)
tower(6,   16, 84,  62, 2)
tower(30,  18, 80,  52, 2)
tower(56,  20, 76,  46, 2)
tower(84,  18, 72,  44, 2)

# great central keep
out.rect(106, 64, 44, 63, WALL)
for x in range(104, 152, 8):
    out.rect(x, 60, 4, 4, WALL)
out.poly([(104, 66), (128, 36), (152, 66)], ROOF)
out.rect(125, 22, 6, 16, WALL)          # spire
out.poly([(126, 22), (142, 26), (126, 30)], (198,42,46))  # pennant
out.rect(126, 30, 4, 8, WALL)
out.rect(112, 70, 5, 7, GLOW)
out.rect(124, 72, 5, 7, GLOW)
out.rect(136, 70, 5, 7, GLOW)
out.rect(118, 52, 4, 5, GLOW2)
out.rect(138, 52, 4, 5, GLOW2)
out.poly([(112, 70), (128, 66), (144, 70), (144, 88), (112, 88)], GLOW2, fill=False)
# great gate (arch) in keep
out.circle(128, 92, 16, DARK)
out.rect(112, 92, 32, 35, DARK)
out.circle(128, 94, 11, GLOW)
out.rect(117, 94, 22, 33, GLOW)
out.rect(120, 98, 16, 29, (255,180,90))
for i in range(4):
    out.rect(121 + i*5, 96, 2, 32, DARK)

# right flanking towers
tower(158, 18, 74, 48, 2)
tower(184, 20, 80, 50, 2)
tower(212, 16, 86, 64, 2)
tower(236, 14, 90, 70, 1)
# torch dots along wall
for tx in range(8, 256, 24):
    out.rect(tx, 94, 2, 3, GLOW)

# ---------- BLOOD MOON with "DEMON KING" ----------
out.circle(128, 34, 33, (226,60,54))
out.circle(150, 48, 25, (96,14,24))
out.circle(128, 32, 31, (238,70,60))
out.circle(128, 34, 34, (190,44,46), fill=False)
for (cx, cy, r, col) in [(108,22,4,(150,28,40)), (118,38,6,(148,26,40)),
                        (136,20,3,(160,34,46)), (120,50,3,(150,28,40)),
                        (100,30,2,(166,40,50)), (142,36,3,(160,34,46)),
                        (130,22,2,(166,40,50))]:
    out.circle(cx, cy, r, col)
out.text(99, 20, "DEMON KING", (255,238,228))

# moon reflection in the blood sea
for y in range(42, 70):
    wd = max(2, 24 - (y - 42) // 3)
    rr = max(150 - (y - 42) * 3, 26)
    gg = 30 + (y - 42)
    bb = 36 + (y - 42)
    out.rect(128 - wd//2, y, wd, 1, (rr, gg, bb))

# ---------- BATS ----------
BAT = (12,4,10)
def bat(x, y, s=1):
    out.poly([(x, y), (x+2*s, y-2*s), (x+5*s, y), (x+3*s, y+1*s), (x, y)], BAT)
    out.poly([(x+5*s, y), (x+8*s, y-2*s), (x+10*s, y), (x+7*s, y+1*s), (x+5*s, y)], BAT)

bat(28, 44, 1)
bat(56, 20, 1)
bat(170, 40, 1)
bat(202, 14, 1)
bat(238, 50, 1)
bat(84, 10, 1)

print(out.stats_text())
finish(out)
