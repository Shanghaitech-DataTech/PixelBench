from pixelbench_api import *

c = new_canvas(16, 16)

# Palette
base_green = c.color('#4a7a2e')
dark_green = c.color('#3a5f23')
light_green = c.color('#5d9440')
dirt = c.color('#8a6a3a')
dirt_dark = c.color('#6e5426')
flower_yellow = c.color('#ffd93d')
flower_center = c.color('#c88a1e')
tuft_dark = c.color('#2c4a1a')

# Base fill
c.rect(0, 0, 16, 16, base_green)

# --- Interleaved dark and light green speckles (periodic, wraparound for seamless) ---
dark_speckles = [
    (1, 2), (3, 9), (5, 14), (8, 4), (10, 11), (13, 6), (15, 13), (2, 6),
    (7, 1), (12, 15), (4, 12), (9, 8), (14, 2), (6, 10), (11, 5), (0, 15),
    (12, 10), (15, 1)
]
for (x, y) in dark_speckles:
    c.set(x, y, dark_green)

light_speckles = [
    (1, 8), (4, 1), (7, 13), (10, 3), (13, 9), (15, 6), (3, 15), (6, 6),
    (9, 1), (12, 13), (14, 4), (2, 10), (5, 5), (8, 15), (11, 8), (0, 11),
    (13, 14), (7, 5), (15, 10)
]
for (x, y) in light_speckles:
    c.set(x, y, light_green)

# --- Tiny yellow flowers: yellow center + petals around ---
flowers = [(3, 3), (12, 12), (2, 13)]
for (fx, fy) in flowers:
    c.set(fx, fy, flower_yellow)
    c.set((fx+1) % 16, fy, flower_yellow)
    c.set(fx, (fy+1) % 16, flower_yellow)
    c.set((fx+1) % 16, (fy+1) % 16, flower_yellow)
    c.set(fx, fy, flower_center)  # center

# --- Sparse bare dirt patches ---
dirt_1 = [(9, 2), (10, 2), (10, 3), (9, 3), (11, 3)]
for (x, y) in dirt_1:
    c.set(x, y, dirt)
c.set(9, 3, dirt_dark)

dirt_2 = [(5, 9), (6, 9), (6, 10)]
for (x, y) in dirt_2:
    c.set(x, y, dirt)
c.set(5, 9, dirt_dark)

dirt_3 = [(14, 7), (15, 7), (14, 8)]
for (x, y) in dirt_3:
    c.set(x, y, dirt)

# --- Small darker grass tufts ---
tufts = [(1, 14), (7, 7), (11, 1), (4, 6), (13, 5), (9, 15)]
for (tx, ty) in tufts:
    c.set(tx, ty, tuft_dark)
    c.set((tx+1) % 16, ty, tuft_dark)
    c.set(tx, (ty+1) % 16, tuft_dark)

# Edge speckles to ensure seamless stitching looks even
for (x, y, col) in [(15, 3, dark_green), (0, 14, light_green), (15, 12, light_green),
                    (0, 7, dark_green), (8, 0, light_green), (15, 14, dark_green),
                    (0, 1, light_green)]:
    c.set(x, y, col)

save("grass", c)

print(c.stats_text())
print(c.matrix_text(region=(0,0,15,15), indices=True))

finish(c)
