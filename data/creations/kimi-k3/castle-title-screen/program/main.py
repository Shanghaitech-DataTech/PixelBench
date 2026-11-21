# Fantasy RPG title screen — 128x128
# Castle on a seaside cliff at sunset, wide cinematic composition.

# ---------- palette ----------
SKY = ["#352a5e", "#45336b", "#5b3d77", "#7a4a80", "#9c4f78",
       "#c1556b", "#e56d55", "#f4935b", "#ffb863"]
SKY_ROWS = [(0, 12), (12, 22), (22, 32), (32, 42), (42, 52),
            (52, 60), (60, 68), (68, 74), (74, 80)]

SUN_OUT, SUN_MID, SUN_CORE = "#ff9e3d", "#ffc15e", "#ffe08a"
CL_DARK, CL_MID, CL_PINK = "#553a6e", "#7c4d82", "#d96a7e"
CL_WARM, CL_LIT = "#f78d6b", "#ffc98a"

SEA = [("#f0a05c", 80, 85), ("#c07858", 85, 92), ("#7a5a72", 92, 102),
       ("#46527e", 102, 112), ("#2e4470", 112, 128)]
SPARK, ISLAND = "#ffd98a", "#5c3a5e"

ROCK, ROCK_D, ROCK_DD = "#503868", "#33244e", "#241a38"
ROCK_L, RIM, TOP = "#6a4a74", "#e08a5e", "#d98a4a"

CAS, CAS_D, DARK = "#6a4260", "#4a2c48", "#2c1c3c"
FLAG, WIN = "#e83a4e", "#ffd166"

FG, FG_RIM, STAR = "#1c1430", "#8a5a5e", "#ffe9c9"

c = new_canvas(128, 128, name="title")

# ---------- sky ----------
for col, (y0, y1) in zip(SKY, SKY_ROWS):
    c.rect(0, y0, 128, y1 - y0, col)

def skycol(y):
    for col, (y0, y1) in zip(SKY, SKY_ROWS):
        if y0 <= y < y1:
            return col
    return SKY[-1]

# faint stars high up
c.set(10, 5, STAR); c.set(22, 9, STAR); c.set(6, 16, STAR)

# ---------- large orange sun ----------
c.circle(92, 58, 21, SUN_OUT)
c.circle(92, 58, 16, SUN_MID)
c.circle(92, 58, 11, SUN_CORE)
# retro scanline gaps across the lower half
import math
for y in (66, 70, 74, 78):
    dx = int(math.sqrt(max(0, 21 * 21 - (y - 58) ** 2)))
    c.line(92 - dx, y, 92 + dx, y, skycol(y))

# ---------- layered clouds ----------
def cloud(rows, col):
    for (y, x, w) in rows:
        c.rect(x, y, w, 1, col)

# high dark purple strips
cloud([(13, 10, 18), (14, 6, 30), (15, 12, 20)], CL_DARK)
cloud([(10, 98, 16), (11, 92, 28), (12, 100, 18)], CL_DARK)
# mid violet banks with pink lit tops
cloud([(26, 16, 24), (27, 10, 36), (28, 18, 26)], CL_MID)
cloud([(30, 96, 24), (31, 90, 34), (32, 98, 22)], CL_MID)
cloud([(25, 16, 10)], CL_PINK)
cloud([(29, 96, 22)], CL_PINK)
# warm sunset clouds, two crossing the sun
cloud([(44, 4, 30), (45, 0, 40), (46, 8, 28)], CL_WARM)
cloud([(52, 70, 40), (53, 66, 48), (54, 74, 36)], CL_WARM)
cloud([(64, 78, 30), (65, 74, 40), (66, 82, 26)], CL_WARM)
cloud([(70, 2, 14), (71, 0, 20)], CL_WARM)
cloud([(72, 112, 16), (73, 108, 20)], CL_WARM)
# bright lit edges
cloud([(43, 6, 28), (51, 72, 38), (63, 80, 28), (69, 4, 12)], CL_LIT)

# ---------- sea ----------
for col, y0, y1 in SEA:
    c.rect(0, y0, 128, y1 - y0, col)

# distant island silhouette on the left horizon
c.poly([(2, 80), (4, 76), (6, 74), (8, 76), (11, 80)], ISLAND)

# sun reflection glints on the water (kept right of the cliff edge)
for (y, x, w) in [(81, 86, 10), (83, 80, 10), (83, 96, 8), (86, 88, 10),
                  (89, 84, 8), (89, 96, 10), (92, 90, 8), (95, 94, 10),
                  (98, 88, 8), (102, 94, 10), (106, 90, 8), (110, 96, 8),
                  (115, 94, 10), (90, 2, 7), (100, 4, 6), (108, 112, 8),
                  (118, 100, 6), (86, 118, 8)]:
    c.rect(x, y, w, 1, SPARK)

# small rocky islets in the sea
c.poly([(104, 98), (108, 93), (114, 93), (118, 98)], ROCK_DD)
c.line(108, 93, 114, 93, RIM)
c.poly([(118, 90), (121, 86), (125, 86), (127, 90)], ROCK_DD)
c.line(121, 86, 125, 86, RIM)

# ---------- seaside cliff (jagged silhouette) ----------
CLIFF = [(22, 64), (21, 70), (24, 77), (17, 85), (21, 93), (13, 102),
         (17, 111), (10, 119), (12, 127), (88, 127), (86, 121),
         (78, 113), (81, 104), (72, 95), (76, 87), (68, 78), (71, 71),
         (66, 64)]
c.poly(CLIFF, ROCK)
# shadowed left/lower mass
c.poly([(22, 64), (21, 70), (24, 77), (17, 85), (21, 93), (13, 102),
        (17, 111), (10, 119), (12, 127), (40, 127), (36, 112),
        (42, 98), (36, 86), (44, 74), (38, 64)], ROCK_D)
# darkest base
c.poly([(12, 122), (88, 118), (88, 127), (12, 127)], ROCK_DD)
# sun-facing right face
c.poly([(66, 64), (71, 71), (68, 78), (76, 87), (72, 95), (81, 104),
        (78, 113), (86, 121), (88, 127), (74, 127), (70, 112),
        (62, 98), (66, 86), (58, 76), (60, 66)], ROCK_L)
# warm grassy cliff top + sunlit rim
c.poly([(22, 64), (66, 64), (63, 68), (25, 68)], TOP)
c.line(22, 64, 66, 64, RIM)
c.line(66, 64, 71, 71, RIM)
c.line(68, 78, 76, 87, RIM)
# rock strata dashes
c.line(30, 84, 38, 84, ROCK_L)
c.line(24, 98, 34, 98, ROCK_L)
c.line(34, 112, 44, 112, ROCK_L)
c.line(68, 90, 76, 90, ROCK_D)
c.line(74, 104, 82, 104, ROCK_D)
c.line(70, 120, 80, 120, ROCK_D)

# ---------- castle (own layer, outlined, then blitted) ----------
cast = new_canvas(128, 128, name="castle")
# keep
cast.rect(33, 38, 23, 26, CAS)
for x in range(33, 56, 5):
    cast.rect(x, 35, 3, 3, CAS)
# left tower
cast.rect(23, 30, 11, 34, CAS)
for x in range(22, 34, 5):
    cast.rect(x, 27, 3, 3, CAS)
# right tower (taller)
cast.rect(55, 25, 11, 39, CAS)
for x in range(54, 66, 5):
    cast.rect(x, 22, 3, 3, CAS)
# flagpoles + pennants (wind blowing right)
cast.line(28, 20, 28, 27, DARK)
cast.poly([(29, 21), (37, 23), (29, 25)], FLAG)
cast.line(60, 14, 60, 22, DARK)
cast.poly([(61, 15), (69, 17), (61, 19)], FLAG)

cast.outline(DARK)   # dark contour where castle meets sky

# shadowed left faces
cast.line(23, 31, 23, 62, CAS_D)
cast.line(33, 39, 33, 62, CAS_D)
cast.line(55, 26, 55, 62, CAS_D)
# warm sunset rims on right edges
cast.line(33, 31, 33, 62, CL_WARM)
cast.line(65, 26, 65, 62, CL_WARM)
cast.line(55, 39, 55, 62, CL_WARM)
# gate arch with warm threshold
cast.rect(42, 53, 7, 11, DARK)
cast.set(43, 52, DARK); cast.set(47, 52, DARK)
cast.set(44, 51, DARK); cast.set(45, 51, DARK); cast.set(46, 51, DARK)
cast.rect(42, 62, 7, 1, RIM)
# lit windows
cast.rect(38, 44, 2, 3, WIN)
cast.rect(48, 44, 2, 3, WIN)
cast.rect(27, 38, 2, 3, WIN)
cast.rect(59, 32, 2, 3, WIN)
cast.set(44, 42, WIN); cast.set(60, 44, WIN)
# brick texture
for (x, y) in [(36, 52), (42, 45), (50, 54), (45, 58), (52, 47),
               (27, 50), (30, 58), (58, 52), (62, 56)]:
    cast.set(x, y, CAS_D)

c.blit(cast, 0, 0)

# ---------- dark foreground rocks ----------
c.poly([(0, 116), (8, 108), (16, 114), (22, 122), (24, 128), (0, 128)], FG)
c.line(0, 116, 8, 108, FG_RIM)
c.line(8, 108, 16, 114, FG_RIM)
c.poly([(127, 110), (118, 102), (110, 110), (106, 120), (104, 128),
        (128, 128)], FG)
c.line(127, 110, 118, 102, RIM)
c.line(118, 102, 110, 110, RIM)

# ---------- birds ----------
for (bx, by) in [(26, 18), (34, 14), (20, 24)]:
    c.set(bx - 1, by, DARK); c.set(bx, by + 1, DARK); c.set(bx + 1, by, DARK)

print(c.stats_text())
view(c)
finish(c)
