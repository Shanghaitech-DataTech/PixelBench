# ancient-dragon-battle: 256x256 epic fantasy battlefield
from pixelbench_api import *

W, H = 256, 256

# ---------- palette ----------
SKY_TOP    = "#2b1a3d"   # deep purple
SKY_MID    = "#6e2a4e"   # magenta dusk
SKY_LOW    = "#c8553d"   # burnt orange
SKY_SUN    = "#f2a65a"   # golden
SUN        = "#ffd98a"   # sun core
CLOUD_D    = "#3d1f38"
CLOUD_L    = "#e07a5f"
MTN_FAR    = "#4a2c52"
MTN_NEAR   = "#33203f"
GROUND     = "#241826"
GROUND_D   = "#1a1120"
CASTLE_ST  = "#3a3644"
CASTLE_D   = "#26232e"
CASTLE_L   = "#575066"
FIRE_1     = "#ffdd55"
FIRE_2     = "#ff9a3c"
FIRE_3     = "#e8491d"
SMOKE_1    = "#4a4453"
SMOKE_2    = "#6b6478"
SMOKE_3    = "#2e2a38"
DRAGON_B   = "#5a2438"   # dragon body dark red
DRAGON_B2  = "#7d3348"   # dragon belly / lighter
DRAGON_W   = "#3a1626"   # wing membrane dark
DRAGON_O   = "#1d0b13"   # dragon outline / darkest
DRAGON_E   = "#ffcf4d"   # dragon eye
KNIGHT_A   = "#8a93a5"   # armour light
KNIGHT_B   = "#5c6473"   # armour dark
KNIGHT_O   = "#14161d"   # dark outline
SPEAR      = "#6e5a3a"   # spear shaft
SPEAR_T    = "#b8c4cc"   # spear tip
SHIELD     = "#7a3040"   # shield red
SHIELD_B   = "#c9a227"   # shield boss gold
TOWER_W    = "#4a3f33"   # siege tower wood
TOWER_D    = "#2e2720"
TOWER_L    = "#6b5d48"
ARROW      = "#1d1a22"
ARROW_F    = "#ff9a3c"   # flaming arrow
EMBER      = "#ffb347"
SILH       = "#171019"   # far soldier silhouette
BANNER     = "#8e2f3c"

# ---------- sky ----------
sky = new_canvas(W, H, name="sky")
# vertical gradient bands
grad = [(0, 26, SKY_TOP), (26, 52, SKY_MID), (52, 78, SKY_LOW), (78, 100, SKY_SUN)]
for y0, y1, col in grad:
    sky.rect(0, y0, W, y1 - y0, col)
# smooth the band seams with dithering
sky.dither(0, 22, W, 8, [SKY_TOP, SKY_MID], pattern="bayer4")
sky.dither(0, 48, W, 8, [SKY_MID, SKY_LOW], pattern="bayer4")
sky.dither(0, 74, W, 8, [SKY_LOW, SKY_SUN], pattern="bayer4")
# sun low on horizon
sky.circle(178, 96, 14, SUN, fill=True)
sky.circle(178, 96, 10, "#fff3c4", fill=True)
# sun glow dither
for r, col in [(18, SKY_SUN), (24, SKY_LOW)]:
    for a in range(0, 360, 15):
        import math
        x = int(178 + r * math.cos(math.radians(a)))
        y = int(96 + r * math.sin(math.radians(a)) * 0.5)
        sky.set(x, y, col)
# clouds — dark bands across the sky
def cloud(c, x, y, w, col, h=3):
    c.rect(x, y, w, h, col)
    c.rect(x + 2, y - 2, w - 6, 2, col)
    c.rect(x + 5, y + h, w - 12, 1, col)
cloud(sky, 8, 30, 70, CLOUD_D)
cloud(sky, 30, 42, 90, CLOUD_D, h=2)
cloud(sky, 140, 26, 80, CLOUD_D)
cloud(sky, 150, 58, 70, CLOUD_L, h=2)
cloud(sky, 20, 66, 60, CLOUD_L, h=2)
cloud(sky, 90, 50, 50, CLOUD_D, h=2)
# thin streaks catching light
sky.rect(60, 36, 40, 1, CLOUD_L)
sky.rect(160, 44, 50, 1, CLOUD_L)
sky.rect(100, 70, 70, 1, "#f2a65a")

# ---------- distant mountains ----------
mtn = new_canvas(W, H, name="mountains")
mtn.poly([(0, 108), (30, 88), (60, 104), (95, 82), (130, 106), (165, 90),
          (200, 108), (230, 94), (256, 106), (256, 130), (0, 130)], MTN_FAR)
mtn.poly([(0, 122), (40, 100), (80, 118), (120, 98), (160, 120), (210, 102),
          (256, 120), (256, 140), (0, 140)], MTN_NEAR)
# snow caps catching sunset
for cx, cy in [(95, 82), (120, 98), (165, 90), (40, 100)]:
    mtn.set(cx, cy, "#c98a7a")
    mtn.set(cx + 1, cy + 1, "#c98a7a")
    mtn.set(cx - 1, cy + 1, "#a05a5a")

# ---------- ground ----------
gnd = new_canvas(W, H, name="ground")
gnd.rect(0, 138, W, H - 138, GROUND)
# battle-scarred foreground: darker patches, craters
gnd.rect(0, 200, W, H - 200, GROUND_D)
for cx, cy, r in [(40, 190, 8), (120, 210, 12), (200, 185, 7), (90, 175, 5), (170, 225, 10)]:
    gnd.circle(cx, cy, r, GROUND_D, fill=True)
    gnd.circle(cx, cy, r - 3, "#120b16", fill=True)
# scattered rocks / debris
for x, y in [(30, 165), (70, 172), (150, 160), (220, 170), (110, 195), (240, 200), (60, 220), (190, 240)]:
    gnd.set(x, y, "#3d3145")
    gnd.set(x + 1, y, "#3d3145")
    gnd.set(x, y + 1, "#2a2230")

# ---------- castle ----------
cas = new_canvas(W, H, name="castle")
CX = 128  # castle centre
# main keep
cas.rect(CX - 34, 92, 68, 50, CASTLE_ST)
cas.rect(CX - 34, 92, 68, 50, CASTLE_ST)
# keep shading
cas.rect(CX - 34, 92, 10, 50, CASTLE_L)
cas.rect(CX + 24, 92, 10, 50, CASTLE_D)
# keep crenellations
for i in range(0, 68, 8):
    cas.rect(CX - 34 + i, 86, 5, 6, CASTLE_ST)
# side towers
for tx in [CX - 52, CX + 38]:
    cas.rect(tx, 74, 14, 68, CASTLE_ST)
    cas.rect(tx, 74, 4, 68, CASTLE_L)
    cas.rect(tx + 10, 74, 4, 68, CASTLE_D)
    for i in range(0, 14, 5):
        cas.rect(tx + i, 68, 3, 6, CASTLE_ST)
# tall central spire
cas.rect(CX - 8, 58, 16, 40, CASTLE_ST)
cas.rect(CX - 8, 58, 4, 40, CASTLE_L)
cas.poly([(CX - 10, 58), (CX + 10, 58), (CX, 40)], CASTLE_D)
cas.line(CX, 40, CX, 30, CASTLE_D)
cas.rect(CX - 1, 30, 3, 4, BANNER)  # banner
# curtain wall
cas.rect(CX - 70, 118, 140, 24, CASTLE_ST)
cas.rect(CX - 70, 118, 6, 24, CASTLE_L)
for i in range(0, 140, 10):
    cas.rect(CX - 70 + i, 112, 6, 6, CASTLE_ST)
# gate
cas.rect(CX - 8, 122, 16, 20, CASTLE_D)
cas.poly([(CX - 8, 122), (CX + 8, 122), (CX + 8, 130), (CX - 8, 130)], "#17141d")
# arrow-slit windows (some glowing from fire inside)
for wx, wy in [(CX - 20, 100), (CX - 6, 96), (CX + 8, 100), (CX + 20, 96),
               (CX - 46, 84), (CX + 44, 84), (CX - 2, 66), (CX + 4, 66)]:
    cas.rect(wx, wy, 2, 5, "#1a1620")
for wx, wy in [(CX - 20, 100), (CX + 8, 100), (CX - 2, 66)]:
    cas.rect(wx, wy, 2, 5, FIRE_2)
# dark outline on castle silhouette edges
cas.rect(CX - 71, 117, 142, 1, KNIGHT_O)
cas.rect(CX - 35, 91, 70, 1, KNIGHT_O)

# ---------- fire on the castle ----------
fire = new_canvas(W, H, name="fire")
def flame(c, x, y, w, h, seed=0):
    # layered flame licks
    c.poly([(x, y + h), (x + w, y + h), (x + w // 2, y)], FIRE_3)
    c.poly([(x + 1, y + h), (x + w - 1, y + h), (x + w // 2 + (seed % 3) - 1, y + 2)], FIRE_2)
    c.poly([(x + 2, y + h), (x + w - 2, y + h), (x + w // 2, y + h - h // 2 + 1)], FIRE_1)
# fires on rooftops
flame(fire, CX - 30, 76, 10, 12, 1)
flame(fire, CX + 18, 80, 12, 14, 2)
flame(fire, CX - 4, 48, 8, 10, 0)
flame(fire, CX - 60, 104, 9, 10, 3)
flame(fire, CX + 50, 106, 10, 11, 1)
flame(fire, CX - 20, 104, 7, 8, 2)
flame(fire, CX + 30, 102, 8, 9, 0)
# fire at the gate
fire.rect(CX - 14, 138, 28, 6, FIRE_3)
fire.rect(CX - 10, 136, 20, 4, FIRE_2)
fire.rect(CX - 6, 134, 12, 3, FIRE_1)
# fire creeping down the wall
fire.rect(CX - 40, 112, 3, 8, FIRE_3)
fire.rect(CX + 44, 114, 3, 6, FIRE_3)
fire.set(CX - 41, 110, FIRE_2)
fire.set(CX + 45, 112, FIRE_2)

# ---------- smoke columns ----------
smk = new_canvas(W, H, name="smoke")
def smoke_col(c, x, y_top, y_bot, w0=3, w1=7):
    import random
    rnd = random.Random(x * 7 + y_top)
    n = y_bot - y_top
    for i in range(n):
        t = i / max(1, n - 1)
        w = int(w0 + (w1 - w0) * t)
        cx = x + int((rnd.random() - 0.5) * 6 * t) - int(t * 10)  # drift left
        col = SMOKE_1 if t < 0.4 else (SMOKE_2 if t < 0.75 else SMOKE_3)
        c.rect(cx, y_top + i, w, 1, col)
        if rnd.random() < 0.3:
            c.set(cx - 1, y_top + i, col)
smoke_col(smk, CX - 26, 20, 78, 3, 8)
smoke_col(smk, CX + 22, 30, 82, 3, 7)
smoke_col(smk, CX - 2, 8, 50, 2, 5)
smoke_col(smk, CX - 58, 60, 106, 2, 5)
smoke_col(smk, CX + 52, 64, 108, 2, 5)
# drifting smoke haze over the sky
for x, y, w in [(30, 84, 60), (110, 78, 70), (190, 88, 50), (60, 100, 40)]:
    smk.rect(x, y, w, 2, SMOKE_3)
    smk.rect(x + 5, y - 2, w - 15, 2, SMOKE_3)

# ---------- dragon ----------
drg = new_canvas(W, H, name="dragon")
DX, DY = 78, 34  # dragon centre (upper-left sky, flying toward castle)
# wings — spread, membrane dark
# left wing (behind, sweeping up-left)
drg.poly([(DX - 6, DY + 2), (DX - 40, DY - 16), (DX - 52, DY - 6),
          (DX - 30, DY + 6), (DX - 44, DY + 10), (DX - 8, DY + 10)], DRAGON_W)
# wing finger bones
drg.line(DX - 6, DY + 3, DX - 40, DY - 15, DRAGON_O)
drg.line(DX - 6, DY + 4, DX - 50, DY - 5, DRAGON_O)
drg.line(DX - 6, DY + 6, DX - 42, DY + 9, DRAGON_O)
# right wing (raised)
drg.poly([(DX + 6, DY), (DX + 34, DY - 22), (DX + 50, DY - 18),
          (DX + 30, DY - 4), (DX + 44, DY + 2), (DX + 8, DY + 8)], DRAGON_W)
drg.line(DX + 7, DY, DX + 34, DY - 21, DRAGON_O)
drg.line(DX + 8, DY + 1, DX + 49, DY - 17, DRAGON_O)
drg.line(DX + 8, DY + 4, DX + 42, DY + 1, DRAGON_O)
# body — serpentine, heading right toward castle
drg.ellipse(DX, DY + 6, 12, 6, DRAGON_B)
drg.ellipse(DX - 2, DY + 8, 9, 4, DRAGON_B2)  # belly highlight
# neck curving up to head
drg.line(DX + 10, DY + 4, DX + 18, DY - 4, DRAGON_B)
drg.line(DX + 11, DY + 6, DX + 19, DY - 2, DRAGON_B)
# head
drg.poly([(DX + 16, DY - 6), (DX + 30, DY - 4), (DX + 32, DY - 1),
          (DX + 24, DY + 2), (DX + 15, DY + 1)], DRAGON_B)
# jaw open with fire breath
drg.poly([(DX + 22, DY + 1), (DX + 30, DY + 1), (DX + 24, DY + 5)], DRAGON_O)
drg.set(DX + 27, DY - 3, DRAGON_E)  # eye
drg.set(DX + 28, DY - 3, DRAGON_E)
# horns
drg.line(DX + 17, DY - 6, DX + 13, DY - 10, DRAGON_O)
drg.line(DX + 19, DY - 7, DX + 16, DY - 11, DRAGON_O)
# fire breath streaming down toward castle
drg.line(DX + 26, DY + 4, DX + 34, DY + 16, FIRE_1)
drg.line(DX + 28, DY + 3, DX + 38, DY + 13, FIRE_2)
drg.line(DX + 25, DY + 5, DX + 30, DY + 18, FIRE_3)
drg.set(DX + 36, DY + 18, FIRE_2)
drg.set(DX + 32, DY + 20, FIRE_1)
# tail sweeping left with spade tip
drg.line(DX - 11, DY + 6, DX - 26, DY + 12, DRAGON_B)
drg.line(DX - 11, DY + 8, DX - 24, DY + 15, DRAGON_B)
drg.poly([(DX - 26, DY + 12), (DX - 32, DY + 10), (DX - 30, DY + 16)], DRAGON_O)
# back spikes
for i in range(5):
    sx = DX - 8 + i * 4
    drg.line(sx, DY + 1, sx - 1, DY - 3, DRAGON_O)
# legs tucked
drg.line(DX + 4, DY + 11, DX + 6, DY + 15, DRAGON_B)
drg.line(DX - 4, DY + 11, DX - 2, DY + 15, DRAGON_B)
drg.set(DX + 6, DY + 16, DRAGON_O)
drg.set(DX - 2, DY + 16, DRAGON_O)
# dark outline pass on body
drg.outline(DRAGON_O)

# ---------- siege towers ----------
twr = new_canvas(W, H, name="towers")
def siege_tower(c, x, y, w, h):
    # y = top of tower, sits on ground
    c.rect(x, y, w, h, TOWER_W)
    c.rect(x, y, 3, h, TOWER_L)          # lit side
    c.rect(x + w - 3, y, 3, h, TOWER_D)  # shaded side
    # dark outline
    c.rect(x - 1, y - 1, w + 2, 1, KNIGHT_O)
    c.rect(x - 1, y - 1, 1, h + 1, KNIGHT_O)
    c.rect(x + w, y - 1, 1, h + 1, KNIGHT_O)
    # drawbridge at top
    c.rect(x - 4, y, w + 8, 4, TOWER_D)
    c.rect(x - 4, y, w + 8, 1, KNIGHT_O)
    # platform rails
    c.rect(x, y + 4, w, 1, KNIGHT_O)
    # lattice cross-braces
    for i in range(y + 8, y + h - 4, 8):
        c.line(x + 2, i, x + w - 2, i + 5, TOWER_D)
        c.line(x + w - 2, i, x + 2, i + 5, TOWER_D)
    # wheels
    c.circle(x + 4, y + h + 1, 3, TOWER_D, fill=True)
    c.circle(x + w - 4, y + h + 1, 3, TOWER_D, fill=True)
    c.set(x + 4, y + h + 1, TOWER_L)
    c.set(x + w - 4, y + h + 1, TOWER_L)
    # soldiers pushing at base (silhouettes)
    for sx in [x - 3, x + w + 2]:
        c.rect(sx, y + h - 6, 3, 7, SILH)
        c.set(sx + 1, y + h - 8, SILH)
    # fire arrow hit on tower
    c.rect(x + w // 2, y + h // 3, 2, 3, FIRE_3)
    c.set(x + w // 2, y + h // 3 - 1, FIRE_2)
siege_tower(twr, 34, 118, 16, 34)
siege_tower(twr, 196, 114, 18, 38)

# battering ram near gate
twr.rect(96, 148, 40, 6, TOWER_W)
twr.rect(96, 148, 40, 1, KNIGHT_O)
twr.rect(96, 153, 40, 1, TOWER_D)
twr.poly([(92, 147), (98, 151), (92, 155)], "#8a8f99")  # ram head
for px in [100, 112, 124, 136]:
    twr.rect(px, 154, 3, 6, SILH)  # soldiers
    twr.set(px + 1, 152, SILH)

# ---------- knights on ramparts ----------
knt = new_canvas(W, H, name="knights")
def knight(c, x, y, face=1, shield=True, spear=True):
    # y = feet; ~10px tall
    c.rect(x, y - 9, 3, 3, KNIGHT_B)          # legs
    c.rect(x, y - 7, 4, 5, KNIGHT_A)          # torso
    c.set(x + (1 if face > 0 else 2), y - 10, KNIGHT_A)  # head
    c.rect(x, y - 11, 3, 2, KNIGHT_A)         # helm
    c.set(x + (2 if face > 0 else 0), y - 10, KNIGHT_O)  # helm slit
    c.rect(x - 1, y - 7, 1, 5, KNIGHT_O)      # outline left
    c.rect(x + 4, y - 7, 1, 5, KNIGHT_O)      # outline right
    if spear:
        c.line(x + (5 if face > 0 else -1), y - 20, x + (5 if face > 0 else -1), y - 2, SPEAR)
        c.poly([(x + (5 if face > 0 else -1), y - 22), (x + (5 if face > 0 else -1) - 1, y - 19),
                (x + (5 if face > 0 else -1) + 1, y - 19)], SPEAR_T)
    if shield:
        c.rect(x + (4 if face > 0 else -2), y - 7, 2, 4, SHIELD)
        c.set(x + (4 if face > 0 else -2), y - 6, SHIELD_B)
# knights along the curtain wall top (y=112 line)
for i, kx in enumerate(range(CX - 64, CX + 66, 12)):
    if CX - 10 <= kx <= CX + 8:  # skip gate
        continue
    knight(knt, kx, 112, face=1 if kx < CX else -1, shield=(i % 2 == 0), spear=(i % 3 != 2))
# knights on keep roof (y=86)
for kx in [CX - 26, CX - 14, CX + 12, CX + 24]:
    knight(knt, kx, 86, face=-1 if kx < CX else 1, shield=True, spear=True)
# knights in tower tops
knight(knt, CX - 49, 68, face=1, shield=False, spear=True)
knight(knt, CX + 41, 68, face=-1, shield=True, spear=False)
# banner on rampart
knt.line(CX - 58, 112, CX - 58, 96, SPEAR)
knt.poly([(CX - 58, 96), (CX - 50, 98), (CX - 58, 101)], BANNER)
knt.line(CX + 62, 112, CX + 62, 94, SPEAR)
knt.poly([(CX + 62, 94), (CX + 70, 96), (CX + 62, 99)], BANNER)

# ---------- soldiers in formation (foreground, silhouettes) ----------
sol = new_canvas(W, H, name="soldiers")
def soldier(c, x, y, hgt=14, spear_h=26, shield=False):
    # dark silhouette marching right, y = feet
    top = y - hgt
    c.rect(x, top + 3, hgt // 3 + 1, hgt - 5, SILH)   # body
    c.circle(x + hgt // 6, top + 1, hgt // 6, SILH, fill=True)  # head
    # spear
    c.line(x + hgt // 3 + 2, y - spear_h, x + hgt // 3 + 2, y - 2, SILH)
    c.poly([(x + hgt // 3 + 2, y - spear_h - 2), (x + hgt // 3 + 1, y - spear_h + 1),
            (x + hgt // 3 + 3, y - spear_h + 1)], "#4a4453")
    if shield:
        c.rect(x - 2, top + 4, 3, hgt - 8, "#241826")
# two ranks marching toward the castle
for row, (yy, hh, sp) in enumerate([(252, 16, 30), (244, 14, 26), (238, 12, 22)]):
    for i in range(9):
        x = 8 + i * 14 + (row * 5)
        if x > 240:
            continue
        soldier(sol, x, yy, hgt=hh, spear_h=sp, shield=(i % 2 == 0))
# a standard bearer
sol.line(196, 252, 196, 220, SILH)
sol.poly([(196, 220), (208, 224), (196, 229)], BANNER)
sol.rect(193, 236, 6, 16, SILH)
sol.circle(196, 234, 3, SILH, fill=True)

# ---------- arrows ----------
arr = new_canvas(W, H, name="arrows")
def arrow(c, x0, y0, x1, y1, flaming=False):
    c.line(x0, y0, x1, y1, ARROW)
    # head
    import math
    ang = math.atan2(y1 - y0, x1 - x0)
    for da in (2.6, -2.6):
        hx = int(x1 + 3 * math.cos(ang + da))
        hy = int(y1 + 3 * math.sin(ang + da))
        c.line(x1, y1, hx, hy, ARROW)
    if flaming:
        c.set(x0, y0, ARROW_F)
        c.set(x0 - 1, y0, FIRE_3)
        c.set(x0 + 1, y0 + 1, FIRE_2)
# volleys arcing up from the ground toward the castle
arrow(arr, 60, 150, 92, 118, flaming=True)
arrow(arr, 80, 146, 110, 116)
arrow(arr, 44, 158, 70, 122, flaming=True)
arrow(arr, 200, 148, 172, 118, flaming=True)
arrow(arr, 220, 152, 190, 120)
arrow(arr, 236, 158, 206, 124, flaming=True)
# arrows from the castle raining down
arrow(arr, 110, 96, 140, 130)
arrow(arr, 150, 94, 178, 128, flaming=True)
arrow(arr, 96, 100, 122, 136)
# stray arrows in the sky near the dragon
arrow(arr, 130, 60, 152, 78)
arrow(arr, 40, 70, 66, 88)

# ---------- embers ----------
emb = new_canvas(W, H, name="embers")
import random
rnd = random.Random(42)
for _ in range(90):
    x = rnd.randint(0, W - 1)
    y = rnd.randint(0, H - 1)
    # embers concentrate around the castle and drift up-left
    if 40 <= x <= 210 and 20 <= y <= 150 and rnd.random() < 0.85:
        col = rnd.choice([EMBER, FIRE_2, FIRE_1, FIRE_3])
        emb.set(x, y, col)
        if rnd.random() < 0.3:
            emb.set(x, y - 1, col)
# a few foreground sparks
for _ in range(20):
    x = rnd.randint(0, W - 1)
    y = rnd.randint(150, H - 1)
    emb.set(x, y, rnd.choice([EMBER, FIRE_3]))

# ---------- foreground framing (dark vignette rocks) ----------
fr = new_canvas(W, H, name="frame")
fr.poly([(0, 256), (0, 216), (24, 232), (52, 222), (70, 256)], "#120b16")
fr.poly([(256, 256), (256, 210), (232, 228), (206, 224), (186, 256)], "#120b16")
fr.rect(0, 254, W, 2, "#120b16")

# ---------- composite ----------
result = flatten([sky, mtn, gnd, smk, cas, fire, twr, knt, sol, arr, drg, emb, fr], name="result")
print(result.stats_text())
save("ancient-dragon-battle", result, indexed=True)
finish(result)
