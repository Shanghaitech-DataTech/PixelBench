from pixelbench_api import *

src = canvas('input')
SW, SH = 37, 33
OUT_W, OUT_H = 45, 40
DX, DY = 4, 2

# ============ FRAME 1: Original ============
f1 = new_canvas(OUT_W, OUT_H, name='frame1')
f1.blit(src, DX, DY)

# ============ FRAME 2: Recoil ============
f2 = new_canvas(OUT_W, OUT_H, name='frame2')

# Lean: shift rows to the right, more at top → body leans back
def lean_dx(y):
    return round((SH - 1 - y) * 0.1)

# Draw all source pixels with lean + left foot lift
for y in range(SH):
    ls = lean_dx(y)
    for x in range(SW):
        idx = src.get(x, y)
        if idx != 0:
            fx = x + ls + DX
            fy = y + DY
            if x <= 16 and y >= 26:
                fy = y + DY - 4  # left foot lifts
            f2.set(fx, fy, idx)

# PEY: pupil rolls upward (dark in the cyclops eye goes to top)
for y in range(SH):
    ls = lean_dx(y)
    for x in range(SW):
        idx = src.get(x, y)
        # The pupil is the dark (idx 1) at the eye area center of the cyclops
        if idx == 1 and 16 <= x <= 22 and 15 <= y <= 19:
            # Roll the pupil UP by 3
            f2.set(x + ls + DX, y + DY - 3, idx)
            # Clear where the pupil was
            f2.set(x + ls + DX, y + DY, 0)

# MO: mouth opens
# Open the monster's mouth - a wide open gape
MOUTH_DARK = (30, 20, 20, 255)
for y in range(19, 27):
    ls = lean_dx(y)
    # Mouth gets wider / more open with a visible opening
    if y <= 20:
        ml, mr = 14, 25
    elif y <= 22:
        ml, mr = 13, 26
    elif y <= 24:
        ml, mr = 14, 25
    elif y <= 25:
        ml, mr = 15, 24
    else:
        ml, mr = 16, 23
    for mx in range(ml + ls + DX, mr + ls + DX + 1):
        f2.set(mx, y + DY, MOUTH_DARK)

# Teeth in the open mouth
TEETH = (245, 220, 200, 255)
for y in range(19, 23):
    ls = lean_dx(y)
    for x in range(15 + ls + DX, 24 + ls + DX + 1):
        if y <= 22:
            f2.set(x, y + DY, TEETH)

# Clear any mouth-artifacts from body region
for y in range(19, 27):
    ls = lean_dx(y)
    for x in range(14 + ls + DX, 26 + ls + DX):
        pass  # keep as is

# Clean up mouth edges - draw mouth lip border around the open mouth
LIP = (180, 130, 60, 255)  # brown lip color similar to eyebrand
for y in range(18, 27):
    ls = lean_dx(y)
    for x in range(13 + ls + DX, 25 + ls + DX):
        if y >= 18 and y <= 23:
            pass  # already filled

# The mouth body outline around the open mouth
for y in range(18, 27):
    ls = lean_dx(y)
    if y <= 20:
        pass

# Redraw the character's side of the mouth with proper outline
LIP_DARK = (100, 100, 80, 255)
for y in range(18, 27):
    ls = lean_dx(y)
    for x in range(20 + ls + DX, 21 + ls + DX + 1):
        if y >= 21 and y <= 22:
            f2.set(x, y + DY, LIP_DARK)

# Verify all features present
print("=== FRAME 1 ===")
print(f1.stats_text())

print("=== FRAME 2 ===")
print(f2.stats_text())

print("=== FRAME 3 ===")

# ============ FRAME 3: Impact with red filter ============
f3 = f2.copy(name='frame3')

# Apply red filter: give the whole monster a strong red overlay
for y in range(OUT_H):
    for x in range(OUT_W):
        idx = f3.get(x, y)
        if idx != 0:
            pal = f3.palette()
            col = pal[idx]['rgba']
            r, g, b, a = col[0], col[1], col[2], col[3]
            # Red filter
            new_r = min(255, int(r * 0.3) + 180)
            new_g = int(g * 0.4)
            new_b = int(b * 0.45)
            f3.set(x, y, (new_r, new_g, new_b))

for c in canvases():
    print(c)

finish([f1, f2, f3])
