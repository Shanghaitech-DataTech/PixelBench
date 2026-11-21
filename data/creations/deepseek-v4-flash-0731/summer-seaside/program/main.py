from pixelbench_api import new_canvas, finish

W = H = 128
c = new_canvas(W, H, name="summer_seaside")


def col(hexcode):
    return c.color(hexcode)


# ---------------- palette ----------------
SKY_TOP   = col("#5CB8EF")
SKY_MID   = col("#7CCAF2")
SKY_LOW   = col("#A6E0F6")
SUN_HALO  = col("#FFF9A8")
SUN      = col("#FFF24E")
WHITE     = col("#FFFFFF")
CLOUD_SHD = col("#EAF6FD")
REFLECT   = col("#FFF7C0")
SEA_BANDS = [(78, 3, "#145A9E"), (81, 3, "#1968AC"), (84, 3, "#1D7CB8"),
            (87, 4, "#2290C2"), (91, 3, "#28A4C3"), (94, 4, "#31B8BD"),
            (98, 3, "#43CEAF"), (101, 3, "#5ADCA2")]
SAND       = col("#F3D48C")
SAND_LIGHT = col("#FBE7B2")
SAND_DARK  = col("#DFBE77")
UMB_RED    = col("#E8312E")
POLE       = col("#8A6642")
TOWEL_A    = col("#FF9E42")
TOWEL_B    = col("#FFF3DC")
FLIP_SOLE  = col("#3DB9E8")
FLIP_STRAP = col("#E8312E")
HULL       = col("#B83A2E")

# ---------------- sky ----------------
c.rect(0, 0, W, 20, SKY_TOP)     # rows 0..19
c.rect(0, 20, W, 30, SKY_MID)    # rows 20..49
c.rect(0, 50, W, 28, SKY_LOW)    # rows 50..77

# ---------------- sun ----------------
c.circle(100, 22, 14, SUN_HALO)
c.circle(100, 22, 9, SUN)

# ---------------- sea ----------------
for y0, hgt, hexc in SEA_BANDS:
    c.rect(0, y0, W, hgt, col(hexc))

# sun reflection shimmer on the sea
for y, x0, x1 in [(81, 97, 103), (85, 96, 104), (89, 95, 106),
                 (93, 94, 107), (97, 93, 109), (101, 95, 108)]:
    c.line(x0, y, x1, y, REFLECT)

# small white glints on the sea
for x, y in [(10, 90), (18, 96), (46, 88), (66, 99), (74, 93), (86, 98),
             (110, 100), (120, 92)]:
    c.set(x, y, WHITE)

# ---------------- clouds ----------------
def cloud(blobs, shade=None):
    for (bx, by, br) in blobs:
        c.circle(bx, by, br, WHITE)

cloud([(22, 16, 6), (30, 12, 7), (38, 15, 5), (27, 19, 5), (19, 20, 4)])
c.line(18, 21, 38, 21, CLOUD_SHD)
cloud([(74, 28, 5), (82, 26, 6), (88, 29, 4)])
c.line(72, 31, 90, 31, CLOUD_SHD)
cloud([(13, 40, 4), (19, 38, 4)])
cloud([(112, 40, 4), (117, 37, 3)])

# ---------------- gulls ----------------
def gull(x, y):
    c.line(x - 6, y - 4, x, y, WHITE)
    c.line(x + 6, y - 4, x, y, WHITE)

gull(48, 34)
gull(86, 52)

# ---------------- sailboat far out ----------------
c.line(31, 80, 31, 89, POLE)
c.poly([(31, 81), (31, 89), (38, 89)], WHITE)   # main sail
c.poly([(31, 83), (31, 89), (25, 89)], WHITE)   # jib
c.rect(27, 88, 10, 2, HULL)

# ---------------- sand ----------------
c.rect(0, 104, W, 24, SAND)       # rows 104..127
c.rect(0, 104, W, 3, SAND_DARK)   # wet sand strip
# texture specks
for x in range(1, 128, 4):
    y = 110 + (x * 7) % 14
    c.set(x, y, SAND_DARK)
for x in range(3, 128, 5):
    y = 108 + (x * 5) % 16
    c.set(x, y, SAND_LIGHT)

# umbrella shadow on the sand (sun is up-right)
c.ellipse(44, 113, 13, 3, SAND_DARK)

# ---------------- umbrella ----------------
cx, cy, rx, ry = 58, 103, 17, 11
# spike
c.line(cx, cy - ry - 3, cx, cy - ry, POLE)
for y in range(cy - ry, cy + 1):
    for x in range(cx - rx, cx + rx + 1):
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
            c.set(x, y, UMB_RED if ((x - cx) // 3) % 2 == 0 else WHITE)
# pole
c.rect(cx - 1, cy, 2, 13, POLE)  # rows 103..115

# ---------------- towel ----------------
tx, ty, tw, th = 76, 113, 34, 9
for i in range(th):
    c.rect(tx, ty + i, tw, 1, TOWEL_A if (i // 2) % 2 == 0 else TOWEL_B)

# ---------------- flip-flops ----------------
def flipflop(x, y):
    c.rect(x, y, 6, 3, FLIP_SOLE)
    c.line(x + 1, y, x + 3, y - 2, FLIP_STRAP)
    c.line(x + 5, y, x + 3, y - 2, FLIP_STRAP)

flipflop(84, 123)
flipflop(95, 123)

# ---------------- foam waves ----------------
for x in range(1, 128, 3):
    if (x // 3) % 2 == 1:
        c.set(x, 103, WHITE)
for x in range(2, 128, 11):
    c.circle(x, 103, 2, WHITE)
for x in range(6, 128, 14):
    c.set(x, 105, WHITE)
    c.set(x + 1, 104, WHITE)

# ---------------- report ----------------
print(c.stats_text())
print("colors used:", len(c.palette()))

finish(c)
