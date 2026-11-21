# Vintage sewing machine, 48x48, transparent bg, slightly angled side view
from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, None, name="output")

PAL = {
    "D": c.color("#12101a", "ink"),
    "H": c.color("#211f2d", "iron1"),
    "#": c.color("#2e2b3c", "iron2"),
    "=": c.color("#403a52", "iron3"),
    "-": c.color("#57506d", "iron4"),
    "+": c.color("#726a8b", "iron5"),
    "m": c.color("#453f55", "chrome0"),
    "n": c.color("#6b647f", "chrome1"),
    "o": c.color("#948da6", "chrome2"),
    "p": c.color("#c3bdcd", "chrome3"),
    "q": c.color("#f0edf5", "chrome4"),
    "a": c.color("#6b4f1e", "brass1"),
    "b": c.color("#a87c33", "brass2"),
    "z": c.color("#e0b466", "brass3"),
    "r": c.color("#5c1019", "cloth1"),
    "s": c.color("#8b1a24", "cloth2"),
    "t": c.color("#b8262f", "cloth3"),
    "u": c.color("#d9484f", "cloth4"),
    "v": c.color("#f39b95", "cloth5"),
    "w": c.color("#3f2314", "wood0"),
    "x": c.color("#5e3720", "wood1"),
    "y": c.color("#7d4b2b", "wood2"),
    "Z": c.color("#9d6538", "wood3"),
}
R = lambda ch, n: ch * n

ROWS = [
    # ---------- thread spool on the spool pin ----------
    (4,  [(32, "n")]),
    (5,  [(29, R("x", 6))]),
    (6,  [(30, "t" + R("u", 2) + "t")]),
    (7,  [(30, R("t", 4))]),
    (8,  [(29, R("x", 6))]),
    (9,  [(32, "o")]),
    # ---------- body: top plane, shoulder ----------
    (10, [(12, R("+", 5)), (28, R("+", 6))]),
    (11, [(10, R("-", 7)), (17, R("-", 10)), (27, R("-", 7))]),
    (12, [(9, "-=" + R("=", 22) + "HD")]),
    (13, [(9, "-=" + R("=", 22) + "HD")]),
    (14, [(9, "-=" + R("#", 22) + "HD")]),
    (15, [(9, "-=" + R("#", 22) + "HD")]),
    (16, [(9, "-=" + R("#", 22) + "HD")]),
    # ---------- head | throat | column ----------
    (17, [(9, "-=" + R("#", 5) + "HD"), (18, R("D", 9)), (26, "=" + R("#", 7) + "D")]),
    (18, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (19, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (20, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (21, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (22, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (23, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (24, [(9, "-=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (25, [(10, "=" + R("#", 5) + "HD"), (26, "=" + R("#", 7) + "D")]),
    (26, [(11, R("#", 5) + "H"), (26, "=" + R("#", 7) + "D")]),
    # ---------- needle bar | presser bar ----------
    (27, [(12, "oo"), (15, "nn"), (26, "=" + R("#", 7) + "D")]),
    (28, [(12, "oo"), (15, "nn"), (26, "=" + R("#", 7) + "D")]),
    (29, [(11, "ooo"), (15, "nn"), (26, "=" + R("#", 7) + "D")]),
    # ---------- presser foot ----------
    (30, [(9, R("o", 8)), (26, "=" + R("#", 7) + "D")]),
    (31, [(25, "=" + R("#", 8) + "D")]),
    # ---------- bed plate : lit top surface then dark iron ----------
    (32, [(4, "m" + R("p", 15) + R("=", 17) + R("p", 5) + "o")]),
    (33, [(4, "m" + R("p", 37) + "o")]),
    (34, [(3, R("=", 41))]),
    (35, [(3, R("H", 42))]),
    (36, [(3, R("D", 42))]),
    # ---------- wooden table ----------
    (37, [(4, R("x", 40))]),
    (38, [(2, R("Z", 44))]),
    (39, [(2, R("y", 44))]),
    (40, [(2, R("y", 44))]),
    (41, [(2, R("x", 44))]),
    (42, [(2, R("w", 44))]),
]

CLOTH = [
    (31, [(4, R("t", 20))]),
    (32, [(3, R("t", 21))]),
    (33, [(2, R("t", 17))]),
    (34, [(2, R("t", 15))]),
    (35, [(2, R("t", 15))]),
    (36, [(2, R("t", 15))]),
    (37, [(2, R("t", 14))]),
    (38, [(3, R("t", 13))]),
    (39, [(3, R("t", 12))]),
    (40, [(4, R("t", 11))]),
    (41, [(5, R("r", 4)), (10, R("r", 4))]),
]


def paint(rows):
    for y, segs in rows:
        for x0, s in segs:
            assert 0 <= x0 and x0 + len(s) <= W, (y, x0, len(s))
            for i, ch in enumerate(s):
                if ch != ".":
                    c.set(x0 + i, y, PAL[ch])


paint(ROWS)
paint(CLOTH)

# ---------- cloth shading ----------
c.line(5, 31, 22, 31, PAL["u"])            # lit top surface
c.line(8, 31, 12, 31, PAL["v"])
c.set(4, 31, PAL["t"]); c.set(23, 31, PAL["s"]); c.set(22, 32, PAL["s"])
c.line(4, 33, 8, 33, PAL["u"])             # fold over the bed edge
c.line(10, 33, 18, 33, PAL["t"])
c.line(2, 34, 3, 34, PAL["v"])
c.line(5, 34, 9, 34, PAL["u"])
c.line(3, 35, 4, 39, PAL["u"])             # lit left side of the drape
c.line(2, 35, 2, 36, PAL["s"])
c.line(7, 35, 7, 40, PAL["s"])             # folds
c.line(6, 36, 6, 39, PAL["t"])
c.line(11, 34, 11, 39, PAL["s"])
c.line(10, 35, 10, 38, PAL["t"])
c.line(14, 34, 14, 40, PAL["r"])
c.line(2, 37, 14, 37, PAL["s"])
c.line(12, 41, 13, 41, PAL["r"])
c.line(10, 31, 17, 31, PAL["s"])           # shadow under the presser foot

# ---------- brass pinstripe on the arm ----------
c.line(19, 14, 26, 14, PAL["b"])
c.set(20, 13, PAL["z"]); c.set(23, 13, PAL["z"]); c.set(25, 13, PAL["a"])
c.set(21, 15, PAL["a"]); c.set(24, 15, PAL["z"])

# ---------- chrome dial on head ----------
c.set(12, 18, PAL["o"])
c.set(11, 19, PAL["o"]); c.set(12, 19, PAL["q"]); c.set(13, 19, PAL["o"])
c.set(12, 20, PAL["o"])

# ---------- handwheel ----------
WHEEL = [
    "....p....",
    "...pop...",
    "..poHop..",
    "..pHHHp..",
    ".poHHHop.",
    ".pHHqHHp.",
    "poHHqHHop",
    ".pHHqHHp.",
    ".poHHHop.",
    "..pHHHp..",
    "..poHop..",
    "...pop...",
    "....p....",
]
for i, row in enumerate(WHEEL):
    for j, ch in enumerate(row):
        if ch != ".":
            c.set(34 + j, 15 + i, PAL[ch])
for x, y in [(38, 17), (38, 18), (36, 21), (40, 21)]:
    c.set(x, y, PAL["o"])

# ---------- presser foot toe + needle (in front of the cloth) ----------
c.set(9, 31, PAL["n"]); c.set(10, 31, PAL["n"])
c.line(13, 29, 13, 32, PAL["q"])
c.set(13, 28, PAL["p"])

save("sewing", c)
print(c.stats_text())
txt = c.matrix_text().split("\n")
print("    " + "".join(str(x % 10) for x in range(48)))
for ln in txt:
    if ln.startswith("  ") and len(ln) > 46:
        print(ln[2:])
finish(c)
