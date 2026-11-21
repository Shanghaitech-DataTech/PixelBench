c = new_canvas(64, 64, name="output")

# ---------------- palette ----------------
TUNNEL   = c.color("#0c1020", "tunnel")
TUNNEL2  = c.color("#161e32", "tunnel2")
WALL     = c.color("#262d40", "wall")
WALL2    = c.color("#3b4560", "wall2")
STREAK   = c.color("#3a4b70", "streak")
STREAK2  = c.color("#6786a8", "streak2")
FLOOR    = c.color("#555a68", "floor")
FLOOR2   = c.color("#686e7c", "floor2")
FLOOR_D  = c.color("#3f4450", "floor_d")
YELLOW   = c.color("#e8c24a", "yellow")
YELLOW_D = c.color("#a8872c", "yellow_d")
GLASS    = c.color("#9ed8ea", "glass")
GLASS_D  = c.color("#4d7f99", "glass_d")
FRAME    = c.color("#e2ecf4", "frame")
FRAME_D  = c.color("#8e99a8", "frame_d")
TRAIN    = c.color("#aeb6c4", "train")
TRAIN_L  = c.color("#d4dbe4", "train_l")
TRAIN_D  = c.color("#848d9c", "train_d")
TRAIN_S  = c.color("#5a6271", "train_s")
RED      = c.color("#cf4038", "red")
WIN      = c.color("#1b2638", "win")
WIN_L    = c.color("#93a9c2", "win_l")
LIGHT    = c.color("#fff4cf", "light")
LIGHT_D  = c.color("#d8c08a", "light_d")
GLOW     = c.color("#7e7a5f", "glow")
SIGN_BG  = c.color("#17477d", "sign_bg")
WHITE    = c.color("#eef3f8", "white")
BENCH    = c.color("#8a5a32", "bench")
BENCH_D  = c.color("#5e3c21", "bench_d")
METAL    = c.color("#98a2b2", "metal")
SK       = c.color("#e0a878", "sk")
SK3      = c.color("#f0c9a0", "sk3")
HAIR     = c.color("#2b2320", "hair")
HAIR2    = c.color("#5c3a22", "hair2")
COAT_A   = c.color("#3c6f8f", "coat_a")
COAT_B   = c.color("#8a3a52", "coat_b")
COAT_C   = c.color("#3d7a52", "coat_c")
PANT_A   = c.color("#2a3550", "pant_a")
PANT_B   = c.color("#43405c", "pant_b")
SHOE     = c.color("#15171f", "shoe")
SHADOW   = c.color("#43485a", "shadow")

# ================= ceiling =================
c.rect(0, 0, 64, 64, TUNNEL)
c.rect(0, 0, 64, 5, WALL)
for lx in (3, 19, 35, 51):
    c.rect(lx, 1, 10, 2, LIGHT)
    c.rect(lx, 3, 10, 1, LIGHT_D)
c.rect(0, 5, 64, 1, WALL2)

# ================= track void + tunnel mouth =================
c.rect(0, 6, 64, 38, TUNNEL)
c.rect(47, 6, 17, 38, TUNNEL2)
for sy, x0, x1 in ((20, 48, 63), (23, 51, 62), (26, 47, 63),
                   (30, 50, 60), (33, 48, 63), (36, 52, 62), (39, 49, 59)):
    c.line(x0, sy, x1, sy, STREAK)
c.line(48, 27, 58, 27, STREAK2)
c.line(49, 34, 59, 34, STREAK2)
for dx, dy, col in ((50, 18, LIGHT), (55, 17, LIGHT_D), (59, 17, STREAK2), (63, 16, STREAK2)):
    c.set(dx, dy, col)
# tunnel perspective: ceiling and wall lines converging to the vanishing point
c.line(47, 6, 63, 14, STREAK)
c.line(47, 12, 63, 15, STREAK)
c.line(47, 43, 63, 20, STREAK)
c.line(47, 38, 63, 19, STREAK)
c.line(47, 16, 63, 16, STREAK2)
for cx, cy in ((48, 9), (53, 12), (57, 13)):
    c.set(cx, cy, STREAK2)

# ================= arriving train =================
c.poly([(0, 15), (36, 15), (41, 17), (46, 22), (46, 42), (0, 42)], TRAIN)
c.rect(0, 15, 37, 2, TRAIN_L)
c.line(36, 15, 41, 17, TRAIN_L)
c.line(41, 17, 46, 22, TRAIN_L)
# carriage windows (above the barrier, fully readable)
c.rect(2, 19, 9, 9, WIN)
c.rect(30, 19, 6, 9, WIN)
for wx, ww in ((2, 9), (30, 6)):
    c.rect(wx, 19, ww, 1, WIN_L)
c.rect(4, 22, 2, 6, WIN_L)
c.rect(8, 23, 2, 5, WIN_L)
c.rect(33, 22, 2, 6, WIN_L)
# livery stripe + body shading
c.rect(0, 30, 46, 2, RED)
c.rect(0, 33, 46, 2, TRAIN_D)
c.rect(0, 37, 46, 5, TRAIN_S)
# open train doorway, warm interior light
c.rect(17, 17, 12, 24, TRAIN_D)
c.rect(18, 18, 10, 22, LIGHT)
c.rect(18, 18, 10, 1, WHITE)
c.rect(20, 23, 3, 10, TRAIN_S)   # passengers inside, backlit
c.rect(19, 21, 5, 3, TRAIN_S)
c.rect(25, 25, 3, 8, TRAIN_S)
c.rect(25, 23, 3, 3, TRAIN_S)
# cab front + headlight
c.rect(38, 20, 8, 7, WIN)
c.rect(38, 20, 8, 1, WIN_L)
c.set(40, 23, WIN_L)
c.rect(40, 31, 6, 4, TRAIN_L)
c.rect(41, 32, 5, 3, LIGHT)
c.line(46, 33, 51, 33, LIGHT_D)
c.line(46, 34, 54, 34, GLOW)
# horizontal motion smear
for sy, x0, x1 in ((18, 0, 14), (29, 2, 15), (29, 31, 37), (36, 2, 16), (36, 31, 38)):
    c.line(x0, sy, x1, sy, TRAIN_D)

# ================= platform edge doors (half height) =================
c.rect(0, 26, 64, 1, FRAME)
c.rect(0, 27, 64, 1, FRAME_D)
for px in (0, 16, 32, 48):
    c.rect(px, 27, 2, 16, FRAME)
    c.line(px + 1, 28, px + 1, 42, FRAME_D)
for px in (0, 32, 48):                      # closed bays
    c.line(px + 8, 28, px + 8, 42, FRAME_D)
    c.line(px + 4, 41, px + 6, 33, GLASS)
    c.line(px + 11, 40, px + 13, 35, GLASS_D)
    c.line(px + 2, 42, px + 15, 42, GLASS_D)
# open bay at x=16: leaves retracted both sides
c.rect(17, 27, 2, 16, FRAME_D)
c.rect(29, 27, 2, 16, FRAME_D)
c.rect(0, 43, 64, 1, FRAME_D)

# ================= platform floor =================
c.rect(0, 44, 64, 20, FLOOR)
c.rect(0, 44, 64, 1, FLOOR_D)
c.rect(0, 45, 64, 2, YELLOW)
c.dither(0, 46, 64, 1, [YELLOW_D, YELLOW], pattern="checker")
c.rect(0, 47, 64, 1, YELLOW_D)
c.dither(0, 57, 64, 4, [FLOOR, FLOOR2], pattern="bayer4")
c.line(0, 56, 63, 56, FLOOR_D)
c.line(0, 61, 63, 61, FLOOR_D)
# light spilling from the open doorway: tight pool, soft edge
c.poly([(19, 48), (29, 48), (30, 53), (18, 53)], GLOW)
c.rect(20, 48, 8, 2, LIGHT_D)
c.line(18, 53, 29, 53, GLOW)
for mx in (4, 36, 52):
    c.rect(mx, 49, 7, 1, YELLOW_D)

# ================= hanging signs =================
# exit sign over the tunnel end
c.line(42, 5, 42, 7, METAL)
c.line(58, 5, 58, 7, METAL)
c.rect(37, 7, 26, 10, SIGN_BG)
c.rect(37, 7, 26, 1, WHITE)
c.text(38, 9, "EXIT", WHITE)
# platform number + direction arrow
c.line(5, 5, 5, 7, METAL)
c.line(15, 5, 15, 7, METAL)
c.rect(2, 7, 17, 9, SIGN_BG)
c.rect(2, 7, 17, 1, WHITE)
c.text(4, 9, "3", WHITE)
c.poly([(10, 11), (14, 11), (14, 9), (17, 12), (14, 15), (14, 13), (10, 13)], WHITE)

# ================= bench =================
c.rect(46, 34, 17, 2, BENCH)
c.rect(46, 37, 17, 2, BENCH)
c.rect(46, 32, 2, 12, METAL)
c.rect(61, 32, 2, 12, METAL)
c.rect(45, 42, 19, 3, BENCH)
c.rect(45, 44, 19, 1, BENCH_D)
c.rect(47, 45, 2, 9, METAL)
c.rect(60, 45, 2, 9, METAL)
c.rect(46, 54, 4, 1, SHADOW)
c.rect(59, 54, 4, 1, SHADOW)

# ================= passenger A: far left, standing, waiting =================
c.rect(5, 33, 4, 4, SK)
c.rect(5, 32, 4, 2, HAIR)
c.rect(4, 37, 6, 7, COAT_A)
c.rect(10, 38, 1, 5, COAT_A)
c.set(10, 43, SK)
c.rect(5, 44, 2, 5, PANT_A)
c.rect(8, 44, 2, 5, PANT_A)
c.rect(4, 49, 3, 1, SHOE)
c.rect(8, 49, 3, 1, SHOE)
c.rect(3, 50, 9, 1, SHADOW)

# ================= passenger B: centre, striding for the open door =================
c.rect(25, 31, 4, 4, SK3)
c.rect(25, 30, 4, 2, HAIR2)
c.rect(23, 35, 6, 9, COAT_B)
c.rect(29, 36, 2, 4, COAT_B)
c.rect(31, 39, 2, 2, SK3)
c.rect(21, 37, 2, 4, COAT_B)
c.set(21, 41, SK3)
c.line(27, 44, 31, 53, PANT_B)
c.line(28, 44, 32, 53, PANT_B)
c.line(25, 44, 22, 53, PANT_B)
c.line(24, 44, 21, 53, PANT_B)
c.rect(31, 54, 3, 1, SHOE)
c.rect(20, 54, 3, 1, SHOE)
c.rect(20, 55, 14, 1, SHADOW)

# ================= passenger C: right, seated on the bench with a bag =================
c.rect(52, 28, 4, 4, SK)
c.rect(52, 27, 5, 2, HAIR)
c.rect(51, 32, 5, 9, COAT_C)
c.rect(56, 33, 1, 5, COAT_C)
c.rect(48, 41, 8, 3, PANT_A)
c.rect(48, 44, 3, 7, PANT_A)
c.rect(46, 51, 5, 2, SHOE)
c.rect(50, 33, 2, 7, COAT_C)
c.set(50, 40, SK)
c.rect(56, 39, 4, 4, BENCH_D)
c.line(56, 38, 59, 38, BENCH)

# ---- speed cues: pale trailing smear on the train body only ----
c.line(12, 44 - 15, 16, 44 - 15, TRAIN_L)
c.line(13, 33, 16, 33, TRAIN_L)

# ---- rim light so the seated figure reads against the dark tunnel ----
c.line(57, 27, 57, 31, WIN_L)
c.set(56, 26, WIN_L)
c.line(50, 32, 50, 33, WIN_L)

# ---- foreground floor depth ----
c.line(0, 62, 63, 62, FLOOR_D)
c.rect(0, 63, 64, 1, FLOOR2)

print(c.stats_text())
view(c)
finish(c)
