from pixelbench_api import *
import math, random

c = new_canvas(64, 64, name="result")

def C(h, n):
    return c.color(h, n)

# ---------------- palette ----------------
sky0 = C("#070a18", "sky0"); sky1 = C("#0b1020", "sky1")
sky2 = C("#111830", "sky2"); sky3 = C("#1a2240", "sky3")
glow1 = C("#23243f", "glow1"); glow2 = C("#302f4c", "glow2")
rain = C("#4e5f92", "rain"); rain2 = C("#8093c8", "rain2")

wall0 = C("#141826", "wall0"); wall1 = C("#1f2434", "wall1")
wall2 = C("#2a3145", "wall2"); wall3 = C("#3d4762", "wall3")
roof0 = C("#0e111c", "roof0"); roof1 = C("#232a3b", "roof1")

signbg = C("#090b16", "signbg"); signglow = C("#251d10", "signglow")
signtext = C("#ffe9a0", "signtext")

awnA = C("#7e3436", "awnA"); awnA2 = C("#a3443f", "awnA2")
awnB = C("#a0937a", "awnB"); awnB2 = C("#cfc2a2", "awnB2")
awnsh = C("#1c1618", "awnsh")

frame0 = C("#31384e", "frame0"); frame1 = C("#4b5676", "frame1")
frame2 = C("#7180aa", "frame2")

in0 = C("#fffbdc", "in0"); in1 = C("#ffeec0", "in1")
in2 = C("#f6dc98", "in2"); in3 = C("#e3c176", "in3")
shelf = C("#96682a", "shelf"); floor1 = C("#c6a166", "floor1")
floor2 = C("#a37e49", "floor2")
pr = C("#c8443c", "pr"); pg = C("#3f9a56", "pg"); pb = C("#3a6fb2", "pb")
pw = C("#f2eeda", "pw"); py = C("#dfa832", "py")
neon = C("#e0483a", "neon")

doorlight = C("#fff6cc", "doorlight"); dframe = C("#3a4460", "dframe")

coat0 = C("#e8c23a", "coat0"); coat1 = C("#a8862a", "coat1")
coat2 = C("#4a3d10", "coat2"); boot = C("#111319", "boot")

bike0 = C("#0b0d13", "bike0"); bike1 = C("#39415a", "bike1")
bike2 = C("#7c8aaa", "bike2")

rack0 = C("#222838", "rack0"); rack1 = C("#525e7c", "rack1")
ur = C("#a8383a", "ur"); ur2 = C("#cc5a52", "ur2")
ut = C("#268a8a", "ut"); ut2 = C("#45b8b0", "ut2")

walk0 = C("#0f121b", "walk0"); walk1 = C("#181d29", "walk1")
walk2 = C("#222939", "walk2"); walk3 = C("#303950", "walk3")
curb = C("#39435e", "curb"); shad0 = C("#070910", "shad0")

rw1 = C("#6a5a30", "rw1"); rw2 = C("#8f7842", "rw2"); rw3 = C("#453a20", "rw3")
rd1 = C("#a08a4a", "rd1"); rd2 = C("#c8ab5e", "rd2")

pud0 = C("#0a101c", "pud0"); pud1 = C("#121e32", "pud1")
pud2 = C("#21364e", "pud2"); pud3 = C("#3a587c", "pud3")

poster = C("#4a5a7e", "poster"); poster2 = C("#8b9ab8", "poster2")

# ---------------- sky ----------------
c.rect(0, 0, 64, 64, sky0)
c.rect(0, 4, 64, 4, sky1)
c.rect(0, 8, 64, 3, sky2)
c.rect(0, 10, 64, 2, sky3)
c.rect(2, 2, 26, 1, sky1)
c.rect(36, 5, 22, 1, sky2)
# haze / light pollution above the store
c.rect(4, 8, 56, 3, glow1)
c.dither(0, 8, 5, 3, [glow1, sky2], pattern="bayer4")
c.dither(59, 8, 5, 3, [glow1, sky2], pattern="bayer4")
c.rect(14, 10, 34, 1, glow2)

# ---------------- building shell ----------------
c.rect(1, 11, 62, 1, wall3)
c.rect(1, 12, 62, 1, roof1)
c.rect(1, 13, 62, 34, wall1)     # y 13..46
c.rect(1, 13, 1, 34, wall2)
c.rect(62, 13, 1, 34, wall0)

# sign band
c.rect(3, 13, 58, 8, signbg)
c.rect(13, 13, 38, 8, signglow)
c.text(17, 14, "STORE", signtext)

# ---------------- window ----------------
c.rect(4, 25, 34, 22, frame0)    # frame x4..37 y25..46
c.rect(4, 25, 34, 1, frame1)
c.rect(4, 25, 1, 22, frame1)
c.rect(37, 25, 1, 22, frame1)
c.rect(6, 27, 30, 18, in1)       # glass x6..35 y27..44

c.rect(6, 27, 30, 1, in0)        # ceiling light
c.text(10, 28, "OPEN", neon, spacing=0)

# products on upper shelf
items1 = [(7, 2, pr), (10, 2, pb), (13, 3, pg), (17, 2, pw), (20, 2, py),
          (23, 2, pr), (26, 3, pb), (30, 2, pg), (33, 2, py)]
for x, w, colr in items1:
    c.rect(x, 35, w, 2, colr)
c.rect(6, 37, 30, 1, shelf)

# products on lower shelf
items2 = [(7, 3, py), (11, 2, pg), (14, 2, pw), (17, 3, pr), (21, 2, pb),
          (24, 2, pg), (27, 2, py), (30, 2, pw), (33, 2, pr)]
for x, w, colr in items2:
    c.rect(x, 38, w, 2, colr)
c.rect(6, 40, 30, 1, shelf)

# floor
c.rect(6, 41, 30, 4, floor1)
c.rect(6, 41, 30, 1, floor2)
for x in (8, 13, 19, 26, 32):
    c.rect(x, 42, 1, 3, in3)
for x in (10, 23, 30):
    c.rect(x, 43, 2, 2, in3)
c.rect(4, 45, 34, 2, frame0)
c.rect(4, 45, 34, 1, frame1)

# ---------------- pillar + door ----------------
c.rect(38, 25, 3, 22, wall1)
c.rect(38, 25, 1, 22, wall2)

c.rect(41, 25, 12, 22, dframe)
c.rect(41, 25, 12, 1, frame1)
c.rect(43, 27, 8, 18, doorlight)
c.rect(43, 27, 8, 1, in0)
c.rect(51, 33, 1, 9, frame2)
c.set(51, 42, frame0)

# ---------------- person in raincoat (back view, 7x15 at x43 y31) ----------------
person = [
    "...Y...",
    "..YYY..",
    ".DYYYD.",
    ".DKKKD.",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    "DYYYYYD",
    ".DYYYD.",
    ".B...B.",
]
pmap = {"Y": coat0, "D": coat1, "K": coat2, "B": boot}
for j, row in enumerate(person):
    for i, ch in enumerate(row):
        if ch in pmap:
            c.set(43 + i, 31 + j, pmap[ch])

# ---------------- right wall ----------------
c.rect(53, 25, 10, 22, wall1)
c.rect(53, 25, 1, 22, wall2)
c.rect(55, 29, 7, 9, frame0)
c.rect(56, 30, 5, 7, poster)
c.rect(56, 30, 5, 2, poster2)
c.rect(57, 33, 3, 1, poster2)
c.rect(62, 25, 1, 22, wall0)

# ---------------- awning ----------------
for i in range(0, 54, 6):
    seg = min(6, 54 - i)
    x0 = 2 + i
    base = awnA if (i // 6) % 2 == 0 else awnB
    hi = awnA2 if (i // 6) % 2 == 0 else awnB2
    c.rect(x0, 21, seg, 3, base)
    c.rect(x0, 21, seg, 1, hi)
for i in range(0, 54, 6):
    seg = min(6, 54 - i)
    x0 = 2 + i
    base = awnA if (i // 6) % 2 == 0 else awnB
    c.rect(x0 + 1, 24, max(1, seg - 2), 1, base)
c.rect(2, 25, 54, 1, awnsh)

# ---------------- sidewalk ----------------
c.rect(0, 47, 64, 17, walk0)
c.rect(0, 47, 64, 2, walk1)
c.rect(0, 47, 64, 1, curb)
rng2 = random.Random(99)
for _ in range(46):
    x = rng2.randrange(0, 64); y = rng2.randrange(49, 64)
    c.set(x, y, walk2)
for _ in range(18):
    x = rng2.randrange(0, 64); y = rng2.randrange(50, 64)
    c.set(x, y, walk3)

# wet reflections: vertical streaks of light on the pavement
def streaks(x0, x1, ytop, col1, col2, col3, seed, skip=0.22):
    rr = random.Random(seed)
    for x in range(x0, x1 + 1):
        if rr.random() < skip:
            continue
        h = 3 + rr.randrange(0, 8)
        for k in range(h):
            y = ytop + k
            if y > 63:
                break
            t = k / float(max(1, h - 1))
            colr = col1 if t < 0.30 else (col2 if t < 0.70 else col3)
            c.set(x, y, colr)

streaks(5, 37, 48, rw2, rw1, rw3, 11, 0.12)
streaks(41, 53, 48, rd2, rd1, rw3, 22, 0.10)
streaks(5, 53, 57, rw3, walk2, walk0, 33, 0.55)

# silhouette of the person mirrored in the wet ground
for x in range(44, 50):
    for y in range(48, 54):
        if c.get(x, y) in (rd2, rd1):
            c.set(x, y, rw3)

# ---------------- puddles ----------------
def puddle(cx, cy, rx, ry, seed):
    c.ellipse(cx, cy, rx, ry, pud0)
    rr = random.Random(seed)
    for dx in range(-rx + 1, rx):
        if rr.random() < 0.42:
            continue
        hw = int(ry * math.sqrt(max(0.0, 1.0 - (dx / float(rx)) ** 2)))
        if hw <= 0:
            continue
        top = cy - hw
        ln = rr.randrange(1, max(2, 2 * hw + 1))
        colr = rr.choice([pud1, pud2, rw3, pud1, rw1])
        for k in range(ln):
            y = top + k
            if 0 <= cx + dx < 64 and 0 <= y < 64:
                c.set(cx + dx, y, colr)
    for dx in range(-rx + 1, rx):
        y = cy - int(round(ry * math.sqrt(max(0.0, 1.0 - (dx / float(rx)) ** 2))))
        if (dx * 5 + seed) % 3 != 0 and 0 <= cx + dx < 64 and 0 <= y < 64:
            c.set(cx + dx, y, pud3)

puddle(24, 59, 14, 4, 5)
puddle(53, 56, 8, 3, 9)
puddle(8, 60, 5, 2, 3)

# ripples where rain hits the water
c.ellipse(20, 58, 3, 1, pud3, fill=False)
c.ellipse(31, 61, 4, 1, pud2, fill=False)
c.ellipse(55, 56, 3, 1, pud3, fill=False)
c.ellipse(9, 60, 2, 1, pud2, fill=False)

# ---------------- umbrella rack ----------------
c.ellipse(58, 51, 5, 1, shad0)
c.rect(55, 49, 7, 2, rack0)
c.rect(55, 45, 1, 5, rack0)
c.rect(61, 45, 1, 5, rack0)
c.rect(55, 45, 7, 1, rack1)
# red umbrella
c.rect(56, 38, 2, 7, ur)
c.rect(56, 38, 1, 7, ur2)
c.set(57, 37, ur2)
# teal umbrella
c.rect(59, 41, 2, 4, ut)
c.rect(59, 41, 1, 4, ut2)
c.set(60, 40, ut2)

# ---------------- bicycle ----------------
c.ellipse(12, 57, 8, 1, shad0)
for (hx, hy) in [(7, 53), (18, 53)]:
    c.circle(hx, hy, 4, bike1, fill=False)
    c.set(hx, hy - 4, bike2)
    c.set(hx, hy + 4, bike2)
    c.set(hx - 4, hy, bike2)
    c.set(hx + 4, hy, bike2)
    c.set(hx, hy, bike2)
    c.line(hx, hy, hx + 2, hy - 2, bike0)
    c.line(hx, hy, hx - 2, hy + 2, bike0)
# frame
c.line(7, 53, 12, 53, bike1)      # chain stay
c.line(7, 53, 11, 47, bike1)      # seat stay
c.line(12, 53, 11, 47, bike1)     # seat tube
c.line(11, 47, 17, 49, bike1)     # top tube
c.line(12, 53, 17, 49, bike1)     # down tube
c.line(17, 49, 18, 53, bike1)     # fork
c.line(17, 49, 16, 45, bike1)     # head tube
c.rect(8, 45, 4, 1, bike0)        # saddle
c.rect(14, 45, 5, 1, bike2)       # handlebar

# ---------------- rain ----------------
bright = {in0, in1, in2, in3, floor1, floor2, doorlight, signtext,
          shelf, pr, pg, pb, pw, py, neon}
rng = random.Random(2024)
for _ in range(80):
    x0 = rng.randrange(-4, 68)
    y0 = rng.randrange(0, 62)
    ln = rng.choice([2, 3, 3, 4, 4, 5])
    colr = rain if rng.random() < 0.72 else rain2
    for i in range(ln):
        px = x0 - (i // 2)
        py = y0 + i
        if 0 <= px < 64 and 0 <= py < 64 and c.get(px, py) not in bright:
            c.set(px, py, colr)

for _ in range(30):
    x = rng.randrange(0, 64); y = rng.randrange(52, 64)
    if c.get(x, y) not in bright:
        c.set(x, y, rain2)

save("store", c)
print(c.stats_text())
finish(c)
