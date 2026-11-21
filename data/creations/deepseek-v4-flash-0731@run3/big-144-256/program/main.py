from pixelbench_api import *

out = input_canvas.copy(name="output")

# ---- register colours ----
C_DOOR   = out.color((38, 52, 74), "door")
C_DOOR2  = out.color((58, 70, 96), "door2")
C_GLOW   = out.color((96, 104, 130), "glow")
C_GLOW2  = out.color((130, 130, 160), "glow2")
C_ROBE   = out.color((18, 22, 46), "robe")
C_ROBE2  = out.color((26, 32, 60), "robe2")
C_HOOD   = out.color((34, 40, 76), "hood")
C_RIM    = out.color((120, 130, 190), "rim")
C_WARM   = out.color((210, 200, 160), "warm")
C_BOOT   = out.color((10, 12, 30), "boot")
C_STAFF  = out.color((74, 56, 36), "staff")
C_ORB    = out.color((255, 244, 196), "orb")
C_ORB2   = out.color((255, 208, 96), "orb2")
C_ORB3   = out.color((150, 170, 230), "orb3")
C_HAND   = out.color((30, 36, 66), "hand")
C_V1     = out.color((18, 58, 32), "v1")
C_V2     = out.color((46, 104, 56), "v2")
C_V3     = out.color((74, 146, 82), "v3")
C_V4     = out.color((118, 190, 120), "v4")
C_V5     = out.color((154, 214, 158), "v5")

# =====================================================
# 1. ARCHWAY: light the doorway interior behind the mage
out.rect(103, 163, 26, 50, C_DOOR)
out.rect(106, 163, 20, 50, C_DOOR2)
for yy in range(166, 214, 2):
    for xx in range(104, 130, 2):
        d = max(abs(xx - 122), abs(yy - 196))
        if d < 10:
            out.set(xx, yy, C_GLOW)
        elif d < 16:
            out.set(xx, yy, C_DOOR2)
        else:
            out.set(xx, yy, C_DOOR)

# =====================================================
# 2. CLOAKED MAGE, seen from behind, walking into tower
ROBE = C_ROBE; ROBE2 = C_ROBE2
out.ellipse(113, 212, 15, 4, C_GLOW2)          # light pool at entrance
out.poly([(101, 186), (125, 186), (132, 210), (94, 210)], ROBE)      # robe silhouette
out.poly([(106, 187), (120, 187), (124, 209), (102, 209)], ROBE2)    # robe inner
out.ellipse(113, 183, 11, 9, C_HOOD)                                  # hood
out.circle(113, 180, 6, C_HOOD)
out.poly([(107, 177), (119, 177), (119, 171), (113, 168), (107, 171)], C_HOOD)
out.poly([(109, 177), (113, 168), (113, 177)], C_ROBE)
out.ellipse(99, 196, 6, 7, ROBE2)              # left sleeve
out.ellipse(127, 196, 6, 7, ROBE2)             # right sleeve
out.rect(102, 206, 7, 6, C_BOOT)
out.rect(105, 209, 6, 3, C_BOOT)
out.rect(118, 206, 7, 6, C_BOOT)
out.rect(120, 209, 6, 3, C_BOOT)
out.line(126, 188, 130, 206, C_RIM)
out.line(124, 186, 128, 196, C_WARM)
out.line(113, 169, 118, 171, C_WARM)
out.line(118, 175, 122, 180, C_WARM)
out.rect(119, 168, 3, 44, C_STAFF)             # staff
out.rect(120, 168, 1, 44, (96, 74, 48))
out.rect(117, 194, 4, 4, C_HAND)               # hands
out.rect(121, 194, 3, 4, C_HAND)
out.circle(120, 165, 5, C_ORB3)                # orb
out.circle(120, 166, 4, C_ORB2)
out.circle(120, 166, 3, C_ORB)
out.set(120, 165, (255, 255, 230))
out.set(116, 161, C_ORB3); out.set(124, 161, C_ORB3)
out.set(113, 166, C_ORB2); out.set(127, 166, C_ORB2)
out.set(120, 158, C_ORB3)

# =====================================================
# 3. VINES
def leaf(x, y, shade=C_V3):
    out.set(x, y, shade)
    if x + 1 < 144: out.set(x + 1, y, shade)
    out.set(x, y + 1, shade)
def leafhi(x, y):
    out.set(x, y, C_V4); out.set(x, y + 1, C_V5)

stem = [(66, 212), (68, 200), (71, 188), (70, 176), (73, 164), (76, 152),
        (78, 140), (82, 128), (86, 116), (90, 106), (94, 96), (98, 88)]
for i in range(len(stem) - 1):
    out.line(stem[i][0], stem[i][1], stem[i + 1][0], stem[i + 1][1], C_V1)
    out.line(stem[i][0] + 1, stem[i][1], stem[i + 1][0] + 1, stem[i + 1][1], C_V2)
out.line(71, 200, 64, 206, C_V1)
out.line(73, 176, 64, 184, C_V1)
out.line(78, 140, 66, 146, C_V1)
out.line(86, 116, 76, 120, C_V1)
out.line(90, 106, 98, 100, C_V2)
for (lx, ly) in [(64, 205), (68, 196), (74, 178), (79, 168), (77, 150), (83, 138),
                (81, 124), (90, 112), (93, 100), (99, 90), (65, 188), (88, 128)]:
    leaf(lx, ly)
    leafhi(lx + 3, ly - 1)
    leaf(lx - 1, ly + 2, C_V2)
out.line(82, 128, 82, 140, C_V2)
out.line(73, 164, 73, 176, C_V2)
out.line(90, 106, 92, 118, C_V2)
for (tx, ty) in [(82, 140), (73, 174), (92, 117)]:
    leaf(tx, ty, C_V3); leaf(tx + 2, ty + 1, C_V4)

stem2 = [(100, 156), (99, 164), (98, 172), (99, 180), (97, 188), (98, 196)]
for i in range(len(stem2) - 1):
    out.line(stem2[i][0], stem2[i][1], stem2[i + 1][0], stem2[i + 1][1], C_V1)
out.line(99, 164, 93, 162, C_V1)
out.line(98, 180, 92, 184, C_V1)
for (lx, ly) in [(95, 160), (92, 175), (97, 170), (90, 186), (95, 190), (94, 198)]:
    leaf(lx, ly); leafhi(lx + 2, ly - 1)
    leaf(lx - 1, ly + 1, C_V2)

stem3 = [(131, 210), (133, 200), (131, 190), (134, 180), (133, 170), (135, 162)]
for i in range(len(stem3) - 1):
    out.line(stem3[i][0], stem3[i][1], stem3[i + 1][0], stem3[i + 1][1], C_V1)
out.line(133, 200, 138, 204, C_V1)
out.line(133, 180, 139, 176, C_V2)
for (lx, ly) in [(137, 202), (135, 192), (137, 183), (138, 172), (134, 164), (139, 196)]:
    leaf(lx, ly); leafhi(lx + 1, ly + 1)
    leaf(lx - 1, ly, C_V2)

for (sx, sv) in [(108, 156), (116, 155), (125, 158)]:
    out.line(sx, sv, sx, sv + 10, C_V1)
    out.line(sx + 1, sv, sx + 1, sv + 7, C_V2)
    leaf(sx - 1, sv + 4)
    leaf(sx + 1, sv + 8, C_V3)

out.line(58, 216, 96, 218, C_V1)
out.line(62, 218, 66, 228, C_V1)
out.line(80, 218, 84, 230, C_V1)
for (lx, ly) in [(60, 220), (72, 222), (88, 220), (64, 214), (83, 232)]:
    leaf(lx, ly); leafhi(lx + 2, ly + 1)
    leaf(lx - 1, ly - 1, C_V2)

# ---- inspection ----
print(out.stats_text())
pal = out.palette()
col_of = {p["index"]: p["rgba"] for p in pal}
def cls(x, y):
    r, g, b, a = col_of[out.get(x, y)]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    if lum < 30: return '@'
    if lum < 58: return '#'
    if lum < 95: return 'o'
    if lum < 138: return ':'
    if lum < 175: return '.'
    return ' '
for y in range(155, 216):
    line = ""
    for x in range(88, 140):
        nm = col_of[out.get(x, y)][0]
        ch = "."
        for k in ["orb3", "orb2", "orb", "warm", "rim", "glow2", "glow", "door2", "door",
                  "robe2", "robe", "hood", "staff", "boot", "hand", "v5", "v4", "v3", "v2", "v1"]:
            if nm == k:
                ch = k[0].upper() if k[0] in "orwgdbshv" else k[:1]
                break
        line += ch
    print(f"y={y:3d} {line}")

finish(out)
