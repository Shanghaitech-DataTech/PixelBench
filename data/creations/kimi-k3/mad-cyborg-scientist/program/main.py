import math

# ---------------- palette ----------------
BG0="#0b0d14"; BG1="#131726"; BG2="#1d2440"; BG3="#29325a"; BG4="#3b4b7e"
INK="#131118"
SKIN_H="#f6cf9f"; SKIN="#e0a578"; SKIN_S="#b57e52"; SKIN_D="#8a5a38"; SCAR="#a84a3c"
MET_H="#eef3f8"; MET_L="#c2cad4"; MET="#828a96"; MET_D="#454b55"; MET_V="#2b3039"
EYE_CORE="#fff6cf"; EYE_HOT="#ffa43c"; EYE_RED="#e8402a"; EYE_DK="#7a1e1a"
HAIR_H="#fbf8ec"; HAIR="#efeada"; HAIR_S="#c8c3b0"; HAIR_D="#99947f"
COAT_H="#eae4d4"; COAT="#ded6c4"; COAT_S="#aaa189"; COAT_D="#7c7260"; STAIN="#716c4e"
APRON_L="#b07a4a"; APRON="#8a542f"; APRON_D="#5c3920"
BELT="#3f2a18"; BRASS="#d0a84c"; BRASS_D="#8a6c2c"
TEETH="#f4eedd"; MOUTH="#43120e"
CABLE="#22242e"; WIRE_R="#c03028"; WIRE_Y="#d8a830"; WIRE_B="#2f6dc0"
RIM="#8fc7ee"; SCLERA="#f2eee2"; IRIS="#33507a"
AURA="#8a2a1e"

c = new_canvas(64, 64, background=BG0, name="mad_cyborg_scientist")
set = c.set

def thick_line(x0, y0, x1, y1, col, w=1):
    steps = max(abs(x1-x0), abs(y1-y0), 1)
    r = w // 2
    for i in range(steps + 1):
        t = i / steps
        x = round(x0 + (x1-x0)*t); y = round(y0 + (y1-y0)*t)
        c.rect(x-r, y-r, w, w, col)

# ---------------- background: radial lab glow, light from upper-left ----------------
for y in range(64):
    for x in range(64):
        d = ((x-27)*0.95)**2 + ((y-21)*1.05)**2
        col = BG4 if d < 42 else BG3 if d < 92 else BG2 if d < 168 else BG1 if d < 300 else BG0
        set(x, y, col)
# distant specks
for (x,y) in [(8,12),(55,8),(60,30),(6,34),(48,4),(58,40),(4,44),(59,14)]:
    set(x, y, BG3)

# ---------------- torso: dirty lab coat ----------------
c.poly([(6,64),(6,52),(12,45),(20,41),(27,40),(36,40),(44,41),(52,45),(58,52),(58,64)], COAT)
# lit left panel
c.poly([(6,64),(6,52),(12,45),(19,41),(19,64)], COAT_H)
# shadowed right panel
c.poly([(45,41),(52,45),(58,52),(58,64),(46,64)], COAT_S)
# coat folds + stains
c.line(13, 50, 11, 63, COAT_D)
c.line(50, 50, 53, 63, COAT_D)
for (x,y) in [(14,57),(15,57),(14,58),(48,60),(49,60),(10,47)]:
    set(x, y, STAIN)
# pocket with pens
c.rect(12, 51, 5, 4, COAT_S)
c.line(12, 54, 16, 54, INK)
set(13, 50, WIRE_R); set(15, 50, WIRE_B)

# high collar flaps
c.poly([(16,43),(13,33),(19,35),(25,43)], COAT)
c.poly([(16,43),(13,33),(19,35),(25,43)], INK, fill=False)
c.line(15, 40, 18, 35, COAT_D)
c.poly([(46,43),(49,33),(43,35),(37,43)], COAT_S)
c.poly([(46,43),(49,33),(43,35),(37,43)], INK, fill=False)
c.line(47, 40, 44, 35, COAT_D)

# ---------------- leather apron ----------------
c.poly([(26,42),(38,42),(41,56),(23,56)], APRON)
c.poly([(23,56),(41,56),(44,64),(20,64)], APRON)
# shading + highlight
c.poly([(35,42),(38,42),(41,56),(35,56)], APRON_D)
c.poly([(41,56),(44,64),(36,64),(35,56)], APRON_D)
c.line(25, 44, 24, 55, APRON_L)
c.line(21, 58, 20, 63, APRON_L)
for (x,y) in [(29,47),(30,47),(29,48),(33,51),(34,52),(33,52)]:
    set(x, y, APRON_D)
set(30, 48, STAIN); set(34, 51, STAIN)

# ---------------- tool belt ----------------
c.rect(16, 56, 32, 3, BELT)
c.rect(30, 56, 5, 3, BRASS)
set(32, 57, INK)
set(31, 56, "#e8cc80")
# pouches
c.rect(21, 57, 5, 5, APRON_D)
c.line(21, 58, 25, 58, APRON_L)
c.rect(39, 57, 5, 5, APRON_D)
c.line(39, 58, 43, 58, APRON_L)
# screwdriver in left loop
set(18, 55, MET_L); set(18, 56, MET_L)
c.rect(17, 57, 3, 3, WIRE_R)
# wrench hanging right
set(46, 57, MET_L); set(48, 57, MET_L)
c.rect(46, 58, 2, 5, MET)
set(46, 58, MET_L)
set(47, 62, MET_D)

# ---------------- neck ----------------
c.rect(27, 36, 5, 6, SKIN_S)
c.rect(32, 36, 5, 6, MET_D)
for y in range(36, 38):
    for x in range(27, 32):
        set(x, y, SKIN_D)
    for x in range(32, 37):
        set(x, y, MET_V)
c.line(34, 38, 34, 41, CABLE)
set(33, 39, WIRE_R); set(33, 40, WIRE_R)

# ---------------- head base: left skin / right metal ----------------
cx, cy, rx, ry = 31, 24, 11, 13
for y in range(cy-ry-1, cy+ry+2):
    for x in range(cx-rx-1, cx+rx+2):
        t = ((x-cx)/rx)**2 + ((y-cy)/ry)**2
        if t <= 1.0:
            if t > 0.83:
                set(x, y, INK); continue
            j = (y*5) % 3 - 1
            split = cx + j + (1 if y > 30 else 0)
            light = (-(x-cx) - 0.9*(y-cy)) / rx
            if x <= split:
                col = SKIN_H if light > 0.6 else SKIN if light > -0.3 else SKIN_S if light > -1.1 else SKIN_D
            else:
                col = MET_H if light > 0.6 else MET_L if light > -0.3 else MET if light > -1.1 else MET_D
            set(x, y, col)
# jagged split crack
for y in range(12, 37):
    sx = 31 + ((y % 3) - 1) + (1 if y > 30 else 0)
    set(sx, y, INK)
set(29, 15, SCAR); set(30, 18, SCAR); set(29, 33, SCAR)

# ---------------- human features (left) ----------------
# raised brow
c.line(23, 18, 28, 17, HAIR)
set(24, 17, HAIR)
# wide mad eye
c.rect(24, 20, 4, 2, SCLERA)
set(26, 20, INK); set(26, 21, INK)
set(25, 20, "#ffffff")
set(24, 21, "#c05848")
c.line(24, 19, 27, 19, SKIN_D)
set(25, 22, SKIN_S); set(26, 22, SKIN_S); set(24, 23, SKIN_S)
# forehead wrinkles
c.line(23, 15, 27, 15, SKIN_S)
c.line(24, 13, 27, 13, SKIN_S)
# nose
set(30, 22, SKIN_H); set(30, 23, SKIN_H); set(30, 24, SKIN)
set(31, 23, SKIN_S); set(31, 24, SKIN_S); set(31, 25, SKIN_S)
set(29, 26, SKIN); set(29, 27, SKIN_D)
set(32, 24, MET); set(32, 25, MET); set(32, 26, MET_D)
# cheek wrinkles
set(23, 26, SKIN_S); set(22, 28, SKIN_S); set(24, 28, SKIN_S)
# chin
set(28, 35, SKIN_H); set(29, 36, SKIN_S)

# ---------------- robot features (right) ----------------
# brow plate
c.line(34, 17, 39, 16, MET_V)
# eye socket
c.ellipse(37, 21, 4, 3, MET_V)
set(33, 21, MET_D); set(41, 21, MET_D); set(37, 18, MET_D); set(37, 24, MET_D)
for (x,y) in [(33,19),(41,19),(33,23),(41,23)]:
    set(x, y, MET_L)
# glowing lens
c.circle(37, 21, 2, EYE_RED)
c.circle(37, 21, 1, EYE_HOT)
set(37, 21, EYE_CORE); set(36, 20, EYE_CORE)
# glow aura
set(35, 17, EYE_DK); set(39, 17, EYE_DK); set(34, 25, AURA); set(40, 25, AURA)
set(33, 24, "#a03a28")
# plate seams + rivets
c.line(34, 15, 40, 15, MET_D)
set(34, 14, MET_L); set(40, 14, MET_L)
c.line(40, 26, 41, 29, INK)
set(40, 25, MET_L); set(41, 27, MET_L)
set(42, 22, MET_H); set(39, 33, MET_L); set(43, 18, MET_L)
# jaw vent
c.line(36, 33, 40, 33, MET_V)
c.line(36, 34, 40, 34, MET_V)
set(34, 35, MET_D); set(35, 36, MET_D)
set(36, 35, MET_D); set(37, 36, MET_D); set(38, 35, MET_V)
# exposed split wires
set(32, 27, WIRE_R); set(31, 28, WIRE_Y)

# ---------------- maniacal grin ----------------
# dark mouth opening
c.line(25, 29, 39, 29, MOUTH)
c.line(24, 32, 38, 32, MOUTH)
set(23, 30, MOUTH); set(24, 29, MOUTH)
set(40, 29, MOUTH); set(41, 28, MOUTH)
# teeth row: human enamel left, steel right
for x in range(25, 40):
    col = TEETH if x < 33 else MET_L
    set(x, 30, col); set(x, 31, col)
for gx in (27, 30, 33, 36):
    set(gx, 30, INK); set(gx, 31, INK)
# lips / jaw lines
set(23, 29, SKIN_D); set(24, 28, SKIN_D)
c.line(25, 32, 31, 32, SKIN_S)
c.line(34, 32, 39, 31, MET_D)

# ---------------- ears ----------------
# human ear
c.line(18, 22, 18, 25, SKIN)
set(19, 23, SKIN_D); set(19, 24, SKIN_S); set(18, 21, SKIN_S)
# robot audio dish
c.circle(45, 23, 2, MET_D)
set(45, 23, INK)
set(44, 21, MET_L); set(46, 21, MET_L); set(43, 23, MET_L)
set(44, 22, MET_H)

# ---------------- messy white hair ----------------
c.ellipse(31, 9, 12, 5, HAIR)
spikes = [
    [(20,11),(17,1),(25,8)],
    [(24,9),(26,-1),(30,8)],
    [(29,8),(35,-2),(36,8)],
    [(35,8),(44,1),(41,10)],
    [(40,10),(48,5),(43,13)],
    [(21,12),(12,7),(20,16)],
    [(19,15),(11,13),(18,20)],
]
for s in spikes:
    c.poly(s, HAIR)
# shading + highlight
c.ellipse(31, 11, 10, 3, HAIR_S)
c.ellipse(27, 6, 7, 3, HAIR_H)
set(30, 12, HAIR_D); set(36, 12, HAIR_D); set(24, 13, HAIR_D)
# left sideburn
c.line(19, 15, 19, 20, HAIR_S)
set(20, 17, HAIR)
# strays
c.line(16, 4, 13, 1, HAIR_H)
c.line(45, 3, 48, 0, HAIR)
set(22, 3, HAIR_H); set(38, 2, HAIR_H)

# ---------------- brain electrode plugs ----------------
# plug on metal skull
c.rect(37, 4, 3, 3, MET_D)
set(37, 4, MET_L); set(38, 5, INK)
c.path("M38 4 Q42 -1 45 3", CABLE, fill=False)
set(45, 3, WIRE_R); set(46, 2, WIRE_Y); set(47, 4, WIRE_Y)
# temple plug
c.rect(43, 10, 3, 3, MET_D)
set(44, 11, INK)
c.path("M44 12 Q47 16 45 21", CABLE, fill=False)
# scalp plug in hair (human side)
c.rect(22, 5, 3, 3, MET_D)
set(23, 6, WIRE_B)
c.line(23, 4, 21, 2, CABLE)

# ---------------- robotic arm (raised) ----------------
# shoulder joint
c.circle(50, 45, 3, MET_D)
c.circle(50, 45, 1, MET_V)
set(48, 43, MET_L); set(52, 43, MET_L); set(48, 47, MET_D); set(52, 47, MET_D)
# upper arm
thick_line(50, 44, 54, 32, MET, 4)
thick_line(49, 43, 53, 32, MET_L, 1)
c.line(51, 38, 54, 38, MET_D)
# elbow
c.circle(54, 31, 2, MET_D)
set(53, 30, MET_L); set(54, 31, MET_V)
# forearm
thick_line(54, 30, 56, 22, MET, 4)
thick_line(53, 29, 55, 22, MET_H, 1)
thick_line(57, 29, 58, 23, CABLE, 1)
# wrist + palm
c.rect(55, 20, 4, 2, MET_D)
c.poly([(55,20),(60,19),(61,14),(56,13)], MET_L)
c.line(60, 19, 61, 14, MET)
set(55, 20, MET_D)
# claw fingers
thick_line(56, 14, 53, 10, MET, 2)
set(52, 9, MET_H); set(53, 10, MET_D)
thick_line(58, 13, 58, 8, MET, 2)
set(58, 7, MET_H); set(58, 10, MET_D)
thick_line(60, 15, 63, 10, MET, 2)
set(63, 9, MET_H); set(61, 12, MET_D)
thick_line(55, 18, 52, 15, MET_D, 2)
set(52, 15, MET_L)
# gaps between claw fingers + knuckles
set(55, 9, INK); set(56, 10, INK); set(56, 9, INK)
set(60, 8, INK); set(60, 9, INK); set(61, 10, INK)
c.line(56, 16, 60, 16, MET_D)
# dangling cables
c.path("M55 23 Q48 30 50 40", CABLE, fill=False)
c.path("M57 23 Q53 32 54 39", WIRE_R, fill=False)
set(50, 40, MET_L); set(51, 40, MET_D); set(54, 39, WIRE_Y)
c.path("M50 48 Q48 52 50 56", CABLE, fill=False)

# ---------------- rim light (strong contrast) ----------------
for (x,y) in [(47,6),(46,9),(48,5)]:
    set(x, y, RIM)
set(47, 23, RIM); set(42, 18, RIM); set(42, 27, RIM)
set(59, 25, RIM); set(60, 18, RIM); set(63, 11, RIM); set(58, 7, RIM)
for y in (50, 53, 57, 61):
    set(58, y, RIM)
# extra warm highlights
set(21, 14, SKIN_H); set(22, 12, HAIR_H); set(25, 4, HAIR_H)

print(c.stats_text())
save("mad_cyborg_scientist", c)
view(c)
finish(c)
