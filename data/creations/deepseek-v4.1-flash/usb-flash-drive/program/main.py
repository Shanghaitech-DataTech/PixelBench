from pixelbench_api import *

W, H = 32, 32
c = new_canvas(W, H, background=None, name="usb")

OUT    = "#12161f"   # dark outline
MET_X  = "#f4f8fd"   # brightest specular
MET_L  = "#cbd5e1"   # light metal
MET_M  = "#97a3b1"   # mid metal
MET_D  = "#6b7583"   # dark metal
MET_DD = "#48505c"   # darkest metal
SEAM   = "#2b323c"   # recessed seam / panel
GROOVE = "#3a414c"   # grip groove
CAV    = "#1c222b"   # inner cavity
LEA    = "#7d4a2e"   # leather strap
LEA_L  = "#a0673f"
LEA_D  = "#57301e"
STITCH = "#e2c69a"
GOLD   = "#e6bc52"   # connector contacts
RG_X   = "#ffeeb0"   # brass ring highlight
RG_L   = "#f2d478"
RG_M   = "#cda64e"
RG_D   = "#9a7631"
LED    = "#5fe0cf"
LED_D  = "#2f8f86"


def hspan(y, x0, x1, colr):
    c.rect(x0, y, x1 - x0 + 1, 1, colr)


# ===================== brass keyring =====================
ring_spans = {
    1: (15, 17), 2: (14, 18), 3: (13, 19), 4: (12, 20),
    5: (11, 21), 6: (11, 21), 7: (11, 21), 8: (12, 20),
    9: (13, 19), 10: (14, 18), 11: (15, 17),
}
hole_spans = {3: (16, 16), 4: (15, 17), 5: (14, 18),
              6: (14, 18), 7: (15, 17), 8: (16, 16)}

for y, (x0, x1) in ring_spans.items():
    hspan(y, x0, x1, OUT)                       # outer outline
for y, (x0, x1) in ring_spans.items():
    for x in range(x0 + 1, x1):                 # band + shading
        d = (x - 16) + (y - 6)
        if d <= -3:
            colr = RG_X
        elif d <= 0:
            colr = RG_L
        elif d <= 3:
            colr = RG_M
        else:
            colr = RG_D
        c.set(x, y, colr)
for y, (x0, x1) in hole_spans.items():
    hspan(y, x0, x1, None)                      # punch the hole

# ===================== leather keychain strap (in front of ring) ====
c.rect(13, 11, 6, 6, OUT)      # dark silhouette x13..18, y11..16
c.rect(14, 11, 4, 1, LEA_D)    # shadowed fold at the top
c.rect(14, 12, 4, 5, LEA)      # leather body
c.rect(14, 12, 1, 5, LEA_L)    # lit left face
c.rect(17, 12, 1, 5, LEA_D)    # shaded right face
c.set(15, 12, STITCH)          # stitching
c.set(16, 13, STITCH)
c.set(15, 14, STITCH)

# ===================== metal casing =====================
TOP, BOT = 15, 25
c.rect(9, TOP, 14, BOT - TOP + 1, OUT)          # silhouette x9..22
for p in ((9, TOP), (22, TOP), (9, BOT), (22, BOT)):
    c.set(*p, None)                             # bevelled corners

BODY = {10: MET_L, 11: MET_X, 12: MET_L, 13: MET_L,
        14: MET_M, 15: MET_M, 16: MET_M, 17: MET_M,
        18: MET_D, 19: MET_D, 20: MET_DD, 21: MET_D}
CAP = {10: MET_M, 11: MET_M, 12: MET_M, 13: MET_M,
       14: MET_M, 15: MET_M, 16: MET_D, 17: MET_D,
       18: MET_D, 19: MET_D, 20: MET_DD, 21: MET_DD}

for y in (19, 20, 21, 22, 23, 24):
    for x in range(10, 22):
        c.set(x, y, BODY[x])
for y in (16, 17):
    for x in range(10, 22):
        c.set(x, y, CAP[x])

# rim light under the housing seam
for x in (11, 12, 13):
    c.set(x, 19, MET_X)
for x in (14, 15, 16, 17):
    c.set(x, 19, MET_L)

# lighter left edge on the housing cap
for y in (16, 17):
    c.set(10, y, MET_L)
    c.set(11, y, MET_L)
    c.set(12, y, MET_M)

# seam under the cap
for x in range(10, 22):
    c.set(x, 18, SEAM)

# recessed grip groove
for x in range(11, 21):
    c.set(x, 21, GROOVE)

# LED indicator near the plug end
c.rect(18, 23, 3, 2, SEAM)
c.set(19, 23, LED)
c.set(19, 24, LED_D)

# ===================== USB connector =====================
C0, C1 = 26, 30
for y in range(C0, C1 + 1):
    c.set(10, y, OUT)
    c.set(21, y, OUT)
SHELL = {11: MET_X, 12: MET_L, 13: MET_L, 14: MET_L,
         15: MET_M, 16: MET_M, 17: MET_M,
         18: MET_D, 19: MET_D, 20: MET_DD}
for y in (26, 27, 28):
    for x, colr in SHELL.items():
        c.set(x, y, colr)

# small shell notches
c.set(14, 27, OUT)
c.set(17, 27, OUT)

# open front: dark cavity with four gold contacts
for y in (29, 30):
    hspan(y, 11, 20, CAV)
for x in (13, 15, 17, 19):
    c.set(x, 29, GOLD)

print(c.stats_text())
print(c.matrix_text(indices=False))

save("usb_flash_drive", c)
finish(c)
