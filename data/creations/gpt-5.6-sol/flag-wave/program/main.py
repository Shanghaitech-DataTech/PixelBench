# Three-frame flag wave on a shared canvas with extra vertical motion room.
BG = 0
INK = 1
RED = 2
ORANGE = 3
PURPLE = 4
DEEP_PURPLE = 5


def expanded_original(name):
    c = new_canvas(48, 64, background=None, name=name)
    c.blit(input_canvas, 0, 4)
    return c


def draw_flag_pose(name, tops):
    c = expanded_original(name)
    # Remove the original cloth while retaining the pole and its attachment edge.
    c.clear(20, 0, 28, 44)

    # Each cloth slice is one native 4 px cell wide: dark edging, five cloth
    # cells, then dark edging. Varying slice heights gives a crisp wave.
    accents = {
        0: {1},
        1: {0, 1},
        2: {0, 1, 2},
        3: {1, 2},
        4: {2},
        5: {1},
        6: {0},
    }
    for col, top in enumerate(tops):
        x = 20 + col * 4
        c.rect(x, top, 4, 4, INK)
        for row in range(5):
            colour = ORANGE if row in accents[col] else RED
            c.rect(x, top + 4 + row * 4, 4, 4, colour)
        c.rect(x, top + 24, 4, 4, INK)

    # Keep a strong, readable hoist seam against the pole.
    c.rect(20, tops[0], 4, 4, INK)
    c.rect(20, tops[0] + 24, 4, 4, INK)
    return c


# Frame 1 preserves every original pixel, shifted only to provide shared room.
f1 = expanded_original('frame_1_high')
# The fly end passes through the centre while a smaller ripple crosses the cloth.
f2 = draw_flag_pose('frame_2_mid', [16, 12, 12, 16, 20, 20, 16])
# The wave reverses: the fly end reaches its lowest point.
f3 = draw_flag_pose('frame_3_low', [16, 20, 20, 24, 28, 32, 36])

view(f1, scale=8, margin=0)
view(f2, scale=8, margin=0)
view(f3, scale=8, margin=0)
finish([f1, f2, f3])
