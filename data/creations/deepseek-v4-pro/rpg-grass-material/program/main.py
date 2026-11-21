import random

W, H = 16, 16

c = new_canvas(W, H, name="grass")

# Palette
base    = c.color("#4d8a3a", "base_green")
dark    = c.color("#396b2a", "dark_green")
light   = c.color("#7db95b", "light_green")
tuft    = c.color("#2e5a21", "tuft_green")
flower  = c.color("#f2d43b", "flower_yellow")
fcenter = c.color("#c9a32a", "flower_center")
dirt    = c.color("#8a6b4a", "dirt_brown")

# Base grass
c.rect(0, 0, W, H, base)

# Seamless helper: draw a small cluster of pixels, wrapping around tile edges.
def draw_wrapped(c, x, y, cells, colour):
    for dx, dy in cells:
        c.set((x + dx) % W, (y + dy) % H, colour)

# Interleaved dark/light grass speckles (single pixels, placed first so
# features drawn later stay clean on top).
random.seed(2024)
for i in range(22):
    x = random.randrange(W)
    y = random.randrange(H)
    c.set(x, y, dark if i % 2 == 0 else light)

# Sparse bare-dirt patches
dirt_cells = [(0, 0), (1, 0), (0, 1), (1, 1)]
draw_wrapped(c, 1, 14, dirt_cells, dirt)
draw_wrapped(c, 13, 1, dirt_cells, dirt)

# Small darker grass tufts: a base pixel with three blades fanning upward
tuft_cells = [(0, 0), (0, -1), (-1, -1), (1, -1)]
draw_wrapped(c, 2, 4,  tuft_cells, tuft)
draw_wrapped(c, 8, 3,  tuft_cells, tuft)
draw_wrapped(c, 6, 13, tuft_cells, tuft)
draw_wrapped(c, 14, 11, tuft_cells, tuft)

# Tiny yellow flowers: a small plus of petals with a darker center
flower_cells = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
for fx, fy in [(4, 10), (11, 5)]:
    draw_wrapped(c, fx, fy, flower_cells, flower)
    c.set(fx % W, fy % H, fcenter)

finish(c)
