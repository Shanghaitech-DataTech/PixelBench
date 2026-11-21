from pixelbench_api import new_canvas, view, save, finish

W = H = 32
c = new_canvas(W, H, name="spellbook")

# ---- palette: 8 colours ----
OUT   = "#1b1020"   # dark outline / deepest shadow
LEA_D = "#4a2419"   # leather shadow
LEA_M = "#7d3f27"   # leather mid
LEA_L = "#b06a3f"   # leather highlight
PAGE  = "#e6d9b0"   # page block
MET_D = "#7c8494"   # metal shade
MET_L = "#d5dce6"   # metal light
GEM   = "#3fc0a8"   # magic gem

# silhouette
X0, Y0, X1, Y1 = 3, 3, 28, 28
CX, CY = 17, 15          # emblem centre


def in_rr(x, y, x0, y0, x1, y1, cham):
    if x < x0 or x > x1 or y < y0 or y > y1:
        return False
    return min(x - x0, x1 - x) + min(y - y0, y1 - y) >= cham


def dia(x, y, cx, cy):
    return abs(x - cx) + abs(y - cy)


def corner_cap(x, y):
    """Diagonal metal cap on one of the four outer corners."""
    for (ox, oy, sx, sy) in ((X0 + 1, Y0 + 1, 1, 1), (X1 - 1, Y0 + 1, -1, 1),
                             (X0 + 1, Y1 - 1, 1, -1), (X1 - 1, Y1 - 1, -1, -1)):
        u = (x - ox) * sx
        v = (y - oy) * sy
        if 0 <= u <= 5 and 0 <= v <= 5 and u + v <= 4:
            if u + v >= 3:
                return MET_L          # lit diagonal edge
            if u <= 1 and v <= 1:
                return MET_L          # rivet
            return MET_D
    return None


def color_at(x, y):
    if not in_rr(x, y, X0, Y0, X1, Y1, 3):
        return None                                   # transparent
    if not in_rr(x, y, X0 + 1, Y0 + 1, X1 - 1, Y1 - 1, 2):
        return OUT                                    # 1px outline

    # clasp strap wrapping the fore-edge
    if 24 <= x <= 27 and 14 <= y <= 17:
        if y == 14:
            return MET_L
        if y == 17:
            return OUT
        return MET_D
    if x == 24 and y in (13, 18):
        return OUT

    # central emblem: metal-framed gem
    d = dia(x, y, CX, CY)
    if d <= 5:
        if d <= 2:
            if dia(x, y, CX - 1, CY - 1) <= 1:
                return MET_L                          # glint
            return GEM
        if d == 3:
            return OUT
        if d == 4:
            return MET_L if (x - CX) + (y - CY) < 0 else MET_D
        return OUT                                    # d == 5 outer line

    cap = corner_cap(x, y)
    if cap:
        return cap

    # ---- spine ----
    if x <= 8:
        if y in (12, 18):
            return LEA_L if x <= 7 else LEA_D
        if y in (13, 19):
            return LEA_D if x <= 7 else OUT
        if x == 8:
            return OUT                                # hinge groove
        if x == 4:
            return LEA_L
        if x <= 6:
            return LEA_M
        return LEA_D

    if x == 9:
        return LEA_D                                  # cover shadow by hinge

    # ---- page block (fore-edge) ----
    if x >= 25:
        if x == 27:
            return LEA_D
        if y in (8, 12, 20, 24):
            return LEA_D
        return PAGE

    # ---- front cover ----
    if y == 4 or x == 10:
        return LEA_L
    if y >= 26 or x >= 23:
        return LEA_D
    if (x, y) in ((12, 7), (20, 8), (11, 16), (13, 21), (21, 20), (22, 11),
                  (14, 9), (19, 22)):
        return LEA_D                       # leather grain
    if (x, y) in ((12, 6), (20, 7), (12, 20), (21, 19)):
        return LEA_L                       # worn highlights
    return LEA_M


for y in range(H):
    for x in range(W):
        col = color_at(x, y)
        if col is not None:
            c.set(x, y, col)

print(c.stats_text())
save("spellbook", c, indexed=True)
print(view(c, scale=16, margin=0))
print(c.matrix_text(indices=True))
finish(c)
