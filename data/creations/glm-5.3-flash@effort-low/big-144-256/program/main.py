c = input_canvas.copy(name="output")

# ---- palette for edits ----
VINE_D  = c.color("#17301f", "vine_dark")
VINE_M  = c.color("#245233", "vine_mid")
VINE_L  = c.color("#3d7a4a", "vine_light")
CLOAK_D = c.color("#14232b", "cloak_dark")
CLOAK_M = c.color("#1e3944", "cloak_mid")
CLOAK_L = c.color("#2c5464", "cloak_light")
ORB     = c.color("#bff4ff", "orb")
ORB_H   = c.color("#7fd8f0", "orb_halo")
WOOD    = c.color("#3a2a1a", "wood")

# ---- vines climbing the tower walls ----
def vine(x0, y0, y1, sway=3, step=9):
    import math
    pts = []
    for y in range(y0, y1, 2):
        x = x0 + int(round(sway * math.sin((y - y0) / 14.0)))
        pts.append((x, y))
    for (x, y) in pts:
        c.set(x, y, VINE_M)
        c.set(x + 1, y, VINE_D)
    # leaves
    for k, (x, y) in enumerate(pts):
        if k % 3 == 0:
            side = 1 if (k // 3) % 2 == 0 else -1
            c.set(x + side, y - 1, VINE_L)
            c.set(x + side * 2, y - 1, VINE_M)
            c.set(x + side, y, VINE_M)
            c.set(x + side, y + 1, VINE_L)

# left wall vine: from ground up along the wall edge
vine(4, 215, 130, sway=3)
vine(10, 218, 150, sway=2)
# right wall vine
vine(138, 212, 132, sway=2)
vine(131, 216, 160, sway=2)
# a short tendril creeping over the archway stone (left jamb)
vine(50, 224, 196, sway=2)
vine(78, 224, 206, sway=2)

# ---- cloaked mage at the archway, facing away, walking in ----
# body: dark teal cloak, back to viewer, slight walking stride
# head/hood around y=203-208, body to y=224
c.rect(60, 204, 8, 18, CLOAK_M)          # main cloak mass
c.rect(59, 208, 10, 13, CLOAK_M)
c.rect(61, 202, 6, 4, CLOAK_D)           # hood top
c.rect(60, 205, 8, 3, CLOAK_D)           # hood shadow (face hidden, back view)
c.set(63, 203, CLOAK_L)
c.set(64, 203, CLOAK_L)
c.line(60, 221, 61, 225, CLOAK_D)        # trailing hem left
c.line(67, 221, 66, 226, CLOAK_D)        # stepping leg right
c.set(62, 226, CLOAK_D)
c.set(66, 227, CLOAK_D)
c.set(59, 214, CLOAK_L)                  # cloak fold highlights
c.set(60, 218, CLOAK_L)
c.set(68, 212, CLOAK_L)
c.set(67, 217, CLOAK_L)

# staff held in right hand, planted forward
c.line(70, 200, 69, 227, WOOD)
c.set(70, 201, WOOD)
# glowing orb at staff top
c.circle(70, 198, 2, ORB)
c.set(70, 198, ORB)
c.circle(70, 198, 3, ORB_H, fill=False)
c.set(70, 194, ORB_H)
c.set(70, 202, ORB_H)
c.set(66, 198, ORB_H)
c.set(74, 198, ORB_H)
# soft glow cast on the ground ahead
c.set(68, 229, ORB_H)
c.set(72, 230, ORB_H)
c.set(70, 231, ORB_H)

finish(c)
