import math

W, HC = 52, 54
OU    = (66, 33, 16)      # dark brown outline
WOOD  = (188, 108, 12)
WOODL = (252, 196, 76)
WOODH = (255, 231, 90)
WOODD = (116, 52, 28)
SKIN  = (197, 149, 106)
SKINL = (246, 211, 155)
SKINM = (241, 216, 179)
SAGE  = (104, 120, 98)
SAGEL = (164, 180, 150)
STRW  = (241, 247, 247)
STRD  = (225, 212, 194)
BLACK = (18, 19, 17)


def erase_rect(c, x0, x1, y0, y1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            c.set(x, y, None)


def limb_arc(c, cx, cy, R, a0, a1, base, taper):
    """Solid tapered arc band for a bow limb (outline added afterwards)."""
    N = 1400
    for i in range(N + 1):
        u = i / N
        a = a0 + (a1 - a0) * u
        w = base * (taper + (1 - taper) * (math.sin(math.pi * u) ** 0.5))
        r = R - w / 2
        while r <= R + w / 2 + 1e-9:
            x = int(round(cx + r * math.cos(a)))
            y = int(round(cy + r * math.sin(a)))
            d = r - (R - w / 2)
            if d < 1.0 or d > w - 1.0:
                col = OU
            elif d > w - 2.4:
                col = WOODL
            elif d < 2.0:
                col = WOODD
            else:
                col = WOOD
            c.set(x, y, col)
            r += 0.4


def seg(c, p0, p1, w, color):
    """Thick limb as a rotated rectangle."""
    x0, y0 = p0
    x1, y1 = p1
    d = math.hypot(x1 - x0, y1 - y0)
    px, py = -(y1 - y0) / d * w / 2.0, (x1 - x0) / d * w / 2.0
    c.poly([(x0 + px, y0 + py), (x1 + px, y1 + py),
            (x1 - px, y1 - py), (x0 - px, y0 - py)], color, fill=True)


# ================= frame 1 : the original picture =================
f1 = new_canvas(W, HC, name='frame1')
f1.blit(input_canvas, 6, 6)

# ================= body for frame 2 (resting bow removed) =================
body2 = input_canvas.copy(name='body2')
erase_rect(body2, 24, 34, 0, 18)     # old upper limb, string, tip ornament
erase_rect(body2, 26, 34, 19, 24)    # old string / limb / hand
erase_rect(body2, 22, 34, 25, 26)    # stray string pixels
erase_rect(body2, 23, 34, 27, 34)    # old lower limb
erase_rect(body2, 22, 34, 35, 38)    # old tail of the lower limb

f2 = new_canvas(W, HC, name='frame2')
f2.blit(body2, 4, 6)

# ================= the bow, fully bent =================
CX, CY, R = 26.56, 23.61, 20.43
A0, A1 = math.radians(-65.6), math.radians(71.6)
T1 = (35, 5)          # upper tip
T2 = (33, 43)         # lower tip
APEX = (26, 23)       # string fully drawn back to the jaw

bowc = new_canvas(W, HC, name='bow')
limb_arc(bowc, CX, CY, R, A0, A1, 6.2, 0.34)
bowc.circle(T1[0], T1[1], 1, WOODH)
bowc.circle(T2[0], T2[1], 1, WOODH)
bowc.outline(OU)
f2.blit(bowc, 0, 0)

# grip wrap at the riser, then the string pulled to the anchor
for y in range(20, 28):
    for x in range(44, 48):
        v = f2.get(x, y)
        if v and v != input_canvas.get(0, 0):
            pass
f2.rect(46, 20, 2, 8, WOODD)

f2.line(T1[0], T1[1], APEX[0], APEX[1], STRW)
f2.line(APEX[0], APEX[1], T2[0], T2[1], STRW)
f2.set(APEX[0], APEX[1], STRD)

# ================= arms and hands =================
arms = new_canvas(W, HC, name='arms')
# bow arm, extended out to the grip
seg(arms, (28, 28), (43, 25), 4, SAGE)
seg(arms, (29, 27), (42, 24), 2, SAGEL)
# bow hand gripping the riser
arms.ellipse(45, 24, 3, 3, SKIN)
arms.set(44, 22, SKINL)
arms.set(46, 22, SKINL)
arms.set(44, 26, SKINL)
# drawing arm: elbow pulled back and up, forearm to the jaw
seg(arms, (24, 31), (15, 24), 4, SKIN)
seg(arms, (15, 24), (25, 23), 4, SKIN)
seg(arms, (16, 23), (24, 22), 1, SKINL)
# drawing hand at the anchor point
arms.ellipse(26, 23, 2, 2, SKIN)
arms.set(26, 22, SKINL)
arms.set(27, 23, SKINL)
arms.outline(OU)
f2.blit(arms, 0, 0)

print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text(region=(10, 10, 51, 45)))

finish([f1, f2])
