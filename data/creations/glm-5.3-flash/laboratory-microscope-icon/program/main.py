# ============================================================
# 32x32 laboratory microscope icon - three-quarter view
# ============================================================
c = new_canvas(32, 32, name="microscope")

# ---- palette ----
INK   = c.color("#1a2130", "ink")
L1    = c.color("#cbd6e4", "metal_light")
L2    = c.color("#96a5bc", "metal_mid")
L3    = c.color("#5f6e88", "metal_dark")
L4    = c.color("#3c4960", "metal_deep")
GLS   = c.color("#1f3f6e", "glass")
GLH   = c.color("#7fb5e8", "glass_hi")
STGL  = c.color("#71839f", "stage_top")
STG   = c.color("#4b5b76", "stage_front")
STGD  = c.color("#33415a", "stage_edge")
BASE  = c.color("#2b364c", "base")
BASEL = c.color("#4e5d78", "base_top")
KNB   = c.color("#e3a73f", "knob")
KNBH  = c.color("#f6cd74", "knob_hi")
KNBD  = c.color("#9a681f", "knob_dark")
LIT   = c.color("#f7ecc0", "lamp")

# ---- arm (drawn first: everything else sits in front of it) ----
arm = [(20,3),(23,3),(25,6),(26,9),(27,13),(28,18),(28,26),(24,26),(24,20),(24,18),
       (23,17),(23,15),(22,14),(22,13),(21,12),(21,10),(20,9),(20,7),(19,6),(19,4),(20,3)]
c.poly(arm, L2, fill=True)
for x in range(20, 24):
    c.set(x, 3, L1)              # light catches the top of the arm

# rim light along the arm's outer (right) edge
w, h, buf = c.to_rgba()
def alpha_at(x, y):
    if 0 <= x < w and 0 <= y < h:
        return buf[4 * (y * w + x) + 3]
    return 0
for y in range(4, 27):
    for x in range(28, 18, -1):
        if alpha_at(x, y):
            c.set(x, y, L1)
            break

# ---- base ----
c.rect(6, 26, 21, 1, BASEL)      # top surface  x=6..26
c.rect(4, 27, 25, 2, BASE)       # body         x=4..28, y=27..28
c.rect(5, 29, 23, 1, L4)         # bottom shade x=5..27

# ---- body tube (tilted = three-quarter view) ----
tube = [(13,17,5),(13,17,6),(14,18,7),(14,18,8),(14,18,9),
        (15,19,10),(15,19,11),(16,20,12)]
for x0, x1, y in tube:
    c.set(x0, y, L1)
    for x in range(x0+1, x1):
        c.set(x, y, L2)
    c.set(x1, y, L3)

# ---- eyepiece ----
c.rect(13,2,5,1,L1)              # top rim
c.set(14,2,GLS); c.set(15,2,GLS); c.set(16,2,GLS)   # dark opening
c.set(14,2,GLH)                  # lens glint
c.rect(12,3,7,1,L2)              # shoulder
c.set(12,3,L1); c.set(18,3,L3)
c.rect(13,4,5,1,L3)              # junction ring

# ---- nosepiece + objective ----
c.rect(16,13,5,1,L4)             # ring
c.rect(15,14,7,1,L3)             # turret
c.set(15,14,L4); c.set(21,14,L4)
c.set(16,15,L1)                  # objective body
for x in range(17,20): c.set(x,15,L2)
c.set(20,15,L3)
for x in range(16,19): c.set(x,16,L2)
c.set(19,16,L3); c.set(20,16,L3)
c.rect(16,17,5,1,L4)             # tip / lens

# ---- stage ----
c.rect(5,18,19,1,STGL)           # top surface x=5..23
c.rect(5,19,19,1,STG)
c.rect(6,20,18,1,STGD)           # front edge
c.rect(15,18,7,1,GLS)            # slide
c.set(16,18,GLH); c.set(20,18,GLH)

# ---- illuminator ----
c.rect(16,21,6,1,L4)             # condenser
for x in range(17,21): c.set(x,21,LIT)
c.rect(15,22,8,4,L4)             # housing
for y in range(22,26): c.set(15,y,L3)

# ---- focus knob ----
c.circle(27,22,2,KNB)
c.set(26,20,KNBH); c.set(25,21,KNBH)
c.set(29,22,KNBD); c.set(29,23,KNBD); c.set(28,24,KNBD); c.set(27,24,KNBD)

# ---- ink outline: dilate the silhouette by 1 px ----
w, h, buf = c.to_rgba()
def alpha_now(x, y):
    if 0 <= x < w and 0 <= y < h:
        return buf[4 * (y * w + x) + 3]
    return 0
edge = [(x,y) for y in range(h) for x in range(w)
        if alpha_now(x,y) == 0 and (alpha_now(x+1,y) or alpha_now(x-1,y)
                                    or alpha_now(x,y+1) or alpha_now(x,y-1))]
for x, y in edge:
    c.set(x, y, INK)

print(c.stats_text())
finish(c)
