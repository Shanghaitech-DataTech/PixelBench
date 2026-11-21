import math

c = new_canvas(16, 16, name="result")

GROOVE = "#2f1d10"
KO = "#5a3a20"
KI = "#3d2412"

# boards: (cols, base, dark, light, cap)
BOARDS = [
    ([0,1,2,3,15], "#c0946a", "#a87c52", "#d6ae86", "#7e5636"),
    ([5,6,7,8],    "#7d5233", "#664129", "#9a6d47", "#a8784f"),
    ([10,11,12,13],"#a06f45", "#8a5c39", "#bb8d60", "#7e5636"),
]

# base wood
for cols, base, dark, light, cap in BOARDS:
    for x in cols:
        for y in range(16):
            c.set(x, y, base)

# alternating board-end caps (top and bottom rows)
for cols, base, dark, light, cap in BOARDS:
    for x in cols:
        c.set(x, 0, cap)
        c.set(x, 15, cap)

# dark seam grooves + edge bevels (shadow on left edge, highlight on right edge)
for y in range(16):
    for g in (4, 9, 14):
        c.set(g, y, GROOVE)
    c.set(0, y, "#9a6f47")
    c.set(3, y, "#d6ae86")
    c.set(5, y, "#5f3f28")
    c.set(8, y, "#91633f")
    c.set(10, y, "#7d5536")
    c.set(13, y, "#bb8d60")
    c.set(15, y, "#9a6f47")

# wavy vertical wood-grain strands (period 16 -> seamless vertical tiling)
def wob(y, amp, phase, off):
    return off + round(amp * math.sin(2*math.pi*y/16 + phase))

strands = [
    (0, 1, 0.9, "#a87c52"),
    (1, 1, 3.4, "#d6ae86"),
    (1, 1, 1.8, "#8f643f"),
    (6, 1, 2.3, "#664129"),
    (7, 1, 5.5, "#9a6d47"),
    (11, 1, 4.1, "#8a5c39"),
    (12, 1, 0.6, "#bb8d60"),
]
for y in range(16):
    for off, amp, ph, col in strands:
        x = wob(y, amp, ph, off)
        if 0 <= x <= 15:
            c.set(x, y, col)

# wood knots: small oval eye with a short dark streak
def knot(cx, cy):
    for x, y, co in [
        (cx, cy, KO), (cx+1, cy, KO), (cx+2, cy, KO),
        (cx, cy+1, KO), (cx+1, cy+1, KI), (cx+2, cy+1, KO),
        (cx+1, cy+2, KO), (cx+1, cy+3, KO),
    ]:
        if 0 <= x <= 15 and 0 <= y <= 15:
            c.set(x, y, co)

knot(6, 4)
knot(11, 11)
knot(0, 8)

print(c.stats_text())
print(c.matrix_text())

finish(c)
