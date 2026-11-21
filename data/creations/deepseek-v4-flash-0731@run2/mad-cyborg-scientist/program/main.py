import math

c = new_canvas(64, 64)

def col(s):
    return c.color(s)

# ---------------- palette ----------------
bkg = col("#0b0f17")
halo1 = col("#0e1320")
halo2 = col("#121a2c")
halo3 = col("#17223a")

skin_hi = col("#f2c89a")
skin = col("#d9a878")
skin_sh = col("#b57a52")
skin_dk = col("#7a4a30")
skin_line = col("#3a2012")

metal_hi = col("#d8e0e8")
metal = col("#9aa2ac")
metal_mid = col("#66707c")
metal_dk = col("#343c48")
metal_line = col("#181c24")

glow_out = col("#0a5a60")
glow = col("#12c8c0")
glow_hi = col("#a8fff4")

hair_hi = col("#f8f8f6")
hair = col("#d8d8d4")
hair_sh = col("#9c9c9c")
hair_dk = col("#52525a")

coat = col("#d8d2c4")
coat_sh = col("#a89e8c")
coat_dk = col("#6e6656")
stain = col("#9a8a68")
stain_dk = col("#6e5e42")

apron = col("#7a4a24")
apron_hi = col("#a06a38")
apron_dk = col("#4c2e14")
apron_line = col("#301c0c")

belt = col("#3a2412")
belt_hi = col("#5a3c1e")
buckle = col("#c8b268")
pouch = col("#6a4a26")

cable_red = col("#d43a2a")
cable_blue = col("#2a6ad4")
cable_yel = col("#e0b82a")
cable_blk = col("#20242c")

tooth = col("#f4f0e4")
mouthc = col("#380c06")
tongue = col("#a03028")
white = col("#f4f4f4")
iris = col("#2a5a34")
brow = col("#33231a")
boltc = col("#c8ccd4")

# ---------------- background ----------------
c.rect(0, 0, 64, 64, bkg)
c.circle(31, 24, 26, halo1)
c.circle(31, 24, 20, halo2)
c.circle(31, 24, 15, halo3)

# ---------------- torso ----------------
c.poly([(6, 45), (58, 45), (53, 63), (11, 63)], coat)
c.poly([(42, 45), (58, 45), (52, 63), (44, 63)], coat_sh)
c.poly([(24, 44), (40, 44), (36, 47), (28, 47)], coat_dk)
c.poly([(6, 45), (15, 45), (14, 52), (9, 54)], coat)
c.ellipse(14, 54, 4, 3, stain)
c.ellipse(26, 59, 5, 3, stain_dk)
c.ellipse(38, 57, 4, 3, stain)
c.ellipse(30, 62, 5, 2, stain)

# leather apron
c.poly([(19, 46), (45, 46), (42, 63), (22, 63)], apron)
c.poly([(19, 46), (30, 46), (28, 63), (22, 63)], apron_hi)
c.poly([(38, 46), (45, 46), (42, 63), (39, 63)], apron_dk)
c.rect(24, 49, 6, 6, apron_dk)
c.line(20, 48, 33, 48, apron_line)
c.line(20, 45, 19, 51, apron_line)
c.line(44, 45, 45, 51, apron_line)

# tool belt
c.rect(10, 57, 44, 3, belt)
c.rect(12, 57, 10, 4, belt_hi)
c.rect(28, 57, 8, 4, buckle)
c.rect(31, 57, 3, 2, boltc)
c.rect(44, 57, 8, 4, belt_hi)
c.rect(13, 54, 4, 3, pouch)
c.rect(46, 54, 4, 3, pouch)
c.rect(16, 49, 2, 6, metal_mid)
c.rect(15, 48, 4, 2, metal)
c.rect(16, 55, 2, 2, cable_red)

# ---------------- neck ----------------
c.rect(27, 39, 6, 6, skin_sh)
c.rect(33, 39, 5, 6, metal_mid)
c.set(32, 39, metal_line)

# ---------------- head ----------------
def head_half(cx, cy, rx, ry, right, color):
    pts = [(cx, cy)]
    if right:
        for deg in range(-90, 91, 4):
            a = math.radians(deg)
            pts.append((round(cx + rx * math.cos(a)), round(cy + ry * math.sin(a))))
    else:
        for deg in range(90, 271, 4):
            a = math.radians(deg)
            pts.append((round(cx + rx * math.cos(a)), round(cy + ry * math.sin(a))))
    c.poly(pts, color)

head_half(32, 25, 15, 16, False, skin)
head_half(32, 25, 15, 16, True, metal_mid)

# hair mass on top
c.ellipse(32, 12, 17, 7, hair)
c.ellipse(32, 9, 15, 5, hair_hi)
c.poly([(17, 12), (23, 6), (19, 1)], hair)
c.poly([(24, 9), (30, 2), (31, 0)], hair_hi)
c.poly([(32, 8), (38, 1), (40, 4)], hair)
c.poly([(38, 9), (43, 4), (46, 7)], hair_sh)
c.line(44, 9, 46, 10, hair_sh)
c.line(18, 7, 17, 13, hair_sh)
c.line(16, 15, 17, 21, hair_sh)
c.set(16, 19, hair_sh)
c.line(43, 10, 42, 16, hair_dk)
# stray strands over face
c.line(21, 13, 20, 17, hair)
c.line(23, 7, 24, 11, hair_hi)
c.line(42, 10, 41, 14, hair_sh)
c.set(22, 15, hair_sh)

# electrode plugs on hair top
for (px, py) in [(21, 4), (26, 3), (31, 4), (36, 3), (41, 5)]:
    c.set(px, py, metal_hi)
    c.set(px, py + 1, metal)
    c.set(px - 1, py, metal_dk)
c.line(21, 4, 17, 1, cable_red)
c.line(26, 3, 23, 0, cable_blue)
c.line(31, 4, 29, 0, cable_yel)
c.line(36, 3, 39, 0, cable_blue)
c.line(41, 5, 44, 2, cable_red)

# electrode band across forehead
c.rect(17, 11, 30, 3, metal_dk)
c.set(18, 12, metal_hi)
c.set(31, 12, metal_hi)
c.set(45, 11, metal_hi)
for bx in (20, 25, 30, 35, 40, 45):
    c.set(bx, 12, boltc)
c.rect(40, 13, 6, 2, metal)
c.set(39, 12, metal_hi)

# split seam between halves
for y in range(9, 42):
    c.set(31 if y % 3 else 32, y, metal_line)
for y in range(10, 40, 2):
    c.set(34, y, metal_hi)

# skin shading + rim light on left
c.line(17, 20, 17, 30, skin_hi)
c.set(18, 28, skin_hi)
c.set(18, 30, skin_hi)
c.line(18, 32, 21, 38, skin_dk)
c.set(22, 39, skin_dk)
c.set(19, 24, skin_hi)
c.set(20, 27, skin_hi)

# robot plates
c.rect(33, 13, 10, 5, metal)
c.line(34, 15, 41, 15, metal_dk)
c.set(33, 13, metal_hi)
c.set(42, 17, metal_hi)
c.rect(34, 19, 6, 5, metal)
c.rect(34, 27, 8, 5, metal)
c.set(34, 31, metal_dk)
c.set(41, 27, metal_line)
c.rect(34, 33, 8, 5, metal_dk)
c.set(41, 36, metal)
c.set(34, 33, boltc)
c.set(41, 33, boltc)
c.set(35, 35, metal_mid)
c.set(39, 35, metal_mid)
# cybernetic ear plate
c.rect(44, 20, 3, 8, metal)
c.rect(45, 21, 1, 6, metal_dk)
c.set(44, 20, metal_hi)
c.set(45, 24, glow)
c.set(46, 23, metal_hi)
c.line(43, 22, 43, 27, metal_line)

# robot eye socket
c.rect(34, 20, 7, 6, metal_dk)
c.rect(35, 21, 5, 4, metal_line)
c.rect(36, 21, 3, 3, glow_out)
c.set(36, 21, glow)
c.set(37, 21, glow)
c.set(38, 21, glow)
c.set(36, 22, glow)
c.set(37, 22, glow_hi)
c.set(38, 22, glow)
c.set(36, 23, glow)
c.set(37, 23, glow)
c.set(38, 23, glow)
c.set(35, 22, glow_out)
c.set(39, 22, glow_out)
c.set(37, 20, glow)
c.set(39, 24, metal_hi)

# human eye (left)
c.rect(20, 22, 7, 4, skin_dk)
c.rect(21, 21, 5, 4, white)
c.set(21, 22, white)
c.set(22, 22, iris)
c.set(23, 22, iris)
c.set(24, 22, white)
c.set(23, 21, white)
c.set(22, 23, skin_line)
c.line(20, 25, 27, 25, skin_sh)
c.line(20, 20, 27, 20, skin_line)
c.line(19, 19, 26, 18, brow)
c.set(20, 18, brow)
c.set(20, 21, skin_line)
c.line(21, 26, 26, 26, skin_sh)

# nose
c.line(27, 20, 27, 28, skin_sh)
c.set(28, 23, skin_hi)
c.set(27, 27, skin_sh)
c.set(26, 28, skin_dk)
c.set(29, 29, skin_dk)
c.set(28, 29, skin_sh)

# mouth — maniacal grin
c.rect(19, 31, 22, 6, mouthc)
for i in range(10):
    c.set(20 + i * 2, 31, tooth)
    c.set(20 + i * 2, 32, tooth)
for i in range(9):
    c.set(21 + i * 2, 35, tooth)
c.rect(25, 33, 9, 2, mouthc)
c.set(28, 33, tongue)
c.set(30, 33, tongue)
c.line(19, 36, 40, 36, skin_line)
c.set(18, 30, skin_line)
c.set(41, 30, skin_line)
c.set(19, 29, skin_line)
c.set(40, 29, skin_line)
c.set(19, 30, mouthc)
c.set(40, 30, mouthc)
c.set(18, 31, skin_line)
c.set(41, 31, skin_line)

# ---------------- robotic arm (right, foreground) ----------------
def quad(p0, p1, w, color):
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    L = (dx * dx + dy * dy) ** 0.5 or 1
    px, py = -dy / L * w / 2, dx / L * w / 2
    c.poly([
        (round(x0 + px), round(y0 + py)),
        (round(x1 + px), round(y1 + py)),
        (round(x1 - px), round(y1 - py)),
        (round(x0 - px), round(y0 - py)),
    ], color)

# arm segments
quad((51, 46), (55, 38), 5, metal_line)
quad((46, 30), (55, 38), 5, metal_line)
quad((51, 46), (55, 38), 3, metal_mid)
quad((46, 30), (55, 38), 3, metal_mid)
quad((51, 46), (55, 38), 1.6, metal)
c.circle(55, 38, 2, metal)
c.set(54, 37, metal_hi)
c.set(52, 43, metal_hi)
c.circle(46, 30, 3, metal_dk)
c.set(45, 29, metal)

# hand — prosthetic with claw fingers
c.rect(40, 23, 7, 7, metal)
c.rect(40, 21, 2, 4, metal)
c.rect(42, 20, 2, 4, metal)
c.rect(44, 21, 2, 4, metal)
c.rect(45, 25, 3, 2, metal)
c.set(42, 23, metal_dk)
c.set(44, 23, metal_dk)
c.set(41, 24, metal_hi)
c.set(45, 26, metal_dk)
c.set(42, 20, metal_hi)
c.set(40, 21, metal_hi)

# LEDs on forearm
c.set(50, 41, glow)
c.set(49, 39, glow)
c.set(50, 40, glow_out)
c.set(48, 41, glow_out)

# cables from wrist hanging down
c.line(46, 30, 46, 40, cable_blk)
c.line(45, 31, 45, 42, cable_red)
c.line(47, 31, 47, 45, cable_blue)
c.line(46, 40, 46, 49, cable_blk)
c.line(47, 45, 48, 52, cable_yel)
c.set(39, 28, cable_blk)
c.line(39, 28, 37, 33, cable_red)
c.set(48, 52, cable_yel)
c.set(46, 43, cable_red)

print(c.stats_text())
print("--- head ---")
print(c.matrix_text(region=(12, 0, 50, 44)))
print("--- body ---")
print(c.matrix_text(region=(8, 38, 60, 63)))

finish(c)
