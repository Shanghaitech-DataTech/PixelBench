from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, "#10141f", name="subway_platform")

def col(hexv, name):
    return c.color(hexv, name)

# ---- palette ----
ceiling  = col("#1a1f2c", "ceiling")
beam     = col("#12161f", "beam")
light    = col("#ffe9a8", "light")
lighthot = col("#fff6d9", "lighthot")
wall     = col("#5d6677", "wall")
walllt   = col("#6b7589", "walllt")
walld    = col("#4d5565", "walld")
wald2    = col("#434b5b", "wald2")
seam     = col("#454d5c", "seam")
sign     = col("#1d6fb0", "sign")
white    = col("#edf2fa", "white")
redc     = col("#d9534f", "red")
bluec    = col("#4a86d6", "blue")
greenc   = col("#57a05c", "green")
train    = col("#c9cfdc", "train")
trainlt  = col("#e7ecf4", "trainlt")
trainmd  = col("#aab2c2", "trainmd")
trainfk  = col("#7d89a0", "trainfk")
window   = col("#ffd97e", "window")
whi      = col("#fff2c2", "whi")
streak   = col("#9fd9ff", "streak")
strehi   = col("#cbeaff", "strehi")
skirt    = col("#3f4553", "skirt")
skdk     = col("#333947", "skdk")
fog2     = col("#5b6881", "fog2")
fog1     = col("#8b98b2", "fog1")
frame    = col("#222733", "frame")
glare    = col("#b9c5da", "glare")
plat     = col("#4c5362", "plat")
pladk    = col("#3b4150", "pladk")
plalt    = col("#6b7488", "plalt")
edge     = col("#e9b84c", "edge")
edd      = col("#b98f33", "edd")
refl     = col("#8fb8e8", "refl")
rehi     = col("#cfe8ff", "rehi")
relo     = col("#5a80b0", "relo")
sil      = col("#232936", "sil")
skd      = col("#191e29", "skd")
rim      = col("#7d8aa6", "rim")
bench    = col("#2e6f9e", "bench")
benchdk  = col("#22506f", "benchdk")
benchlt  = col("#4f9ac4", "benchlt")
bag      = col("#6b4f3f", "bag")
baglt    = col("#8a6b52", "baglt")

def dash(x, y, ln, color):
    c.rect(x, y, ln, 1, color)

# ---------------- ceiling ----------------
c.rect(0, 0, W, 6, ceiling)
c.rect(0, 6, W, 2, beam)
for x in (3, 17, 31, 45, 58):
    c.rect(x, 1, 6, 3, light)
    c.rect(x + 1, 1, 4, 1, lighthot)

# ---------------- wall (station wall, far layer) ----------------
c.rect(0, 8, W, 22, wall)          # rows 8..29
c.rect(0, 8, W, 1, walllt)
c.rect(0, 8, 6, 22, walld)         # far-left fade (depth)
c.rect(0, 8, 3, 22, wald2)
for yy in (13, 18, 23, 28):
    c.rect(0, yy, W, 1, seam)
for xx in range(7, 64, 8):
    c.rect(xx, 8, 1, 22, seam)

# ----- signs (generic, no brand names) -----
# hanging arrow sign pointing right
c.rect(26, 8, 15, 8, sign)
c.rect(26, 8, 15, 8, white, fill=False)
c.rect(29, 11, 8, 2, white)
c.poly([(37, 10), (40, 12), (37, 14)], white)
# wall EXIT sign
c.rect(4, 17, 24, 9, sign)
c.rect(4, 17, 24, 9, white, fill=False)
c.text(6, 19, "EXIT", white, font="5x7")
# route map board
c.rect(46, 8, 12, 8, white)
c.rect(46, 8, 12, 8, seam, fill=False)
c.rect(48, 9, 8, 2, redc)
c.rect(48, 11, 8, 2, bluec)
c.rect(48, 13, 8, 2, greenc)

# ---------------- train behind screen doors ----------------
# underfloor / skirt
c.rect(0, 30, W, 2, trainmd)        # roof top 30..31
c.rect(0, 32, W, 2, trainmd)        # roof
c.rect(0, 34, W, 8, window)        # lit window band 34..41
c.rect(0, 42, W, 7, train)          # body 42..48
c.rect(0, 49, W, 5, skirt)          # skirt 49..53
c.rect(0, 54, W, 3, skdk)           # dark underframe 54..56
# far-left fade over the train (depth / speed haze)
c.rect(0, 32, 5, 25, fog2)
c.rect(5, 32, 6, 25, fog1)
dash(2, 38, 8, streak)

# motion streaks (horizontal speed)
c.rect(13, 36, 7, 3, whi)
c.rect(25, 36, 12, 3, whi)
c.rect(43, 36, 10, 3, whi)
c.rect(56, 37, 5, 2, whi)
dash(20, 33, 12, streak)
dash(40, 33, 13, streak)
dash(15, 43, 9, trainlt)
dash(33, 33, 10, trainlt)
dash(50, 33, 10, trainlt)
dash(21, 45, 12, trainlt)
dash(38, 45, 9, trainlt)
dash(26, 47, 13, streak)
dash(46, 47, 11, streak)
dash(24, 51, 16, relo)
dash(42, 44, 14, relo)
dash(30, 44, 26, strehi)

# ---------------- platform screen doors ----------------
c.rect(0, 30, W, 2, frame)          # header 30..31
for x in (1, 10, 20, 30, 40, 50, 60, 62):
    c.rect(x, 32, 2, 24, frame)
c.rect(0, 56, W, 1, frame)          # threshold
# glass glare diagonals on a few panes
for x0 in (12, 32, 52):
    c.line(x0 + 1, 34, x0 + 2, 53, glare)

# ---------------- platform floor ----------------
c.rect(0, 57, W, 7, plat)           # 57..63
c.rect(0, 57, W, 1, pladk)
for x in (2, 10, 18, 26, 34, 42, 50, 58):
    c.rect(x, 58, 6, 2, plalt)
c.rect(0, 60, W, 1, edge)
for x in (3, 11, 19, 27, 35, 43, 51, 59):
    c.rect(x, 60, 5, 1, edd)
c.rect(0, 62, W, 1, pladk)
dash(13, 58, 8, refl)
dash(30, 59, 10, refl)
dash(47, 59, 12, refl)
dash(20, 61, 15, refl)
dash(41, 61, 19, refl)
dash(2, 61, 9, rehi)
dash(35, 62, 22, relo)

# ---------------- bench ----------------
c.rect(30, 45, 12, 9, bench)        # back 45..53
c.rect(30, 45, 12, 1, benchlt)
c.rect(30, 53, 12, 2, benchlt)      # seat 53..54
c.rect(31, 55, 3, 3, benchdk)
c.rect(40, 55, 3, 3, benchdk)

# ---------------- passengers (silhouettes) ----------------
# P1 standing, looking at phone (left)
c.rect(15, 39, 6, 6, sil)
c.rect(15, 39, 6, 1, skd)
c.rect(15, 40, 1, 4, rim)
c.rect(14, 45, 9, 7, sil)
c.rect(14, 45, 1, 6, rim)
c.rect(21, 45, 2, 7, sil)            # front arm
c.rect(20, 47, 3, 4, streak)         # glowing phone
c.rect(16, 52, 3, 5, skd)
c.rect(19, 52, 3, 5, skd)
c.rect(16, 56, 3, 2, sil)
c.rect(19, 56, 3, 2, sil)

# P2 sitting on the bench
c.rect(32, 40, 6, 6, sil)
c.rect(32, 40, 6, 1, skd)
c.rect(32, 41, 1, 3, rim)
c.rect(31, 45, 8, 6, sil)            # torso
c.rect(31, 45, 1, 5, rim)
c.rect(32, 51, 6, 3, sil)            # lap
c.rect(33, 49, 5, 2, skd)            # arms folded
c.rect(37, 54, 3, 3, skd)            # shins
c.rect(36, 56, 4, 2, skd)            # feet
# P3 walking right with backpack
c.rect(45, 45, 4, 6, bag)
c.rect(45, 45, 4, 1, baglt)
c.rect(49, 38, 6, 6, sil)
c.rect(49, 38, 6, 1, skd)
c.rect(47, 44, 8, 6, sil)
c.rect(47, 44, 1, 5, rim)
c.rect(54, 45, 3, 4, sil)            # front arm swing
c.rect(46, 46, 2, 4, skd)            # back arm
c.rect(52, 50, 3, 6, skd)            # front leg
c.rect(46, 49, 3, 4, skd)            # trailing leg
c.rect(53, 56, 4, 2, sil)            # front foot
c.rect(44, 53, 4, 2, sil)            # lifted back foot

print(c.stats_text())
finish(c)
