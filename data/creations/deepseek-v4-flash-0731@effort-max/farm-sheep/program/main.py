# 32x32 cozy farm sheep - Stardew Valley style, side view facing left.
# Plump woolly body, ear, tail, four legs, soft flat shading, no outline.

c = new_canvas(32, 32)

W = "#F7F0E1"   # warm white wool
H = "#FCF7EA"   # pale highlight fluff
S = "#E2D5B8"   # soft shadow under wool
P = "#F0C7BF"   # pale pink inner ear / snout / blush
E = "#4D4033"   # soft dark brown eye / nose
L = "#A1866E"   # warm tan legs
F = "#6E5F4C"   # muted brown hooves

def add(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)

# ---- head (front, facing left) ----
add(8, 4, 12, W)
add(9, 3, 12, W)
add(10, 3, 4, W); add(10, 5, 6, E); add(10, 7, 12, W)
add(11, 3, 4, W); add(11, 5, 6, E); add(11, 7, 12, W)
add(12, 3, 4, P); add(12, 5, 9, W); add(12, 10, 11, P); add(12, 12, 13, W)
add(13, 3, 3, P); c.set(4, 13, E); add(13, 5, 13, W)
add(14, 4, 13, W)
add(15, 5, 13, W)
add(16, 6, 12, W)
add(17, 7, 11, W)

# fill notch between head and body
add(9, 13, 14, W)

# ---- ear (drawn after head so the pink inner shows) ----
c.set(5, 6, W)
c.set(4, 7, W); c.set(5, 7, P)
c.set(3, 8, W); c.set(4, 8, P)

# ---- body (wool mound) ----
add(9, 15, 24, W)
add(10, 13, 26, W)
add(11, 12, 27, W)
add(12, 13, 28, W)
add(13, 14, 28, W)
add(14, 14, 28, W)
add(15, 13, 28, W)
add(16, 12, 28, W)
add(17, 11, 28, W)
add(18, 10, 27, W)
add(19, 9, 26, W)
add(20, 8, 25, W)

# ---- tail pom ----
add(15, 29, 29, W)
add(16, 29, 30, W)
add(17, 28, 29, W)

# ---- under-body shadow ----
add(21, 8, 24, S)
add(22, 8, 24, S)

# ---- legs + hooves (over shadow) ----
for x0 in (11, 16, 20, 24):
    add(21, x0, x0 + 1, L)
    add(22, x0, x0 + 1, L)
    add(23, x0, x0 + 1, L)
    add(24, x0, x0 + 1, F)
    add(25, x0, x0 + 1, F)

# ---- fluff highlights ----
for x, y in ((10, 8), (18, 9), (22, 10), (26, 12), (7, 10)):
    c.set(x, y, H)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

finish(c)
