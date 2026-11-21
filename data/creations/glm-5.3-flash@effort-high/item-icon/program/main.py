from pixelbench_api import *

# 32x32 ancient golden compass icon, blue crystal center, top-down view
c = new_canvas(32, 32, background=None, name="compass_icon")

# colours
OUT = c.color("#2a1c0e", name="outline_dark")      # thick dark outline
GOLD = c.color("#e8b23a", name="gold")
GOLD_D = c.color("#a8741c", name="gold_dark")
GOLD_L = c.color("#ffd97a", name="gold_light")
FACE = c.color("#3a2c14", name="face_dark")        # dark compass face
FACE_L = c.color("#57431f", name="face_mid")
CRY = c.color("#4aa8e8", name="crystal_blue")
CRY_L = c.color("#a8e0ff", name="crystal_light")
CRY_D = c.color("#1c5c9c", name="crystal_dark")
NEEDLE = c.color("#8a6a28", name="needle_brown")
NEEDLE_L = c.color("#ffe9a8", name="needle_light")

CX, CY = 15, 16

# --- thick dark outer outline (2px) ---
c.circle(CX, CY, 14, OUT, fill=False)
c.circle(CX, CY, 13, OUT, fill=False)

# --- gold rim ---
c.circle(CX, CY, 12, GOLD, fill=False)
c.circle(CX, CY, 11, GOLD_D, fill=False)

# --- inner dark ring + face fill ---
c.circle(CX, CY, 10, OUT, fill=False)
c.circle(CX, CY, 9, FACE, fill=True)

# face shading: lighter crescent top-left
c.circle(CX - 1, CY - 1, 8, FACE_L, fill=False)
# restore inner dark ring edge eaten by shading
c.circle(CX, CY, 9, OUT, fill=False)

# --- tick marks on the face (cardinal + intercardinal) ---
for (tx, ty) in [(CX, CY - 7), (CX, CY + 7), (CX - 7, CY), (CX + 7, CY)]:
    c.set(tx, ty, GOLD_L)   # cardinals
for (tx, ty) in [(CX - 5, CY - 5), (CX + 5, CY - 5), (CX - 5, CY + 5), (CX + 5, CY + 5)]:
    c.set(tx, ty, GOLD_D)   # intercardinals

# --- compass needle (NE-SW), tips reach toward ring ---
c.line(CX + 7, CY - 7, CX + 3, CY - 3, NEEDLE)
c.line(CX - 7, CY + 7, CX - 3, CY + 3, NEEDLE)
# bright north tip
c.set(CX + 7, CY - 7, NEEDLE_L)
c.set(CX + 6, CY - 6, NEEDLE_L)

# --- blue crystal center (diamond gem) ---
c.poly([(CX, CY - 5), (CX + 5, CY), (CX, CY + 5), (CX - 5, CY)], CRY, fill=True)
# facets
c.poly([(CX, CY - 5), (CX + 5, CY), (CX, CY)], CRY_L, fill=True)   # top-right light
c.poly([(CX, CY), (CX, CY + 5), (CX - 5, CY)], CRY_D, fill=True)   # bottom-left dark
# gem outline
c.line(CX, CY - 5, CX + 5, CY, OUT)
c.line(CX + 5, CY, CX, CY + 5, OUT)
c.line(CX, CY + 5, CX - 5, CY, OUT)
c.line(CX - 5, CY, CX, CY - 5, OUT)
# sparkle
c.set(CX - 1, CY - 3, CRY_L)
c.set(CX - 2, CY - 2, CRY_L)

# --- rim highlights (top-left arc) ---
for (hx, hy) in [(5, 9), (5, 10), (6, 7), (7, 6), (9, 5), (10, 5), (8, 6)]:
    c.set(hx, hy, GOLD_L)

# --- screws on the gold rim (4 directions) ---
for (sx, sy) in [(CX, CY - 11), (CX, CY + 11), (CX - 11, CY), (CX + 11, CY)]:
    c.set(sx, sy, GOLD_D)
    c.set(sx, sy, GOLD_D)

# --- small crown loop on top (ancient hanging fob) ---
c.set(CX, 0, OUT)
c.set(CX - 1, 1, OUT)
c.set(CX + 1, 1, OUT)
c.set(CX, 1, GOLD_L)

view(c, scale=16)
save("compass_icon", c, indexed=True)

finish(c)
