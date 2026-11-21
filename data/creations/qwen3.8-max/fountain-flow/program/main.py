# fountain-flow edit: turn the waterless fountain into a running one.
# All feature coordinates below are given in INPUT space; the input is
# blitted at dy=8 so the helpers add DY.
DY = 8
out = new_canvas(64, 84, name="output")
out.blit(input_canvas, 0, DY)

W = "#2ec7dc"    # bright teal water
F = "#1d8baa"    # deep teal water
D = "#ffffffff"  # white foam / jet core

def M(x):
    return 63 - x

def px(pts, col):
    for (x, y) in pts:
        out.set(x, y + DY, col)

def pxm(pts, col):
    for (x, y) in pts:
        out.set(x, y + DY, col)
        out.set(M(x), y + DY, col)

# ============ top jet shooting up from the spout ============
for y in range(-6, 0):
    out.set(31, y + DY, D)
    out.set(32, y + DY, W)
px([(31, -8), (32, -8), (30, -7), (31, -7), (32, -7), (33, -7)], D)   # crown top
pxm([(29, -7), (29, -6), (28, -5), (28, -4)], W)                      # crown sides
arc = [(27, y) for y in range(-3, 10)]                                # falling arcs
pxm(arc, W)
pxm([(27, -1), (27, 3), (27, 7)], D)
pxm([(25, -3), (24, 1)], D)                                           # flying drops
pxm([(26, 9), (27, 9), (28, 9)], D)                                   # landing foam
pxm([(26, 10), (28, 10)], W)
pxm([(30, 5), (30, 6)], D)                                            # spout splash

# ============ cascade: top basin -> middle basin ============
for y in range(12, 16):
    pxm([(20, y)], W)
    pxm([(21, y)], D)
pxm([(20, 16), (21, 16)], D)
pxm([(19, 15), (22, 15), (19, 16), (22, 16)], W)

# ============ cascade: middle basin -> lower basin ============
for y in range(21, 24):
    pxm([(14, y)], W)
    pxm([(15, y)], D)
pxm([(15, 24), (16, 24)], D)
pxm([(14, 24), (17, 24), (15, 25)], W)

# ============ cascade: lower basin -> ground pool ============
for y in range(32, 42):
    pxm([(15, y)], W)
    pxm([(16, y)], D)
    pxm([(17, y)], W)
pxm([(16, 36), (16, 39)], W)   # texture breaks in the foam core
pxm([(15, 42), (16, 42), (17, 42), (16, 43)], D)
pxm([(14, 42), (18, 42), (15, 43), (17, 43)], W)
pxm([(13, 40), (19, 39)], D)   # spray droplets

# ============ front overflow: pool spout gushing down ============
for y in range(58, 67):
    out.set(31, y + DY, W)
    out.set(32, y + DY, D)
out.set(32, 61 + DY, W)
out.set(31, 64 + DY, W)
px([(31, 67), (32, 67)], D)
px([(30, 67), (33, 67), (29, 68), (34, 68)], W)

# ============ ripples / glints on every water surface ============
pxm([(25, 10), (26, 10)], D)          # top basin dashes
pxm([(29, 11), (30, 11)], D)
pxm([(21, 17), (22, 17)], D)          # middle basin dashes
pxm([(24, 18), (25, 18)], D)
pxm([(17, 26), (18, 26)], D)          # lower basin dashes
pxm([(20, 27), (21, 27)], D)
pxm([(13, 47), (14, 47)], D)          # pool dashes
pxm([(16, 48), (17, 48)], D)
pxm([(20, 52), (21, 52)], D)
pxm([(24, 54), (25, 54)], D)
pxm([(27, 50), (28, 50)], D)

view(out)
finish(out)
