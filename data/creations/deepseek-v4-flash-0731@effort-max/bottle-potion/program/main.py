from pixelbench_api import input_canvas, finish

out = input_canvas.copy(name='output')

# --- palette ---
surface   = out.color('#9a4fd6', name='potion_surface')
base      = out.color('#6d2a9e', name='potion')
deep      = out.color('#571d85', name='potion_deep')
dark      = out.color('#381147', name='potion_dark')
bubble    = out.color('#c98cf5', name='bubble')
bubble_hi = out.color('#f3dcff', name='bubble_hi')
sparkle   = out.color('#ff86e0', name='sparkle')

water_idx = out.color('#2f7598')   # existing liquid
band_idx  = out.color('#31121d')   # dark band at liquid bottom

# --- repaint the water purple (slight vertical shading) ---
W, H = out.stats()['size']
for y in range(H):
    for x in range(W):
        c = out.get(x, y)
        if c == water_idx:
            if y == 26:
                out.set(x, y, surface)
            elif y >= 38:
                out.set(x, y, deep)
            else:
                out.set(x, y, base)
        elif c == band_idx:
            out.set(x, y, dark)


def small_circle(cx, cy):
    out.circle(cx, cy, 1, bubble)

def bubble_ring(cx, cy, r):
    out.circle(cx, cy, r, bubble, fill=False)
    out.set(cx - 1, cy - 1, bubble_hi)

def spark(cx, cy):
    for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= cx + dx < W and 0 <= cy + dy < H:
            out.set(cx + dx, cy + dy, sparkle)

# --- bubbles rising inside the potion ---
bubble_ring(33, 35, 3)
bubble_ring(25, 32, 2)
bubble_ring(40, 31, 2)
bubble_ring(44, 36, 2)
small_circle(29, 38)
small_circle(37, 28)
small_circle(22, 29)
small_circle(47, 33)
small_circle(27, 34)
small_circle(35, 39)
small_circle(42, 33)

# --- fizz at the surface and bubbles in the air gap of the bottle ---
small_circle(30, 26)
small_circle(25, 26)
small_circle(24, 20)
small_circle(28, 17)
small_circle(31, 22)
small_circle(36, 21)
small_circle(26, 15)

# --- magical sparkles ---
spark(21, 26)
spark(37, 26)
spark(18, 23)
spark(39, 18)
spark(30, 29)

print(out.stats_text())
print(out.matrix_text(region=(10, 10, 54, 50)))

finish(out)
