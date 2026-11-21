OFF = 14                      # vertical offset of the original art on the taller canvas
out = new_canvas(64, 92, name="output")
out.blit(input_canvas, 0, OFF)

IDX_D = out.color('#1d8baa')          # existing dark cyan
IDX_C = out.color('#2ec7dc')          # existing light cyan
W_LIT = out.color('#8ae8f7', 'wlit')
W_FOAM = out.color('#e9feff', 'wfoam')


def mir(x):
    return 63 - x


# ------------------------------------------------- 1. ripples on the still water
for y in range(OFF + 5, OFF + 58):
    for x in range(64):
        if out.get(x, y) in (IDX_D, IDX_C):
            if y % 3 == 0 and (x + (y // 3) * 2) % 7 in (0, 1):
                out.set(x, y, W_LIT)
            elif (x * 3 + y * 5) % 29 == 0:
                out.set(x, y, W_FOAM)


# ------------------------------------------------------------- 2. the central jet
out.line(31, 14, 31, 9, W_FOAM)
out.line(32, 14, 32, 9, W_LIT)
out.set(31, 8, W_FOAM)
out.set(32, 8, W_FOAM)
out.line(30, 9, 30, 11, W_LIT)
out.line(33, 9, 33, 11, W_LIT)
out.set(30, 7, W_LIT)
out.set(33, 7, W_LIT)
out.line(29, 6, 34, 6, W_LIT)
out.line(28, 7, 35, 7, W_LIT)
out.set(31, 5, W_FOAM)
out.set(32, 5, W_FOAM)
out.set(31, 6, W_FOAM)
out.set(32, 6, W_FOAM)
for (x, y) in [(30, 4), (29, 5), (28, 6), (27, 8), (26, 10),
               (28, 4), (26, 7), (25, 9), (24, 12)]:
    out.set(x, y, W_FOAM)
    out.set(mir(x), y, W_FOAM)


# ------------------------------------- 3. spray arcs, solid then breaking into drops
scratch = new_canvas(64, 92, name="spray")
MARK = out.color('#ff00ff', 'mark')

arcs = [
    ("M 30 10 Q 24 11 23 34", 22, (23, 34)),
    ("M 29 9 Q 18 13 17 41", 26, (17, 41)),
    ("M 29 8 Q 12 17 17 60", 34, (17, 60)),
]
arcs += [("M 33 10 Q 39 11 40 34", 22, (40, 34)),
         ("M 34 9 Q 45 13 46 41", 26, (46, 41)),
         ("M 34 8 Q 51 17 46 60", 34, (46, 60))]

for d, y_break, land in arcs:
    scratch.clear()
    scratch.path(d, MARK, fill=False)
    for y in range(92):
        for x in range(64):
            if scratch.get(x, y) == MARK:
                if y < y_break:
                    out.set(x, y, W_FOAM if y < y_break - 6 else W_LIT)
                elif (x * 2 + y) % 4 != 3:
                    out.set(x, y, W_LIT)
    lx, ly = land
    inx = 1 if lx < 32 else -1
    out.set(lx, ly, W_FOAM)
    out.set(lx + inx, ly, W_FOAM)
    out.set(lx - inx, ly - 1, W_FOAM)
    out.set(lx + inx, ly - 3, W_LIT)


# ----------------------------------------------- 4. water spilling tier over tier
def spill(x, y0, y1, wide=False):
    out.line(x, y0, x, y1, W_LIT)
    out.set(x, y0, W_FOAM)
    out.set(x, y1, W_FOAM)
    if wide:
        out.line(x + 1, y0, x + 1, y1 - 1, IDX_C)
        out.set(x + 1, y0, W_FOAM)
    for yy in range(y0 + 2, y1, 4):
        out.set(x, yy, W_FOAM)
    # splash where it lands
    out.set(x - 1, y1, W_LIT)
    out.set(x + (2 if wide else 1), y1, W_LIT)
    out.set(x - 2, y1 + 1, W_FOAM)
    out.set(x + (3 if wide else 2), y1 + 1, W_FOAM)


for x in (22, mir(22)):               # top tier -> second tier
    spill(x, 25, 31)
for x in (17, mir(17)):               # second tier -> third tier
    spill(x, 35, 39)
for x in (18, 44):                    # third tier -> the big basin, main cascade
    spill(x, 45, 62, wide=True)

# a couple of splash rings on the pool surface
for (cx, cy) in [(20, 64), (43, 64), (31, 66)]:
    out.ellipse(cx, cy, 3, 1, W_LIT, fill=False)
    out.set(cx, cy, W_FOAM)

# ------------------------------------------------- 5. overflow at the basin spout
out.line(31, 71, 31, 76, W_LIT)
out.line(32, 71, 32, 76, IDX_C)
out.set(31, 71, W_FOAM)
out.set(32, 73, W_FOAM)
out.set(31, 76, W_FOAM)
out.set(30, 77, W_LIT)
out.set(33, 77, W_LIT)

view(out)
print(out.stats_text())
finish(out)
