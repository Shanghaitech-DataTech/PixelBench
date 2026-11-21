try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 256
OUT = "#0d0a12"

c = new_canvas(W, H, background="#191036", name="dragon-battle")

# ---------------- SKY: dramatic sunset gradient ----------------
band_ys = [0, 30, 58, 84, 106, 126, 144, 158]
band_cs = ["#191036", "#2e1745", "#4b1d4e", "#6f2547",
           "#93313a", "#bb4a2c", "#e07030", "#f2953e"]
for i, (y0, col) in enumerate(zip(band_ys, band_cs)):
    y1 = band_ys[i + 1] if i + 1 < len(band_ys) else 172
    c.rect(0, y0, W, y1 - y0, col)
for i in range(1, len(band_cs)):
    yb = band_ys[i]
    c.dither(0, yb - 2, W, 2, [band_cs[i - 1], band_cs[i]])
    c.dither(0, yb, W, 2, [band_cs[i], band_cs[i - 1]])

# sun, low on the horizon
c.circle(58, 140, 22, "#f7a04a")
c.circle(58, 140, 15, "#ffd98a")
c.circle(58, 140, 9, "#fff3c8")

# clouds
def streak(x, y, w, h, col):
    c.rect(x, y, w, h, col)

for x, y, w in [(18, 34, 44), (70, 28, 30), (120, 40, 52),
                (190, 30, 40), (150, 52, 36), (30, 56, 40)]:
    streak(x, y, w, 3, "#241543")
for x, y, w in [(100, 70, 60), (20, 78, 46), (170, 66, 44)]:
    streak(x, y, w, 3, "#5c2545")
for x, y, w in [(10, 120, 54), (80, 112, 40), (140, 126, 60)]:
    streak(x, y, w, 3, "#f2a05a")
for x, y, w in [(30, 124, 30), (150, 130, 40), (200, 118, 34)]:
    streak(x, y, w, 2, "#ffcf8a")

# ---------------- MOUNTAINS ----------------
c.poly([(0, 152), (18, 130), (34, 144), (52, 122), (74, 142), (92, 128),
        (112, 146), (132, 132), (150, 148), (172, 126), (194, 144),
        (214, 130), (236, 146), (255, 134), (255, 172), (0, 172)], "#3b2650")
c.poly([(0, 164), (26, 142), (48, 158), (70, 144), (96, 160), (118, 152),
        (140, 166), (140, 178), (0, 178)], "#2a1c40")

# ---------------- GROUND ----------------
c.rect(0, 166, W, H - 166, "#262015")
c.poly([(104, 256), (108, 196), (126, 178), (150, 170), (180, 164),
        (214, 160), (255, 158), (255, 256)], "#2b2318")
# road to the gate
c.poly([(184, 172), (208, 172), (224, 256), (162, 256)], "#31281a")
# foreground shadow strip + texture
c.rect(0, 234, W, H - 234, "#1a140e")
for i in range(60):
    x = (i * 53) % W
    y = 236 + (i * 29) % 18
    c.set(x, y, "#241c12")

# ---------------- CASTLE ----------------
STONE = "#4d4a55"; STONE_D = "#35323d"; STONE_L = "#63606e"
SLIT = "#191621"; KEEP = "#3f3c47"

# keep behind the wall
c.rect(178, 88, 38, 44, KEEP)
for x in range(180, 214, 7):
    c.rect(x, 84, 4, 4, KEEP)
c.rect(178, 88, 38, 3, "#4a4753")
for wx, wy in [(186, 98), (198, 94), (206, 104), (190, 112), (204, 116)]:
    c.rect(wx, wy, 2, 3, "#ff9a3c")

# curtain wall
c.rect(150, 122, 92, 52, STONE)
for x in range(150, 242, 7):
    c.rect(x, 118, 4, 4, STONE)
c.rect(150, 122, 92, 2, STONE_L)
for yy in range(128, 168, 6):
    for xx in range(152, 240, 10):
        c.set(xx + ((yy // 6) % 2) * 5, yy, STONE_D)
c.rect(150, 168, 92, 6, STONE_D)
for sx in [160, 174, 214, 228]:
    c.rect(sx, 138, 2, 5, SLIT)
    c.rect(sx, 150, 2, 5, SLIT)

# left tower
c.rect(140, 100, 18, 74, STONE)
for x in range(140, 158, 6):
    c.rect(x, 96, 4, 4, STONE)
c.rect(140, 100, 2, 74, STONE_L)
c.rect(156, 100, 2, 74, STONE_D)
for wy in [112, 128, 144]:
    c.rect(147, wy, 2, 5, SLIT)

# right tower (burning)
c.rect(232, 92, 20, 82, STONE)
for x in range(232, 252, 6):
    c.rect(x, 88, 4, 4, STONE)
c.rect(232, 92, 2, 82, STONE_L)
for wy in [106, 122, 138]:
    c.rect(241, wy, 2, 5, SLIT)
c.rect(233, 94, 18, 16, "#6e3a2e")   # fire-lit stone

# gate
c.rect(186, 150, 20, 24, "#14111a")
c.rect(188, 154, 16, 20, "#3a2a18")
for i in range(3):
    c.line(191 + i * 4, 154, 191 + i * 4, 173, "#241a0e")
c.set(189, 163, "#c8a03a"); c.set(202, 163, "#c8a03a")

# banners
for bx in [158, 220]:
    c.rect(bx, 124, 3, 9, "#8a2430")
    c.set(bx + 1, 133, "#c8a03a")

# ---------------- FIRE ----------------
def flame(cc, cx, base, h, w):
    cc.poly([(cx - w, base), (cx - w // 2, base - h), (cx, base - h - 3),
             (cx + w // 2, base - h + 2), (cx + w, base)], "#ff6b1a")
    cc.poly([(cx - w // 2, base), (cx - w // 3, base - int(h * 0.6)),
             (cx, base - int(h * 0.7)), (cx + w // 3, base - int(h * 0.4)),
             (cx + w // 2, base)], "#ffb020")
    cc.poly([(cx - 1, base), (cx, base - int(h * 0.35)), (cx + 1, base)], "#ffe066")

flame(c, 238, 90, 14, 5)
flame(c, 247, 90, 10, 4)
flame(c, 206, 120, 12, 5)
flame(c, 218, 120, 9, 4)
flame(c, 196, 120, 8, 4)
flame(c, 196, 86, 10, 4)

# ---------------- SMOKE ----------------
def smoke_col(cc, x, y0, n, w0, drift=-1):
    for i in range(n):
        y = y0 - i * 4
        if y < -3:
            break
        w = w0 + i // 2
        xx = x + drift * i // 2 + (2 if i % 2 else 0)
        col = ["#3f3f49", "#54545e", "#6a6a74"][i % 3]
        cc.rect(xx, y, w, 3, col)

smoke_col(c, 243, 84, 22, 5, -1)
smoke_col(c, 210, 112, 14, 4, -1)
smoke_col(c, 196, 80, 10, 3, -1)

# ---------------- FIGURES LAYER (outlined) ----------------
f = new_canvas(W, H, name="figures")

def knight(fx, x, y, face=1, tone=0):
    ARM = ["#a7adb8", "#939aa6"][tone]
    ARMD = "#5f6570"; HELM = "#b6bcc6"; PLUME = "#8a2430"
    SHLD = "#8a2430"; GOLD = "#c8a03a"; WOOD = "#6b4a2a"; TIP = "#d8dce2"
    fx.rect(x + 1, y - 12, 3, 3, HELM)
    fx.set(x + 2, y - 13, PLUME)
    fx.set(x + (3 if face > 0 else 1), y - 11, "#141019")
    fx.rect(x + 1, y - 9, 3, 4, ARM)
    fx.rect(x + 1, y - 5, 1, 5, ARMD)
    fx.rect(x + 3, y - 5, 1, 5, ARMD)
    sx = x - 1 if face > 0 else x + 4
    fx.rect(sx, y - 9, 2, 5, SHLD)
    fx.set(sx, y - 9, GOLD)
    if face > 0:
        fx.line(x + 5, y - 16, x + 2, y + 1, WOOD)
        fx.set(x + 5, y - 16, TIP); fx.set(x + 4, y - 15, TIP)
    else:
        fx.line(x, y - 16, x + 3, y + 1, WOOD)
        fx.set(x, y - 16, TIP); fx.set(x + 1, y - 15, TIP)

# knights on the ramparts
for i, kx in enumerate([154, 162, 170, 178, 212, 220, 228, 236]):
    knight(f, kx, 122, face=1 if i % 2 else -1, tone=i % 2)
# knights on the left tower
knight(f, 144, 100, face=-1)
knight(f, 151, 100, face=1, tone=1)

def siege_tower(fx, x, gy):
    WOOD = "#5f4126"; WOODD = "#3c2a16"; WOODL = "#7a5632"; HIDE = "#6e4a28"
    fx.rect(x, gy - 48, 22, 42, WOOD)
    fx.rect(x - 2, gy - 52, 26, 5, WOODL)
    fx.rect(x - 2, gy - 52, 26, 1, "#8a6238")
    fx.line(x + 1, gy - 46, x + 20, gy - 10, WOODD)
    fx.line(x + 20, gy - 46, x + 1, gy - 10, WOODD)
    fx.rect(x, gy - 34, 22, 1, WOODD)
    fx.rect(x, gy - 20, 22, 1, WOODD)
    fx.rect(x + 5, gy - 32, 12, 11, HIDE)
    fx.line(x + 5, gy - 32, x + 16, gy - 21, WOODD)
    fx.circle(x + 4, gy - 4, 3, WOODD)
    fx.circle(x + 17, gy - 4, 3, WOODD)
    fx.set(x + 4, gy - 4, WOOD); fx.set(x + 17, gy - 4, WOOD)
    for sx in [x + 3, x + 10, x + 17]:
        fx.rect(sx, gy - 58, 3, 3, "#8f95a0")
        fx.rect(sx, gy - 55, 3, 3, "#6f7580")
        fx.line(sx + 2, gy - 62, sx + 1, gy - 52, "#3c2a16")

siege_tower(f, 92, 206)
siege_tower(f, 122, 200)

def soldier(fx, x, y, col):
    fx.set(x + 1, y - 9, col)
    fx.rect(x, y - 8, 3, 4, col)
    fx.rect(x, y - 4, 3, 4, col)
    fx.line(x + 4, y - 13, x + 2, y + 1, "#171221")
    fx.set(x + 4, y - 13, "#9aa0aa")

for x in range(8, 66, 9):
    soldier(f, x, 216, "#2a2338")
for x in range(4, 74, 9):
    soldier(f, x, 224, "#322a44")
for x in range(0, 84, 9):
    soldier(f, x, 233, "#2a2338")
for x in range(0, 94, 10):
    soldier(f, x, 244, "#241e30")
# banner carrier in the formation
f.line(84, 214, 84, 244, "#3c2a16")
f.rect(85, 216, 8, 6, "#8a2430")
f.set(85, 216, "#c8a03a")

f.outline(OUT)
c.blit(f, 0, 0)

# ---------------- DRAGON ----------------
d = new_canvas(112, 72, name="dragon")
BODY = "#2c1f36"; BELLY = "#4a3556"; MEMB = "#6e2b45"; DARK = "#1c1428"

# tail
d.poly([(64, 42), (86, 32), (94, 24), (104, 28), (98, 34), (88, 46), (68, 50)], BODY)
d.poly([(94, 24), (106, 18), (100, 34)], DARK)
# wings
d.poly([(42, 38), (14, 6), (24, 18), (26, 12), (34, 24), (38, 18), (46, 30)], MEMB)
d.line(42, 38, 14, 6, DARK)
d.line(42, 38, 26, 12, DARK)
d.line(42, 38, 34, 24, DARK)
d.poly([(60, 38), (88, 6), (78, 18), (76, 12), (68, 24), (64, 18), (56, 30)], MEMB)
d.line(60, 38, 88, 6, DARK)
d.line(60, 38, 76, 12, DARK)
d.line(60, 38, 68, 24, DARK)
# body + belly
d.ellipse(50, 42, 20, 8, BODY)
d.ellipse(50, 45, 15, 5, BELLY)
# back spikes
for sx in range(38, 64, 6):
    d.poly([(sx, 35), (sx + 2, 30), (sx + 4, 35)], DARK)
# neck + head
d.poly([(36, 42), (28, 24), (34, 20), (44, 36)], BODY)
d.poly([(34, 22), (26, 12), (16, 8), (8, 12), (6, 16), (12, 17), (20, 18), (28, 26)], BODY)
d.poly([(10, 16), (2, 22), (14, 21)], "#241a30")
d.set(8, 17, "#e8e4da"); d.set(11, 18, "#e8e4da")
d.set(22, 14, "#ffcf4a"); d.set(21, 14, "#ff9a3c")
d.line(24, 10, 30, 4, DARK)
d.line(20, 9, 24, 3, DARK)
# legs + claws
d.poly([(42, 48), (40, 56), (46, 56), (46, 48)], BODY)
d.poly([(56, 48), (54, 56), (60, 56), (60, 48)], BODY)
d.set(40, 57, "#e8e4da"); d.set(54, 57, "#e8e4da")

d.outline(OUT)
c.blit(d, 106, 10)

# ---------------- ARROWS ----------------
def arrow(cc, x, y):
    cc.line(x, y, x + 9, y - 6, "#1a1424")
    cc.set(x + 9, y - 6, "#cfd4dc")
    cc.set(x + 8, y - 5, "#cfd4dc")

for ax, ay in [(24, 118), (44, 132), (66, 112), (88, 142), (112, 96),
               (36, 152), (58, 158), (140, 108), (76, 96), (100, 122)]:
    arrow(c, ax, ay)

# ---------------- EMBERS ----------------
emb = [(150, 70), (160, 55), (170, 90), (185, 40), (200, 60), (210, 30),
       (225, 75), (235, 45), (190, 100), (160, 110), (140, 95), (220, 110),
       (205, 85), (175, 20), (245, 60), (130, 60), (155, 35), (230, 20)]
for i, (ex, ey) in enumerate(emb):
    c.set(ex, ey, ["#ffe066", "#ffb020", "#ff6b1a"][i % 3])

print(c.stats_text())
finish(c)
