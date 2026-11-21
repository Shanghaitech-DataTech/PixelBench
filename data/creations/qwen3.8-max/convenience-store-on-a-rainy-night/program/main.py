import random
random.seed(11)

c = new_canvas(64, 64, name="store")

# ---------------- palette ----------------
SKY       = "#080d1e"
SKY2      = "#111a34"
FAR_BLD   = "#0d1428"
FAR_WIN   = "#6d5c3a"
ROOF      = "#151b30"
ROOF_HI   = "#2a3352"
WALL      = "#1b2138"
WALL_HI   = "#2b3455"
FRAME     = "#2b3455"
FRAME_HI  = "#4a5885"
TRIM      = "#0f1424"

SIGN_BG   = "#eef6ee"
SIGN_SH   = "#bccfc2"
SIGN_INK  = "#26355c"
RED       = "#d4483c"
GREEN     = "#41ab74"

GLOW      = "#fff4cc"
WARM      = "#ffdf9b"
WARM2     = "#eec279"
FLOOR_I   = "#e2b26c"
FLOOR_SH  = "#c3934f"
SHELF     = "#b8813f"
SHELF_D   = "#8b5c2b"
PROD_R    = "#e0574a"
PROD_B    = "#5b8fd8"
PROD_G    = "#63bb7f"
PROD_W    = "#fff6e0"
COOL      = "#d3e8ef"
COOL_D    = "#a2c5d4"
GLASS_R   = "#d9ecf2"
DOOR_GL   = "#b7d2dd"

SIDEWALK  = "#181e33"
SIDEWALK2 = "#212947"
TILE      = "#2b3454"
CURB      = "#3b4670"
STREET    = "#10162a"
SPILL_D   = "#3a3550"
SPILL_M   = "#6b5844"
SPILL_B   = "#a9874c"
PUDDLE    = "#0d1730"
PUDDLE_R  = "#c9a45a"
PUDDLE_HI = "#4d5f8e"
SHADOW    = "#0b1020"

RAIN_FAR  = "#37476f"
RAIN      = "#64789f"
RAIN_HI   = "#93a7cf"
RAIN_GL   = "#44547c"

BIKE      = "#0e1322"
BIKE_HI   = "#59648a"
WHEEL     = "#46547c"
WHEEL_HI  = "#8b9cc4"
METAL     = "#77839f"
RACK      = "#2a3352"

COAT      = "#f2c33d"
COAT_D    = "#bd8c26"
COAT_HI   = "#ffe286"
SKIN      = "#e8b48c"
HAIR      = "#33261d"
BOOT      = "#221d31"
PANTS     = "#2f3b60"
UMB_R     = "#c4483e"
UMB_B     = "#4272c6"
UMB_T     = "#3fae94"
UMB_D     = "#241f33"
OPEN_BG   = "#a8322a"
OPEN_FG   = "#ffeccd"
CLERK     = "#4a6ea8"

def tube(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)
    c.line(x0, y0 + 1, x1, y1 + 1, col)

# ---------------- sky ----------------
c.rect(0, 0, 64, 7, SKY)
c.rect(0, 5, 64, 2, SKY2)
c.rect(0, 2, 11, 5, FAR_BLD)
c.rect(9, 4, 6, 3, FAR_BLD)
c.rect(50, 3, 14, 4, FAR_BLD)
for (x, y) in [(2, 3), (5, 4), (7, 3), (53, 4), (57, 5), (60, 4)]:
    c.set(x, y, FAR_WIN)

# ---------------- roof + sign ----------------
c.rect(0, 7, 64, 1, ROOF_HI)
c.rect(0, 8, 64, 1, ROOF)
c.dither(0, 8, 64, 1, [ROOF, "#3b3450"], pattern="checker")

c.rect(0, 9, 64, 6, SIGN_BG)
c.rect(0, 14, 64, 1, SIGN_SH)
c.rect(0, 9, 64, 1, "#ffffff")
# original (non-brand) sign graphics: cup icon + abstract word bars
c.rect(4, 10, 7, 1, SIGN_INK)
c.rect(5, 11, 5, 3, PROD_W)
c.rect(5, 12, 5, 1, RED)
c.set(5, 14, SIGN_SH); c.set(9, 14, SIGN_SH)
c.rect(14, 10, 20, 2, SIGN_INK)
c.rect(14, 13, 13, 1, "#5d6f9c")
c.rect(37, 10, 4, 4, GREEN)
c.set(38, 11, PROD_W)
c.rect(45, 10, 15, 2, SIGN_INK)
c.rect(45, 13, 9, 1, "#5d6f9c")
c.rect(0, 15, 64, 2, TRIM)
for x in range(4, 64, 8):
    c.set(x, 16, GLOW)
    c.set(x, 15, SPILL_B)

# ---------------- storefront shell ----------------
c.rect(0, 17, 64, 30, FRAME)
c.rect(0, 17, 64, 1, FRAME_HI)
c.rect(0, 18, 64, 1, "#212a48")

# ================= LEFT WINDOW =================
c.rect(3, 20, 23, 22, WARM)
c.rect(3, 20, 23, 2, GLOW)
c.rect(4, 22, 11, 1, SHELF_D)
c.rect(4, 23, 1, 14, SHELF_D)
c.rect(14, 23, 1, 14, SHELF_D)
prods = [PROD_R, PROD_B, PROD_W, PROD_G, PROD_R, PROD_W]
for row, by in ((24, 26), (29, 31), (34, 36)):
    c.rect(5, by, 9, 1, SHELF)
    for i in range(4):
        c.rect(5 + i * 2, row, 2, by - row, prods[(i + row) % len(prods)])
c.rect(16, 33, 10, 1, WARM2)
c.rect(16, 34, 10, 4, SHELF_D)
c.rect(17, 35, 8, 1, "#6f4a24")
c.rect(17, 29, 4, 4, "#39456b")
c.rect(18, 30, 2, 2, COOL)
c.rect(22, 29, 4, 4, CLERK)
c.rect(23, 31, 2, 2, PROD_W)
c.rect(23, 26, 2, 3, SKIN)
c.rect(23, 25, 2, 1, HAIR)
c.rect(3, 38, 23, 4, FLOOR_I)
c.rect(3, 38, 23, 1, FLOOR_SH)
for x in (6, 12, 19):
    c.rect(x, 39, 1, 3, WARM2)

# ================= RIGHT WINDOW =================
c.rect(42, 20, 20, 22, WARM)
c.rect(42, 20, 20, 2, GLOW)
c.rect(42, 22, 20, 9, OPEN_BG)
c.rect(42, 22, 20, 1, "#7d231d")
c.rect(42, 30, 20, 1, "#7d231d")
c.text(42, 23, "OPEN", OPEN_FG, spacing=0, font="5x7")
c.rect(43, 32, 9, 7, COOL_D)
c.rect(43, 32, 9, 1, COOL)
c.rect(47, 32, 1, 7, "#8fb3c4")
for yy in (34, 36, 38):
    c.rect(43, yy, 9, 1, COOL)
for (xx, yy, cc) in [(44, 33, PROD_B), (45, 35, PROD_R), (49, 33, PROD_G),
                     (50, 35, PROD_W), (44, 37, PROD_W), (49, 37, PROD_B)]:
    c.set(xx, yy, cc)
c.rect(54, 32, 7, 7, SHELF)
for yy in (34, 36):
    c.rect(54, yy, 7, 1, SHELF_D)
for (xx, yy, cc) in [(55, 33, PROD_R), (58, 33, PROD_B), (55, 35, PROD_G),
                     (58, 35, PROD_W), (56, 37, PROD_R), (59, 37, PROD_B)]:
    c.set(xx, yy, cc)
c.rect(42, 39, 20, 3, FLOOR_I)
c.rect(42, 39, 20, 1, FLOOR_SH)

# ---------------- glass reflections ----------------
c.line(6, 41, 18, 21, GLASS_R)
c.line(8, 41, 20, 21, GLASS_R)
c.line(45, 41, 57, 21, GLASS_R)
c.line(47, 41, 59, 21, GLASS_R)

# ---------------- frames / mullions ----------------
c.rect(26, 18, 2, 29, FRAME)
c.rect(40, 18, 2, 29, FRAME)
c.rect(26, 18, 1, 29, FRAME_HI)
c.rect(40, 18, 1, 29, FRAME_HI)
c.rect(0, 18, 3, 24, FRAME)
c.rect(61, 18, 3, 24, FRAME)
c.rect(0, 18, 1, 24, FRAME_HI)
c.rect(2, 42, 24, 1, FRAME_HI)
c.rect(41, 42, 20, 1, FRAME_HI)
c.rect(0, 42, 26, 5, WALL)
c.rect(41, 42, 23, 5, WALL)
c.rect(0, 42, 26, 1, WALL_HI)
c.rect(41, 42, 23, 1, WALL_HI)
for x in range(1, 26, 6):
    c.rect(x, 44, 4, 2, "#222a45")
for x in range(43, 60, 6):
    c.rect(x, 44, 4, 2, "#222a45")

# ================= DOORWAY =================
c.rect(28, 20, 12, 27, GLOW)
c.rect(28, 20, 12, 2, "#fffbe8")
c.rect(28, 40, 12, 7, FLOOR_I)
c.rect(28, 40, 12, 1, FLOOR_SH)
c.rect(29, 26, 3, 10, WARM2)
c.rect(30, 28, 2, 3, PROD_R)
# slid-back door leaf (right)
c.rect(36, 20, 4, 26, DOOR_GL)
c.rect(36, 20, 4, 1, FRAME_HI)
c.rect(36, 20, 1, 26, FRAME)
c.rect(39, 20, 1, 26, FRAME)
c.rect(36, 45, 4, 1, FRAME)
c.line(37, 44, 39, 24, GLASS_R)
c.rect(36, 30, 1, 6, METAL)
c.rect(27, 19, 14, 1, FRAME_HI)
c.rect(28, 46, 12, 1, "#2c3550")
c.rect(28, 47, 12, 1, SHADOW)

# ---------------- ground shadow line ----------------
c.rect(0, 47, 64, 1, SHADOW)

# ---------------- sidewalk ----------------
c.rect(0, 48, 64, 12, SIDEWALK)
c.rect(0, 48, 64, 2, SPILL_M)
c.dither(0, 50, 64, 1, [SPILL_M, SPILL_D], pattern="checker")
c.rect(0, 51, 64, 2, SPILL_D)
c.dither(0, 53, 64, 1, [SPILL_D, SIDEWALK2], pattern="checker")
c.rect(0, 54, 64, 3, SIDEWALK2)
c.dither(0, 57, 64, 1, [SIDEWALK2, SIDEWALK], pattern="checker")
c.rect(0, 58, 64, 2, SIDEWALK)
c.poly([(28, 48), (40, 48), (46, 57), (22, 57)], SPILL_M)
c.poly([(30, 48), (38, 48), (40, 53), (28, 53)], SPILL_B)
c.dither(22, 55, 24, 3, [SPILL_M, SPILL_D], pattern="checker")
for x in (20, 40, 60):
    c.line(x, 48, x - 2, 59, TILE)
c.line(0, 53, 63, 53, TILE)
for (dx, dy) in [(6, 50), (58, 49), (16, 56), (60, 55)]:
    c.set(dx, dy, PUDDLE_HI)
c.rect(0, 60, 64, 1, CURB)
c.rect(0, 61, 64, 1, "#232c4c")
c.rect(0, 62, 64, 2, STREET)
c.rect(0, 62, 64, 1, "#1b2440")
for x in range(2, 62, 7):
    c.rect(x, 63, 3, 1, SPILL_D)
for (dx, dy) in [(31, 62), (35, 63), (26, 63), (44, 62), (50, 63), (12, 63), (57, 62)]:
    c.set(dx, dy, PUDDLE_R)

# ---------------- puddles + reflections ----------------
c.poly([(24, 50), (44, 50), (50, 59), (18, 59)], PUDDLE)
c.poly([(18, 50), (24, 50), (20, 55), (14, 55)], PUDDLE)
c.poly([(46, 51), (60, 51), (63, 58), (44, 58)], PUDDLE)
c.poly([(2, 56), (14, 56), (12, 60), (0, 60)], PUDDLE)
c.line(24, 50, 44, 50, PUDDLE_HI)
c.line(46, 51, 60, 51, PUDDLE_HI)
c.line(2, 56, 14, 56, PUDDLE_HI)
for (rx, w, y0, y1) in [(33, 4, 51, 59), (26, 2, 52, 58), (41, 2, 52, 58),
                        (52, 3, 52, 58), (8, 2, 57, 60)]:
    for y in range(y0, y1):
        if (y + rx) % 3 != 2:
            c.rect(rx - w // 2, y, w, 1, PUDDLE_R if y % 3 == 0 else SPILL_B)
for (rx, y0, y1) in [(22, 53, 58), (48, 54, 58), (12, 58, 60)]:
    for y in range(y0, y1):
        if y % 2 == 0:
            c.set(rx, y, PUDDLE_HI)

# ---------------- bicycle ----------------
BIKE_F  = "#9fb0d6"
BIKE_DK = "#0e1322"
c.circle(7, 52, 5, WHEEL, fill=False)
c.circle(18, 52, 5, WHEEL, fill=False)
for (hx, hy) in [(5, 48), (4, 49), (4, 50), (16, 48), (15, 49), (14, 50)]:
    c.set(hx, hy, WHEEL_HI)
for (hx, hy) in [(9, 56), (10, 55), (20, 56), (21, 55)]:
    c.set(hx, hy, WHEEL_HI)
c.set(7, 52, METAL); c.set(18, 52, METAL)
c.line(7, 52, 12, 53, BIKE_F)
c.line(12, 53, 10, 44, BIKE_F)
c.line(12, 53, 17, 45, BIKE_F)
c.line(10, 44, 17, 45, BIKE_F)
c.line(17, 45, 18, 52, BIKE_F)
c.line(7, 52, 10, 46, BIKE_DK)
c.line(18, 52, 15, 47, BIKE_DK)
c.line(7, 53, 18, 53, BIKE_DK)
c.rect(8, 43, 4, 1, BIKE_HI)
c.rect(8, 43, 2, 1, BIKE_F)
c.line(16, 43, 19, 43, BIKE_HI)
c.set(19, 43, METAL); c.set(16, 43, METAL)
c.rect(11, 52, 3, 2, BIKE_DK)
c.set(13, 54, METAL)
c.set(5, 47, RED)          # rear reflector
c.set(20, 42, GLOW)        # dynamo lamp
c.rect(19, 44, 5, 4, "#38436b")
c.rect(19, 44, 5, 1, METAL)
for xx in (20, 22):
    c.line(xx, 45, xx, 47, BIKE_DK)
# warm rim light from the shop on top edges
for (hx, hy) in [(8, 42), (9, 42), (17, 44), (18, 44), (20, 43), (21, 43)]:
    c.set(hx, hy, SPILL_B)
c.rect(2, 57, 21, 1, SHADOW)

# ---------------- umbrella rack ----------------
for (ux, uy, col) in [(44, 36, UMB_R), (47, 34, UMB_B), (50, 35, UMB_T), (52, 37, UMB_R)]:
    c.line(ux, uy + 12, ux + 1, uy, col)
    c.set(ux, uy + 1, col)
    c.set(ux + 2, uy + 1, col)
    c.set(ux + 1, uy - 1, UMB_D)
    c.set(ux, uy + 13, UMB_D)
c.rect(43, 48, 11, 6, "#38436b")
c.rect(43, 48, 11, 1, METAL)
c.rect(43, 49, 1, 5, "#4d5f8e")
c.rect(53, 49, 1, 5, "#1e2540")
for xx in (45, 48, 51):
    c.rect(xx, 49, 1, 5, "#242c4a")
c.rect(42, 54, 13, 1, SHADOW)
for (dx, dy) in [(45, 55), (50, 56), (47, 57)]:
    c.set(dx, dy, PUDDLE_HI)

# ---------------- person in raincoat ----------------
# wet reflection under feet
c.rect(30, 48, 4, 1, SPILL_B)
c.rect(30, 50, 4, 1, COAT_D)
c.rect(31, 52, 2, 1, SPILL_M)
# legs + boots
c.rect(29, 41, 2, 4, PANTS)
c.rect(32, 41, 2, 4, PANTS)
c.rect(28, 45, 3, 2, BOOT)
c.rect(32, 45, 4, 2, BOOT)
c.rect(28, 45, 3, 1, "#3a3350")
# coat
c.rect(28, 29, 8, 10, COAT)
c.rect(28, 39, 8, 1, COAT)
c.rect(28, 40, 8, 1, COAT_D)
c.rect(35, 29, 1, 10, COAT_D)
c.rect(28, 29, 1, 10, COAT_HI)
c.rect(32, 32, 1, 7, COAT_D)
c.rect(29, 35, 6, 1, COAT_D)
# hood + head
c.rect(28, 23, 6, 6, COAT)
c.rect(29, 22, 4, 1, COAT)
c.set(28, 23, None); c.set(33, 23, None)
c.rect(29, 23, 2, 1, COAT_HI)
c.rect(30, 25, 3, 3, SKIN)
c.rect(30, 25, 3, 1, HAIR)
c.rect(29, 25, 1, 3, COAT_D)
c.rect(28, 28, 6, 1, COAT_D)
# arms + carried umbrella
c.rect(27, 30, 2, 7, COAT)
c.rect(27, 37, 2, 1, COAT_D)
c.set(27, 38, SKIN); c.set(28, 38, SKIN)
c.rect(35, 31, 1, 5, COAT_D)
c.line(28, 38, 25, 48, UMB_D)
c.line(27, 38, 24, 47, UMB_R)
c.set(24, 48, UMB_D)

# ---------------- rain ----------------
for i in range(34):
    x = random.randint(-4, 68)
    y = random.choice(list(range(0, 8)) + list(range(47, 61)))
    k = random.randint(1, 3)
    col = RAIN_FAR if k == 1 else (RAIN if k == 2 else RAIN_HI)
    c.line(x, y, x - k, y + 2 * k, col)
for i in range(16):
    x = random.randint(0, 63)
    y = random.randint(9, 44)
    c.line(x, y, x - 1, y + 2, RAIN_GL)
for i in range(6):
    x = random.randint(0, 63)
    y = random.randint(42, 44)
    c.line(x, y, x - 1, y + 2, RAIN_GL)
for i in range(10):
    x = random.randint(0, 62)
    y = random.randint(48, 60)
    c.rect(x, y, 2, 1, RAIN_FAR)

view(c)
print(c.stats_text())
finish(c)
