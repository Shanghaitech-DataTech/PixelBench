# red-roofed-forge-house — 128x128 isometric RTS tile
c = new_canvas(128, 128, name="forge_house")

def poly(pts, col): c.poly(list(pts), col, fill=True)
def ln(x0, y0, x1, y1, col): c.line(x0, y0, x1, y1, col)
def b45(x0, y0, x1, y1, col):  # 2px beam along a 45-degree edge
    c.line(x0, y0, x1, y1, col); c.line(x0 + 1, y0, x1 + 1, y1, col)

# palette
GROUND   = c.color("#5f7a3c")
GRASS_D  = c.color("#4a6130")
GRASS_L  = c.color("#748c4a")
STONE    = c.color("#8d8d85")
GLOW_DIM = c.color("#8a4a14")
GLOW_MID = c.color("#c86a1e")
WALL_L   = c.color("#e8d5a8")
WALL_D   = c.color("#cdb689")
BEAM     = c.color("#4a2a18")
ROOF_A   = c.color("#c8472f")
ROOF_B   = c.color("#b23a26")
ROOF_LN  = c.color("#8c2a1c")
ROOF_FAR = c.color("#8a2a1e")
ROOF_FLN = c.color("#6f2117")
RIDGE    = c.color("#ea7a5c")
FIRE_D   = c.color("#c8500f")
FIRE_M   = c.color("#f2801e")
FIRE_Y   = c.color("#ffd23f")
FIRE_C   = c.color("#ffe98a")
WOOD     = c.color("#8a5a2e")
WOOD_D   = c.color("#6a421e")
WOOD_R   = c.color("#3e2a16")
WOOD_T   = c.color("#a5713a")
BRICK    = c.color("#6e4434")
BRICK_D  = c.color("#502f22")
BRICK_T  = c.color("#7d5240")
HOLE     = c.color("#241410")
SMOKE_1  = c.color("#cfcfcf")
SMOKE_2  = c.color("#9a9a9a")

# ---------- ground tile (45-degree diamond, clipped by canvas bottom) ----------
poly([(64, 26), (118, 80), (64, 134), (10, 80)], GROUND)
for (x, y) in [(24,84),(30,92),(96,88),(100,80),(88,100),(40,64),(90,60),
               (28,72),(104,72),(60,120),(70,122),(50,112),(80,108),(38,106)]:
    c.set(x, y, GRASS_D)
for (x, y) in [(34,70),(92,72),(56,116),(76,96),(44,100)]:
    c.set(x, y, GRASS_L)
c.rect(93, 95, 3, 2, STONE); c.rect(98, 90, 2, 2, STONE)

# glow spill on the ground in front of the furnace
poly([(36, 93), (41, 98), (36, 103), (31, 98)], GLOW_DIM)
c.set(35, 97, GLOW_MID); c.set(36, 98, GLOW_MID); c.set(37, 97, GLOW_MID)

# ---------- walls ----------
poly([(26, 50), (64, 88), (64, 114), (26, 76)], WALL_L)   # left face
poly([(64, 88), (102, 50), (102, 76), (64, 114)], WALL_D) # right face
poly([(83, 53), (64, 88), (102, 50)], WALL_D)             # gable end

# timber beams
b45(26, 50, 64, 88, BEAM)      # left wall top
b45(26, 76, 64, 114, BEAM)     # left wall bottom
b45(64, 88, 102, 50, BEAM)     # right wall top
b45(64, 114, 102, 76, BEAM)    # right wall bottom
b45(26, 50, 26, 76, BEAM)      # left corner post
b45(102, 50, 102, 76, BEAM)    # right corner post
b45(64, 88, 64, 114, BEAM)     # shared front post
ln(30, 74, 38, 64, BEAM)       # left brace
ln(92, 66, 98, 60, BEAM)       # right brace
ln(83, 54, 83, 68, BEAM)       # gable post

# ---------- furnace arch (left wall) ----------
ln(31, 74, 31, 87, BEAM); ln(45, 74, 45, 87, BEAM); ln(31, 87, 45, 87, BEAM)
for (x, y) in [(32,73),(33,72),(35,71),(37,71),(39,71),(41,71),(43,72),(44,73)]:
    c.set(x, y, BEAM)
c.rect(32, 76, 13, 11, FIRE_D)
for (x, y) in [(35,74),(36,74),(37,74),(38,74),(39,74),(40,74),(41,74),
               (33,75),(34,75),(42,75),(43,75)]:
    c.set(x, y, FIRE_D)
c.rect(34, 78, 9, 9, FIRE_M)
c.rect(36, 80, 5, 7, FIRE_Y)
c.rect(37, 82, 3, 4, FIRE_C)

# ---------- window (right wall) ----------
c.rect(84, 66, 8, 9, BEAM, fill=False)
c.rect(85, 67, 6, 7, FIRE_M)
ln(88, 67, 88, 73, BEAM); ln(85, 70, 90, 70, BEAM)

# ---------- door (right wall) ----------
c.rect(66, 90, 8, 12, BEAM, fill=False)
c.rect(67, 91, 6, 10, WOOD_D)
ln(70, 91, 70, 100, BEAM)
c.set(72, 97, WOOD_R)

# ---------- hanging sign (right wall) ----------
ln(80, 73, 80, 77, BEAM); ln(81, 73, 81, 77, BEAM)
c.rect(74, 78, 16, 11, BEAM, fill=False)
c.rect(75, 79, 14, 9, WOOD)
ln(81, 79, 81, 87, WOOD_D)
# little flame icon
c.set(82, 80, FIRE_M)
for x in range(81, 84): c.set(x, 81, FIRE_M)
for x in range(80, 85): c.set(x, 82, FIRE_M)
for x in range(81, 84): c.set(x, 83, FIRE_M)
c.set(82, 82, FIRE_Y); c.set(82, 83, FIRE_Y)

# ---------- roof: far slope ----------
poly([(45, 15), (56, 4), (94, 42), (83, 53)], ROOF_FAR)
ln(50, 14, 60, 24, ROOF_FLN); ln(62, 26, 72, 36, ROOF_FLN)

# ---------- roof: near slope, tiled bands ----------
ts = [0.0, 0.22, 0.44, 0.66, 0.88, 1.0]
def pt(t, front):
    if front: return (83 - 23 * t, 53 + 39 * t)
    return (45 - 23 * t, 15 + 39 * t)
for i in range(5):
    a1, a2 = pt(ts[i], False), pt(ts[i], True)
    b2, b1 = pt(ts[i+1], True), pt(ts[i+1], False)
    poly([a1, a2, b2, b1], ROOF_A if i % 2 == 0 else ROOF_B)
for i in range(1, 5):
    p1, p2 = pt(ts[i], False), pt(ts[i], True)
    ln(p1[0], p1[1], p2[0], p2[1], ROOF_LN)
    start = 3 if i % 2 else 7
    for s in range(start, 36, 9):
        x, y = p1[0] + s, p1[1] + s
        c.set(x, y, ROOF_LN); c.set(x + 1, y - 1, ROOF_LN)

# roof edges
ln(22, 54, 60, 92, BEAM); ln(23, 54, 61, 92, BEAM)   # eave
ln(83, 53, 64, 88, BEAM); ln(83, 53, 102, 50, BEAM)  # over gable
ln(83, 53, 94, 42, BEAM); ln(45, 15, 56, 4, BEAM)    # hip edges
ln(56, 4, 94, 42, ROOF_FLN)                          # far eave
ln(45, 15, 83, 53, RIDGE)                            # ridge highlight

# ---------- chimney ----------
poly([(66, 8), (72, 14), (66, 20), (60, 14)], BRICK_T)      # top
poly([(66, 11), (69, 14), (66, 17), (63, 14)], HOLE)        # flue
poly([(60, 14), (66, 20), (66, 40), (60, 34)], BRICK)       # left face
poly([(66, 20), (72, 14), (72, 34), (66, 40)], BRICK)       # right face
ln(60, 21, 66, 21, BRICK_D); ln(60, 27, 66, 27, BRICK_D); ln(60, 33, 66, 33, BRICK_D)
ln(67, 24, 71, 24, BRICK_D); ln(68, 30, 72, 30, BRICK_D)
# smoke
c.set(66, 5, SMOKE_1); c.set(67, 5, SMOKE_1)
c.set(69, 3, SMOKE_1); c.set(70, 3, SMOKE_1)
c.set(72, 1, SMOKE_2); c.set(73, 1, SMOKE_2); c.set(72, 2, SMOKE_2)
c.set(64, 7, SMOKE_2)

# ---------- stacked barrels ----------
# bottom barrel A
c.rect(48, 96, 13, 15, WOOD)
for y in range(96, 111): c.set(48, y, WOOD_D); c.set(49, y, WOOD_D); c.set(59, y, WOOD_D); c.set(60, y, WOOD_D)
ln(48, 100, 60, 100, WOOD_R); ln(48, 106, 60, 106, WOOD_R)
ln(48, 96, 60, 96, WOOD_D)
c.set(48, 96, WOOD_R); c.set(60, 96, WOOD_R); c.set(48, 110, WOOD_R); c.set(60, 110, WOOD_R)
# top barrel B
c.rect(50, 84, 9, 13, WOOD)
for y in range(84, 97): c.set(50, y, WOOD_D); c.set(58, y, WOOD_D)
ln(50, 88, 58, 88, WOOD_R); ln(50, 93, 58, 93, WOOD_R)
c.ellipse(54, 85, 4, 2, WOOD_D, fill=False)
c.ellipse(54, 85, 3, 1, WOOD_T)
# barrel C
c.rect(62, 102, 11, 15, WOOD)
for y in range(102, 117): c.set(62, y, WOOD_D); c.set(63, y, WOOD_D); c.set(71, y, WOOD_D); c.set(72, y, WOOD_D)
ln(62, 106, 72, 106, WOOD_R); ln(62, 112, 72, 112, WOOD_R)
c.ellipse(67, 103, 5, 2, WOOD_D, fill=False)
c.ellipse(67, 103, 4, 1, WOOD_T)

print(c.stats_text())
finish(c)
