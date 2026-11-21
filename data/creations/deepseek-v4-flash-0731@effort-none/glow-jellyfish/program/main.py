from pixelbench_api import *

c = new_canvas(16, 16, background=(0,0,0,0), name="jellyfish")

OUT = "#0b1524"
DARK = "#1e4e7e"
MID  = "#3d8bbf"
BRT  = "#76c8f0"
CORE = "#baeaff"
HI   = "#e0f7ff"
AURA = "#28547f"
TEN  = "#4f9fd0"
TENL = "#8ed4f0"

# ============ 1. Aura (bottom) ============
aura_px = [
    (2,5),(12,5),(2,6),(12,6),(2,7),(12,7),(2,8),(12,8),
    (3,4),(11,4),(5,1),(10,1),(4,10),(11,10),(3,9),(12,9),
]
for (x,y) in aura_px:
    if 0<=x<=15 and 0<=y<=15:
        c.set(x, y, AURA)

# ============ 2. Bell interior ============
bell = {
    1: {7:CORE, 8:CORE},
    2: {6:BRT, 7:CORE, 8:CORE, 9:BRT},
    3: {5:BRT, 6:CORE, 7:CORE, 8:CORE, 9:CORE, 10:BRT},
    4: {5:MID, 6:BRT, 7:CORE, 8:CORE, 9:CORE, 10:BRT, 11:MID},
    5: {4:MID, 5:BRT, 6:CORE, 7:CORE, 8:CORE, 9:CORE, 10:BRT, 11:MID},
    6: {4:MID, 5:BRT, 6:CORE, 7:CORE, 8:CORE, 9:CORE, 10:BRT, 11:MID},
    7: {4:MID, 5:BRT, 6:CORE, 7:CORE, 8:CORE, 9:CORE, 10:BRT, 11:MID},
    8: {4:MID, 5:BRT, 6:CORE, 7:CORE, 8:CORE, 9:CORE, 10:BRT, 11:MID},
    9: {5:DARK, 6:MID, 7:BRT, 8:CORE, 9:BRT, 10:MID, 11:DARK},
    10:{6:DARK, 7:MID, 8:MID, 9:DARK},
}
for y, row in bell.items():
    for x, col in row.items():
        c.set(x, y, col)

# ============ 3. Tentacle skirt ============
# Wavy tentacle strands hanging below the bell lip
tent = {
    # each: list of (y, is_light_tip)
    5:  [(11,False),(12,False),(13,True)],
    6:  [(11,False),(12,True)],
    7:  [(11,False),(12,False),(13,False),(14,True)],
    8:  [(11,False),(12,False),(13,False),(14,True)],
    9:  [(11,False),(12,False),(13,True)],
    10: [(11,False),(12,True)],
    11: [(11,False),(12,False),(13,True)],
}
for x, pts in tent.items():
    for (y, light) in pts:
        c.set(x, y, TENL if light else TEN)

# ============ 4. Outline ============
outline = {
    1:  [6,9],
    2:  [5,10],
    3:  [5,10],
    4:  [4,11],
    5:  [4,11],
    6:  [4,11],
    7:  [4,11],
    8:  [4,11],
    9:  [5,11],
    10: [6,9],
    11: [5,11],
}
for y, xs in outline.items():
    for x in xs:
        c.set(x, y, OUT)

# ============ 5. Highlights ============
hi_px = [
    (7,1),(8,1),(7,2),(8,2),(6,3),(9,3),
    (6,5),(9,5),(7,6),(8,6),(5,4),(10,4),
]
for (x,y) in hi_px:
    c.set(x, y, HI)

# Inner glow shimmer patches
shimmer = [
    (6,6),(9,6),(7,7),(8,7),(6,8),(9,8),
]
for (x,y) in shimmer:
    c.set(x, y, BRT)

print(c.stats_text())
print(c.matrix_text(region=(0,0,15,15), indices=False))

finish(c)
