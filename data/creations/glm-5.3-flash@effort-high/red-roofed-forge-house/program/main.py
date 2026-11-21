# red-roofed-forge-house — 128x128 isometric RTS-style tile
YO = 6
c = new_canvas(128, 128, background=None, name="forge-house")

# ---------------- palette ----------------
for name, hx in [
    ('outline','#2b1a12'),
    ('grass1','#6da24e'),('grass2','#5c8c40'),('grass3','#49763a'),('grass_lite','#82b45e'),
    ('soil_lite','#7a5734'),('soil_dark','#5a3d26'),
    ('found','#7d5f3a'),('dirt','#9c7a4e'),
    ('plaster_lite','#e6d3a8'),('plaster_dark','#c6ad85'),
    ('timber','#6b4423'),('timber_dark','#4a2e18'),
    ('roof_base','#b23c28'),('roof_row','#8c2418'),('roof_tick','#6e1a0f'),
    ('roof_lite','#d05a3c'),('ridge_lite','#ef8a70'),('eave_dark','#521409'),
    ('stone','#8a8a92'),('stone_dark','#63636b'),
    ('brick','#9c6b58'),('brick_dark','#6f463a'),('brick_top','#5c382e'),('hole','#24100c'),
    ('glow1','#ffd66b'),('glow2','#ff9a3d'),('glow3','#e85414'),('glow4','#a03310'),('glow_dark','#2a0d06'),
    ('wood','#8a5a2c'),('wood_lite','#a9763f'),('wood_dark','#66401f'),('band','#3f2c1c'),
    ('smoke1','#cfd4d8'),('smoke2','#a8b0b6'),
    ('metal','#3f3f46'),
]:
    globals()[name] = c.color(hx, name=name)

def P(x, y): return (x, y + YO)
def Y(y): return y + YO
def pts(*ps): return [P(x, y) for x, y in ps]
def ln(p, q, col): c.line(p[0], p[1], q[0], q[1], col)

# ---------------- ground platform (RTS tile diamond) ----------------
c.poly(pts((64,36),(124,66),(64,96),(4,66)), grass1)
c.poly(pts((4,66),(64,96),(64,102),(4,72)), soil_lite)      # platform side L
c.poly(pts((64,96),(124,66),(124,72),(64,102)), soil_dark)  # platform side R
ln(P(4,66), P(64,36), outline)
ln(P(64,36), P(124,66), outline)
ln(P(4,72), P(64,102), outline)
ln(P(64,102), P(124,72), outline)

# grass texture
for (x, y) in [(30,64),(38,70),(48,76),(60,82),(74,84),(88,78),(100,68),(108,62),
               (52,56),(70,50),(90,54),(104,58),(28,70),(44,84),(78,86),(58,60),(96,64)]:
    c.set(*P(x, y), grass3)
for (x, y) in [(34,66),(56,78),(72,88),(96,72),(102,60),(48,60),(86,60),(66,92)]:
    c.set(*P(x, y), grass_lite); c.set(*P(x, y+1), grass_lite)
# stones
for (x, y) in [(58,88),(106,64),(33,74)]:
    c.rect(x, Y(y), 3, 2, stone); c.rect(x, Y(y)+1, 3, 1, stone_dark)

# building shadow + foundation
c.poly(pts((64,72),(96,56),(104,60),(72,76)), grass3)
c.poly(pts((64,39),(97,56),(64,73),(31,56)), found)

# furnace glow spill on the ground (in front of the arch)
c.poly(pts((38,59),(58,69),(46,75),(26,65)), glow4)
c.poly(pts((38,60),(54,68),(44,72),(30,64)), glow3)
c.set(*P(40,62), glow2); c.set(*P(46,65), glow2); c.set(*P(50,67), glow2)

# dirt path in front of the door
c.poly(pts((72,70),(84,64),(94,69),(82,75)), dirt)
for (x, y) in [(76,69),(84,68),(80,72),(88,70)]:
    c.set(*P(x, y), soil_dark)

# ---------------- walls ----------------
c.poly(pts((64,72),(96,56),(96,32),(64,48)), plaster_dark)   # right face
c.poly(pts((32,56),(64,72),(64,48),(32,32)), plaster_lite)   # left face
c.poly(pts((32,32),(64,48),(48,24)), plaster_lite)           # gable

# silhouette outlines
ln(P(32,56), P(32,32), outline)
ln(P(32,56), P(64,72), outline)
ln(P(64,72), P(96,56), outline)
ln(P(96,56), P(96,32), outline)

# timber framing
c.rect(*P(32,32), 2, 24, timber)          # left corner post
c.rect(*P(62,48), 2, 25, timber_dark)     # front corner post
c.rect(*P(94,32), 2, 24, timber_dark)     # right corner post
ln(P(64,60), P(96,44), timber_dark)       # mid beam right face
ln(P(64,71), P(96,55), timber_dark)       # base plank right face
ln(P(34,53), P(45,42), timber_dark)       # brace left face
ln(P(35,37), P(41,43), timber_dark)
ln(P(35,31), P(45,26), timber_dark)       # gable braces
ln(P(61,46), P(52,30), timber_dark)
# plaster speckles
for (x, y) in [(40,38),(50,52),(56,60),(44,64),(70,40),(80,48),(88,40),(74,58),(84,52),(38,48)]:
    c.set(*P(x, y), plaster_dark if x < 64 else plaster_lite)

# door on right face
c.poly(pts((70,51),(82,45),(82,63),(70,69)), wood)
c.poly(pts((70,51),(82,45),(82,63),(70,69)), outline, fill=False)
ln(P(74,49), P(74,67), timber_dark)
ln(P(78,47), P(78,65), timber_dark)
c.set(*P(80,56), metal); c.set(*P(80,57), metal)

# lit vent window on the gable
c.poly(pts((44,28),(50,31),(50,36),(44,33)), glow2)
c.poly(pts((44,28),(50,31),(50,36),(44,33)), outline, fill=False)
ln(P(44,31), P(50,34), timber_dark)

# ---------------- furnace arch (stone rim + glow) ----------------
outer_d = "M 38 65 L 38 51 C 38 45 44 44 48 48 C 52 52 58 55 58 61 L 58 75 L 38 65 Z"
inner_d = "M 41 66.5 L 41 54 C 41 50 45 49.5 48 52.5 C 51 55.5 55 58 55 63.5 L 55 72.5 L 41 66.5 Z"
c.path(outer_d, stone)
c.path(outer_d, outline, fill=False)
c.path(inner_d, glow_dark)
c.path(inner_d, glow4, fill=False)
c.poly(pts((43,61),(43,48),(48,45),(53,55),(53,66)), glow3)
c.poly(pts((45,59),(45,50),(48,47),(51,55),(51,64)), glow2)
c.poly(pts((46,57),(46,51),(48,49),(50,53),(50,61)), glow1)
c.set(*P(44,57), glow1); c.set(*P(51,59), glow1)
# keystone
c.rect(46, Y(38), 5, 3, stone); ln(P(46,38), P(51,38), stone_dark)

# ---------------- roof ----------------
c.poly(pts((48,24),(80,8),(100,34),(68,50)), roof_base)

def rp(s, t):
    return (int(round(48 + 32*s + 20*t)), int(round(YO + 24 - 16*s + 26*t)))

row_ts = [0.16, 0.32, 0.48, 0.64, 0.80, 0.93]
for t in row_ts:
    ln(rp(0.03, t), rp(0.97, t), roof_row)
    ln(rp(0.06, t - 0.055), rp(0.94, t - 0.055), roof_lite)
for i in range(len(row_ts) - 1):
    t0 = row_ts[i]
    ss = [0.16, 0.40, 0.64, 0.88] if i % 2 == 0 else [0.28, 0.52, 0.76]
    for s in ss:
        ln(rp(s, t0 + 0.03), rp(s, t0 + 0.11), roof_tick)

ln(P(48,24), P(80,8), ridge_lite)                 # ridge highlight
ln(rp(0.0, 0.06), rp(1.0, 0.06), roof_lite)
c.poly(pts((68,50),(100,34),(100,36),(68,52)), eave_dark)   # eave thickness
ln(P(80,8), P(100,34), eave_dark)                 # roof right edge
ln(P(48,24), P(68,50), eave_dark)                 # barge over gable
ln(P(32,32), P(48,24), timber_dark)               # gable top edge

# ---------------- chimney ----------------
c.poly(pts((74,26),(78,30),(78,16),(74,12)), brick)
c.poly(pts((78,30),(82,26),(82,12),(78,16)), brick_dark)
c.poly(pts((78,8),(82,12),(78,16),(74,12)), brick_top)
c.poly(pts((78,10),(80,12),(78,14),(76,12)), hole)
for y in (17, 21, 25):
    ln(P(74,y), P(78,y), brick_dark)
for y in (19, 23, 27):
    ln(P(78,y), P(82,y), brick_top)
ln(P(74,12), P(74,26), outline)
ln(P(82,12), P(82,26), outline)
ln(P(74,12), P(78,8), outline)
ln(P(78,8), P(82,12), outline)
c.poly(pts((78,22),(82,26),(78,30),(74,26)), eave_dark, fill=False)  # flashing
# smoke
for (x, y, col) in [(78,5,smoke2),(79,4,smoke1),(77,3,smoke2),(79,2,smoke1),(80,1,smoke2),(81,0,smoke2)]:
    c.set(*P(x, y), col)

# ---------------- wooden sign ----------------
c.rect(*P(24,52), 2, 23, wood_dark)               # post
c.rect(*P(13,53), 13, 2, wood_dark)               # arm
ln(P(11,55), P(11,57), metal); ln(P(23,55), P(23,57), metal)
c.rect(*P(9,58), 17, 13, wood)
c.rect(*P(9,58), 17, 13, outline, fill=False)
c.rect(*P(10,59), 15, 11, wood_lite, fill=False)
# flame icon
c.set(*P(17,61), glow2)
c.set(*P(16,62), glow2); c.set(*P(17,62), glow1); c.set(*P(18,62), glow2)
c.set(*P(16,63), glow2); c.set(*P(17,63), glow1); c.set(*P(18,63), glow2)
c.set(*P(16,64), glow3); c.set(*P(17,64), glow2); c.set(*P(18,64), glow3)
c.set(*P(17,65), glow3)

# ---------------- stacked barrels ----------------
def barrel(bx, by):
    c.rect(bx-6, Y(by-14), 13, 14, wood)
    ln(P(bx-6,by-14), P(bx-6,by-1), outline)
    ln(P(bx+6,by-14), P(bx+6,by-1), outline)
    ln(P(bx-6,by-1), P(bx+6,by-1), outline)
    ln(P(bx-6,by-10), P(bx+6,by-10), band)
    ln(P(bx-6,by-5), P(bx+6,by-5), band)
    for sx in (-3, 2):
        for (a, b) in [(-13,-11),(-9,-6),(-4,-2)]:
            ln(P(bx+sx,by+a), P(bx+sx,by+b), wood_dark)
    ln(P(bx-5,by-13), P(bx-5,by-2), wood_lite)
    c.ellipse(bx, Y(by-14), 6, 3, wood_lite)
    c.ellipse(bx, Y(by-14), 6, 3, outline, fill=False)
    c.ellipse(bx, Y(by-14), 3, 1, wood_dark)

barrel(100, 74)   # back barrel
barrel(90, 82)    # front barrel
barrel(90, 69)    # stacked on top of front barrel

# a few foreground tufts
for (x, y) in [(56,84),(72,90),(64,80),(50,88)]:
    c.set(*P(x, y), grass_lite); c.set(*P(x, y+1), grass_lite)

# ---------------- report + submit ----------------
print(c.stats_text())
print("--- barrels ---")
print(c.matrix_text(region=(82, 58, 110, 92)))
print("--- gable vent ---")
print(c.matrix_text(region=(40, 30, 56, 46)))
finish(c)
