from pixelbench_api import *

c = new_canvas(64, 64, background="#0d0d14", name="cyborg")

# palette
SKIN   = c.color("#d9a066", "skin")
SKIN2  = c.color("#b07a44", "skin_sh")
SKIN3  = c.color("#8a5a30", "skin_dk")
MET    = c.color("#9aa4b4", "metal")
MET2   = c.color("#6a7488", "metal_sh")
MET3   = c.color("#c8d2e0", "metal_hi")
GLOW   = c.color("#5cf2ff", "glow")
GLOW2  = c.color("#1a9dbb", "glow_dk")
HAIR   = c.color("#e8e8e8", "hair")
HAIR2  = c.color("#b4b4b4", "hair_sh")
COAT   = c.color("#c4bfae", "coat")
COAT2  = c.color("#948f7e", "coat_sh")
COAT3  = c.color("#6e6a5c", "coat_dk")
APRON  = c.color("#5c3a20", "apron")
APRON2 = c.color("#3d2513", "apron_dk")
BELT   = c.color("#2e1c0e", "belt")
DARK   = c.color("#181820", "dark")
MOUTH  = c.color("#3a0d0d", "mouth")
TEETH  = c.color("#f0ece0", "teeth")
RED    = c.color("#b03030", "red")
BOLT   = c.color("#d8b04a", "brass")
CABLE  = c.color("#33333c", "cable")

# ---------- HAIR (messy white, drawn first behind head) ----------
for x, y in [(19,7),(20,6),(21,7),(22,5),(23,6),(24,4),(25,5),(26,4),(27,6),
             (28,4),(29,5),(30,4),(31,6),(32,4),(33,5),(34,4),(35,6),(36,5),
             (37,4),(38,6),(39,5),(40,7),(41,6),(42,8),(43,7),(44,9),(18,9),
             (45,10),(46,12),(17,11),(47,14),(16,13),(18,6),(43,5),(44,6)]:
    c.set(x, y, HAIR)
c.rect(19, 7, 26, 3, HAIR)          # top of head hair mass
c.rect(17, 9, 30, 3, HAIR)
c.rect(16, 12, 3, 3, HAIR)          # side tufts
c.rect(45, 11, 3, 3, HAIR)
# hair shadow
for x in range(19, 45):
    c.set(x, 10, HAIR2)
for x, y in [(21,8),(26,7),(31,8),(36,7),(41,8),(24,9),(34,9),(44,12),(17,13),(47,13)]:
    c.set(x, y, HAIR2)

# ---------- FACE: left human (x21-31), right metal (x32-43) ----------
c.rect(21, 11, 11, 21, SKIN)        # left face
c.rect(32, 11, 12, 21, MET)         # right metal head
# jaw taper
c.rect(22, 30, 20, 2, SKIN)
c.set(32, 30, MET); c.set(33, 30, MET); c.set(34, 30, MET); c.set(35, 30, MET)
for x in range(22, 32):
    c.set(x, 32, SKIN2)
for x in range(32, 36):
    c.set(x, 32, MET2)
c.set(21, 30, SKIN2); c.set(21, 31, SKIN2)
# shading left face
for y in range(11, 31):
    c.set(21, y, SKIN2)
for x in range(23, 31):
    c.set(x, 29, SKIN2)
c.set(22, 28, SKIN2); c.set(30, 27, SKIN2)
# metal shading: vertical panel lines + rivets
for y in range(11, 31):
    c.set(36, y, MET2); c.set(41, y, MET2)
c.set(43, 11, MET3)
for y in range(12, 30, 2):
    c.set(32, y, MET2)
for x, y in [(33,13),(40,13),(33,26),(40,26),(38,22),(34,19)]:
    c.set(x, y, MET3)
# metal plate seam on cheek
c.line(37, 24, 42, 27, MET2)

# ---------- BROW / FOREHEAD ----------
c.rect(22, 13, 9, 1, SKIN3)         # left brow
c.rect(33, 13, 9, 1, MET2)          # metal brow ridge

# ---------- EYES ----------
# left human eye: wide mad
c.rect(23, 16, 4, 2, "#f4f4f4")
c.set(25, 16, DARK); c.set(25, 17, DARK)   # pupil looking right
c.set(23, 15, SKIN3); c.set(26, 15, SKIN3) # upper lid
c.set(24, 18, SKIN2); c.set(25, 18, SKIN2)
# right glowing cybernetic eye (big lens)
c.circle(38, 17, 2, GLOW2)
c.set(38, 17, GLOW); c.set(37, 16, GLOW)
c.circle(38, 17, 3, MET2, fill=False)
c.set(38, 13, GLOW); c.set(38, 21, GLOW)   # glow cross flare
c.set(35, 17, GLOW); c.set(41, 17, GLOW)
c.set(38, 14, GLOW2); c.set(38, 20, GLOW2)
c.set(36, 15, GLOW2); c.set(40, 19, GLOW2)

# ---------- NOSE (left human) ----------
c.line(27, 19, 26, 22, SKIN2)
c.set(26, 23, SKIN3); c.set(27, 23, SKIN3)
# metal nose vent right
c.line(37, 19, 38, 22, MET2)
c.set(37, 22, MET3); c.set(38, 22, MET3)

# ---------- MANIACAL GRIN ----------
c.rect(24, 26, 14, 3, MOUTH)
for x in range(24, 38, 2):
    c.set(x, 26, TEETH)
c.set(24, 28, TEETH); c.set(27, 28, TEETH); c.set(30, 28, TEETH); c.set(33, 28, TEETH); c.set(36, 28, TEETH)
c.set(23, 27, SKIN3); c.set(38, 27, MET2)
# grin creases
c.line(22, 24, 24, 26, SKIN2)
c.line(39, 24, 37, 26, MET2)

# ---------- BRAIN ELECTRODE PLUGS (top of head) ----------
for i, x in enumerate([26, 31, 36]):
    c.rect(x, 8, 2, 3, MET2)
    c.set(x, 7, MET3)
    c.set(x, 8, BOLT)
# cables from plugs going up/back
c.line(27, 7, 30, 3, CABLE); c.line(30, 3, 36, 2, CABLE)
c.line(32, 7, 34, 3, CABLE)
c.line(37, 7, 42, 4, CABLE); c.line(42, 4, 48, 6, CABLE)
c.set(30, 2, CABLE); c.set(36, 1, CABLE); c.set(49, 6, CABLE)

# ---------- EAR / side bolt ----------
c.set(20, 20, SKIN3); c.set(20, 21, SKIN3)
c.rect(43, 19, 2, 3, MET2); c.set(44, 20, MET3)

# ---------- NECK ----------
c.rect(27, 33, 10, 4, SKIN2)
for x in range(32, 37):
    c.set(x, 33, MET2)
c.line(29, 34, 29, 36, SKIN3)

# ---------- TORSO: dirty lab coat ----------
c.rect(16, 37, 32, 4, COAT)         # shoulders
c.rect(14, 40, 36, 12, COAT)
c.rect(13, 44, 38, 10, COAT)
c.rect(12, 50, 40, 8, COAT)
# coat shading
for y in range(37, 58):
    c.set(12, y, COAT2) if y >= 40 else c.set(16, y, COAT2)
    c.set(51, y, COAT2)
for x in range(13, 52):
    c.set(x, 57, COAT2)
# collar
c.line(26, 37, 28, 41, COAT3)
c.line(38, 37, 36, 41, COAT3)
c.set(27, 37, COAT3); c.set(37, 37, COAT3)
# coat stains / dirt
for x, y in [(18,45),(19,46),(18,47),(44,42),(45,43),(22,52),(23,53),(41,50),(40,51),(46,54),(17,54)]:
    c.set(x, y, COAT2)
c.set(20, 48, COAT3); c.set(43, 47, COAT3)

# ---------- LEATHER APRON (center) ----------
c.rect(25, 41, 14, 17, APRON)
for y in range(41, 58):
    c.set(25, y, APRON2); c.set(38, y, APRON2)
for x in range(25, 39):
    c.set(x, 57, APRON2)
c.set(26, 43, APRON2); c.set(35, 46, APRON2); c.set(30, 50, APRON2)
# apron straps
c.line(26, 38, 26, 41, APRON); c.line(37, 38, 37, 41, APRON)

# ---------- TOOL BELT ----------
c.rect(12, 50, 40, 3, BELT)
for x in range(14, 51, 4):
    c.set(x, 51, BOLT)
# pouches
c.rect(15, 53, 4, 4, BELT); c.set(16, 54, BOLT)
c.rect(45, 53, 4, 4, BELT); c.set(47, 54, BOLT)
# hanging tools
c.line(17, 57, 17, 61, MET2); c.set(17, 61, MET3)   # screwdriver
c.line(47, 57, 47, 60, MET2); c.set(47, 60, RED)    # handle
c.set(18, 58, MET2)

# ---------- EXPOSED METAL ROBOTIC ARM (left side, raised) ----------
# shoulder joint
c.circle(14, 41, 3, MET2)
c.set(14, 41, MET3)
c.set(12, 39, MET3); c.set(16, 43, MET2)
# upper arm going up-left
c.line(13, 39, 9, 31, MET)
c.line(12, 39, 8, 31, MET2)
c.set(13, 40, MET3)
# elbow joint
c.circle(9, 30, 2, MET2); c.set(9, 30, MET3)
# forearm going up-right toward head
c.line(10, 29, 14, 22, MET)
c.line(9, 29, 13, 22, MET2)
# wires on arm
c.set(11, 35, CABLE); c.set(10, 33, CABLE); c.set(11, 27, CABLE); c.set(12, 25, CABLE)
# prosthetic hand near face, fingers spread
c.rect(13, 18, 4, 4, MET2)          # palm
c.set(13, 18, MET3)
c.line(13, 18, 12, 15, MET)         # finger 1
c.line(15, 18, 15, 14, MET)         # finger 2
c.line(16, 19, 18, 16, MET)         # finger 3
c.set(12, 14, MET3); c.set(15, 13, MET3); c.set(18, 15, MET3)
# cables from wrist trailing down
c.line(16, 22, 19, 27, CABLE); c.line(19, 27, 18, 33, CABLE)
c.line(15, 22, 17, 26, CABLE)
c.set(18, 34, CABLE); c.set(17, 36, CABLE)

# ---------- RIGHT SIDE: coat arm + hint of metal hand ----------
for y in range(41, 56):
    c.set(51, y, COAT2)
c.rect(50, 41, 3, 14, COAT)
for y in range(41, 55):
    c.set(52, y, COAT2)
c.rect(50, 55, 3, 4, MET2)          # robotic hand at side
c.set(50, 55, MET3)
c.set(49, 58, MET2); c.set(53, 58, MET2)

# ---------- rim light (strong contrast, cyan from right) ----------
for y in range(11, 31):
    if c.get(43, y) not in (0,):
        pass
c.set(44, 12, MET3); c.set(44, 14, MET3)
# glow light spill on right of coat
for y in range(38, 50):
    c.set(50, y, COAT2)
c.set(49, 40, COAT2); c.set(49, 44, COAT2)

print(c.stats_text())
view(c, margin=0)
save("mad-cyborg-scientist", c)
finish(c)
