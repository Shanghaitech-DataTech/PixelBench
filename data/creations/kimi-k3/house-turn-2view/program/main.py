# House turn: 45-degree and 90-degree views, fixed elevated isometric camera.
INK   = 'c3'; WOOD = 'c1'; WOODD = 'c0'; WOODL = 'c2'
PLAS  = 'c9'; PLASD = 'c8'
ROOFM = 'c5'; ROOFD = 'c4'; ROOFL = 'c6'; RIDGE = 'c7'
SHAD  = 'c10'
W, H = 112, 157

def shadow(c, cx, cz, rx, rz):
    c.ellipse(cx, cz, rx, rz, SHAD, fill=True)

def finial(c, cx, ztop, zbot):
    c.line(cx, zbot, cx, ztop + 4, INK)
    for dz in range(ztop, ztop + 4):
        c.line(cx - 1, dz, cx + 1, dz, RIDGE)
    c.set(cx, ztop, INK)

def roof_plane(c, pts, courses=(0.30, 0.55, 0.80), col=ROOFM):
    (ax, ay), (bx, by), (cx2, cy2), (dx, dy) = pts
    c.poly(pts, col, fill=True)
    c.poly(pts, INK, fill=False)
    for t in courses:
        x0 = ax + (dx - ax) * t; y0 = ay + (dy - ay) * t
        x1 = bx + (cx2 - bx) * t; y1 = by + (cy2 - by) * t
        c.line(round(x0), round(y0), round(x1), round(y1), ROOFD)
    for t in (0.42, 0.68):
        xa = ax + (dx - ax) * t; ya = ay + (dy - ay) * t
        xb = bx + (cx2 - bx) * t; yb = by + (cy2 - by) * t
        for s in (0.25, 0.55, 0.85):
            px = xa + (xb - xa) * s; py = ya + (yb - ya) * s
            c.line(round(px), round(py), round(px), round(py + 3), ROOFD)
    hx0 = ax + (dx - ax) * 0.12; hy0 = ay + (dy - ay) * 0.12
    hx1 = bx + (cx2 - bx) * 0.12; hy1 = by + (cy2 - by) * 0.12
    c.line(round(hx0), round(hy0), round(hx1), round(hy1), ROOFL)

def eave_beam(c, x0, y0, x1, y1):
    c.line(x0, y0, x1, y1, INK)
    c.line(x0, y0 + 1, x1, y1 + 1, WOODD)
    c.line(x0, y0 + 2, x1, y1 + 2, WOODL)

def plank_wall(c, x0, z0, x1, z1, step=8):
    c.rect(x0, z0, x1 - x0 + 1, z1 - z0 + 1, PLAS, fill=True)
    for x in range(x0 + step, x1, step):
        c.line(x, z0 + 1, x, z1 - 1, PLASD)
    c.line(x0, z1, x1, z1, INK)

def corner_post(c, x, z0, z1):
    c.line(x, z0, x, z1, INK)
    c.line(x + 1, z0 + 1, x + 1, z1 - 1, WOODD)

def door(c, cx, zbase, w=17, h=30):
    x0, x1 = cx - w // 2, cx + w // 2
    zt = zbase - h
    c.rect(x0 - 7, zbase + 1, w + 15, 3, PLASD, fill=True)
    c.rect(x0 - 4, zbase - 1, w + 9, 2, PLAS, fill=True)
    c.rect(x0 - 3, zt - 2, w + 7, h + 2, INK, fill=True)
    c.rect(x0 - 2, zt - 1, w + 5, h + 1, WOODD, fill=True)
    c.rect(x0, zt + 4, w + 1, h - 4, WOOD, fill=True)
    c.circle(cx, zt + 4, w // 2, WOOD, fill=True)
    c.rect(x0, zt + 1, w + 1, 3, WOOD, fill=True)
    for x in range(x0 + 4, x1, 4):
        c.line(x, zt + 5, x, zbase - 1, WOODD)
    c.line(x0, zt + 12, x1, zt + 12, WOODD)
    c.line(x0, zt + 21, x1, zt + 21, WOODD)
    c.set(cx + 5, zt + 17, INK)

def window(c, cx, zc, w=9, h=13):
    x0, x1 = cx - w // 2, cx + w // 2
    z0, z1 = zc - h // 2, zc + h // 2
    c.rect(x0 - 2, z0 - 1, w + 5, h + 3, INK, fill=True)
    c.rect(x0 - 1, z0, w + 3, h + 1, WOOD, fill=True)
    c.rect(x0, z0 + 1, w + 1, h - 1, ROOFM, fill=True)
    c.rect(x0 + 1, z0 + 2, 3, 4, ROOFL, fill=True)
    c.line(cx, z0 + 1, cx, z1 - 1, WOODD)
    c.line(x0, zc, x1, zc, WOODD)
    c.rect(x0 - 2, z1 + 1, w + 5, 2, WOODD, fill=True)

# ================================================================ FRAME 1 (45 deg)
f1 = new_canvas(W, H, name='frame1_45deg')
shadow(f1, 56, 143, 44, 9)

# right wall (recedes up-right) with its window
f1.poly([(74, 96), (98, 84), (98, 128), (74, 140)], PLAS, fill=True)
f1.poly([(74, 96), (98, 84), (98, 128), (74, 140)], INK, fill=False)
for (x, zt, zb) in ((80, 94, 136), (87, 91, 132), (94, 87, 129)):
    f1.line(x, zt, x, zb, PLASD)
f1.line(74, 139, 98, 127, PLASD)
f1.rect(84, 100, 9, 15, INK, fill=True)
f1.rect(85, 101, 7, 13, WOOD, fill=True)
f1.rect(86, 102, 5, 11, ROOFM, fill=True)
f1.rect(86, 103, 2, 4, ROOFL, fill=True)
f1.line(88, 102, 88, 112, WOODD)
f1.line(86, 107, 91, 107, WOODD)
f1.rect(83, 115, 11, 2, WOODD, fill=True)

# front wall + door
plank_wall(f1, 14, 96, 74, 140)
corner_post(f1, 14, 96, 140)
corner_post(f1, 73, 96, 140)
door(f1, 44, 140)

# roof: ridge from front apex (56,26) to back (86,14); front end finialed
finial(f1, 56, 10, 30)
f1.line(86, 10, 86, 18, INK)                      # back ridge cap
f1.line(85, 10, 87, 10, RIDGE)
roof_plane(f1, [(56, 26), (86, 14), (104, 74), (12, 92)])          # front-facing slope
f1.poly([(86, 14), (104, 74), (76, 86), (56, 26)], ROOFD, fill=True)  # right slope
f1.poly([(86, 14), (104, 74), (76, 86), (56, 26)], INK, fill=False)
f1.line(90, 34, 96, 60, ROOFM)
f1.line(84, 48, 90, 70, ROOFM)
eave_beam(f1, 12, 92, 76, 86)
eave_beam(f1, 76, 86, 104, 74)

view(f1)

# ================================================================ FRAME 2 (90 deg)
f2 = new_canvas(W, H, name='frame2_90deg')
shadow(f2, 56, 143, 42, 9)

# the right-hand wall now faces us, with its window
plank_wall(f2, 18, 96, 94, 140)
corner_post(f2, 18, 96, 140)
corner_post(f2, 93, 96, 140)
window(f2, 56, 112)

# roof seen square from that side: ridge now runs straight across the view
# (side-on = exactly 90 degrees); both gable-end ridge poles visible.
finial(f2, 26, 22, 44)
finial(f2, 88, 22, 44)
roof_plane(f2, [(26, 44), (88, 44), (100, 92), (12, 92)],
           courses=(0.28, 0.52, 0.76))
eave_beam(f2, 12, 92, 100, 92)

view(f2)

finish([f1, f2])
