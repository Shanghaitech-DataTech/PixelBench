from pixelbench_api import *

out = input_canvas.copy(name="output")

# ---------------- palette ----------------
out.color((252, 214, 150), "glowbright")
out.color((232, 190, 132), "glowwarm")
out.color((168, 138, 92), "glowmid")
out.color((120, 96, 60), "glowdim")

# ---------------- vines ----------------
VLEAF = [131, 151, 116, 129, 130, 135, 149, 150, 152, 136, 140]


def strand(pts, stem_i=131):
    for a, b in zip(pts, pts[1:]):
        out.line(a[0], a[1], b[0], b[1], stem_i)
    n = len(VLEAF)
    for i, (x, y) in enumerate(pts):
        d = 1 if (i // 2) % 2 == 0 else -1
        if y >= 1 and i % 2 == 0:
            out.rect(x + d * 2, y - 1, 2, 3, VLEAF[i % n])
        if y >= 2 and i % 5 == 2:
            out.rect(x - d, y - 2, 3, 2, VLEAF[(i + 1) % n])


# hanging strands down the tower walls
strand([(14, 2), (12, 8), (16, 14), (13, 20), (17, 27), (15, 34), (19, 42), (17, 48)])
strand([(24, 2), (22, 10), (26, 18), (23, 27), (27, 36), (25, 45), (29, 55)])
strand([(38, 2), (36, 10), (40, 18), (37, 26), (41, 35), (39, 44), (43, 54)])
strand([(50, 4), (48, 14), (52, 24), (49, 34), (53, 45), (51, 56), (55, 68)])
strand([(62, 2), (60, 12), (64, 21), (61, 31), (65, 42), (62, 52)])
strand([(76, 4), (74, 14), (78, 24), (75, 35), (79, 46), (77, 57)])
strand([(90, 6), (88, 16), (92, 28), (89, 40), (93, 52), (91, 64)])
strand([(104, 10), (102, 22), (106, 34), (103, 46), (107, 58), (105, 70)])
# horizontal creepers
strand([(12, 84), (22, 81), (32, 85), (42, 83), (52, 87), (62, 84), (72, 88)], 116)
strand([(16, 120), (26, 117), (36, 121), (46, 118), (56, 122), (66, 119)], 151)

# ---------------- doorway jambs darkened ----------------
for y in range(194, 218):
    for x in range(37, 41):
        out.set(x, y, "c95")
    for x in range(64, 68):
        out.set(x, y, "c91")

# vines draped beside the archway
strand([(33, 166), (31, 174), (35, 181), (33, 188), (36, 195), (34, 202), (36, 210)])
strand([(67, 163), (69, 171), (66, 178), (70, 186), (67, 193), (70, 201), (68, 209)])
# leaf clusters on the arch stones
for (lx, ly) in [(38, 182), (39, 181), (38, 184), (40, 180),
                (63, 181), (64, 180), (63, 184), (65, 179),
                (34, 196), (33, 197), (35, 195),
                (69, 194), (70, 193), (68, 195),
                (37, 210), (38, 211), (36, 209),
                (64, 208), (65, 209)]:
    out.set(lx, ly, 136)
for (lx, ly) in [(38, 186), (63, 185), (34, 199), (69, 197)]:
    out.set(lx, ly, 151)

# ---------------- Mage at the archway, walking into the tower ----------------
# glow halo / spill behind and around
out.circle(62, 168, 7, "glowdim")
out.circle(62, 168, 4, "glowmid")
out.circle(62, 168, 2, "glowwarm")
for (px, py) in [(60, 172), (58, 174), (60, 176), (57, 178), (59, 180),
                (57, 182), (56, 184), (63, 175), (62, 178), (61, 181),
                (66, 176), (65, 180), (64, 184), (63, 188), (62, 192),
                (67, 186), (66, 190), (65, 194), (64, 198), (63, 202)]:
    out.set(px, py, "glowdim")
# cloak body (back view, walking toward the doorway)
out.poly([(45, 193), (60, 193), (66, 214), (39, 214)], "c53")
out.poly([(47, 198), (59, 198), (62, 212), (43, 213)], "c58")
out.poly([(49, 202), (57, 202), (60, 211), (45, 211)], "c91")
out.line(39, 214, 66, 214, "c53")
out.line(41, 216, 64, 216, "c91")
out.line(50, 196, 49, 213, "c58")
out.line(55, 196, 56, 213, "c58")
out.line(60, 197, 61, 212, "c95")
for (px, py) in [(44, 195), (43, 199), (42, 204), (41, 208), (40, 212)]:
    out.set(px, py, 100)
# hood (back of head)
out.circle(52, 186, 7, "c53")
out.circle(52, 186, 6, "c58", fill=False)
out.ellipse(52, 189, 4, 4, "c91")
# staff
out.line(62, 172, 62, 214, 81)
out.set(61, 205, 82)
out.circle(60, 204, 2, "c53")
# glowing orb
out.circle(62, 167, 2, "glowbright")
out.circle(62, 165, 1, "glowwarm")
out.set(62, 163, "glowbright")
# hood rim lit by the orb
for (px, py) in [(58, 186), (59, 188), (59, 190), (58, 192), (57, 194), (60, 183)]:
    out.set(px, py, "glowdim")
# boots under the hem (mid stride)
out.set(42, 218, "c58")
out.set(46, 219, "c95")
out.set(53, 219, "c95")
out.set(58, 219, "c91")
out.set(52, 220, "c95")
# warm light pooling at the threshold
for (px, py) in [(40, 217), (42, 218), (44, 220), (46, 221), (48, 222),
                (50, 221), (52, 222), (54, 221), (56, 220), (58, 219),
                (60, 218), (62, 217)]:
    out.set(px, py, "glowdim")

print(out.stats_text())
finish(out)
