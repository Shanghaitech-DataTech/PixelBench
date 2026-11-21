from pixelbench_api import new_canvas, finish, flatten, save

W, H = 64, 64
c = new_canvas(W, H, background=(30, 19, 12), name="tavern")

# Palette
OUT       = c.color((24, 14, 8),   name="outline")
WALL_DARK = c.color((30, 19, 12),  name="wall_dark")
WALL_A    = c.color((74, 49, 28),  name="wall_a")
WALL_B    = c.color((62, 40, 23),  name="wall_b")
FLOOR_D   = c.color((26, 17, 10),  name="floor_dark")
FLOOR_A   = c.color((58, 38, 21),  name="floor_a")
FLOOR_B   = c.color((48, 31, 18),  name="floor_b")
BAR_TOP   = c.color((133, 86, 45), name="bar_top")
BAR_TOP_H = c.color((152, 102, 54), name="bar_top_hi")
BAR_FRONT = c.color((98, 62, 33),  name="bar_front")
BAR_SHAD  = c.color((72, 44, 24),  name="bar_shadow")
SHELF     = c.color((112, 74, 38), name="shelf")
SHELF_SH  = c.color((78, 50, 26),  name="shelf_shadow")
BACK_GLOW = c.color((96, 63, 35),  name="backbar_glow")
BACK_GLOW_HI = c.color((122, 82, 46), name="backbar_glow_hi")
LAMP_SHADE= c.color((58, 36, 20),  name="lamp_shade")
GLOW_OUT  = c.color((80, 52, 28),  name="glow_out")
GLOW_IN   = c.color((150, 105, 55), name="glow_in")
BULB      = c.color((255, 220, 120), name="bulb")
GLASS     = c.color((206, 188, 146), name="glass")
GLASS_HI  = c.color((232, 218, 180), name="glass_hi")
LIQUID_A  = c.color((196, 132, 48), name="liquid_amber")
LIQUID_B  = c.color((120, 70, 40),  name="liquid_dark")
STOOL_SEAT= c.color((96, 60, 34),  name="stool_seat")
STOOL_LEG = c.color((58, 36, 20),  name="stool_leg")
BARREL    = c.color((108, 70, 38), name="barrel")
BARREL_HI = c.color((126, 84, 46), name="barrel_hi")
BARREL_BD = c.color((44, 27, 15),  name="barrel_band")
BOTTLE_G  = c.color((74, 140, 82), name="bottle_green")
BOTTLE_A  = c.color((196, 128, 52), name="bottle_amber")
BOTTLE_R  = c.color((172, 66, 58), name="bottle_red")
BOTTLE_B  = c.color((78, 118, 172), name="bottle_blue")
BOTTLE_HI = c.color((238, 236, 214), name="bottle_hi")

# ---------------- Wall ----------------
c.rect(0, 0, 64, 32, WALL_DARK)
for i in range(8):
    x = i * 8
    col = WALL_A if i % 2 == 0 else WALL_B
    c.rect(x, 0, 7, 32, col)

# ceiling shadow
c.rect(0, 0, 64, 1, OUT)

# ---------------- Floor ----------------
c.rect(0, 52, 64, 12, FLOOR_D)
for j, y in enumerate([52, 55, 58, 61]):
    col = FLOOR_A if j % 2 == 0 else FLOOR_B
    c.rect(0, y, 64, 3, col)
c.rect(2, 51, 60, 2, (20, 12, 7))

# ---------------- Shelf ----------------
c.rect(4, 23, 56, 4, OUT)
c.rect(5, 24, 54, 2, SHELF)
c.rect(5, 26, 54, 1, SHELF_SH)

# warm back-bar glow strip behind the glasses
c.rect(4, 27, 56, 5, BACK_GLOW)
c.rect(4, 27, 56, 1, BACK_GLOW_HI)

def bottle(cx, bottom, h, col):
    # dark silhouette
    c.rect(cx - 2, bottom - h, 5, h + 1, OUT)
    # body
    c.rect(cx - 1, bottom - h + 1, 3, h - 1, col)
    # neck
    c.rect(cx, bottom - h + 1, 1, 3, col)
    # cap
    c.set(cx, bottom - h, OUT)
    # shine
    c.set(cx - 1, bottom - h + 2, BOTTLE_HI)

bottles = [(8, 11, BOTTLE_G), (15, 13, BOTTLE_A), (22, 10, BOTTLE_B),
           (29, 12, BOTTLE_R), (36, 11, BOTTLE_G), (43, 13, BOTTLE_A),
           (50, 10, BOTTLE_B), (57, 12, BOTTLE_R)]
for bx, bh, col in bottles:
    bottle(bx, 23, bh, col)

# ---------------- Lamps ----------------
for lx in (13, 32, 51):
    c.line(lx, 0, lx, 3, OUT)
    c.rect(lx - 3, 2, 7, 5, OUT)
    c.rect(lx - 2, 3, 5, 3, LAMP_SHADE)
    c.rect(lx - 4, 5, 9, 5, GLOW_OUT)
    c.rect(lx - 2, 6, 5, 3, GLOW_IN)
    c.rect(lx - 1, 7, 3, 2, BULB)

# ---------------- Bar counter ----------------
c.rect(2, 32, 60, 20, OUT)
c.rect(3, 33, 58, 3, BAR_TOP)
c.rect(3, 33, 58, 1, BAR_TOP_H)
c.rect(3, 36, 58, 14, BAR_FRONT)
c.rect(3, 47, 58, 4, BAR_SHAD)
# wood grain on front
for gx in range(8, 60, 8):
    c.line(gx, 37, gx, 45, OUT)

# ---------------- Glasses on bar ----------------
def glass(cx, bottom, h, liquid):
    c.rect(cx - 3, bottom - h, 7, h + 1, OUT)
    c.rect(cx - 2, bottom - h + 1, 5, h - 1, GLASS)
    c.rect(cx - 2, bottom - 3, 5, 3, liquid)
    c.line(cx - 1, bottom - h + 1, cx - 1, bottom - 3, GLASS_HI)

glass(13, 35, 8, LIQUID_A)
glass(26, 35, 8, LIQUID_B)
glass(39, 35, 8, LIQUID_A)
glass(50, 35, 8, LIQUID_B)

# ---------------- Barrels ----------------
def barrel(cx, cy):
    c.ellipse(cx, cy, 7, 7, OUT, fill=True)
    c.ellipse(cx, cy, 6, 6, BARREL, fill=True)
    c.line(cx - 5, cy - 3, cx + 5, cy - 3, BARREL_BD)
    c.line(cx - 5, cy + 3, cx + 5, cy + 3, BARREL_BD)
    c.line(cx - 3, cy - 5, cx - 3, cy + 5, BARREL_HI)

barrel(9, 55)
barrel(55, 55)

# ---------------- Stools ----------------
def stool(cx):
    c.rect(cx - 4, 48, 9, 5, OUT)
    c.rect(cx - 3, 49, 7, 3, STOOL_SEAT)
    c.line(cx - 3, 52, cx - 3, 61, STOOL_LEG)
    c.line(cx + 2, 52, cx + 2, 61, STOOL_LEG)
    c.line(cx, 52, cx, 58, STOOL_LEG)
    c.rect(cx - 4, 56, 8, 2, STOOL_LEG)

stool(21)
stool(32)
stool(43)

# ---------------- Smoke layer ----------------
smoke = new_canvas(W, H, background=None, name="smoke")
SMOKE1 = smoke.color((210, 196, 168, 46), name="smoke_light")
SMOKE2 = smoke.color((180, 168, 144, 34), name="smoke_dim")
# wispy horizontal bands drifting near the lamps and above the bar
for row, (y, x0, x1, col) in enumerate([
        (9, 6, 36, SMOKE1),
        (11, 18, 48, SMOKE2),
        (14, 8, 42, SMOKE2),
        (17, 26, 60, SMOKE2),
        (20, 12, 52, SMOKE1),
]):
    for x in range(x0, x1):
        if (x + row) % 3 != 0:
            smoke.set(x, y, col)
        smoke.set(x + 1, y + 1, col)

result = flatten([c, smoke], name="result")

print(result.stats_text())
print(result.matrix_text(region=(0, 0, 63, 31)))
print(result.matrix_text(region=(0, 32, 63, 63)))

finish(result)
