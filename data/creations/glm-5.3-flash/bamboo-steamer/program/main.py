import math

c = new_canvas(32, 32, None, "bamboo-steamer")

# ---------------- palette ----------------
BAM_LIGHT = c.color("#F2DFAE", "bamboo_light")
BAM_MID   = c.color("#D6AC70", "bamboo_mid")
BAM_DARK  = c.color("#A87C42", "bamboo_dark")
BAM_EDGE  = c.color("#6B4A26", "bamboo_edge")
INTERIOR  = c.color("#43301B", "interior")
DOUGH_HI  = c.color("#FDF8EC", "dough_highlight")
DOUGH     = c.color("#F2E7CF", "dough")
DOUGH_SH  = c.color("#D8C6A4", "dough_shade")
PLEAT     = c.color("#C2A47A", "pleat")
STEAM     = c.color((238, 246, 246, 190), "steam")
SHADOW    = c.color((52, 38, 22, 60), "ground_shadow")


def ell(cx, cy, a, b, phi):
    """SVG path data for a tilted ellipse (phi deg, y-down screen)."""
    t = math.radians(phi)
    ux, uy = math.cos(t), math.sin(t)
    vx, vy = -math.sin(t), math.cos(t)
    k = 0.5522847498
    P0 = (cx + a * ux, cy + a * uy)
    P1 = (cx + b * vx, cy + b * vy)
    P2 = (cx - a * ux, cy - a * uy)
    P3 = (cx - b * vx, cy - b * vy)
    f = lambda p: "%.2f %.2f" % p
    return ("M " + f(P0) +
            " C " + f((P0[0] + k * b * vx, P0[1] + k * b * vy)) + " " +
                    f((P1[0] + k * a * ux, P1[1] + k * a * uy)) + " " + f(P1) +
            " C " + f((P1[0] - k * a * ux, P1[1] - k * a * uy)) + " " +
                    f((P2[0] + k * b * vx, P2[1] + k * b * vy)) + " " + f(P2) +
            " C " + f((P2[0] - k * b * vx, P2[1] - k * b * vy)) + " " +
                    f((P3[0] - k * a * ux, P3[1] - k * a * uy)) + " " + f(P3) +
            " C " + f((P3[0] + k * a * ux, P3[1] + k * a * uy)) + " " +
                    f((P0[0] - k * b * vx, P0[1] - k * b * vy)) + " " + f(P0) + " Z")


# ---------------- 1. ground shadow ----------------
c.ellipse(17, 25.3, 12.5, 1.5, SHADOW)
c.rect(5, 25, 23, 1, SHADOW)
c.set(4, 25, SHADOW)
c.set(28, 25, SHADOW)

# ---------------- 2. wall ----------------
c.rect(4, 15, 25, 10, BAM_MID)          # y15..24
c.rect(4, 16, 1, 8, BAM_DARK)           # left silhouette
c.rect(28, 16, 1, 8, BAM_DARK)          # right silhouette
c.rect(4, 20, 25, 1, BAM_DARK)          # bamboo strip line
c.rect(4, 22, 25, 1, BAM_DARK)          # bamboo strip line
for sx in (8, 12, 16, 20, 24):
    c.rect(sx, 20, 1, 3, BAM_DARK)      # vertical stitches
c.rect(4, 23, 25, 1, BAM_LIGHT)         # lit band
c.rect(4, 24, 25, 1, BAM_EDGE)          # base edge

# ---------------- 3. rim + opening ----------------
c.ellipse(16, 15, 12, 4.5, BAM_MID)
c.ellipse(16, 15.1, 10.5, 3.3, INTERIOR)

# ---------------- 4. dumplings ----------------
DUM = (".PPP.", "PDPDP", "HHDDS", "HHDDS", ".HSS.")
DCOL = {"P": PLEAT, "D": DOUGH, "H": DOUGH_HI, "S": DOUGH_SH}
for ox in (7, 13, 19):
    for j, row in enumerate(DUM):
        for i, ch in enumerate(row):
            if ch == ".":
                continue
            x, y = ox + i, 13 + j
            if ((x - 16) / 10.5) ** 2 + ((y - 15.1) / 3.3) ** 2 <= 1.0:
                c.set(x, y, DCOL[ch])

# ---------------- 5. rim edges ----------------
c.ellipse(16, 15, 12, 4.5, BAM_EDGE, fill=False)
c.path("M 5.5 15.1 A 10.5 3.3 0 0 1 26.5 15.1", BAM_DARK, fill=False)
c.path("M 5.5 15.1 A 10.5 3.3 0 0 0 26.5 15.1", BAM_EDGE, fill=False)

# ---------------- 6. lid (ajar: right side lifted) ----------------
c.path(ell(13.5, 8.8, 10.5, 3, -10), BAM_EDGE, fill=True)     # lid thickness
c.path(ell(13.5, 6.5, 10.5, 3, -10), BAM_MID, fill=True)      # lid top face
c.path(ell(12, 6.0, 6, 1.6, -10), BAM_LIGHT, fill=True)       # sheen
c.path(ell(13.5, 6.5, 7.5, 2.0, -10), BAM_DARK, fill=False)   # weave ring
c.path(ell(13.5, 6.5, 3.8, 1.0, -10), BAM_DARK, fill=False)   # weave ring
c.ellipse(18, 3.5, 1.4, 1.2, BAM_EDGE)                        # knob
c.ellipse(17.8, 3.3, 0.9, 0.8, BAM_MID)
c.set(17, 3, BAM_LIGHT)
c.path(ell(13.5, 6.5, 10.5, 3, -10), BAM_EDGE, fill=False)    # lid outline

# ---------------- 7. steam ----------------
pal = {e["index"]: e["rgba"] for e in c.palette()}
sr, sg, sb, sa = pal[STEAM]
al = sa / 255.0
for (x, y) in [
    (25, 11), (26, 10), (26, 9), (27, 8), (27, 7), (28, 6), (28, 5),
    (27, 4), (28, 3), (28, 2), (29, 1), (29, 0),
    (5, 12), (4, 11), (4, 10), (3, 9), (3, 8), (4, 7), (3, 6), (3, 5), (2, 4),
    (22, 3), (23, 2),
]:
    idx = c.get(x, y)
    rgba = pal.get(idx) if idx is not None else None
    if rgba is None or rgba[3] == 0:
        c.set(x, y, STEAM)
    else:
        dr, dg, db, da = rgba
        c.set(x, y, c.color((round(sr * al + dr * (1 - al)),
                             round(sg * al + dg * (1 - al)),
                             round(sb * al + db * (1 - al)), 255)))

print(c.stats_text())
print(c.matrix_text())
finish(c)
