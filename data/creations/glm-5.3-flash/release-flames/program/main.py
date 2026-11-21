from pixelbench_api import *

W, H = 88, 63
OX = 8

C_M = '#f27219'    # flame orange  (c12 in source)
C_N = '#f4a30c'    # flame yellow  (c13)
C_O = '#fed32c'    # flame hot     (c14)
C_F = '#010202'    # near-black outline (c5)

# ---------------- frame 1 : original picture content ----------------
f1 = new_canvas(W, H, background=None, name='frame1')
f1.blit(input_canvas, OX, 0)

# ---------------- frame 2 : fire spell thrust ----------------
f2 = f1.copy(name='frame2')
i_m = f2.color(C_M); i_n = f2.color(C_N); i_o = f2.color(C_O)
flame_idx = {i_m, i_n, i_o}


def shift_band(c, x0, y0, w, h, dx):
    s = c.select(x0, y0, w, h)
    s.move_to(x0 + dx, y0, c)


# --- pose: body leans into the thrust, front foot steps forward ---
shift_band(f2, OX, 0, 47, 14, 4)        # head / hair
shift_band(f2, OX, 14, 47, 11, 3)       # shoulders + casting arm
shift_band(f2, OX, 25, 47, 9, 2)        # waist
shift_band(f2, OX, 34, 47, 20, 1)       # skirt
shift_band(f2, OX + 18, 54, 12, 7, 5)   # front foot steps forward
f2.set(32, 54, C_F)                     # ankle bridge

# --- wipe the old flame (every flame-coloured pixel) ---
for y in range(H):
    for x in range(W):
        if f2.get(x, y) in flame_idx:
            f2.set(x, y, None)

# restore the little ember that floats beside the hair (shifted with the head)
f2.set(44, 12, C_M); f2.set(44, 13, C_M); f2.set(45, 13, C_M)

# --- fiery trail: orange rim, yellow body, hot core, rising towards the ball ---
TRAIL = {
    52: (21, 24), 53: (20, 24), 54: (20, 25), 55: (19, 25), 56: (19, 25),
    57: (19, 24), 58: (18, 24), 59: (18, 24), 60: (18, 23), 61: (17, 23),
    62: (17, 23), 63: (17, 22), 64: (16, 22), 65: (16, 22), 66: (16, 21),
}
for x, (t, b) in TRAIL.items():
    for y in range(t, b + 1):
        if y == t or y == b:
            col = C_M
        elif x >= 62 and t < y < b:
            col = C_O
        elif x <= 54 and 21 <= y <= 23:
            col = C_O
        else:
            col = C_N
        f2.set(x, y, col)
for x, y in [(55, 18), (58, 17), (61, 16), (64, 15)]:   # licks off the top edge
    f2.set(x, y, C_M)
# the burst leaves the knuckles: bridge the flame base to the fist
for x, y in [(50, 21), (51, 22), (51, 23)]:
    f2.set(x, y, C_M)

# --- fireball: round body, hot core pushed towards the direction of travel ---
CX, CY = 73, 19
for dy in range(-8, 9):
    for dx in range(-8, 9):
        d = (dx * dx + dy * dy) ** 0.5
        if d > 6.8:
            continue
        d2 = ((dx - 2) ** 2 + dy * dy) ** 0.5
        col = C_O if d2 <= 2.8 else (C_N if d2 <= 4.8 else C_M)
        f2.set(CX + dx, CY + dy, col)

# licks around the ball's rim
for x, y in [(70, 12), (73, 12), (76, 13), (79, 15), (80, 18), (80, 21),
             (78, 24), (74, 26), (70, 26), (67, 24), (66, 21), (67, 17), (69, 14)]:
    f2.set(x, y, C_M)

# stray sparks drifting along the flight path
for x, y, col in [
    (56, 16, C_M), (59, 14, C_N), (62, 13, C_M), (66, 11, C_N), (70, 9, C_M),
    (74, 8, C_O), (78, 9, C_M), (82, 12, C_N),
    (57, 27, C_M), (61, 28, C_N), (65, 28, C_M), (69, 29, C_N), (73, 29, C_M),
    (77, 28, C_N), (80, 26, C_M),
    (82, 16, C_M), (84, 19, C_N), (83, 22, C_M), (82, 25, C_N), (85, 20, C_M),
]:
    f2.set(x, y, col)

print(f1.stats_text())
print(f2.stats_text())

names = {p['index']: p['name'] for p in f2.palette()}
print('--- fist + trail check (runs) ---')
for y in range(18, 28):
    rr = []
    x = 44
    while x <= 84:
        v = f2.get(x, y)
        if v == 0:
            x += 1
            continue
        xs = x
        while x <= 84 and f2.get(x, y) == v:
            x += 1
        rr.append(f"{xs}-{x-1}:{names.get(v, v)}")
    print(f"y{y}: " + ("  ".join(rr) if rr else "-"))

finish([f1, f2])
